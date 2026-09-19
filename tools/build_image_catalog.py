#!/usr/bin/env python3
"""Validate the image register and generate offline writing / Ren'Py lookup files.

Run from any directory with Python 3.9+: python tools/build_image_catalog.py [--check] [--code-only]
The JSON register is the source of truth; no external packages or network are used.
"""

import argparse
import ast
from collections import Counter, defaultdict
import html
import json
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".gif"}
STATUS = {"当前使用", "候选", "待修正", "停用"}
AVAILABILITY = {"可调用", "仅参考", "待制作", "仅界面", "已删除"}
KINDS = {"portrait": "立绘", "background": "背景", "cg": "CG", "reference": "参考", "ui": "界面", "texture": "纹理"}
PARTS = {"portrait": 4, "background": 2, "cg": 3, "reference": 2, "ui": 2, "texture": 2}
NUMBER = re.compile(r"[0-9]{2,}")
TAG = re.compile(r"[a-z][a-z0-9_]*")
IMAGE_NAME = re.compile(r"[a-z][a-z0-9_]*(?: [a-z0-9_]+)+")
IMAGE_DEFINITION = re.compile(r"^\s*image\s+([\w ]+?)\s*(?:=\s*(.+)|:)\s*$")


class CatalogError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CatalogError(message)


def numbered(value, label, allow_zero=False):
    require(isinstance(value, str) and NUMBER.fullmatch(value), label + " 必须是至少两位的数字字符串")
    require(allow_zero or int(value) > 0, label + " 不能使用 00")


def image_definitions(game):
    """Read explicit image names, including ATL names for collision detection."""
    definitions = defaultdict(list)
    for source in sorted(game.rglob("*.rpy")):
        relative = source.relative_to(game)
        if source.name == "image_codes.rpy" or any(p in {"cache", "saves", "work"} for p in relative.parts):
            continue
        for line_number, line in enumerate(source.read_text(encoding="utf-8-sig").splitlines(), 1):
            match = IMAGE_DEFINITION.match(line)
            if match:
                definitions[" ".join(match[1].split())].append((match[2], f"{relative}:{line_number}"))
    return definitions


def original_image_path(name, definitions, trail=()):
    """Resolve only verifiable literal image paths / aliases / im.Scale wrappers."""
    require(name not in trail, "已有 image 定义形成循环：" + " -> ".join(trail + (name,)))
    entries = definitions.get(name, [])
    require(len(entries) == 1, f"目标 image {name!r} 应有唯一显式定义，实际 {len(entries)} 处")
    expression, location = entries[0]
    require(expression is not None, f"{location} 为 ATL 定义，不能静态确认原图；请先定义独立静态 image")
    try:
        node = ast.parse(expression, mode="eval").body
    except SyntaxError as error:
        raise CatalogError(f"{location} 无法静态解析 image 表达式：{error.msg}") from error
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
        if isinstance(node.func.value, ast.Name) and node.func.value.id == "im" and node.func.attr == "Scale" and node.args:
            node = node.args[0]
    require(isinstance(node, ast.Constant) and isinstance(node.value, str), f"{location} 只支持字符串、已有 image 别名或 im.Scale 的静态原图核对")
    value = node.value
    if value in definitions:
        return original_image_path(value, definitions, trail + (name,))
    return value


