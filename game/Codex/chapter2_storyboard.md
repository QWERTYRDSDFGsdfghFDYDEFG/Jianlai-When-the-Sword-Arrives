# 第二章当前分镜入口

更新：2026-10-16。记录当前脚本已经执行的文字顺序、归属、画面与缺项，供分镜维护及后续补图使用。

[第二章全章分镜工作簿](F:/图片素材/第二章全章分镜.xlsx) · [原文与改编并排阅读版（HTML）](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_review/第二章_原文与改编分镜对照.html) · [原文与改编并排阅读版（Excel）](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_review/第二章_原文与改编分镜对照.xlsx)

正文唯一权威是 [script_chapter2.rpy](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy)。本入口不重复完整对白；逐条文字、演出事件及原页对应见上述工作簿和阅读版。上述工作簿与阅读版仍为2026-10-12快照，本轮未回写外部导出；其中旧画面状态与行号不代表当前实现，后续补图以本项目分镜入口及当前脚本为准。图片稳定代号以 [image_catalog.json](F:/project/JianlaiWhentheSwordArrives/game/image_catalog.json) 为准；剧情改编与运行验收见 [压缩记录](F:/project/JianlaiWhentheSwordArrives/game/Codex/story_compression_record.md)。

## 统计与使用方式

- 原文253页保留为历史层，不作为当前文字页数；当前为226条文字（T001–T226）与2处无字停留（V01、V02），合计228个演出事件，覆盖11场、56个单元。
- 当前使用32张图片（原27张加第8场5张）。56单元中，28个“已接入”、3个“复用已接入”、6个“已有图待补差分”、19个“黑场待补图”。6个差分单元集中在第1场及第2场开头，可共用稳定状态，不等于必须新做6张图。
- 共100条文字显示在黑场：T107仅为第7场入夜过渡，其余T128–T226共99条属于08-04起及第9–11场待补图内容。不能把100条全部计作新图，也不能将后99条视作美术完成。
- 表中T/V为当前实际事件编号；L为当前脚本正文或pause行号，范围包括中间演出指令。单元ID沿用原表，含05-02a、05-02b、06-01a/b/c、06-06，不重新编号。
- “已接入”表示当前脚本确实调用该图，不表示新增切法、动态镜头、分层人物或所有美术细节已经完成。“待补”列写具体当前缺口及可复用条件。

## 两处无字及归属

- **V01／02-04／L80**：客栈前切到CG02·02·03，陈、朱察觉远处吴懿；隐藏文字窗后点击继续，下一事件T041才说明来人身份。
- **V02／07-05／L271**：切到CG02·07·05，陈弯身放箱；隐藏文字窗后点击继续，再进入CG02·07·06站稳临窗的T105。两处都是无参数pause，可点击、可快进；不是已实现的定时短停或连续动作动画。
- 陈平安24条内心文字使用cpa_thought与“陈平安·心声”；吴懿4条使用wy_thought与“吴懿·心声”。心声结束后清除副标，不能当作同行者听见的对白。
- 崔东山2句使用cds_memory，属于被忆及的话；金色儒衫小人儿6句使用jssr_thought，标明“气府内·心声”。气府动作及不能直说的因果仍由旁白承担。
- 积香庙小神拜谢归jixiang_shen。宁姑娘相关第三人称段落继续归旁白；后段陈自我提醒才是具名心声。
- 让路前置到03-02，在quay图上先交代移开行人再抛舟。T122移入08-03作为拍肩触发，原P140及P141的原文历史归属不改。

## 单元表

### 第1场：溪边歇脚与师徒闲谈

