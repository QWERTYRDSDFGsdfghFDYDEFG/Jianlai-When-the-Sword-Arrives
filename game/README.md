# When the Sword Arrives

> 基于《剑来》书简湖篇改编的 2D 叙事游戏 / 视觉小说原型。  
> 核心体验不是战力成长，而是规矩、人情、选择与代价。

---

## 项目现状

当前工程处于 **Ren'Py 可玩原型开发阶段**。

已经具备：

- 基础 Ren'Py 工程结构
- 主菜单、设置、存档、读档等默认流程
- 从 `label start` 到 `chapter12_start` 的完整主线跳转链
- 多章主线脚本
- 部分背景、角色图与音频素材

当前重点：

- 重排章节节奏与断点
- 补齐基础演出、立绘、背景与音频
- 做出可交给外部测试者的第一版可玩流程

---

## 文档入口

先按这个顺序读：

1. `README.md`：项目状态、剧情范围、目录入口
2. `GDD.md`：设计目标、体验基调、叙事边界
3. `Codex/00_MASTER_PROMPT.md`：工程执行规则
4. `Codex/01_FIRST_PLAYABLE.md`：第一版可玩验收口径

按任务类型补读：

- 演出 / 分镜 / 立绘摆位：`《剑来》VN演出与构图总手册.md`
- 角色图工作流：`Codex/character_image_index.md`
- 陈平安出图：`陈平安出图总手册.md`
- 序章逐场执行：`script逐场分镜表.md`、`script_RenPy演出脚本执行表.md`
- Chapter 2-5 逐场执行：`script_chapter2~5逐场分镜表.md`、`script_chapter2~5_RenPy演出脚本执行表.md`
- 剧情瘦身记录：`Codex/story_compression_record.md`

---

## 故事范围

当前主线围绕《剑来》书简湖篇展开，时间线大致从：

> 陈平安离开大隋山崖书院  
> 到  
> 书简湖问心局结束，陈平安继续北归

重点内容包括：

- 山崖书院分别后的归乡路
- 入书简湖前的顾璨危机预警
- 顾璨与青峡岛母子的问心主线
- 刘志茂、刘老成、刘重润、马远致等人物线
- 书简湖大势与崔瀺布局的上层揭示

---

## 章节规划

现有脚本跳转链：

```text
script.rpy
  -> script_chapter2.rpy
  -> script_chapter3.rpy
  -> script_chapter4.rpy
  -> script_chapter5.rpy
  -> script_chapter6.rpy
  -> script_chapter7.rpy
  -> script_chapter8.rpy
  -> script_chapter9.rpy
  -> script_chapter10.rpy
  -> script_chapter11.rpy
  -> script_chapter12.rpy
```

当前“文件章节”不等于最终“游戏章节”。短期先保持可运行，长期按下表逐步重整：

| 最终章 | 章节名 | 对应来源 |
| --- | --- | --- |
| 序章 | 山崖别离 | `script.rpy` |
| 第一章 | 归乡路上 | `script_chapter2.rpy` + `script_chapter3.rpy` + `script_chapter4.rpy` 前半 |
| 第二章 | 书简湖初见 | `script_chapter4.rpy` 后半 |
| 第三章 | 青峡岛饭桌 | `script_chapter5.rpy` |
| 第四章 | 心中杀刀 | `script_chapter6.rpy` |
| 第五章 | 请你不要失望 | `script_chapter7.rpy` 前半 |
| 第六章 | 红酥小传 | `script_chapter7.rpy` 后半 + `script_chapter8.rpy` 尾部 |
| 第七章 | 善恶一线 | `script_chapter8.rpy` 主体 |
| 第八章 | 珠钗岛与阎王殿 | `script_chapter9.rpy` |
| 第九章 | 亡魂账本 | `script_chapter10.rpy` 前段 |
| 第十章 | 小泥鳅问心 | `script_chapter10.rpy` 中段 |
| 第十一章 | 刘志茂的酒碗 | `script_chapter10.rpy` 后段 |
| 第十二章 | 雪中顾璨 | `script_chapter10.rpy` 结尾 |
| 第十三章 | 宫柳岛旧情 | `script_chapter11.rpy` 前半 |
| 第十四章 | 年关阴物 | `script_chapter11.rpy` 后半 |
| 第十五章 | 山盟与远路 | `script_chapter12.rpy` 前段 |
| 第十六章 | 书简湖大变 | `script_chapter12.rpy` 中前段 |
| 第十七章 | 三返青峡岛 | `script_chapter12.rpy` 中段 |
| 第十八章 | 新约 | `script_chapter12.rpy` 中后段 |
| 第十九章 | 离湖 | `script_chapter12.rpy` 后段 |
| 第二十章 | 先生缓缓归 | `script_chapter12.rpy` 结尾 |

优先整理顺序：

1. `script_chapter12.rpy`
2. `script_chapter10.rpy`
3. `script_chapter11.rpy`
4. `script_chapter2.rpy` + `script_chapter3.rpy`

---

## 主要目录

```text
.
├── README.md
├── GDD.md
├── Codex/
├── script.rpy
├── script_chapter*.rpy
├── characters.rpy
├── bg_images.rpy
├── audio_index.rpy
├── mood_system.rpy
├── screens.rpy
├── gui.rpy
├── images/
├── audio/
├── gui/
└── lh/
```

其中：

- `lh/`：角色母版、身份标准、补图计划
- `Codex/`：工作流、命名、导入、生图规则
- `script*.rpy`：剧情脚本

---

## 本地运行

1. 安装 Ren'Py。
2. 在 Ren'Py Launcher 中导入本项目目录。
3. 点击 `Launch Project`。

最少自检：

- 新游戏可从 `label start` 进入
- `jump` 链不断
- 角色名均已定义
- 图片、音频路径存在
- 存档、读档、快进、回看、设置菜单可用

---

## 版权说明

本项目为非商业性质同人创作与游戏开发实践项目。  
《剑来》相关世界观、角色与设定版权归原作者及相关版权方所有。  
项目中的部分音频和参考素材仅用于学习、研究与非商业原型验证。