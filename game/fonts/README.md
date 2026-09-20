# 游戏中文字体

正文、角色姓名与界面统一在 `game/gui.rpy` 引用 `noto_sans_sc_light.ttf`。

- 字体：Noto Sans SC，静态 Light，字重 300，与原精简字库的字重一致。
- 字库：保留原字体全部 30,890 个 Unicode 映射，没有按当前剧情裁剪。
- 来源：本机 `C:/Windows/Fonts/NotoSansSC-VF.ttf`，内部版本 `2.04;241114210130;non-release`。
- 制作：FontTools 4.65.0 的 `fontTools.varLib.instancer.instantiateVariableFont`，固定 `wght=300`，开启 `optimize=True`、`updateFontNames=True` 后保存。使用静态字体，避免依赖可变字体默认轴或额外的运行时字重设置。
- 源文件 SHA256：`763146584cf0710223441356b4395e279021b0806c196614377a7a0174ae074a`。
- 游戏字体 SHA256：`caa5a9a8ba383dfc5a863e7eb5cbb8bd553a0e63dd062c3ee70871fbd8dfeae6`。
- 版权：© 2014–2021 Adobe，保留字体名 `Source`。SIL Open Font License 1.1 全文见同目录 `ofl.txt`，随字体一起打包。

维护时应检查新增正文、角色名和界面文字的字形覆盖，并在游戏中验证。遇到缺字，应补齐字库，保留正确原文。不要重新指向缺少“箓、煊、瀺、蕖”等字的 `SourceHanSansLite.ttf`。

`screens.rpy` 中快进三角符号的 `DejaVuSans.ttf` 为符号专用字体，继续保留。