当前全场只显示溪边整图。裴钱仍在持针处理脚底，收针后的稳定状态尚未接入；不能沿用历史标题把动作写成已经收住。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 01-01 | 溪边歇脚与挑疱 | T001–T003<br>[L9–11](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:9) | CG02·01·01 | 已有图待补差分 | 补一张同构图、裴钱已收针坐稳的完成差分，供第3句及01-02至01-04长谈共用；无须为这些单元各补一套背景。 |
| 01-02 | 想家与访友打算 | T004–T011<br>[L15–22](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:15) | CG02·01·01 | 已有图待补差分 | 沿用01-01待补的收针完成态；访友地名和计划保留心声，不列为必须补回忆CG。 |
| 01-03 | 学师父与马屁宝典 | T012–T018<br>[L24–35](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:24) | CG02·01·01 | 已有图待补差分 | 沿用01-01待补的稳定休息差分，解决持针姿态承载长谈；现阶段不要求每句表情差分。 |
| 01-04 | 挖宝玩笑与裴钱表态 | T019–T026<br>[L37–46](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:37) | CG02·01·01 | 已有图待补差分 | 与01-01共用收针后稳定状态；未来挖宝不需要画成当前行动。 |

### 第2场：郡城门前相邀

吴懿按远处来人、近前邀请的次序出现。开头三人迈步图承载长段旧事，仍需稳定处理；02-04 已落实无字来人镜头。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 02-01 | 入城与旧事 | T027–T031<br>[L51–55](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:51) | CG02·02·01 | 已有图待补差分 | 长段旧事需要可久停的停步状态。可评估提早复用现有observe图，或补同街景停步差分；当前尚未实施该调整。 |
| 02-02 | 城中日常与回家心情 | T032–T035<br>[L56–61](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:56) | CG02·02·01 | 已有图待补差分 | 与02-01共用一个停步处理即可；不必为政局背景新增朝堂图。 |
| 02-03 | 陈平安观察与程家旧交 | T036–T040<br>[L68–74](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:68) | CG02·02·02 | 已接入 | 无必需新图；剑修冲突是心中假设，不得补成当前战斗。 |
| 02-04 | 察觉来人 | V01<br>[L80](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:80) | CG02·02·03 | 已接入 | 无必需补图。无参数pause不是定时自动短停，不能登记为已实现运镜或走近动画。 |
| 02-05 | 吴懿说明来意 | T041–T047<br>[L84–91](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:84) | CG02·02·04 | 已接入 | 无必需补图；没有单独冷脸转笑动画，不将旧提案记为已实现。 |
| 02-06 | 询问为难与吴懿回应 | T048–T054<br>[L96–103](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:96) | CG02·02·05 | 已接入 | 现有整图可承载当前对白，无必需补图。 |
| 02-07 | 应允与离开客栈门前 | T055–T056<br>[L108–110](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:108) | CG02·02·06 | 已接入 | 当前文字已补足离开过程，无必需补图。若以后撤去这句旁白，才需要转身跟随或到达结果承接。 |

### 第3场：核舟化船、纸人迎客与登船

实际次序为先疏散，再抛核舟、楼船化形、符纸化少女、搭板、登船后升空。核舟与楼船都位于干燥街面上方，升空图已能看到众人上船后的结果。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 03-01 | 来到开阔处 | T057<br>[L114](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:114) | CG02·03·01 | 已接入 | 无必需补图；不得将人物改记为站在水面或水中码头。 |
| 03-02 | 先让路，再抛出核舟 | T058–T059<br>[L116–121](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:116) | CG02·03·01 → CG02·03·02 | 已接入 | 让路动作由保留旁白交代，当前无必需补图。若要把让路改为无字，需要独立清场结果或挥袖差分；不能宣称已有移人动画。 |
| 03-03 | 楼船显形，低悬街面 | T060<br>[L125](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:125) | CG02·03·03 | 已接入 | 当前低悬状态已可见，无必需补图；无需重列完整船展开动画。 |
| 03-04 | 松手落符纸 | T061<br>[L129](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:129) | CG02·03·04 | 已接入 | 无必需补图；符纸落地过程仍是静态关键相位加文字。 |
| 03-05 | 纸人已化少女 | T062<br>[L133](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:133) | CG02·03·05 | 已接入 | 无必需补图；身份因果由前后图和保留短旁白共同成立。 |
| 03-06 | 板落稳后相邀登船 | T063–T067<br>[L137–144](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:137) | CG02·03·06 | 已接入 | 当前图与下一张全员登船后的升空图足以承接，无必需单独补登船动画；不把本图记为全员已上船。 |
| 03-07 | 升空远游 | T068<br>[L149](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:149) | CG02·03·07 | 已接入 | 无必需补图；不再沿用旧提案把“全员登船结果”列为缺失。 |
| 03-08 | 船上俯江建立 | T069<br>[L153](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:153) | CG02·03·08 | 已接入 | 无必需补图；江名、尺度仍由必要文字承接。 |

