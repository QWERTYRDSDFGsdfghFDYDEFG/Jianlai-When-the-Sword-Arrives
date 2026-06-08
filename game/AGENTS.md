# When the Sword Arrives（项目工作约定 / 快速入口）

> 适用范围：本文件所在目录及其子目录（整个 `game/` 工程树）。

---

## 0. 安全与操作红线（必须遵守）

### 禁止批量删除

禁止批量删除文件或目录。

不要使用：
- `del /s`、`rd /s`、`rmdir /s`
- PowerShell：`Remove-Item -Recurse`
- `rm -rf`

需要删除文件时，只能一次删除一个明确路径的文件。

正确示例：
- `Remove-Item "C:\path\to\file.txt"`

如果确实需要批量删除：停止操作，改由你（用户）手动删除后我再继续。

### 不擅自大改结构/不删既有内容

- 不一次性重写目录结构。
- 不擅自删除已有剧情、素材、系统文件或 Ren'Py 生成/依赖文件。
- 先保证可运行，再增强表现（剧情、演出、资源、UI、系统）。

---

## 1. 项目是什么（定位）

- 类型：Ren'Py 2D 叙事游戏 / 视觉小说原型
- 题材：基于《剑来》“书简湖篇”改编（同人性质的原型验证）
- 核心体验：不以“战力成长”为主，而是“规矩/人情/选择/代价”的问心主题；节奏偏慢、留白、沉静、压抑。
- 当前状态：可玩原型开发阶段（主线脚本已连通到 `chapter12_start`）。

入口文档（先读）：
- `README.md`：项目状态、剧情范围、章节规划与短期建议
- `GDD.md`：目标、体验、表现风格与修改约束
- `Codex/00_MASTER_PROMPT.md`：通用执行原则（别删、别乱改结构、先跑起来）
- `Codex/01_FIRST_PLAYABLE.md`：第一版可玩原型验收与测试流程
- `Codex/剧情压缩删减记录.md`：仅记录可压缩/可删减候选（含定位方式）

---

## 2. 如何运行（本地启动）

1. 安装 Ren'Py（使用 Ren'Py Launcher）。
2. 在 Ren'Py Launcher 中 `Add Existing Project` / 导入本目录：`E:\新建文件夹\When the Sword Arrives\game`。
3. 点击 `Launch Project` 运行。

运行时关键自检点：
- 新游戏从 `label start` 进入不报错。
- `jump` 链不断、不会黑屏卡死。
- 角色名均已定义（见 `characters.rpy`）。
- 背景图片/音频路径存在（缺失会直接报错）。
- 存档/读档/快进/回看/设置菜单可用。

---

## 3. 目录结构（你应该先看哪些）

核心脚本与系统：
- `script.rpy`：开场入口（`label start`）
- `script_chapter2.rpy` ~ `script_chapter12.rpy`：当前章节脚本（通过 `jump chapter2_start` 等连接）
- `characters.rpy`：角色变量（Character）定义；新增角色必须先在这里补齐
- `bg_images.rpy`：背景资源 `image bg ...` 定义（含必要的 `im.Scale(...)`）
- `audio_index.rpy`：配音 ID 映射表（脚本里用 `voice voice_id("...")`）
- `mood_system.rpy`：心境 HUD/菜单与数值调整 API（见 `story_mood_event` / `story_mood_choice`）
- `screens.rpy`、`gui.rpy`、`options.rpy`：UI、界面、构建/偏好与工程配置

资源目录：
- `images/`：背景/角色/CG 等图片（`bg_images.rpy` 引用这里的文件）
- `audio/`：音频资源（含 `audio/voice/...` 配音分目录）
- `gui/`：Ren'Py GUI 资源

运行时/生成物（一般不需要手工改）：
- `cache/`：Ren'Py 缓存
- `saves/`：存档（不同机器通常也会在用户目录的 Ren'Py 存档路径）
- `*.rpyc`：Ren'Py 编译产物（不要手改；修改应改对应 `.rpy`）

---

## 4. 脚本与资源约定（写法要一致）

### 4.0 图片生成尺寸统一要求

- 后续所有新生成图片（包括角色立绘、CG、背景、宣传图、参考图）默认目标尺寸统一为 `1920 x 1080`。
- 如无用户明确批准，不要擅自改成其他分辨率或纵向尺寸。
- 若某次出图工具本身不便直接精确控制尺寸，也必须在提示词或流程中优先朝 `1920 x 1080` 的横版成图目标靠拢。

