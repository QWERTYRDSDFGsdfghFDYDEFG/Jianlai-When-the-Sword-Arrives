# When the Sword Arrives

一款基于《剑来》书简湖篇改编的非商业 Ren'Py 视觉小说。陈平安离开大隋书院，去书简湖见旧友顾璨。一路上的规矩、人情与选择，将他带入崔巉布下的问心局。

## 项目状态

项目处于可玩原型阶段，主线已从序章连到第十二章。下一步是补齐关键场景的画面与音频，完成首轮外部试玩验收。

- **第二章剧情**采用 2026-10-29 确认稿，共 19 段、487 条正文。三人在紫阳府留宿一夜，陈平安与朱敛在宴前长谈，翌晨离府。[当前剧本](game/script_chapter2.rpy) · [改编与验收记录](game/Codex/story_compression_record.md)
- **第二章画面**已接入登船、入府、赴宴等段落的部分镜头。雨停廊下已有两句配图，宴前长谈、席间和雨夜仍有缺图。补图时按当前分镜定位。[第二章分镜与缺图清单](game/Codex/chapter2_storyboard.md)
- **试玩功能**支持存读档、回看及快进。对白默认 A2，可在设置中切换到 B2。通读序章后，会解锁陈平安与李宝瓶的回廊背景，可在画像鉴赏中查看。[对白布局记录](work/art/dialogue_no_portrait/record.json) · [画像鉴赏记录](game/Codex/art_gallery_plan.md)

## 本地运行

在 Ren'Py Launcher 中导入本项目根目录（包含 `game` 的这一层），选中项目并点击 `Launch Project`。从主菜单选择「新游戏」进入序章。测试主线、存读档和菜单时，按[第一版可玩验收清单](game/Codex/01_FIRST_PLAYABLE.md)逐项检查。

## 开发入口

协作前先读[项目约定](AGENTS.md)。修改 `game/` 下的内容时，再读[游戏工程约定](game/AGENTS.md)。

| 要做的事 | 从这里开始 |
| --- | --- |
| 查故事范围、设计方向或章节规划 | [叙事边界](game/GDD.md) · [玩法设计](GDD.md) · [章节规划](game/README.md#章节规划) |
| 查角色母版或确认图片采用状态 | [角色与图片索引](game/Codex/character_image_index.md) |
| 在剧本中调用图片 | [代号写法](game/Codex/image_code_guide.md) · [按图查代号](game/Codex/image_code_gallery.html) |
| 制作场景图或主菜单背景 | [场景图制作流程](.agents/skills/jianlai-scene-production/SKILL.md) · [主菜单背景规范](game/Codex/main_menu_background_sop.md) |

维护本页时，直接更新对应的现状条目。每轮试作、返工和验收细节写入对应制作记录，在这里保留入口即可。

## 版权与协作

《剑来》的世界观、角色与设定归原作者及相关版权方所有。部分音频和参考素材仅供学习与原型验证，公开试玩前须核实授权并替换不适合公开的素材。

欢迎提交试玩反馈、剧情校对意见或 Pull Request。维护者邮箱 `1622381732@qq.com`，X / Twitter 账号 `@p2GEEign7`。