def validate_catalog(data, root=ROOT):
    require(isinstance(data, dict) and data.get("schema_version") == 1, "只支持 schema_version: 1")
    for key in ("characters", "expressions", "assets"):
        require(isinstance(data.get(key), list), f"{key} 必须是数组")
    reserved_codes = data.get("reserved_codes", [])
    require(isinstance(reserved_codes, list), "reserved_codes 必须是数组")
    reserved = set()
    for code in reserved_codes:
        require(isinstance(code, str), "保留编号必须是字符串")
        kind = next((kind for kind, prefix in KINDS.items() if re.fullmatch(
            prefix + r"[0-9]{2,}" + r"·[0-9]{2,}" * (PARTS[kind] - 1), code)), None)
        require(kind is not None, f"保留编号格式不合法：{code}")
        for index, part in enumerate(code[len(KINDS[kind]):].split("·")):
            numbered(part, f"保留编号 {code} 第 {index + 1} 段", allow_zero=kind == "portrait" and index == 3)
        require(code not in reserved, f"保留编号重复：{code}")
        reserved.add(code)
    characters = {}
    image_tags = set()
    declared_variables = set(re.findall(
        r"^\s*define\s+([a-z][a-z0-9_]*)\s*=\s*Character\(",
        (root / "game/characters.rpy").read_text(encoding="utf-8-sig"), re.MULTILINE,
    ))
    registered_variables = set()
    character_names = set()
    for char in data["characters"]:
        require(isinstance(char, dict), "角色登记必须是对象")
        numbered(char.get("id"), "角色编号")
        cid = char["id"]
        require(cid not in characters, f"角色编号重复：{cid}")
        require(isinstance(char.get("name"), str) and char["name"].strip(), f"角色 {cid} 缺少姓名")
        require(char["name"] not in character_names, f"角色姓名重复：{char['name']}")
        character_names.add(char["name"])
        require(isinstance(char.get("variables"), list) and all(isinstance(v, str) and TAG.fullmatch(v) for v in char["variables"]), f"角色 {cid} 的 variables 必须是变量名数组")
        for variable in char["variables"]:
            require(variable in declared_variables, f"角色 {cid} 的对白变量未在 characters.rpy 定义：{variable}")
            require(variable not in registered_variables, f"对白变量重复登记：{variable}")
            registered_variables.add(variable)
        tag = char.get("image_tag", "")
        require(isinstance(tag, str) and TAG.fullmatch(tag), f"角色 {cid} 的 image_tag 不合法")
        require(tag != "bg" and tag not in image_tags, f"角色 {cid} 的 image_tag 重复或占用 bg：{tag}")
        image_tags.add(tag)
        characters[cid] = char
    expressions = set()
    for expression in data["expressions"]:
        require(isinstance(expression, dict), "表情登记必须是对象")
        numbered(expression.get("id"), "表情编号", allow_zero=True)
        eid = expression["id"]
        require(eid not in expressions, f"表情编号重复：{eid}")
        require(isinstance(expression.get("name"), str) and expression["name"].strip(), f"表情 {eid} 缺少名称")
        expressions.add(eid)
    game = (root / "game").resolve()
    definitions = image_definitions(game)
    codes, aliases, registered_paths = set(), set(), set()
    for asset in data["assets"]:
        require(isinstance(asset, dict), "资产登记必须是对象")
        code = asset.get("code")
        require(isinstance(code, str) and code, "资产缺少 code")
        require(code not in reserved, f"图片代号属于已移出资产的保留编号，不得复用：{code}")
        require(code not in codes, f"图片代号重复：{code}")
        codes.add(code)
        kind = asset.get("kind")
        require(kind in KINDS, f"{code} 的 kind 不合法：{kind}")
        pattern = KINDS[kind] + r"[0-9]{2,}" + (r"·[0-9]{2,}" * (PARTS[kind] - 1))
        require(re.fullmatch(pattern, code), f"{code} 不符合 {KINDS[kind]} 的代号格式")
        parts = code[len(KINDS[kind]):].split("·")
        for index, part in enumerate(parts):
            numbered(part, f"{code} 第 {index + 1} 段", allow_zero=kind == "portrait" and index == 3)
        for field in ("title", "notes"):
            require(isinstance(asset.get(field), str), f"{code} 缺少文本字段 {field}")
        require(asset["title"].strip(), f"{code} 缺少中文名称")
        require(asset.get("status") in STATUS, f"{code} 的采用状态不合法")
        availability = asset.get("availability")
        require(availability in AVAILABILITY, f"{code} 的可用状态不合法")
        ids = asset.get("character_ids")
        require(isinstance(ids, list) and all(isinstance(cid, str) and cid in characters for cid in ids), f"{code} 引用了未登记的角色号")
        require(len(ids) == len(set(ids)), f"{code} 重复登记角色号")
        if kind in {"portrait", "reference"}:
            require(parts[0] in characters and parts[0] in ids, f"{code} 的首段角色号必须登记到 character_ids")
        if kind == "portrait":
            require(ids == [parts[0]], f"{code} 的立绘只能登记一个角色")
            require(parts[3] in expressions, f"{code} 引用了未登记表情号 {parts[3]}")
        path, target, alias = (asset.get(field) for field in ("path", "target", "alias"))
        if availability in {"待制作", "已删除"}:
            require(path is None and target is None and alias is None, f"{code} {availability}时 path/target/alias 必须为 null")
            if availability == "已删除":
                require(asset["status"] == "停用", f"{code} 已删除资产必须标为停用")
                require(all(field in asset for field in ("path", "target", "alias")), f"{code} 已删除资产必须显式登记 path/target/alias 为 null")
            continue
        require(isinstance(path, str) and path, f"{code} 缺少原图路径")
        relative = PurePosixPath(path)
        require("\\" not in path and not relative.is_absolute() and ".." not in relative.parts and ":" not in path, f"{code} 图片路径必须为 game 内相对路径")
        absolute = (game / path).resolve()
        require(game in absolute.parents and absolute.is_file(), f"{code} 图片不存在或越出 game：{path}")
        require(relative.suffix.lower() in SUFFIXES, f"{code} 不支持的图片格式：{path}")
        registered_paths.add(relative.as_posix())
        if kind in {"ui", "texture"}:
            require(availability == "仅界面", f"{code} 界面与纹理必须标为仅界面")
        if kind == "reference":
            require(availability == "仅参考", f"{code} 参考图必须标为仅参考")
        if availability != "可调用":
            require(target is None and alias is None, f"{code} 非剧情可调用资产不得设置 target/alias")
            continue
        require(kind in {"portrait", "background", "cg"}, f"{code} 的类别不能直接用于剧情")
        require(isinstance(target, str) and IMAGE_NAME.fullmatch(target), f"{code} 的目标 image 名不合法")
        require(isinstance(alias, str) and IMAGE_NAME.fullmatch(alias), f"{code} 的 alias 不合法")
        require(alias not in aliases and alias not in definitions, f"{code} 的 alias 已被占用：{alias}")
        aliases.add(alias)
        expected_tag = characters[parts[0]]["image_tag"] if kind == "portrait" else "bg"
        require(alias.split()[0] == target.split()[0] == expected_tag, f"{code} 的 alias、target 必须保持同一图层 tag：{expected_tag}")
        source = original_image_path(target, definitions)
        require(source == path, f"{code} 原图路径与 target 不一致：登记 {path}；目标 {source}")
    scanned = set()
    for folder in ("images", "lh", "gui"):
        for image in (game / folder).rglob("*"):
            if image.is_file() and image.suffix.lower() in SUFFIXES:
                scanned.add(image.relative_to(game).as_posix())
    missing = sorted(scanned - registered_paths)
    require(not missing, "以下项目图片尚未登记：\n" + "\n".join(missing))
    return data


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=4)