### 第4场：船上望乡

仍在船上俯瞰御江。故乡、沿途故人及楚夫人是联想和未来拜访计划，未切成已经抵达这些地方的画面。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 04-01 | 望景而想家 | T070–T073<br>[L154–157](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:154) | CG02·03·08 | 复用已接入 | 无必需补图；未来拜访仍须保留语言，不以家乡CG误示已抵达。 |

### 第5场：下船、小神拜谢与引路

下船进行态只承担一句邀请，随后分别切到拜谢、退场后的对话及沿河引路。老河神有独立说话人归属。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 05-01 | 抵达并下船 | T074<br>[L162](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:162) | CG02·05·01 | 已接入 | 无必需补图；下船进行态未被用于本场后续长谈。 |
| 05-02a | 老河神拜谢与遣退 | T075–T076<br>[L167–169](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:167) | CG02·05·02 | 已接入 | 无必需补图；退出结果已由下一张after图提供。 |
| 05-02b | 小神退场后的吴陈对话 | T077–T078<br>[L174–176](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:174) | CG02·05·03 | 已接入 | 无必需补图。 |
| 05-03 | 引路与队尾拌嘴 | T079–T081<br>[L181–185](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:181) | CG02·05·04 | 已接入 | 当前仅三句，可沿用既有图；若扩成长聊再补停步差分，当前不新增整套行走资产。 |

### 第6场：旧伴去向、吴懿心声与近府

双人交谈图与吴懿闭口近景已接入。于禄相关内容只作为吴懿心声，结束后恢复当面对话；最后复用沿河引路图，府门在下一场建立。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 06-01a | 旧伴去向 | T082–T083<br>[L191–193](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:191) | CG02·06·01 | 已接入 | 无必需补图；画外不等于裴朱退场。 |
| 06-01b | 吴懿想起于禄 | T084–T087<br>[L201–204](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:201) | CG02·06·02 | 已接入 | 无必需补图；未制作于禄幻象，也不应把念头当陈平安听见的对白。 |
| 06-01c | 初访与安排住处 | T088–T091<br>[L212–218](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:212) | CG02·06·01 | 复用已接入 | 无必需补图；住处在第7场建立。 |
| 06-06 | 沿河行进，府门在望 | T092<br>[L223](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:223) | CG02·05·04 | 复用已接入 | 当前旁白与下镜gate共同承接，无必需补图；不得登记本图已画出府门。 |

### 第7场：府门迎接与临河高楼安顿