### 4.0.1 角色出图前，先查身份索引

- 当用户要求生成、修改、重绘某个角色的图片、立绘、表情图、动作图、场景图时，必须先查看 `Codex/角色出图身份索引.md`。
- 若索引中已登记该角色，必须先读取对应身份标准文件，再编写提示词或进入出图流程。
- 若该角色在索引中同时挂有“逐场分镜表”与“Ren'Py 演出脚本执行表”，也必须一起查看，不要只看人设文件。
- 不要依赖用户每次手动提醒“先看某某标准文件”。
- 若用户只说简称、别名或习惯叫法，也应先按索引中的触发词匹配。
- 若索引中没有该角色，先在 `lh/` 目录与相关标准文件中查找；若仍无结果，再向用户确认是否需要为该角色建立新的身份标准。

当前已建立明确映射的角色示例：
- 陈平安 -> `lh/cpa/CPA_FACE_IDENTITY_STANDARD.md`
- 裴钱 -> `lh/peiqian/PEIQIAN_FACE_IDENTITY_STANDARD.md`

### 4.0.2 角色图不只看人设，还要看场次演出口径

- 如果用户要的不是泛用立绘，而是“某角色在某一场戏里的图”，必须同时回查该角色关联的分镜表与演出表。
- 序章 / `script.rpy` 相关，优先看：
  - `script逐场分镜表.md`
  - `script_RenPy演出脚本执行表.md`
- Chapter 2 到 Chapter 5 相关，优先看：
  - `script_chapter2~5逐场分镜表.md`
  - `script_chapter2~5_RenPy演出脚本执行表.md`
- 角色身份标准负责锁定“这个人是谁”；分镜表和演出表负责锁定“这场戏怎么站、怎么演、怎么构图”。

### 4.1 配音：用稳定 ID，不要在剧情里写硬路径

- 规范：剧情脚本中写 `voice voice_id("voice.xxx")`
- 映射：在 `audio_index.rpy` 的 `VOICE_INDEX` 里维护 `"voice.xxx" -> "audio/voice/.../0001.mp3"`
- 好处：脚本稳定、资源路径可重排、缺失时能快速定位

### 4.2 背景：统一在 `bg_images.rpy` 定义 `image bg ...`

- 脚本中尽量只写：`scene bg xxx`
- 新增图片后：先补 `bg_images.rpy` 的 `image bg ... = "images/..."` 再使用

### 4.3 角色：先定义再使用

- 所有说话人变量在 `characters.rpy` 定义（例如 `define cpa = Character("陈平安")`）
- 脚本里出现新说话人前，先把变量补齐，避免运行时报 `NameError`/未定义角色

### 4.4 心境系统（mood）：用现成 API

当前位置：
- `mood_system.rpy` 会把 `mood_hud` 加到 `config.overlay_screens`，非主菜单显示 HUD。

常用调用：
- 事件驱动：`$ story_mood_event("a", "separation")`
- 选择驱动：`$ story_mood_choice("a", "listen")`
- 直接设置：`$ set_mood("a", 60, "detail")`（必要时）

注意：
- `mood_profiles` 的 key 与角色变量不一定同名（例如 `"a"` 对应“李宝瓶”）。
- 若新增 key/事件/选项，请同步维护 `mood_event_delta` / `mood_choice_delta` 的映射。

---

## 5. 第一版可玩（First Playable）交付口径

以 `Codex/01_FIRST_PLAYABLE.md` 为准，核心目标是“可交给外部测试者游玩的最小版本”：
- 能启动/退出
- 能从头读到一个明确结束点（10–30 分钟一次流程）
- 有基础音画呈现
- 若有选项，选项都能得到有效结果且不会破坏主线
- 存档/读档可用（至少 3 个不同位置验证）

每次改完后应至少做静态检查：
- 引号是否闭合、字符串是否跨行错误
- label / jump 是否断链
- 角色变量是否已定义
- 图片/音频路径是否存在且拼写一致

---

## 6. 当前已知信息（便于快速定位）

- 工程名/构建名：`Jianlai-When-the-Sword-Arrives`（见 `options.rpy`）
- 版本号：`1.0`（见 `options.rpy`）
- 存档目录标识：`WhentheSwordArrives-1771234683`（见 `options.rpy`）
- 自动存档：更高频率（`config.autosave_frequency = 10`，并在选项前自动保存）
- 配音偏好：默认开启 `preferences.voice_sustain = True`，并对旧偏好做一次性修正（见 `options.rpy`）