def generate_rpy(data):
    callable_assets = [a for a in data["assets"] if a["availability"] == "可调用"]
    names = {a["code"]: a["alias"] for a in callable_assets}
    unavailable = {a["code"]: f'{a["availability"]}：{a["title"]}' for a in data["assets"] if a["availability"] != "可调用"}
    lines = [
        "# Generated by tools/build_image_catalog.py; edit game/image_catalog.json instead.",
        "# Explicit aliases preserve original image transforms and replacement tags.", "",
    ]
    for asset in callable_assets:
        lines.append(f'image {asset["alias"]} = {json.dumps(asset["target"], ensure_ascii=False)}')
    lines += ["", "define IMAGE_CODE_NAMES = " + json_text(names), "", "define _IMAGE_CODE_UNAVAILABLE = " + json_text(unavailable), "", '''init python:
    def image_code(code):
        """Return an existing image alias; unknown/unavailable codes fail clearly.

        Prefer direct scene/show aliases. For show expression, keep the tag:
        show expression image_code("立绘04·01·01·00") as cds
        """
        if not isinstance(code, str):
            raise TypeError("图片代号必须是字符串，例如 CG01·01·01。")
        key = code.strip().replace(".", "·").replace("_", "·")
        if key in IMAGE_CODE_NAMES:
            return IMAGE_CODE_NAMES[key]
        if key in _IMAGE_CODE_UNAVAILABLE:
            raise ValueError("图片代号 {} 不能用于剧情（{}）；请查看图片代号总表。".format(key, _IMAGE_CODE_UNAVAILABLE[key]))
        raise KeyError("未登记图片代号 {}；请先在 image_catalog.json 登记并生成映射。".format(key))
''']
    return "\n".join(lines)