府内五张已使用最新纸本重绘版。放箱图仍是弯身动作相位，V02 后立即接陈已站直、箱已落地的临窗图；该临窗图已有暮色。T107 切黑只交代张罗和时间继续推进，不算新增缺图单元。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 07-01 | 府门迎接 | T093–T096<br>[L230–236](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:230) | CG02·07·01 | 已接入 | 无必需补图；现图是穿行结果，未实现先门外站定再穿过人群的多状态演出。 |
| 07-02 | 抵达临河客楼 | T097<br>[L242](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:242) | CG02·07·02 | 已接入 | 无必需补图；引路者已可见，不需要另补未知侍者。 |
| 07-03 | 楼层规矩与邀宴 | T098–T100<br>[L248–251](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:248) | CG02·07·03 | 已接入 | 无必需补图；楼层禁限不能仅靠楼梯画面猜，当前两句规矩保留。 |
| 07-04 | 裴钱看陈设 | T101–T104<br>[L257–263](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:257) | CG02·07·04 | 已接入 | 无必需补图；图里没有完整绕楼观看动画，已由对白和静态陈设承接。 |
| 07-05 | 陈平安放下竹箱 | V02<br>[L271](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:271) | CG02·07·05 | 已接入 | 当前短单元与下镜组合已具动作及结果，无必需新图；它是玩家控制停留，不是已实现定时收动作动画，不可在此图新增长对白。 |
| 07-06 | 临窗短谈与天色渐暗 | T105–T107<br>[L277–285](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:277) | CG02·07·06 → 黑场 | 已接入 | 暮色差分已经具备，不再列作待补。楼下张罗未画、未接音效，当前由短旁白兜底；若以后撤此旁白再补对应线索。夜雨坐饮是第10场另需资产。 |

### 第8场：雪茫堂赴宴与旧友重逢

2026-10-16已接入08-01至08-03五张静态图：入夜赴宴、询认、认出笑意、拍肩、收手交谈。当前已按用户“全部替换”的要求统一为v2，孙登先身份与衣装采用已确认的 [彩色母版](F:/project/JianlaiWhentheSwordArrives/game/lh/sdx/sdx_master_v2.png)：灰绿斜襟叠裹短披肩、米白卷袖、左肩布结与深褐腰带。五张场景文件均为`_v2.png`，稳定代号CG02·08·01至CG02·08·05不变；旧v1文件保留并停用，旧v1调用别名兼容映射新图。T122 的拍肩、陈高兴和裴瞪眼作为08-03的触发动作；原P140及P141的历史映射保留，执行归属与原页出处分别记录。08-04前明确退回黑场，后续催席、堂口相迎和宴席仍待补图；226条正文、两处无字停留及音频控制流不变。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 08-01 | 入夜赴宴 | T108–T110<br>[L295–297](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:295) | CG02·08·01 | 已接入 | 夜廊建立图承接三人赴宴与陈停步，竹箱留在客楼。萧鸾身份继续由文字介绍，不将远处女性背影当成专属身份肖像；无必需新图。 |
| 08-02 | 廊下相认 | T111–T121<br>[L304–325](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:304) | CG02·08·02 → CG02·08·03 | 已接入 | 同廊道先询认，在T115“好嘛，原来是你来着！”前切认出笑意；此时尚未拍肩。旧事保留语言，不将银刀、狐魅或完整降妖闪回画成当前事件；无必需新图。 |
| 08-03 | 拍肩与旁观 | T122–T127<br>[L331–342](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:331) | CG02·08·04 → CG02·08·05 | 已接入 | 拍肩图仅承载T122，T123起切手已收回的稳定群像，供裴、朱旁观及孙向同伴介绍陈；裴、朱内心仍由旁白注明，不当成当面对话，也不画出崔东山。无必需新图；静态切换不是连续拍肩动画。 |
| 08-04 | 催席同行 | T128–T132<br>[L349–356](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:349) | 黑场 | 黑场待补图 | 复用夜廊空间补队伍准备前行或到堂口结果，交代催行者和被催者关系；无需完整行走动画。 |
| 08-05 | 吴懿相迎与众人揣测 | T133–T140<br>[L358–369](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:358) | 黑场 | 黑场待补图 | 补堂口吴懿迎陈与宾客旁观的基本站位。涉及挽臂的主体先核原稿指代再制作，不把待核动作当已接入图。 |
| 08-06 | 举杯开席 | T141–T145<br>[L371–375](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:371) | 黑场 | 黑场待补图 | 补雪茫堂席面稳定群像与一个举杯关键状态；酒名和六十坛来历继续由对白承载。 |

### 第9场：且慢行与善恶之问

