# 图片代号化交付与验证

2026-09-18。用户批准方案后实施。入口：[看图速查页](../../game/Codex/image_code_gallery.html)、[代号总表](../../game/Codex/image_code_catalog.md)、[写作指南](../../game/Codex/image_code_guide.md)。

## 实现结果

- 覆盖 `game/images/`、`game/lh/`、`game/gui/` 的 160 张真实图片，共 163 条登记。多出的记录为同一崔东山原图的测试立绘用途和两条待制作需求。
- 24 条剧情 CG、23 条参考、3 条立绘、99 条界面、14 条模型纹理；其中 20 张 CG 和 1 张测试立绘可用于剧情调用。当前没有独立无人背景，背景编号规则已预留。
- 固定 71 个角色编号、9 个表情编号。表情 `00` 表示未标准化原图表情，`05` 表示害羞；没有素材的组合不会自动变成可调用资产。
- 中文代号、现有资源名和实际文件由唯一登记表映射。保留原文件与原 image 定义；未批量改名、修改或复制图片，未改主线文本和既有演出调用。
- 速查页支持名称/代号/用途搜索、类别和可用性筛选、空结果提示、原图查看、写作代号和程序调用复制。

## 修改文件

| 文件 | 作用 |
| --- | --- |
| `game/image_catalog.json` | 唯一可维护的角色、表情与图片登记表 |
| `tools/build_image_catalog.py` | 生成及校验映射、总表和速查页，纯 Python 标准库 |
| `game/image_codes.rpy` | 生成的 21 个兼容别名和中文代号查询函数 |
| `game/Codex/image_code_catalog.md` | 生成的代号总表 |
| `game/Codex/image_code_gallery.html` | 生成的本地看图速查页 |
| `game/Codex/image_code_guide.md` | 编号、写作与更新说明 |
| `game/image_codes_test.rpy` | 独立测试场景、存档隔离与专项运行检查 |
| `README.md`、`game/AGENTS.md`、`game/Codex/naming_guidelines.md`、`game/Codex/character_image_index.md` | 局部补充入口与稳定代号约定，保留原有用户修改 |
| `work/image_codes/.gitignore`、本文件 | 忽略本地验收输出并记录交付结果 |

## 验证结果

1. `python -B tools/build_image_catalog.py --check` 通过：163 条登记、21 条可调用映射、3 个生成产物同步；覆盖全部 160 张原图路径，检查重复编号、角色变量、角色标识、目标原图与别名冲突。
2. 目录错误拦截检查通过：重复代号、缺图、越界路径、错误目标、错误角色标识、待制作却带文件、参考图误登记为剧情可调用均被拒绝；角色变量漏定义和重复占用另行验证。
3. Ren'Py 8.5.3 lint 成功完成，无新增语法、图片引用或章节跳转错误。已有 `im.Scale/im.Crop` 过时提示和中文文件名打包提示保留，本次未改动相关资源。
4. `test image_codes` 最终运行 4 个用例、44 项断言全部通过，耗时约 12.4 秒。覆盖新旧图片名混用、同角色替换、两个独立显示标识、场景清理与退场、三处保存后读取恢复、未知/仅参考/待制作代号报错、回看、快进、设置、存档/读档页面、退出确认、新游戏入口，以及第二至第十二章的快速推进。
5. 已查看运行截图：原图与别名显示正常，新游戏画面保持原样。测试图使用专用缩放以完整显示现有纵向灰蓝实底参考，未改生产演出变换。
6. 本地浏览器页面验收通过：默认 21 条可调用记录、下划线代号搜索、按角色查参考、两条待制作需求、空结果、筛选重置、同页打开原图并返回、复制成功反馈；1280 像素桌面宽度和 390 像素窄屏可读，窄屏无横向溢出。

本地日志、截图和隔离存档在 `qa/`（已忽略）。测试脚本只在指定测试命令或显式 QA 环境变量的 lint/test 命令中重定向存档，普通游戏运行不触发。

## 复验入口

在仓库根目录生成或检查：

```powershell
python -B tools/build_image_catalog.py
python -B tools/build_image_catalog.py --check
```

SDK 位置以根目录 `renpy-sdk-path.txt` 为准。本次使用其内置控制台 Python 调用 `renpy.py`，避免图形启动器的输出管道问题：

```powershell
$env:JIANLAI_IMAGE_CODE_QA_ROOT = Join-Path (Get-Location) 'work/image_codes/qa'
& 'F:\Tools\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe' 'F:\Tools\renpy-8.5.3-sdk\renpy.py' (Get-Location).Path lint 'work/image_codes/qa/lint.txt' --keep-orphan-rpyc
& 'F:\Tools\renpy-8.5.3-sdk\lib\py3-windows-x86_64\python.exe' 'F:\Tools\renpy-8.5.3-sdk\renpy.py' (Get-Location).Path test image_codes --keep-orphan-rpyc --overwrite-screenshots
```

## 未验证范围与现有限制

- 没有加载用户原有存档，也没有逐段人工阅读全部章节及选择分支；已验证的是隔离环境内的新旧图片名混用及三处新建存档恢复。
- 浏览器工具允许本地 HTTP 预览，但禁止 `file://` 导航，因此未自动验证双击 HTML 的离线打开；页面不依赖远程脚本或网络接口。复制按钮显示成功，但自动化工具的虚拟剪贴板不能回读浏览器剪贴板，未完成跨应用粘贴验证。
- 崔东山可调用立绘仍是既有灰蓝实底测试图，尚非透明正式立绘。两条待制作需求不能调用。本次不补图、不裁切表情页、不改变美术采用结论。
- 少量旧身份文档引用的母版或标准文件缺失，已在对应记录说明；存在于磁盘的已确认参考与实际运行文件分别登记，不用猜测补路径。
- 本次是 Windows 工程验收，未重新打包试玩版，也未验证其他平台。