def md(value):
    return str(value).replace("|", "\\|").replace("\r", "").replace("\n", "<br>")


def image_url(path):
    return "../" + quote(path, safe="/") if path else None


def command(asset):
    if asset["availability"] != "可调用":
        return ""
    return ("show " if asset["kind"] == "portrait" else "scene ") + asset["alias"]


def generate_markdown(data):
    names = {c["id"]: c["name"] for c in data["characters"]}
    counts = Counter(a["availability"] for a in data["assets"])
    lines = [
        "# 图片代号总表", "",
        "> 此表由 `tools/build_image_catalog.py` 生成；请修改 `game/image_catalog.json` 后重新生成。", "",
        "[打开看图速查页](image_code_gallery.html) · [编号与写作说明](image_code_guide.md)", "",
        f"共 {len(data['assets'])} 条登记；" + "，".join(f"{key} {counts[key]}" for key in sorted(counts)) + "。", "",
        "采用状态与可用状态独立：候选图可能已接入测试；可调用不代表最终美术已确认。", "",
        "## 固定角色编号", "", "| 编号 | 角色 | 对白变量 | 图片 tag |", "|---|---|---|---|",
    ]
    for char in data["characters"]:
        lines.append(f'| {char["id"]} | {md(char["name"])} | {md(", ".join(char["variables"]))} | `{char["image_tag"]}` |')
    lines += ["", "## 表情编号", "", "00 表示原图表情尚未标准化；其余编号只定义含义，不代表所有角色已拥有对应图片。", "", "| 编号 | 表情 |", "|---|---|"]
    lines += [f'| {e["id"]} | {md(e["name"])} |' for e in data["expressions"]]
    for kind, title in KINDS.items():
        assets = [a for a in data["assets"] if a["kind"] == kind]
        lines += ["", f"## {title}（{len(assets)}）", "", "| 代号 | 名称／角色 | 状态／可用性 | Ren'Py 调用 | 原图 | 用途与说明 |", "|---|---|---|---|---|---|"]
        for asset in assets:
            people = "、".join(names[cid] for cid in asset["character_ids"])
            label = asset["title"] + (" / " + people if people else "")
            path = f'[查看]({image_url(asset["path"])})' if asset["path"] else asset["availability"]
            call = f'`{command(asset)}`' if command(asset) else "—"
            lines.append(f'| `{asset["code"]}` | {md(label)} | {asset["status"]} / {asset["availability"]} | {call} | {path} | {md(asset["notes"])} |')
    return "\n".join(lines) + "\n"