本场全部仍是黑场文字。陈心声、崔东山回忆、陈朱真实问答、气府内心语依靠明确的说话人及副标区分，尚无对应专用图。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 09-01 | 且慢行 | T146–T151<br>[L378–385](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:378) | 黑场 | 黑场待补图 | 先明确本段与宴席及行走段的空间衔接，再补陈平安稳定沉思状态；伞、车轮等比喻不必逐一新增CG。 |
| 09-02 | 忆及崔东山所言 | T152–T153<br>[L389–390](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:389) | 黑场 | 黑场待补图 | 可共用09-01稳定沉思图，以回忆说话人标记区分即可；不必新增现实在场崔东山立绘。 |
| 09-03 | 慢与改过 | T154–T158<br>[L393–399](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:393) | 黑场 | 黑场待补图 | 共用09-01沉思图即可；种子是解释性意象，当前不必追加生长特效。 |
| 09-04 | 善恶之问 | T159–T164<br>[L401–410](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:401) | 黑场 | 黑场待补图 | 确认当前空间后补陈朱稳定双人交谈图，能清晰区别此处真实问答与前后心声；不需新增杀人情境图。 |
| 09-05 | 气府小人急劝 | T165–T171<br>[L413–421](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:413) | 黑场 | 黑场待补图 | 补可辨识为身体内部的气府空间及金色儒衫小人的着急稳定状态；若画冲门，仅作短相位并接站稳状态。 |
| 09-06 | 念及宁姑娘 | T172–T175<br>[L423–426](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:423) | 黑场 | 黑场待补图 | 复用陈的沉思或走路结果状态；宁姑娘并非当前在场，无必需新增宁姑娘出场图。 |
| 09-07 | 气府里的反应 | T176<br>[L429](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:429) | 黑场 | 黑场待补图 | 复用09-05待补气府与小人图即可；可选气急表情差分，非必须全新CG。 |

### 第10场：临窗雨夜长谈

本场全部仍是黑场文字。雨夜坐饮不能视作已经复用第7场的暮色站谈图；雨声、斟酒、雨歇目前由文字交代，没有本章新增音频调用。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 10-01 | 雨夜临窗入座 | T177–T181<br>[L436–443](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:436) | 黑场 | 黑场待补图 | 补同一客楼的雨夜双人坐饮稳定图，保持窗、箱与房间连续；斟酒可由保留旁白承接，不强制多帧倒酒动画。 |
| 10-02 | 河水与光阴长河 | T182–T190<br>[L445–460](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:445) | 黑场 | 黑场待补图 | 共用10-01待补雨夜坐谈图；河水与光阴概念由对白保留，不必补宇宙或光河特效。 |
| 10-03 | 马屁与酒 | T191–T195<br>[L462–470](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:462) | 黑场 | 黑场待补图 | 共用夜谈底图，补或复用陈转向朱、朱酒杯可见的稳定状态；若保留动作旁白可暂不做举杯动画。 |
| 10-04 | 远游与托付裴钱 | T196–T203<br>[L472–483](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:472) | 黑场 | 黑场待补图 | 共用夜谈图，保持裴房方向可交代；未来北俱芦洲与护送计划留语言，不补成当前旅途图。 |
| 10-05 | 朱敛说旧事 | T204–T215<br>[L485–500](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:485) | 黑场 | 黑场待补图 | 共用夜谈空间补朱讲述、陈倾听的稳定状态即可；不将整套少年朱敛风流闪回列为当前必补。 |
| 10-06 | 想起宁姑娘的心声 | T216–T220<br>[L503–507](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:503) | 黑场 | 黑场待补图 | 可共用夜谈图，以心声标记区分；可选陈分神表情，非必须新增宁姑娘立绘。 |
| 10-07 | 回神与雨歇 | T221–T224<br>[L510–516](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:510) | 黑场 | 黑场待补图 | 共用夜谈图，若要撤末旁白再补雨后窗景与杯酒减少的结果差分；当前保留旁白，不宣称已有音效。 |