HTML_TEMPLATE = '''<!doctype html>
<html lang="zh-CN">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>图片代号速查 · 剑来</title>
<style>
:root{color-scheme:light;--paper:#f4f1e9;--ink:#253b36;--muted:#67726d;--line:#d8ddd2;--accent:#355c50}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 system-ui,"Microsoft YaHei",sans-serif}
header,main{max-width:1500px;margin:auto;padding:30px 32px}header{padding-bottom:8px}.eyebrow{font-size:12px;letter-spacing:.2em;color:var(--muted)}h1{font:700 clamp(26px,4vw,42px)/1.3 Georgia,serif;margin:9px 0 12px}p{margin:8px 0;color:var(--muted)}a{color:var(--accent)}
.controls{display:grid;grid-template-columns:2fr 1fr 1fr;gap:14px;margin:20px 0 12px}label{display:block;font-size:13px;font-weight:650}input,select,button,textarea{font:inherit}input,select{display:block;width:100%;margin-top:5px;border:1px solid #a7b9ad;border-radius:7px;padding:10px;background:#fff;color:var(--ink)}
button{border:1px solid #9aada0;background:#fff;color:var(--ink);padding:7px 11px;border-radius:6px;cursor:pointer;font-size:13px}button:hover{background:#e6ede6}button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #518977;outline-offset:3px}
.toolbar{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:15px 0}.toolbar span{font-size:14px;color:var(--muted)}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(285px,1fr));gap:20px}.card{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;min-width:0}.preview{display:flex;align-items:center;justify-content:center;aspect-ratio:16/9;background:repeating-conic-gradient(#e8e6e0 0% 25%,#f3f1eb 0% 50%) 50%/24px 24px;text-decoration:none;color:var(--muted)}.preview img{width:100%;height:100%;object-fit:contain}.content{padding:17px}.code{font-weight:750;font-size:18px;letter-spacing:.03em;margin:0}.card h2{font-size:16px;margin:5px 0 6px;font-weight:550}.badges{display:flex;flex-wrap:wrap;gap:6px}.badge{font-size:11px;padding:2px 8px;background:#edf0e9;border-radius:10px}.callable{background:#dcebe0;color:#255442}.note{font-size:13px;min-height:40px}.path{font-size:11px;overflow-wrap:anywhere;color:var(--muted)}.snippet{display:block;font-size:12px;white-space:pre-wrap;overflow-wrap:anywhere;background:#f2f5f0;padding:8px;border-radius:5px;margin:12px 0}.actions{display:flex;gap:8px;flex-wrap:wrap}.empty{border:1px dashed #9aaea2;padding:40px;text-align:center;border-radius:10px}.toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);max-width:90vw;background:#253b36;color:white;border-radius:8px;padding:10px 20px;box-shadow:0 3px 15px #0003;font-size:14px;z-index:3}dialog{max-width:92vw;width:560px;border:1px solid var(--line);border-radius:10px;padding:24px}dialog::backdrop{background:#0006}dialog textarea{width:100%;min-height:100px;resize:vertical;padding:10px;margin:10px 0}footer{font-size:12px;color:var(--muted);margin:35px 0 0}details{margin:12px 0;font-size:14px}summary{cursor:pointer}details p{max-width:950px}[hidden]{display:none!important}
@media(max-width:650px){header,main{padding:20px 16px}.controls{grid-template-columns:1fr 1fr}.controls label:first-child{grid-column:1/-1}.grid{grid-template-columns:1fr}h1{font-size:29px}.toolbar{align-items:flex-start}}
</style></head>
<body><header><div class="eyebrow">WHEN THE SWORD ARRIVES · 写作工具</div>
<h1>图片代号速查</h1><p>选图、复制代号、继续写故事。点击缩略图可打开原图；本页离线可用。</p>
<details><summary>编号与使用说明</summary><p>立绘：角色 · 服装 · 姿势 · 表情；背景：场景 · 差分；CG：章节 · 事件 · 差分。参考：角色 · 条目。界面与纹理单独登记。编号固定，不随排序改变。</p><p>默认仅展示可调用的剧情图片。候选图可能已用于测试；表情 00 代表原图表情未标准化。“待制作”只占号，没有可调用图片。</p><p>复制 Ren'Py 调用会保留原图片 tag，便于同一角色换图。站位、缩放与转场另写。详细规则见 <a href="image_code_guide.md">写作规范</a>，完整清单见 <a href="image_code_catalog.md">总表</a>。</p></details>
<div class="controls"><label>搜索<input id="search" type="search" placeholder="输入人名、代号、用途或文件名" autocomplete="off"></label><label>图片类别<select id="kind"><option value="">全部类别</option>__KIND_OPTIONS__</select></label><label>可用状态<select id="availability"><option value="可调用" selected>剧情可调用</option><option value="">全部状态</option><option value="仅参考">仅参考</option><option value="待制作">待制作</option><option value="仅界面">仅界面</option><option value="已删除">已删除</option></select></label></div>
</header><main><div class="toolbar"><span id="count" role="status" aria-live="polite"></span><button id="reset" type="button">重置筛选</button></div><div id="grid" class="grid"></div><p id="empty" class="empty" hidden>没有匹配图片。请缩短搜索词，或将可用状态切换为“全部状态”。</p><noscript><p>浏览器已禁用脚本。请打开旁边的 <a href="image_code_catalog.md">图片代号总表</a>。</p></noscript><footer>由项目图片登记表生成。新增、修订或确认图片后，请更新登记表并重新生成本页。</footer></main>
<div id="toast" class="toast" role="status" aria-live="polite" hidden></div>
<dialog id="copy-dialog"><h2>手动复制</h2><p>浏览器暂不允许自动复制，内容已选中，请按 Ctrl+C（Mac 使用 ⌘C）。</p><textarea id="copy-text" readonly aria-label="待复制内容"></textarea><button id="close-copy" type="button">完成</button></dialog>
<script id="catalog-data" type="application/json">__CATALOG_DATA__</script>
<script>
"use strict";
const assets = JSON.parse(document.getElementById("catalog-data").textContent);
const search = document.getElementById("search"), kind = document.getElementById("kind"), availability = document.getElementById("availability"), grid = document.getElementById("grid");
const normalize = value => value.trim().replace(/[._]/g, "·");
let toastTimer;
function toast(message) { const element = document.getElementById("toast"); element.textContent = message; element.hidden = false; clearTimeout(toastTimer); toastTimer = setTimeout(() => { element.hidden = true; }, 2300); }
async function copy(value) {
  try { if (navigator.clipboard && window.isSecureContext) { await navigator.clipboard.writeText(value); toast("已复制"); return; } } catch (_) {}
  const previous = document.activeElement, area = document.createElement("textarea"); area.value = value; area.style.cssText = "position:fixed;left:-9999px;top:0"; document.body.append(area); area.select();
  let success = false; try { success = document.execCommand("copy"); } catch (_) {} area.remove(); if (previous) previous.focus();
  if (success) { toast("已复制"); return; }
  const dialog = document.getElementById("copy-dialog"), field = document.getElementById("copy-text"); field.value = value; dialog.showModal(); field.focus(); field.select();
}
function element(tag, className, text) { const node = document.createElement(tag); if (className) node.className = className; if (text !== undefined) node.textContent = text; return node; }
function card(asset) {
  const article = element("article", "card"), preview = element(asset.url ? "a" : "div", "preview");
  if (asset.url) { preview.href = asset.url; preview.title = "打开原图：" + asset.title; const image = element("img"); image.src = asset.url; image.alt = asset.title; image.loading = "lazy"; image.decoding = "async"; image.addEventListener("error", () => { preview.textContent = "原图无法加载，请检查路径"; }); preview.append(image); } else { preview.textContent = asset.availability === "已删除" ? "已删除 · 保留编号" : "待制作 · 尚无原图"; }
  article.append(preview); const body = element("div", "content"); body.append(element("p", "code", asset.code), element("h2", "", asset.title));
  const badges = element("div", "badges"); [asset.kind_name, asset.status, asset.availability].forEach(text => badges.append(element("span", "badge" + (text === "可调用" ? " callable" : ""), text))); body.append(badges);
  if (asset.people) body.append(element("p", "note", asset.people)); body.append(element("p", "note", asset.notes));
  if (asset.path) body.append(element("p", "path", asset.path)); if (asset.command) body.append(element("code", "snippet", asset.command));
  const actions = element("div", "actions"), writing = element("button", "", "复制写作代号"); writing.type = "button"; writing.addEventListener("click", () => copy("【" + asset.code + "】")); actions.append(writing);
  if (asset.command) { const renpy = element("button", "", "复制 Ren'Py 调用"); renpy.type = "button"; renpy.addEventListener("click", () => copy(asset.command)); actions.append(renpy); } body.append(actions); article.append(body); return article;
}
function render() {
  const query = search.value.trim().toLocaleLowerCase(), canonical = normalize(query);
  const matches = assets.filter(asset => (!kind.value || asset.kind === kind.value) && (!availability.value || asset.availability === availability.value) && (!query || asset.search.includes(query) || normalize(asset.search).includes(canonical)));
  const fragment = document.createDocumentFragment(); matches.forEach(asset => fragment.append(card(asset))); grid.replaceChildren(fragment); document.getElementById("count").textContent = "显示 " + matches.length + " / " + assets.length + " 条登记"; document.getElementById("empty").hidden = matches.length !== 0;
}
search.addEventListener("input", render); kind.addEventListener("change", render); availability.addEventListener("change", render);
document.getElementById("reset").addEventListener("click", () => { search.value = ""; kind.value = ""; availability.value = "可调用"; render(); search.focus(); });
document.getElementById("close-copy").addEventListener("click", () => document.getElementById("copy-dialog").close());
render();
</script></body></html>
'''