### 第11场：翌晨离府与吴懿传讯

本场仍是黑场文字；翌晨离府和吴懿传讯后跳转第三章。传讯信息只向玩家交代，没有提前变成陈平安已知信息。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 11-01 | 翌晨辞府 | T225<br>[L521](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:521) | 黑场 | 黑场待补图 | 补可与第7场空间连续的清晨离府或返乡路结果图；保持三人及行装连续。 |
| 11-02 | 吴懿传讯 | T226<br>[L523](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:523) | 黑场 | 黑场待补图 | 补吴懿独处传讯的稳定图即可；传讯媒介未定，不擅画特定法器，也无需新增父亲接讯CG。 |

## 仍待核实的原文歧义

- **“他竟然挽着师父”**：当前保留原词，尚未确定“他”的指代；不得据此先画定挽臂人物或改变角色关系。
- **“紫气宫”与“雪茫堂”**：孙登先对白沿用“紫气宫”，当前赴宴地称雪茫堂；两者的空间或名称关系未核实，不擅自统一名称或拆成两个新地点。

现有整图无法证明的动作、时间和因果仍保留短旁白。第1场进行态、第2场开头迈步态、08-04起及第9–11场黑场是明确制作缺口；第7场暮色及08-01至08-03五图已经接入，不再列为待补。本文没有授权补写原作、删除更多对白、生成图片或把计划中的资产标记为完成。

## 数据来源与核验

本入口初版由2026-10-12快照 [actual_data.json](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_sync/actual_data.json) 的最终事件顺序与 [unit_visuals.json](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_sync/unit_visuals.json) 的56单元现图核验整理。两份JSON及外部工作簿、阅读版仍保留该日状态；前者的历史字段保留原始来源。本轮以当前脚本逐条对齐原正文更新全部后移行号，并按 [第8场生成与接入记录](F:/project/JianlaiWhentheSwordArrives/work/art/chapter2/c2_08_record.json) 更新五图状态；226条正文、两处无字停留和原文映射不变。孙登先设计依据见 [当前身份标准](F:/project/JianlaiWhentheSwordArrives/game/lh/sdx/sdx_face_ref.md)。

| 来源 | SHA-256 |
|---|---|
| 当前script_chapter2.rpy（2026-10-16） | `5b73e1b1b92fbddd53611eafe2c37a4a67a7c9110e8a95fdebe71ec7c9ac9b26` |
| 原文来源快照（baseline_sha） | `afa033c12b1c6fa57e712a3c6acb28b2a24e678ba07042a39aa225f4f813032c` |
| actual_data.json | `78787f79d0109b1786f39b6de3d7a1c75fbe60ebc3a3fc2a6072dda6d067fd4a` |
| unit_visuals.json | `5eeb4d1e11b56717e093ab9843fa03f54d22a07943eaefd11930d1b2ca9ffeb7` |

核验范围：56单元唯一且全覆盖；228个事件按当前脚本顺序归属；253原页保留历史映射；32张实际图片与两处无字停留可定位；黑场统计分出T107过渡。本轮v2已独立重验：隔离lint退出0，主例66/66与稳定回看12/12合计78/78断言通过；覆盖五镜切换、三处存读档、跨镜回退、回看与08-04退黑，并核对1280×720及1867×1050窗口画面。主线程已目检五镜、大窗、退黑、回看及返回截图；111份原存档、缓存与rpyc文件哈希不变。此次依据独立的`scene8_sdx_v2_20261016/verification.json`，与旧v1同为78/78的验收分开记录，权威入口为上述第8场接入记录。未验证完整十二章回归、旧版本存档迁移、移动端与物理1920×1080全屏；不宣称全部补图、连续动作或全章体验已完成。本文的文档同步另核对链接、行号和统计；脚本或图片后续变更后，应重新核对本入口的行号、哈希及资产状态。