def generate_html(data):
    characters = {c["id"]: c["name"] for c in data["characters"]}
    assets = []
    for asset in data["assets"]:
        item = dict(asset)
        item["people"] = "、".join(characters[cid] for cid in asset["character_ids"])
        item["kind_name"] = KINDS[asset["kind"]]
        item["url"] = image_url(asset["path"])
        item["command"] = command(asset)
        item["search"] = " ".join(str(item[key] or "") for key in ("code", "title", "people", "notes", "path", "alias", "target", "status", "availability")).lower()
        assets.append(item)
    # Escape script delimiters even though all UI content is assigned via textContent.
    payload = json.dumps(assets, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    options = "".join(f'<option value="{html.escape(kind, quote=True)}">{html.escape(label)}</option>' for kind, label in KINDS.items())
    return HTML_TEMPLATE.replace("__KIND_OPTIONS__", options).replace("__CATALOG_DATA__", payload)


def outputs(data, code_only=False):
    generated = {"game/image_codes.rpy": generate_rpy(data)}
    if not code_only:
        generated.update({
            "game/Codex/image_code_catalog.md": generate_markdown(data),
            "game/Codex/image_code_gallery.html": generate_html(data),
        })
    return generated


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="只校验登记及生成文件是否同步，不写文件")
    parser.add_argument("--code-only", action="store_true", help="只生成或检查 game/image_codes.rpy，不处理文档与看图页")
    args = parser.parse_args(argv)
    try:
        data = json.loads((ROOT / "game/image_catalog.json").read_text(encoding="utf-8-sig"))
        validate_catalog(data)
        generated = outputs(data, code_only=args.code_only)
        if args.check:
            stale = [path for path, content in generated.items() if not (ROOT / path).is_file() or (ROOT / path).read_text(encoding="utf-8") != content]
            refresh = "python tools/build_image_catalog.py" + (" --code-only" if args.code_only else "")
            require(not stale, "生成文件缺失或未同步，请运行 " + refresh + "：\n" + "\n".join(stale))
        else:
            for path, content in generated.items():
                destination = ROOT / path
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open("w", encoding="utf-8", newline="\n") as stream:
                    stream.write(content)
        print(f"图片代号{'校验通过' if args.check else '生成完成'}：{len(data['assets'])} 条登记，{sum(a['availability'] == '可调用' for a in data['assets'])} 条剧情可调用，{len(generated)} 个产物同步。")
        return 0
    except (CatalogError, OSError, json.JSONDecodeError) as error:
        print(f"图片代号校验失败：{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
