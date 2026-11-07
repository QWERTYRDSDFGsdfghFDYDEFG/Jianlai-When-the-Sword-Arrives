# 第二章当前分镜入口

更新：2026-10-30。正文仍为2026-10-29用户确认稿；本次仅将雨停廊下定稿图接入摊掌低看及檐外河山两句。本页记录当前脚本的段落顺序、信息归属、已有画面和待补项，不另存完整正文。

正文唯一权威是 [script_chapter2.rpy](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy)。实施范围及本轮验收见 [定稿接入记录](story_compression_record.md)，图片稳定代号见 [image_catalog.json](../image_catalog.json)。下列行号按本次接入脚本定位；正文再次调整后须复核，场头文字可用于检索。

2026-11-01 更新：[第09、10场逐镜表](#c2-scenes-09-10)对应现行剧本从高楼栏杆到朱敛临窗发问的段落。

<a id="c2-rain-y02-formal"></a>

## Y02正式线稿制作（2026-11-07）

**授权与终点。** 用户明确“定下四格分镜，再从Y02开始制作正式线稿”。四格台本现为**当前使用／用户已确认镜头安排**；本次只制作Y02一张独立正式线稿，止于sketch，不自动上色、制作其余三镜或接入游戏。旧雨街素材继续停用。

**记录方式与限制。** 本镜的长期单图记录直接维护在本节，不新增过程稿、预览、备份或临时文件。两人均为匿名群演，没有已确认的正式脸部母版。现行v2检查器无条件要求每人提供face_master，不能诚实表示此情形；独立静态核查者`/root/anonymous_record`已确认该限制。故本节保存真实手工阶段证据，不伪填母版、不登记“无人物”、不声称v2机械通过。默认Python入口无法运行，Ren'Py附带Python也返回系统DLL重定位错误；未运行status/check，未改校验器。此限制不改变用户已确认的匿名人物与镜头范围。

### 出图前阶段证据

| 阶段 | 实际依据、观察与结论 |
| --- | --- |
| brief | 核对现稿395–398行；Y02对应“撑伞的人在雨里，”。两名普通成年人位于听来的故事内，陈平安及陆抬不在雨街。近伞左行露人，中景人右赶空檐；本镜两脚尚在湿街。后接Y03到达结果，不新增跨阶过程。 |
| references | 实际打开确认台本整页，并在内存放大Y02。只用第二格锁机位、匿名成年人轮廓、长袍伞客／短衣裤赶檐人的区别；不把台本当成正式脸部母版。实际绘制将传入整张确认台本并限定只取Y02；旧图和旧PSD不输入。 |
| composition | 目标1920×1080；左街右檐、胸/眼高斜向平视；两人向相反方向行走。以Y02较短的石台左端为建筑基准，后续Y03统一到本镜，暂不改四格台本像素。先保留右侧空檐和上阶通路，再安排两人，略增上下余量保全脚。 |
| space | 独立复核者`/root/y02_space_review`实际查看整页和Y02内存3倍近邻放大，确认二维方案可进入正式线稿。近伞不遮赶檐动作，右柱未堵通路；前脚在街、后掌推地，自身右臂为远侧抬袖、近侧左臂后垂。正式稿须让袖布实际遮额。无需另造3D，不宣称实尺净空、碰撞或檐雨投影通过。 |

来源指纹：确认台本`work/art/chapter2/c2_09_rain_storyboard.png`，SHA256 `efae35d4fe114832c4d60d073586455a9a23ec06a83605219f196b63f5f43147`；剧情`game/script_chapter2.rpy`，SHA256 `757a7f2c370451114a3809b2d34d635a8708b6f5aef48bd38e54878e14c6e30a`。两份文件均只读；构图依据为当次用户确认的台本，程序正文不变。

### 锁定构图与逐人站位

```json
{
  "camera": "1920×1080横向，街边胸/眼高的斜向平视；承接已确认台本Y02，街道向左纵深延伸，不反打、不翻转。",
  "anchors": "按Y02而非Y03扩出的石台锁建筑。右前柱x约0.95、门洞x约0.79–0.94；石台前缘左端约(0.57,0.76)到右近端(0.95,0.98)。坐标是归一化构图锚点，不是实尺。台阶为可跨越的低阶、檐下有完整站立地面，滴水线在遮蔽区外。",
  "action_target": "近处伞客继续朝画左沿街走；中景抬袖者朝画右空屋檐赶去，本镜仍在湿街，未跨阶。",
  "action_space": "两条动线分开；伞不盖住赶檐人的抬袖轮廓；赶檐人与台阶之间保留约一脚步可读空隙，目的平台空着，右柱不入通路。",
  "route": "伞客从左前景走向左方街道纵深。赶檐人从中景湿街朝右侧低阶、门前檐下走；不迎向伞客，不横穿石柱。",
  "continuity": "Y01为同一伞的伞沿细节；Y03使用本Y02石台边界，省略跨阶过程后双脚站稳；Y04同侧收紧。只有台本，无Y03/Y04正式图，因此不声称正式背景跨镜已验。",
  "characters": [
    {
      "character_id": "umbrella_passer",
      "position": "左前景x约0.07–0.25，伞冠x约0.02–0.27，不挡住中景人完整动作。",
      "footing": "足点y约0.92–0.96，左向步行，一脚着地另一脚后跟提起；双脚在湿街，不上台阶。",
      "facing": "头肩胸胯和双脚共同朝画左并随街道略向纵深，后侧视角。",
      "gaze": "沿画左街道前行，不回看赶檐者。",
      "scale_depth": "靠近相机的成人，服装更长、伞冠在身上；不把成人身高差当成前后差。",
      "occlusion": "伞和背侧视角部分遮脸，握柄手和腕应连贯；保留两腿、伞杆结构，不求正面露脸。"
    },
    {
      "character_id": "shelter_seeker",
      "position": "中景x约0.36–0.54，头约(0.49,0.35)，在石台左方街上；后面空檐在右。",
      "footing": "前鞋约(.50,.87)在湿街承接重心，后脚掌蹬地/后跟提起；两脚尚不在台面，支撑与运动方向对应。",
      "facing": "头、胸胯与前脚朝右，身体前倾；自身右臂为远侧抬起挡雨，近侧左臂后垂。",
      "gaze": "看右前方目的檐下与落脚路面，不朝观众。",
      "scale_depth": "普通成年偏瘦体型；处中景且弯身，校正姿态后与伞客成人体量一致，无孩童化。",
      "occlusion": "右臂袖口与前臂连续，袖布实际遮额；左手后垂，不多手。不得用伞再次遮掉赶檐动作。"
    }
  ]
}
```

**独立空间复核保留项。** 伞客看画左路向，头肩、长袍和鞋尖一致；握手、伞杆和伞面轴心需连贯。赶檐人头肩前倾、前鞋向右，目光落向台阶前方，不提前转成Y03/Y04左望；按中景与弯身校正成人体量。平台须有能放下双脚、站直降袖的连续地面，不能以黑门洞代替净空。Y03/Y04只有台本，没有正式图，不声称已完成正式跨镜背景验收。

### 实际绘制请求

内置image_gen；transparent_background=false；唯一参考路径为`F:/project/JianlaiWhentheSwordArrives/work/art/chapter2/c2_09_rain_storyboard.png`。阶段：sketch；执行状态：已完成出图前核对，待实际生成与独立成图复核。

<details>
<summary>Y02正式线稿实际提示词</summary>

```text
Use case: illustration-story / formal production line art.
Produce ONE new independent formal line-art scene for shot Y02 of a restrained Chinese historical visual novel. Target size 1920 x 1080, landscape 16:9. This is the full scene to be used later as a production illustration, NOT a storyboard sheet, NOT a crop/enlargement or grayscale conversion of the sketch.

INPUT REFERENCE: the supplied image is the user-confirmed four-row STORYBOARD. Use ONLY the SECOND row, labelled Y02, as the approved shot, camera, architecture and anonymous costume/action design. The other rows are continuity context only and MUST NOT be reproduced. The Y03 platform has a known left-edge drift; the Y02 SHORTER platform corner is the authoritative geometry. Exactly one borderless widescreen illustration, with no labels, arrows, captions, table, title, split panels or lettering.

NARRATIVE: Two anonymous ordinary adults in a rainy old town. Left foreground umbrella carrier walks screen LEFT and is now clear of the center, revealing a lean man hurrying screen RIGHT toward a shop eave. The second man is STILL ON THE WET STREET, NOT on the step or standing sheltered. The shot accompanies the narration about umbrella-bearers being out in rain. Do not add Chen Ping'an, Lu Tai, a child, any hero, extra pedestrians, swords, book boxes, packs, valuables or other new story.

LOCKED GEOGRAPHY: preserve row Y02's oblique street-side chest-height view. Rainy lane recedes to the left; the modest timber shop, low stone landing, hanging plain lantern and open dark doorway are at right. The closest timber post stays at the extreme right edge, behind/outside the walking route, not between man and shelter. Keep the platform's LEFT start near 57% of width, and its front edge running toward lower right. Do not import Y03's platform extension into the middle of the lane. Leave a clear empty place on the landing behind the runoff line where the same man can stand in the next shot. Low practical one-step height, coherent perspective, posts planted on stone bases, wall/door joints align. No palace ornaments, modern architecture or new signs.

UMBRELLA CARRIER: modest ordinary adult in a plain long coarse-cloth wrap robe, cloth belt and cloth shoes; hair tied simply. In LEFT foreground, back-side three-quarter view walking LEFT, one leg carrying weight and the other heel lifting naturally. Full feet remain inside the image. Head and gaze follow the route, not turned to the viewer. The umbrella naturally partly hides the face. One visible hand holds a straight wooden shaft naturally with continuous wrist and sleeve. Coherent umbrella hub, ribs and canopy; umbrella large enough to cover the wearer but not oversized across the center. Carrier occupies roughly x7–25%, feet around 92% of frame height. Preserve the approved ordinary silhouette; no glamorous facial redesign.

SHELTER SEEKER: lean ORDINARY ADULT, not a boy, simple cloth-tied bun, loose coarse-cloth short wrap tunic with a plain waist tie, calf-length loose trousers, cloth shoes. Position center midground, roughly x36–54% of width; head around x49%, y35%. He leans forward and hurries RIGHT. His own RIGHT arm is the FAR arm: it rises through shoulder-elbow-wrist above his brow, and actual sleeve fabric shields the brow against rain; do not merely show a naked forearm saluting. His near LEFT arm hangs naturally somewhat behind the body. Make the two arms anatomically connected, separated and legible, with no extra hand or fused elbow. The leading foot is at approximately x50%, y87% on the WET STREET just BEFORE the low stone platform; it is NOT on top of the step. Rear foot toes push off the wet street with heel lifted. Leave about one readable short stride of clear pavement before the step. Both feet visible, no floating, no crossing into the riser. Face down/right toward shelter and footing, partially obscured by sleeve and rear-side angle; natural ordinary adult proportions, no hero portrait.

COMPOSITION AND CONTINUITY: the two motion directions are intentionally opposite. Preserve leftward umbrella carrier and rightward shelter seeker, not both going the same way. Foreground carrier is nearer; midground seeker is proportionate after accounting for depth and forward lean. Keep the men separate so the lifted sleeve, forward leg and destination can be read immediately. Keep moderate empty wet street around the feet and clear space inside the eave. The street-level line, the raised landing surface, and roof drip line must be distinct. Rain falls outside the shelter, not across the dry doorway/interior. The future Y03 will use exactly this architecture, so avoid arbitrary platform shape changes.

FORMAL DRAWING QUALITY: refined but economical black and neutral-gray ink/pencil LINEWORK on clean white. Semi-realistic restrained Chinese historical figures and practical Song-inspired vernacular architecture. Reconstruct correct anatomy, hands, footwear, umbrella shaft/hub, timber joints, stone riser and perspective. Clear controlled contours with varied line weights: foreground strongest, midground moderate, distant buildings lighter and simpler. Sparse selective hatch marks only at real occlusion/core shadows. Very few purposeful clothing folds that follow the action. Minimal thin separated rain strokes and sparse broken wet reflections. Do not fill the sky or street with dense pencil scribble, blanket crosshatching, muddy grays, photoreal tone rendering, dark comic screentone, excessive tile/wood texture or a fully shaded grayscale painting. No color, no sepia, no glossy game art, no anime hero features. Formal clean linework should remain easy to color later.

Output only the one independent Y02 illustration. Preserve every storyline constraint and approved row-Y02 geometry; deliberately finish the drawing rather than mechanically copying the worksheet's rough texture.
```

</details>

<a id="c2-rain-shelter-new-sheet"></a>

## 路人躲雨：全新四格粗分镜（2026-11-07，本轮）

**本轮交付：Y01–Y04四格粗分镜。** 用户要求“按照制作流程把‘且慢行’路人躲雨段剧情做新的分镜，之前的不需要”，随后明确批准四格方案及分镜记录、图片索引更新。以本节为当前制作入口；此前05A／05B两行台本、双格分镜、独立05A正式线稿，以及更早的雨街05B／05C和PSD全部停用，原文件保留。已采用的雨停夜廊彩图不在此次否决范围内。

[打开本轮四格台本](../../work/art/chapter2/c2_09_rain_storyboard.png)。用户已明确“定下四格分镜，再从Y02开始制作正式线稿”，四格台本为**当前使用／用户已确认镜头安排**。当前从[Y02正式线稿](#c2-rain-y02-formal)继续；台本采用不等于正式素材、上色或游戏接入通过。

### 剧情与演出设计

依据现稿[第395–398行](../script_chapter2.rpy:395)，从“他想起在青鸾国酒楼里听来的一个故事。”到“慢一点，才看得见人间的苦。”；第402行起的陆抬忆述不纳入本页。剧情正文保持原样。雨街只有两名匿名普通成人；陈平安与陆抬不在现场。Y04的心念仍属于画外陈平安，由旁白叙述。新Y编号只用于本页，不新增或替换程序镜号。

| 镜号 | 画面动作 | 原稿旁白 | 声音、推进与切换（建议） |
| --- | --- | --- | --- |
| Y01 | 伞沿水滴近景，右侧略见街屋，承接夜廊。 | 他想起在青鸾国酒楼里听来的一个故事。 | “故事”句后切入；檐滴接雨声。檐滴匹配切待制作，时长待定。 |
| Y02 | 伞客向左走，露出抬袖朝右侧屋檐赶去的路人；尚在湿街。 | 撑伞的人在雨里， | 固定机位；雨声、湿脚步；逗号处换格，同下一格承载脚本中的同一句旁白，时长待定。 |
| Y03 | 省略跨阶过程，路人已双脚入檐，收步放低衣袖；伞客在左街走远。 | 躲雨的人在檐下。 | 同机位；脚步停、雨声继续；句末停留，点击推进。 |
| Y04 | 同侧略收紧，檐下人静望雨街，伞客在左方更远处。 | 也想起陆抬说过的“留不住”，于是心里只剩一句话：且慢行——慢一点，才看得见人间的苦。 | 只留雨声；读完点击推进；下一段再转陆抬忆述，时长待定。 |

新稿让“雨中行走／檐下停留”形成完整对照。Y03是全新方案的到达结果，并非恢复旧06A／06B文件或重新采用旧画格。建筑以街左、檐右为统一方向，伞客沿左街远去；赶檐人进入右侧遮蔽区后停留。声音、时间和转场均只是制作建议，未实施。

### 实际请求、文件与写入证据

- 内置image_gen单次生成；transparent_background=false；**没有传入任何参考图片**，未输入旧分镜或旧PSD。制作前只查看当前已采用夜廊图以核对衔接，未把它传入生成器。匿名路人没有正式脸部母版，本页不建立主角身份标准。
- 生成工具实际输出：`C:/Users/MSI/.codex/generated_images/01a1b570-a3ee-7550-a7a6-74520845273d/exec-de720a77-4378-4913-b0fe-37e489709e48.png`。
- 原生1024×1536 PNG，2,368,420字节；SHA256：`efae35d4fe114832c4d60d073586455a9a23ec06a83605219f196b63f5f43147`。四格为横向画框，接近16:9，未作为严格16:9单镜交付。
- 仅把本轮交付台本逐字节保存到上述项目路径；以排他创建方式写入新文件，目标不存在才可写，回读字节和SHA256与工具输出一致。没有修改、覆盖、裁切或重新编码任何旧图，没有候选副本、预览、备份或临时文件。
- 分镜文档和图片索引在原文件句柄内定位写入、截尾并同步落盘；写前校验基线SHA256，写后回读比对全部内容及文件标识，并核验指定变更范围外文本不变。写入结果以本轮实际工具回执为准。
- 剧情依据SHA256：`757a7f2c370451114a3809b2d34d635a8708b6f5aef48bd38e54878e14c6e30a`；夜廊项目图SHA256：`f078d454659805112145d545a6710417c46beefc83ec7467f5bd89299b2824a3`。交付核验两者保持原值。

### 独立复核与待定项

独立复核者`/root/rain_story_review`实际查看整页，并逐格对照现稿395–398行：Y01伞沿接滴、Y02伞左行露出右行赶檐者、Y03双脚入檐并降袖、Y04同侧收紧静看左街均可读；两人连续、没有新增主角或归属错误。原旁白逐句完整，Y04明确写“旁白（陈平安的思绪）”；声音、停留、切换和时长均未虚报实现。**未发现阻断粗台本交付的问题。**

正式制作前仍须处理：Y02／Y03灯笼、门框、右柱基本对齐，但Y03石台左端向左扩出，固定背景几何尚不严格一致；雨线为示意，尚未做精确屋檐投影验证；排线与建筑笔触较粗草图要求偏多。上述差异不影响当前镜头叙事阅读，不据此批准连续动画背景。

未执行正式脸部身份、单镜线稿、上色、声音、动态、对白叠放或游戏实机验证；未改脚本、资源定义或图片代号，未运行Ren'Py。交付终点仅为新粗分镜及其记录，用户是否采用画面待确认。

<details>
<summary>本次内置image_gen实际请求全文</summary>

```text
Use case: illustration-story.
Create ONE brand-new rough hand-drawn storyboard worksheet for a restrained Chinese historical visual novel. The user approved this four-panel plan. Do not reuse any prior storyboard image or composition sheet. This is the final requested ROUGH STORYBOARD deliverable, not production line art.

PAGE: clean white upright worksheet, FOUR rows read top to bottom. Each row has a slim left shot-number column, a large landscape 16:9 drawing in the middle, and a spacious Chinese annotation column on the right. Four equal 16:9 picture frames, approximately 62% of page width devoted to the picture column, 31% to notes. Thin ruled table, plenty of white space. At top title “且慢行 · 路人躲雨” and subtitle “新分镜台本｜四格｜雨街是听来的故事”. Column headers “镜号”, “画面”, “旁白／演出与推进”. Use a high-resolution upright page so all Chinese text is clearly readable. Text is crucial, especially the full final narration.

DRAWING: loose economical graphite thumbnails, simplified human figures, gesture and weight readable, basic roof and door geometry. Sparse gray tonal strokes. No dense hatching, roof-tile rendering, elaborate fabric folds or finished faces. Use only tiny muted red arrows for CHARACTER movement, never camera movement. Rough but physically coherent. Song-inspired ordinary timber street, not palatial fantasy. No named characters: Chen Ping'an and Lu Tai are only mentioned in narration/context, NEVER physically present.

NARRATIVE AND GEOGRAPHY:
Only TWO ordinary adults throughout this sheet: an umbrella carrier and a bareheaded man seeking shelter. Same clothes, proportions and umbrella across rows. Umbrella carrier wears a modest long plain robe; face partly hidden by umbrella. Shelter seeker is a lean adult with cloth-tied bun, coarse short wrap tunic, calf-length trousers and cloth shoes, visibly ordinary and slightly hunched. No swords, book boxes, jewelry, jade hairpins, begging, injury, dramatic sobbing or added plot.
Rainy street recedes to LEFT. A simple shop with a deep eave is on RIGHT, with a low stone landing and dark doorway. Establish clear wet street versus covered floor. Roof runoff falls OUTSIDE the sheltered standing zone. A post at the extreme RIGHT must not obstruct the entrance or man's route. Row 2 and Row 3 MUST share exactly the same chest-height oblique fixed camera, door position, landing corners, post and vanishing direction. Row 4 stays on the same side of the axis and moderately tightens framing toward the sheltered man; preserve left street/right shelter orientation. Umbrella carrier moves screen LEFT and continues farther LEFT into the lane. Shelter seeker goes screen RIGHT onto the landing, then stays there. No simultaneous duplicate instances of either person.

ROW 1, left label “Y01”:
Close-up of curved oil-paper umbrella rim in upper half; one water drop falling from the rim around 36% of picture width, 74% of height. Sparse rain behind. A very simple glimpse of street and eave on right establishes environment, but no human portrait. This is an umbrella detail, not a separate new umbrella.
Right column EXACT text, with sensible line breaks:
他想起在青鸾国酒楼里
听来的一个故事。

画面：伞沿一滴水落下。
声音建议：檐滴接雨声。
推进：“故事”句后切入。
檐滴匹配切待制作；时长待定。

ROW 2, left label “Y02”:
Chest-height street-side wide shot. Umbrella carrier in LEFT foreground is walking LEFT and has just cleared the center enough to reveal the shelter seeker behind. The seeker is in center-right midground, leaning forward and stepping RIGHT toward the visibly reachable covered landing, RIGHT forearm/sleeve raised over forehead. Both his feet are still OUTSIDE the landing on the wet street (one taking weight, the other in motion). Destination to his right is empty and clear. Keep full support leg and foot readable. Two small red motion arrows: at carrier pointing LEFT labelled “伞左行”; at seeker pointing RIGHT labelled “赶檐”. No camera arrow. His face is anonymous simplified sketch only.
Right column EXACT text:
撑伞的人在雨里，

画面：伞过，露出抬袖赶檐的人。
声音建议：雨声、湿脚步。
固定机位；与下一格为同一句旁白。
逗号处换格（建议），时长待定。

ROW 3, left label “Y03”:
EXACT SAME fixed camera and architecture as Row 2. Time advances by the small walk into shelter, without drawing extra crossing keyframes. SAME seeker now fully UNDER the deep eave at RIGHT, BOTH feet on the landing behind the roof drip line; body has stopped, weight natural, right sleeve now lowered toward chest. Head still mostly oriented in walking direction, subtly catching breath, no exaggerated emotion. Wet cloth hangs from lowered elbow. SAME umbrella carrier now farther LEFT and slightly smaller along the receding street, still walking left; do not teleport to right or change direction. Dry shelter area must be legible. No extra people. Small label by ground “檐内” and rain edge “落雨线”, kept unobtrusive.
Right column EXACT text:
躲雨的人在檐下。

画面：人已入檐，收步、放下衣袖。
声音建议：脚步停，雨声继续。
同机位；省略跨阶过程。
句末停留，点击推进（建议）。

ROW 4, left label “Y04”:
Same-axis somewhat closer medium-wide view, NOT a reverse view. SAME sheltered man at RIGHT beneath eave, staying at the same spot, hands now lowered comfortably, shoulders settle; he quietly turns head LEFT to watch the rainy street. Modest restrained adult face, no glamour. Keep some of his legs visible and show sheltered ground versus rain. LEFT side retains airy rainy street and SAME umbrella carrier now much farther LEFT and smaller moving away. Rain and empty space between the two people carry the feeling. Do not move the sheltered man back into rain or introduce Lu Tai or Chen Ping'an. No arrows in this still last panel.
Right column EXACT text:
也想起陆抬说过的“留不住”，
于是心里只剩一句话：
且慢行——慢一点，
才看得见人间的苦。

画面：檐下人停看雨街。
声音建议：只留雨声。
同侧略收紧；读完点击推进。
下一段再转陆抬忆述，时长待定。

Bottom footer EXACT text:
本页仅为粗分镜；对白为原稿旁白。声音、停顿与切换均为演出建议。

Ensure all four panels and all notes are fully on page without cropped text. Preserve simplified rough sketch quality and generous negative space. The top-to-bottom reading should clearly show: detail of drop, revealed hurried movement, achieved shelter, quiet pause and looking outward. Do NOT deliver a polished full-page illustration, comic dialogue bubbles, reference montage, old shot IDs 05A/05B/06A/06B, or multiple versions.
Narration attribution: all right-column story text is NARRATOR text. In Row 4 the thinking belongs to Chen Ping'an offscreen, not the anonymous sheltered man; no thought balloons or spoken dialogue. Add small explicit label “旁白（陈平安的思绪）” above that row's narration.
```

</details>

## 2026-11-05 “且慢行”双形式线稿研究

历史目标是章节尾声CG与成就、另做小短片；11月5日曾研究替换切入的方案。2026-11-06用户按当前脚本明确：已完成第09场“雨停夜廊”切入的场景制作，止于“他低头看了一眼”；下一段应做“路边躲雨”。当前范围以下方确认表为准，正文未改。

历史四镜草案为：车轮疾行 → 折草 → 湿栏与手 → 陈平安凝视，曾按约25–30秒构想。该草案未被确认为当前演出安排，不再据此分派车轮、折草等补图；保留研究记录和原图。章末CG、成就及完整短片仍是后续目标。

研究依据：[Gorogoa作者谈画框与蒙太奇](https://blog.playstation.com/2018/03/20/the-power-of-the-frame-in-gorogoa-coming-soon-to-ps4/)；[高畑勋谈线条与留白](https://medium.com/@Film4/isao-takahata-on-the-tale-of-the-princess-kaguya-4221f5df60a9)。借用构图与节奏方法，未把参考作品图像导入生成器。

两张图原生均为1672×941。夜廊切入单图已完成上色并采用；车轮四镜线稿保留为历史草案，状态待修正。
- [雨停夜廊切入彩图](C:/Users/MSI/.codex/generated_images/01a1a90c-e7e6-76b1-8057-9306586218e7/exec-a3a99d79-58d6-4851-8714-7293e7a6f1ea.png)。在修正卷首玉簪的线稿上原位着色。铁券河及远岸用冷蓝灰，暖光落在脸、手和湿栏上，青绿玉簪与叶尖水滴可辨。已回读原PNG并复核静态画面。2026-11-06 又在折草下方已有积水内减弱木纹，补入顺栏面的断续冷灰蓝反光，局部复核通过。2026-11-06 用户以脚本确认其属于第09场雨停夜廊切入，完成范围止于“他低头看了一眼”；后接路边躲雨，不能继续归入未确认的车轮四镜方案。已撤下误加的章末调用。保留[已登记资源](../images/chapter2/c2_end_slow_v1.png)，当前剧情未调用，后续衔接待制作。
- [短片四镜线稿](C:/Users/MSI/.codex/generated_images/01a1a90c-e7e6-76b1-8057-9306586218e7/exec-ceff44fb-579f-48f5-ad65-6f92d1f813b8.png)：03/04草根似穿入栏面，需明确独立断草落在木面，避免被读成同株草跨场迁移。

[任务依据、检索来源与完整提示词](../../work/art/chapter2/c2_slow_attention/basis.json) · [CG实际调用与复核](../../work/art/chapter2/c2_slow_attention/cg_record.json) · [四镜实际调用与复核](../../work/art/chapter2/c2_slow_attention/board_record.json)。独立复核已检查静态身份与空间；声音、时长、动画、成就效果和实机均未验证。

<a id="c2-slow-attention-final-shot"></a>

### 本图分镜归属与定稿（2026-11-06）

本图当前用途为“第二章·第09场·雨停夜廊切入”。用户确认完成的场景制作范围是下面三句旁白，止于“他低头看了一眼”。本图美术采用与工程演出接入分别登记。

| 项目 | 当前确认结果 |
| --- | --- |
| 脚本归属 | 第09场开头，脚本注释镜01及镜02–04；三句旁白位于第387、389、390行。彩图呈现扶栏低看的结果画面。 |
| 画内时空 | 紫阳府临河高楼夜廊，雨已停。 |
| 画面动作 | 陈平安前臂轻搭湿栏，垂眼看近处折草及水滴；远处为江面与人家灯光。 |
| 已完成范围 | “雨已经停了，檐角还在滴水。”→“陈平安沿着廊下慢慢走，一只手轻轻搭在栏杆上。”→“走到灯下，一滴檐水落在他手边。他低头看了一眼。” |
| 后接制作段落 | 当前脚本第395–398行路人躲雨，由本轮全新Y01–Y04粗台本承载；此前雨街分镜及05A正式线稿停用，见[最新记录](#c2-rain-shelter-new-sheet)。 |
| 完成口径 | 用户确认上述切入场景已完成；当前已核实的是一张采用彩图，不据此声称镜01–04各有独立成图，或行走、落滴、低头及声音均已完成。 |
| 工程登记 | 保留图片、定义和CG02·09·01稳定代号，当前剧情无本图调用。既有基名c2_end_slow_v1保留，不据end字样推断章末用途。 |
| 核验与限制 | 原图和项目图SHA256均为f078d454659805112145d545a6710417c46beefc83ec7467f5bd89299b2824a3；本轮只更正记录，图片和剧情脚本未改，实机未验证。 |

<a id="c2-slow-attention-intro-table"></a>

### 切入分镜、台词、转场与缺图表（2026-11-07，本轮新方案）

**已完成的夜廊切入止于现稿第394行；路边躲雨范围为第395–398行。** 当前雨街制作按本轮Y01–Y04粗台本；旧镜号仅保留在脚本注释和历史记录中。游戏中第388行仍是黑场，本轮未增加调用。雨街画的是陈平安听来的故事，不是他亲历躲雨。

| 段落／镜号 | 画面与动作 | 对应台词（保留现稿） | 转场 | 素材状态／待补 |
| --- | --- | --- | --- | --- |
| 已完成｜夜廊切入，镜01–04范围 | 雨停后的夜廊，扶栏缓行，止于灯下低看。采用单图呈现扶栏低看的结果。 | [L391](../script_chapter2.rpy:391)「雨已经停了，檐角还在滴水。」<br>[L393](../script_chapter2.rpy:393)「陈平安沿着廊下慢慢走，一只手轻轻搭在栏杆上。」<br>[L394](../script_chapter2.rpy:394)「走到灯下，一滴檐水落在他手边。他低头看了一眼。」 | 已完成范围到第三句句末。 | **当前使用：夜廊彩图。** 动态与实机效果未验证。 |
| Y01｜伞沿接滴 | 伞沿水滴近景接夜廊。 | [L395](../script_chapter2.rpy:395)「他想起在青鸾国酒楼里听来的一个故事。」 | “故事”句后切入；雨声接续建议，檐滴匹配切待制作。 | 本轮粗台本已交付，画面待用户确认；现有夜廊挂滴不等于落滴动画完成。 |
| Y02｜伞过露人、赶檐 | 伞向左走过，露出抬袖朝右侧屋檐赶去的匿名行人。 | [L397](../script_chapter2.rpy:397)「撑伞的人在雨里，」 | 逗号处换格建议；与Y03为脚本中的同一句旁白。 | 本轮粗台本已交付；此前05A／05B分镜及05A独立正式线稿均停用。 |
| Y03｜已在檐下 | 同机位，省略跨阶过程，行人双脚入檐、降袖收步。 | [L397](../script_chapter2.rpy:397)「躲雨的人在檐下。」 | 脚步停、雨声继续，句末停留及点击推进建议。 | 后半句已有新粗台本承载；石台几何仍需统一。旧06A／06B和05C继续停用，不恢复旧画格。 |
| Y04｜停看雨街 | 同侧略收紧，檐下人看雨，伞客在左街走远；陈平安心念仍属画外旁白。 | [L398](../script_chapter2.rpy:398)「也想起陆抬说过的“留不住”，于是心里只剩一句话：且慢行——慢一点，才看得见人间的苦。」 | 读完点击推进建议，下一段再转陆抬忆述，时长待定。 | 本轮粗台本已交付，未制作陆抬小院、正式单镜、短片或游戏演出。 |

**素材采用边界（2026-11-07，本轮重做）。** 用户要求新的分镜，之前的不需要。本轮仅以[全新四格粗台本](#c2-rain-shelter-new-sheet)继续制作；旧两行台本、双格分镜、05A独立正式线稿和更早的雨街05B／05C及PSD全部停用，文件保留，未输入本轮生成器。夜廊采用彩图不变。[图片索引](character_image_index.md#343-第二章第09场镜04--雨停扶栏2026-11-02)。

**接出边界。** 现稿第402行“又记得陆抬曾经在飞鹰堡小院感慨……”进入后续忆述。本轮不改变文字、归属或演出，时长待配音或阅读节奏确定，不沿用历史车轮草案的25–30秒。

<a id="c2-rain-shelter-handdrawn-sheet"></a>

### 停用历史：路边躲雨两行手绘分镜台本（2026-11-07）

**停用（本轮全新四格方案取代；以下为先前确认与制作历史）。** 用户要求按新规则把之前段落做成手绘台本，并明确批准“允许新建这一张手绘台本”。本轮仅新建[05A／05B手绘台本](C:/Users/MSI/.codex/generated_images/01a19a5d-ef09-7682-afa3-c78a4ca1d1ae/exec-f339ff21-ab4e-48ca-ac66-95784d94eb90.png)一张，采用纵向两行、镜号／画面／旁白与演出／推进四栏。用户随后回复“可以就这样”，确认采用本张手绘台本。原双格保留为已选用构图参考，独立05A正式线稿的采用状态保持原记录；本次确认限于手绘台本，未新增正式素材或接入游戏。

**范围与实际内容。** 依据本页当前采用决定及现稿第395、397行，05A／05B作为镜05同一固定机位的两个动作关键格：05A近伞遮住赶檐人、伞沿接滴；05B伞左移、露出朝右赶檐的普通行人，前鞋越阶将落、后脚仍在湿街，尚未站稳。旁栏收录前句“他想起在青鸾国酒楼里听来的一个故事。”及旁白“撑伞的人在雨里，”。声音和点击推进明确标为建议，时长待定；页底保留“躲雨的人在檐下。”画面承载待定。未恢复06A／06B，未增加陈平安或陆抬在雨街现场。

**工具、参考与文件证据。** 内置 image_gen 一次调用；transparent_background=false；实际传入的唯一参考为[当前双格原图](C:/Users/MSI/.codex/generated_images/01a1a90c-e7e6-76b1-8057-9306586218e7/exec-f111620a-6287-405c-83da-b956de53bd61.png)，只用于人物动作与空间构图，SHA256为910a14c9ebb12ae31cebd47dcf2ba72e1efdb14fa242dbf1bcfdd47b28d895e7。用户早前的手绘台本图用于理解页面形式，本轮未作为参考文件传入。输出原生1199×1312，RGB PNG，1,754,972字节；SHA256为f1f407b2676740f893a78e8217fcc94a4ead79d1cb40b1b022b90c6c8206d9ef。已从实际输出解码核对尺寸并读取文件哈希，未缩放、重新编码、复制或替换任何图片。匿名路人的发髻、短袍、布鞋与伞具仅供本镜辨识，无正式角色脸部母版绑定。

**独立目检（/root/prepare_rain_sheet）。** 复核者实际查看新台本及采用原图后确认：两行粗草图和各栏可读，旁白正确，05A遮挡接滴与05B左移露人、朝右赶檐可读，05B没有画成站稳，只有本次两格。可交付观察台本形式。非阻断差异：05B石台前沿左端比05A向左延伸，背景几何未严格一致；两画框略窄于标准16:9。正式制作前需统一构图，不能把本轮作为严格连续背景、正式人物身份、动态或实机验收。用户已确认本台本采用；上述制作差异和未验证项继续保留。

<details>
<summary>本次实际图像请求（原文）</summary>

工具：image_gen；referenced_image_paths仅含上述双格原图；transparent_background=false。

```text
Use case: illustration-story.
Create ONE independent rough animation storyboard worksheet for the user's Chinese historical visual novel. The user expressly authorizes one new sheet. The provided image is a CONTENT AND GEOGRAPHY reference only: transform its existing 05A and 05B into very loose thumbnail storyboard drawings in the new worksheet format. Preserve the two action beats, screen directions, characters and location; reduce drawing detail drastically.

OUTPUT: a single upright white paper worksheet, two rows read TOP TO BOTTOM. At top a modest title “路边躲雨” and smaller subtitle “镜05｜同一固定机位的两个关键格”. Four table columns from left to right: a narrow shot-number column headed “镜号”, a dominant wide image column headed “画面”, a comfortable notes column headed “旁白／演出”, a narrow timing column headed “推进”. Exactly TWO landscape 16:9 drawn picture boxes, one in each row. Clear black table rules and ample white space. Readable Chinese annotations are essential. Do not add third/fourth panels or any other pictures. Match an animator's practical pencil storyboard sheet rather than a comic page or finished illustration.

DRAWING STYLE: extremely economical rough gray graphite gestural sketches. Visible searching strokes, simple head ovals, basic figure masses, loose clothing contours, minimal architectural perspective outlines. White paper predominates. Only a few rough gray strokes for depth. NO detailed roof tiles, brick textures, dense hatching, rendered shading, elaborate fabric folds, polished contours or photographic details. All scene drawings monochrome. Small muted RED pencil action arrows and brief labels are allowed. Annotations are neatly legible black Chinese handwriting/print; table lines straight. The storytelling can be read even at thumbnail size.

GEOGRAPHY in both frames: SAME fixed oblique street-side standing eye/chest-height camera. Wet open street on LEFT; humble Song-inspired timber shop, deep eave, low stone landing and doorway on RIGHT. One post at far right is outside the man's route. Same doorway, step edge and camera in both panels. Keep architecture to a few lines. Nearby umbrella carrier moves LEFT across the foreground. A lean adult man behind them hurries diagonally RIGHT toward the shop eave, right sleeve over forehead, coarse short tunic, cloth waist belt, calf-length trousers, cloth shoes, small cloth-bound bun. Anonymous ordinary adults only; no named protagonist. The umbrella carrier's face stays concealed.

ROW 05A: left number “05A”. Large foreground oil-paper umbrella at center-left hides the hurrying man's head, lifted sleeve and upper torso; a glimpse of moving calf/foot shows behind the umbrella carrier. The destination doorway/landing at RIGHT is visible. A single visible droplet falls from the umbrella rim; tiny muted red arrow downward and label “接滴”. Tiny far umbrella silhouette on left distance. Draw no full visible face.
Notes text exactly:
前句：
他想起在青鸾国酒楼里
听来的一个故事。

伞沿接滴，遮住赶檐人。
声音建议：檐滴接雨声。
Timing text exactly:
“故事”句后切入
匹配切待制作
时长待定

ROW 05B: left number “05B”. EXACT SAME fixed camera and stable architecture. Foreground umbrella carrier has moved largely out of LEFT edge, revealing the man hurrying RIGHT toward shelter. Clear raised right sleeve and forward leaning pose. His RIGHT leading shoe crosses the step edge, about to touch or just touching the edge; LEFT rear foot remains on wet street, body still moving, not settled. Do not draw a man standing relaxed with both feet on landing. Small muted red LEFT arrow beside umbrella, marked “伞左移”; small RIGHT/diagonal arrow by the man's route, marked “赶檐”. Distant umbrella is occluded by foreground carrier here, not relocated.
Notes text exactly:
旁白：
撑伞的人在雨里，

近伞左移，露出赶檐人。
前鞋越阶将落，尚未站稳。
声音建议：雨声、湿脚步。
Timing text exactly:
同机位
点击推进（建议）
时长待定

Below the table, one unobtrusive footnote exactly:
后半句“躲雨的人在檐下。”的画面承载待定。

Keep the illustration purposefully rough, unfinished and easy to revise. The user's main correction is to see a rough HAND-DRAWN STORYBOARD SCRIPT with notes, not another fully rendered single-frame line drawing. No colored scene, no hero portrait, no new story action, no completed arrival/settling pose, no extra panels.
```

</details>

<a id="c2-rain-shelter-redesign"></a>

### 停用历史：路边躲雨05A／05B及05A正式线稿（2026-11-07）

用户明确旧线稿不用，要求从本地动画分镜资料重新思考，并授权“找到怎么做就生成线稿”。因此停止沿旧05B／05C修补推进；旧文件保留，不作为本次构图或人物输入。首次生成时仅交付四格分镜线稿；其后仅05A上色，最新采用与展示范围以本节决定为准，不改原PSD或剧情。下方11月6日两镜五格与PSD修补记录降为历史，不作为当前执行指令。

**此前采用决定（已被本轮新方案取代）。** 用户明确现有05A／05B只是分镜稿，要求先做05A正式线稿，并批准“允许新建独立05A正式线稿”。05A单幅正式线稿已完成并整理为1920×1080，状态为候选、待用户确认，见[正式线稿记录](#c2-rain-shelter-05a-formal)；原双格分镜保留，05A此前配色仅为分镜色稿，05B仍为分镜线稿。06A／06B停用且已从原图裁去，不再制作或展示。本次止于正式线稿，未上色或接入游戏。

**剧情范围。** “他想起在青鸾国酒楼里听来的一个故事。”接入雨街，05A／05B呈现伞沿接滴、伞过露人与赶檐。05B止于越阶将落，不冒充双脚站稳。“躲雨的人在檐下”及“也想起陆抬说过的‘留不住’……”正文保留，其画面承载另定，这不构成恢复06A／06B的待办；不自动删改剧情。画面中的人是故事里的普通路人，陈平安和陆抬均不在现场。雨停夜廊已采用彩图保持不变。

**空间方案。** 街边胸／眼高斜向平视，湿街在左，铺檐和低石平台在右。近伞客在前景沿街向左；无伞人从中景向右后方进入铺檐，两条路分开。檐柱置于通路外缘，门洞、柱和低台阶跨镜固定。檐口滴水线按投影落在站立区外，不与台阶前沿合成同一根重线。远景小伞从第一格就出现并向左走。无伞人为匿名成年群演，素布束髻、粗布短袍与布鞋，不设定为既有人物母版；新人物细节仅供本次分镜，不反向确立正式身份。

| 画格 | 构图与行动 | 台词、声音与检查点 |
| --- | --- | --- |
| **已选用：05A 接滴** | 近伞在前景遮住无伞人的头肩和举袖，伞沿滴水；右侧目的屋檐始终可见。 | “故事”落音后切入；檐滴接伞滴为待制作的匹配切。现有夜廊彩图的叶尖挂滴不冒称已完成檐滴动画。 |
| **已选用：05B 露人、赶檐** | 同机位，近伞左移，让出中景抬袖赶向右侧屋檐的人。原方案前脚仍在湿地；实际线稿画为前脚越过阶沿、将落／初触缘，尚未全脚落稳；不再安排06A接续承重。 | “撑伞的人在雨里，”；视线从伞移向行人，不用镜头追着伞跑。 |

<details>
<summary>停用的06A／06B设计记录（不再制作或展示）</summary>

| 历史画格 | 原构图与行动 | 原台词与检查点 |
| --- | --- | --- |
| 停用：06A 跨入、收脚 | 同轴收近为全身；同一前脚落到檐下，后脚正在收过滴水线，身体仍向内移动。 | 动作中切，不重复跨步，不调换前后脚；大近伞已出画，远景小伞继续走。 |
| 停用：06B 站稳、停留 | 同一近机位，双脚平稳落在檐内同一平台，重心落稳，肩背松、抬袖臂放低；左侧留雨街。 | “躲雨的人在檐下。”落在站稳；后续“且慢行”旁白继续停留。画人停住、雨仍下，不增摔倒、受伤、救助。 |

</details>

**首次四格方案资料与独立预审（历史）。** Framed Ink印页55（PDF56）看相邻画面焦点位置，印页68–69（PDF69–70）看固定机位内的人物运动与先后显露；本轮已目读原页。《电影镜头设计》印页148、222、324–326（PDF170、244、346–348）分别提供动作中切、兴趣中心转移、匹配镜头与动作划变的区分；/root/rain_film_reference复核既有实读依据。/root/rain_animation_reference空间预审要求：05B脚仍在湿地、06A同一前脚入檐；近远通路分开；滴水线与台阶边缘分别成立；出画的大伞不重现。此为方案预审，不等于实际线稿已通过。目标整张1920×1080，2×2四格，每格横向画幅；实际原生输出1672×941，未放大或改写像素。

**历史状态（本轮已停用）。** [路边躲雨05A／05B双格原图](C:/Users/MSI/.codex/generated_images/01a1a90c-e7e6-76b1-8057-9306586218e7/exec-f111620a-6287-405c-83da-b956de53bd61.png)最初由内置image_gen生成四格，生成标识exec-f111620a-6287-405c-83da-b956de53bd61；该次请求未输入旧线稿。初始1672×941的历史SHA256为aa2142b156a89a7887925d5d5097aa7a5c5c631292e1064e3e30e220175a5c4b，局修线稿历史SHA256为a4eccd6b9f5447c25f6871e9d637939c906f905111879af817dbeabdffc83bf2，05A上色后的历史SHA256为e556495a3ca07af0dd5596ee2bb43d8db61fb5d1e2a504b3ca0636fee55820ad。按用户最新批准已裁去下排，当前为1672×497、全不透明RGBA PNG，SHA256为910a14c9ebb12ae31cebd47dcf2ba72e1efdb14fa242dbf1bcfdd47b28d895e7。05A／05B当前使用（分镜构图已选用；05A分镜色稿待确认，05B保持分镜线稿）；06A／06B停用，已从原文件移除。该分镜仍为同一原文件；另获授权制作的独立05A正式线稿见下节，动画与游戏演出未完成。

<a id="c2-rain-shelter-05a-formal"></a>

**05A独立正式线稿制作历史（2026-11-07，本轮已停用）。** 用户指出现有图只是分镜稿，要求先做正式线稿并授权“开始修改”，随后明确“允许新建独立05A正式线稿”。本次例外仅新制作一张独立正式05A；现有双格分镜保留，05B不推进，06A／06B继续停用。停止点为正式线稿，不自动上色或接入游戏；之前05A上色仅记为分镜色稿，不作为正式美术已完成。

**任务、构图与空间依据。** 沿用本节已确认剧情、镜位和遮挡。街左、檐右，近伞客向左经过，赶檐人向右进檐且头肩仍被伞遮住，右侧保留目的石台与通路；远处只有一名小伞客。正式画幅目标1920×1080，单幅横版，无标题、镜号或拼板。对近伞汇聚、弧面、握柄手及袖口重新落实结构，梳理赶檐人的露出肢体、石台砖缝和梁柱节点，减少不解释结构的碎纹。近伞客与赶檐人均为匿名成人，其脸按剧情遮挡，远人仅作剪影；不绑定陈平安等主角母版。前述独立制作任务单要求重画结构与线条，不以去色、锐化或放大充当正式线稿。

**实际参考与调用。** 内置image_gen成功返回一张新图；transparent_background=false；referenced_image_paths仅含当前双格原图。原图SHA256为910a14c9ebb12ae31cebd47dcf2ba72e1efdb14fa242dbf1bcfdd47b28d895e7，1672×497；已实际查看。请求明确仅采用左05A构图，右05B只是后续动作对照，不出现在结果中。无旧PSD、旧四格底排或主角母版输入。完整实际请求保留在下方。

**实际输出与同文件尺寸整理。** [05A独立正式线稿](C:/Users/MSI/.codex/generated_images/01a1a90c-e7e6-76b1-8057-9306586218e7/exec-8ca83436-2e44-4622-aef9-66e66433db10.png)；生成标识exec-8ca83436-2e44-4622-aef9-66e66433db10。原生1672×941、3,186,611字节，原生SHA256为828ce75b47857893c5879be16c63bbcb9f0fcc66bb5ffef5c1311f1d0c257615。随后在内存中按1.1483253588516746倍等比重采样，竖向居中裁去约0.287像素／边，得到1920×1080；未改变构图、姿态或局部结构。使用FileMode.Open打开这张新原图，写前锁定核验原生哈希，定位写入、截尾、Flush(true)，无另存、替换或中间图文件。回读字节与内存编码一致，最终4,094,673字节、全不透明RGBA PNG，SHA256为7556e593cff66a804ee8ac964f583b03a3ff1b86880a8afd251c2123f9db53a6，原文件标识4222124651165711保持一致。原双格分镜逐字节未变，哈希仍为910a14c9ebb12ae31cebd47dcf2ba72e1efdb14fa242dbf1bcfdd47b28d895e7。

**正式线稿独立复核。** /root/rain_animation_reference实际查看原生图、握手及腿脚局部，并重新查看上述最终哈希图：大伞维持05A遮挡，赶檐人仍只露衣摆、裤腿及鞋，朝画右屋檐行进；近伞客的脚在画外，具体步态不据此宣称完成。握柄手、腕与袖口连接成立，赶檐人的可见腿鞋和湿街接触未见硬伤。柱脚、石台和铺地关系清楚，雨街与檐内干湿可读；线条已重新绘制为独立单幅。最终尺寸整理未引入可见拉伸、截断或线条损坏。近景匿名人物头脸按剧情遮住，远人仅作小剪影，本图不作陈平安或陆抬身份验收。

**保留项与历史采用状态。** 本轮已停用；先前为候选（正式线稿完成，待用户确认）；伞杆延长线与伞顶中轴轻微偏离，原生约15–22像素、最终约17–25像素，独立复核判为非阻挡精修项，未声称已修正。未上色，未制作05B正式图，未绑定bg_images.rpy或剧本调用；转场动画、对白框叠放与游戏实机未验证。本次仅更新既有制作记录和图片索引，不新建记录、候选副本、预览或备份文件。

<details>
<summary>05A正式线稿实际请求</summary>

Use case: illustration-story / production line art.
Create ONE new independent FINAL-LINEWORK drawing for shot 05A of a restrained Chinese historical visual novel. Target 1920 x 1080, landscape 16:9. This is the full-size production line-art stage, NOT a storyboard thumbnail or an enlarged / desaturated copy.

REFERENCE USE: The attached image is a two-panel storyboard sheet. Use ONLY its LEFT panel, 05A, as the composition and blocking reference. The RIGHT panel is a later moment and MUST NOT be reproduced. Output exactly ONE continuous scene filling the entire canvas. Remove all sheet titles, panel labels, borders, gutters and comparison layouts. No text or lettering anywhere. Do not depict 05B or any extra frame. The source sheet remains a separate reference.

NARRATIVE MOMENT: A story heard in a tavern, about ordinary people in rain. A large oil-paper umbrella passes screen-left in the foreground, currently still concealing the head, raised sleeve and upper torso of a second man who is hurrying toward a shop eave on screen-right. This is the BEFORE-REVEAL moment. Do not show the second man fully revealed or already standing under the eave. Do not introduce the storyteller, Chen Ping'an, Lu Tai, a jade hairpin, weapons or a book box.

LOCKED COMPOSITION: Retain the LEFT panel's street-side chest/eye-level oblique view along the rainy lane. Rainy open lane and distant houses on the left; humble tiled timber shop and raised stone landing on the right. Main nearest timber post remains near the far right edge. The same shop doorway, small ceramic jar and leaning bamboo container remain behind the landing. The foreground umbrella canopy occupies roughly the left 60% of the frame; apex around x35%, y15%; its lower curved rim around y53–57%. The carrier's clothed body occupies lower center-left and continues out of the bottom frame. Keep ample readable empty landing to the right. A tiny distant umbrella carrier is visible in the far left street. Preserve this quiet three-depth arrangement; do not add crowds.

FORMAL REDRAW REQUIREMENTS:
1. Reconstruct the oil-paper umbrella with one coherent central hub, ribs meeting that hub, correct smoothly curved canopy, and a believable foreground rim. Each visible rib is a purposeful structural line rather than doubled scribbles. Draw a slender wooden shaft whose connection to the concealed upper structure is plausible and whose visible lower part is firmly held in ONE natural hand. Clearly resolve fingers, thumb, wrist, sleeve opening and shaft occlusion without extra digits.
2. The foreground carrier is an anonymous adult in a plain long coarse-cloth robe walking screen LEFT. Head and face remain completely hidden behind the umbrella. Draw a clean natural garment silhouette and a limited hierarchy of major folds following gravity and walking, with finer secondary seams only where useful. No jewelry or heroic costume.
3. The second anonymous man remains behind the first carrier and canopy, oriented diagonally toward screen RIGHT. Preserve only the original small visible portions: a hem / sleeve fragment behind the umbrella's right underside, plain calf-length trousers, an exposed lower leg and simple cloth shoe on the wet street side of the step. Work out his anatomy behind the occluder so these fragments connect logically; no disembodied leg, duplicated foot, visible new head, long exposed upper body or different pose. The umbrella must still hide the revelation that will happen in 05B. Do not mirror him.
4. Refine architecture as a real humble Song-inspired timber storefront: door jambs meet their beam, panel frames have coherent joints, the near post terminates in a stone base, tile rows follow roof planes. Align the platform's upper surface, vertical step face and paving joints to the same perspective. The front edge stays low enough to step onto and out of the man's way; no impossible raised wall or bent step. Ceramic jar and bamboo container sit with clear contact on the landing. Keep architecture placement stable relative to the LEFT reference panel.
5. Draw rain as fine separated strokes and broken runoff, with a few readable droplets at the RIGHT tip of the large foreground umbrella as the attention point for the preceding eave-drip cut. Wet street has sparse broken reflection marks and small puddle ripples, not an ocean, thick radiating circles or densely scribbled water. Covered landing is mostly dry with faint dampness near its outer edge and no rainfall inside. Roof runoff and the front stone step edge are distinct physical boundaries.
6. Establish deliberate line weight: foreground umbrella, hand and robe clearest; midground architectural structure thinner; distant houses and tiny umbrella simplified and lighter. Use clean continuous contours with selective elegant line breaks, controlled fine internal detail, very sparse short hatching only for necessary overlap or core shadows. Remove the rough pencil grain, crosshatching carpet, muddy tone masses, duplicate construction strokes and indiscriminate tile/wood noise of the storyboard. The result must be suitable for subsequent careful coloring.

STYLE: semi-realistic Chinese historical production illustration, natural anatomy and practical building structure, restrained everyday humanity, refined black and neutral gray INK LINES on a clean white base, no colored pixels, no sepia paper, no filled color, no finished grayscale painting, no heavy comic screen tones, no photoreal render, no anime stylization, no fantasy ornament. Detailed where structure and storytelling need it, spacious and quiet elsewhere.

DELIVERABLE: one standalone 16:9 production line-art frame based on LEFT 05A only, fully redrawn with crisp resolved linework. No heading, no number, no panel borders, no inset, no side-by-side image, no lower row, no arrows. Stop at line art.

</details>

<a id="c2-rain-shelter-two-panel"></a>

**取消下排并原位裁切（2026-11-07）。** 用户先要求“06A和06B已经不需要出现”，再明确批准“允许裁去原图下排并保存”。在同一原PNG中保留[0,0,1672,497)，裁去下方06A／06B；标题、两格标记、格框及05A／05B画面均保留原坐标，不重采样、不重画。06A／06B不再作为当前制作、展示或自动恢复任务，先前生成、分镜与检查文字仅作历史。

**实际写入与验证。** 已确认使用System.Drawing内存裁取与原文件FileMode.Open／ReadWrite直接保存；写入前核对源哈希和并发变更，定位写入后SetLength、Flush(true)，再回读核对写入字节。源SHA256为e556495a3ca07af0dd5596ee2bb43d8db61fb5d1e2a504b3ca0636fee55820ad；当前1672×497、1,639,946字节，SHA256为910a14c9ebb12ae31cebd47dcf2ba72e1efdb14fa242dbf1bcfdd47b28d895e7，RGBA像素SHA256为1f67f0537f093b3f4e0575cd3166c599d122701b0e83c32af9e04b497cc5f7a8。独立PNG解码回读与裁切前上方497行逐字节一致，保留区域像素变化为0；原文件对象ID15762598696002754与编辑前一致。未创建候选、预览、备份、临时文件或另存新图，未删除文件，未改剧情、图片定义或游戏运行素材。

**裁切后独立目检（/root/rain_animation_reference）。** 已实际读取保存后的双格原图：仅见“路边躲雨”标题、05A和05B；两格上下左右黑框完整，底部留白正常，没有06A／06B图像、编号或边框残边。仅验证本次裁切，色彩与人物检查沿用此前05A上色及05B线稿复核，并由保留像素完全一致的差分证据绑定。当前为分镜展示图，未执行游戏对白、动态或实机验证。

<a id="c2-rain-shelter-05a-color"></a>

**05A逐张上色（2026-11-07）。** 用户明确“先做05A”，在已通过局部修补的同一原PNG上继续。场景仍为听来的青鸾国雨街故事：近伞遮住赶檐人的头肩，目的屋檐在右；没有陈平安或陆抬在场。沿用已验证构图、台阶、人物动作和遮挡，本轮只改变05A各材质的色调，不重采样、不移动或重画结构。匿名近伞客和赶檐人均按本镜遮挡保留头脸不可见；远景伞客只有剪影，不新增脸部身份。三人的位置、服装轮廓和道具数保持原稿，未建立正式角色母版。

**配色与实际操作。** 阴雨散射光；湿街、远屋与雨幕偏冷灰，檐下石台浅暖灰，瓦顶灰青，木门与柱灰棕。近景油纸伞灰米褐，近伞客灰青布衣，赶檐人麻灰短袍、灰绿裤、素布鞋，手和裸露小腿用低饱和肤色。沿原伞面、伞柄、手、衣服、门木、陶罐、竹篮、石台与柱础分区映射明暗，保留既有笔触、雨线和碎反光；伞面、手脚轮廓经放大对照后收边。原像素的明暗逐点映射到各材质颜色，未生成替代图、未输入其他角色图、未添加灯笼或新光源。供05B后续衔接的工作色：油纸高光RGB(219,199,161)，近伞客布衣高光(147,164,164)，赶檐人短袍高光(192,179,151)，湿街高光(215,226,226)，石台高光(211,210,190)，门木高光(158,145,121)；这些是本轮方案，尚非用户锁定的角色标准。

**首轮上色原位保存证据。** 编辑前确认使用Node文件接口的r+原文件读写方式，操作只在内存解码、局部颜色映射与编码；以同一已存在文件句柄定位写入、ftruncate及fsync。写入前核对源SHA256和文件对象并再次检测并发变更，编码后先验证像素，再写入并完整回读；未创建图片、脚本、预览、备份或临时文件，未重命名或替换原件。实际调用为exec_command的Node标准输入脚本，退出码0。保存后3,253,659字节，文件对象ID仍为15762598696002754；首轮文件SHA256为b6b2bdd9652fa34900dbfa0027b7316be2293338e54d84f90d3a1150bff3bfbb，RGBA像素SHA256为9ddd320e1d165222c317debaa325f24de3deeab9045ba6ab428671fac66cf532。独立PNG解码回读与内存期望像素逐字节一致。相上色前变化343,410个像素，全部位于05A [8,70,830,489)；05A标记保护区[17,75,65,96)、区域外、其余三格以及全部alpha通道变化均为0。

**建筑分色返修与最终保存。** 首轮独立目检指出灰墙上沿木色形成硬边、门洞深色斜切木板。对照原墨线，将墙面收回梁柱间，补齐门框立柱与横档木色，将暗色收进实际门洞内缘；仅修正建筑局部16,513个像素，涉及[555,122,743,349)，其他色区不动。终端分块传输因接收问题没有触发写入，已结束该等待进程；最终用直接原文件读写完成修补，没有把失败传输计为已保存。续修从首轮已保存像素的色调区间反算明暗并重新分色，未重新生成或移动结构。

最终文件3,251,756字节，SHA256为e556495a3ca07af0dd5596ee2bb43d8db61fb5d1e2a504b3ca0636fee55820ad，RGBA像素SHA256为9b131642a07969b55a38d3c21e7b3a0531270d3012b97a85a5489a3f2326f8ed。实际r+定位写入、ftruncate及fsync后回读逐字节一致，另一PNG解码器读回像素亦与准备结果一致；磁盘文件对象ID15762598696002754仍与本轮编辑前相同。相上色前局修线稿共变化343,410像素，边界[8,70,830,489)；05A保护标记、区域外、其余三格及alpha变化均为0。两份既有制作文档直接原位更新；未改剧情、图片定义、游戏素材，未创建独立图片或新记录文件。

**05A上色独立复核（/root/rain_animation_reference）。** 已读取最终原图并核对上述SHA256，查看整板与局部：两项建筑硬边问题已消除，灰墙位于梁柱之间，门框及横档分色完整，深门洞沿内缘落色；未见新增明显漏色或接缝。暖灰米纸伞、灰青近伞客、麻灰赶檐人层次可读，伞继续遮住后者头肩；手与伞柄、小腿与裤脚及鞋分色明确，水滴与雨丝清楚，冷湿街与较暖石台区分成立。可交付05A本轮着色结果，颜色尚待用户最终确认。头脸按剧情遮挡，不构成脸部身份验证；远人只保留剪影。05B、06A、06B没有本轮色彩通过结论。未执行上色后的动态、对白框或游戏实机验证，未将本次分镜色稿记为正式精绘。

<a id="c2-rain-shelter-local-repair"></a>

**05A／05B局部修补及实际保存（2026-11-07）。** 授权为用户“用05A和05B”后续“开始修改”，目标是上方同一新四格PNG，不恢复旧PSD任务。先核对门洞、门边器物及柱在两格中的横向偏移为836像素、纵向基本固定；真正阶沿在05B比05A低约29像素，不能把石板砖缝误当阶沿。保持05B的脚与台阶关系，以其空平台为依据接回05A地面；05B原错位远景小伞及短倒影以邻近雨街纹理局部补除，使其在这一瞬间由前景伞客遮住，不把远人画成向右跳位。主赶檐人、近伞客、门洞与器物主体、标题、格框和下排不修改。

首次局修保存的历史SHA256为87d141fe8cbbc7788e89f80ad1b94e09ad7e02ab3d2492b727b91aa470a99556。独立目检发现05A左端地面局部模糊、重复弧纹，因此继续只修x427–564、y346–448的接缝，以05B空地面的清晰石板纹理沿阶沿方向接回；05B保持首轮局修结果。返修没有整图生成或新增图像文件。

**线稿局修写入证据。** 使用Windows System.Drawing在内存处理指定区域并编码PNG，随后以FileMode.Open／ReadWrite打开原文件，写回、截断到实际长度并Flush(true)；无另存、新建文件替换、重命名、候选、备份或临时文件。两次写入均有前置哈希与并发变更检查、写后字节哈希回读。最终文件为3,255,818字节，磁盘文件对象ID15762598696002754与编辑前一致；这同时有实际写入记录支持，不只依据路径。最终RGBA像素SHA256为7da2093bca9a49350248095f0bc4406a907165663d34ac60436ecff0f42929e2，磁盘回读与本轮修补期望像素完全一致。相最初原图变化60,562个像素，合并边界为[428,238,1033,489)；05A允许区[427,346,830,489)与05B允许区[969,234,1038,347)之外变化为0。两主人物保护区、下排06A／06B变化均为0。未改剧情、bg_images.rpy或游戏资源文件。

**保存后独立视觉复核（/root/rain_animation_reference）。** 已核对最终SHA256，并查看整板与05A修补处放大画面：模糊和重复弧纹已消除，砖缝清楚，未见明显矩形贴片、双重阶沿或腿脚被台阶吞入；05A／05B的平台关系协调。05B小伞清除区无可辨残人、伞尖或短倒影残留，前鞋仍读作越阶将落／初触缘。结论为本轮局修可接受，可交付已选用的上排分镜线稿；不代表上色、动画逐帧连续性、游戏接入或用户最终美术确认。

**首稿独立目检（/root/rain_animation_reference，2026-11-07）。** 已读取同一SHA256原图，并在内存放大05B／06A／06B足部。05A近伞遮头肩、05B左移露人可读；05B前鞋越沿将落／初触缘，06A前鞋平贴平台且后脚收进，06B两脚落稳、上身直起且手臂下降，未见明显反向或前后腿交换。主行人布束髻、粗布短袍、布带、短裤与素鞋总体连续；05A头部遮挡，匿名群演无正式脸部母版，不宣称主角身份通过。门洞、近远柱和门边器物均保留同侧。可交付为待确认分镜线稿，非正式美术定稿。

**未验证与剩余限制。** 已消除05B远景小伞向右跳位，并将05A可见阶沿和地面接到05B的空间位置；未把背景逐线统一，不能直接作为连续动画帧。滴水线地面投影未精确验证。当前双格板1672×497，各格仍略宽于16:9，不能直接当作正式16:9单镜。05B仅为越阶将落／初触缘，尚非收步站稳；后半句正文的画面承载另定，不恢复06A／06B。

**验证边界。** 当前采用05A／05B两格，原始四格生成与检查记录仅作历史；不能证明雨线、脚步、伞客运动及匹配切已经制作。尚无连续帧、配音时长、游戏对白遮挡或实机验收。人物为新设计的匿名群演，没有已确认脸部母版；只验证本张内部的发髻、衣装、朝向和动作连续性，不宣称主角身份通过。

<details>
<summary>2026-11-07实际生成请求（原文）</summary>

工具：内置image_gen；transparent_background=false；无参考图输入；一次调用。

Use case: illustration-story.
Create ONE NEW monochrome hand-drawn cinematic storyboard sheet for a restrained Chinese historical narrative, titled only “路边躲雨”. This is a fresh design, not an edit of any earlier image. Do not use any previous window-view drawings or character images from this conversation. Target canvas 1920 x 1080, landscape 16:9. Four equally sized cinematic wide frames in a clean 2-by-2 grid, read top left, top right, bottom left, bottom right. Narrow white gutters. Small discreet panel labels exactly “05A”, “05B”, “06A”, “06B”. No other writing, no dialogue, no arrows. Each panel is a successive moment of ONE action in ONE consistent place, never four concept variants.

STORY: A remembered story of ordinary passersby: a large umbrella crosses leftward in the rain, gradually revealing a man hurrying to shelter. He enters a shop eave, brings his rear foot in and stands still while rain and an umbrella farther in the street continue. Do not depict the storyteller or any named protagonist.

LOOK: refined but economical graphite and pen storyboard linework, mostly white paper, varying thin and thicker outlines, a little dry pencil hatching to separate foreground and depth. Accurate natural adult proportions, restrained everyday gestures, historical Chinese / Song-inspired humble timber storefronts, tiled overhang, worn paving. Natural weather, quiet humane feeling. No color, no polished grayscale painting, no fantasy ornament, no anime faces, no decorative dense texture. Prioritize clear silhouette, readable hands, grounded shoes, spatial continuity, and contrast between walking and stopping.

GEOGRAPHY AND CAMERA: street-side camera around a standing person's chest/eye height, oblique view along a narrow rainy lane. Never upstairs, never through a window, no interior window frame or sill. The wet open lane lies on the LEFT and center. A humble storefront with a deep roof overhang and a low covered stone platform is on the RIGHT. A single timber support near the far right edge and the shop doorway behind it are stable landmarks. Roof eave makes a strong diagonal across upper right; the street recedes toward upper left. The pillar is outside the man's walking route, not blocking it. There is clear walking room under the roof. Roof drip boundary lies outward of the dry standing area; it is a broken curtain of sparse drops, not a thick line and not identical to the stone step edge. Under the roof the paving has faint damp shoe marks but no falling rain, no mirror-like standing water. Outside has thin rain streaks, little puddles and broken reflections, never ocean waves.

CHARACTERS kept identical throughout:
A) main unprotected passerby: one ordinary adult man, lean average build, plain cloth-bound small bun, coarse knee-length wrap tunic, simple cloth waist belt, calf-length trousers and plain cloth shoes. Three-quarter rear/side view facing screen RIGHT throughout, never posing toward viewer. His right forearm/sleeve initially raised over his brow against rain. No jade hairpin, weapons, backpack, costume change, youthful hero face, luxury details.
B) one nearer umbrella carrier, plain long robe, face concealed by a big oil-paper umbrella, walking from screen RIGHT toward LEFT in the foreground wet lane. Their lane is closer to camera than A's diagonal route toward the shelter; they do not collide. Their umbrella is overhead, shaft attached naturally to a hand.
C) one very small distant umbrella silhouette in the left background, already present in 05A and walking gradually leftward in each frame. It stays a distant ordinary figure, not another focal character. No other crowd.

PANEL 05A (top left): wide establishing frame, fixed camera. The large foreground oil-paper umbrella spans much of the center-left foreground, its canopy overlaps and hides most of A's raised arm/head and upper torso behind it. A hint of his moving lower leg may show below but his whole action must not yet be revealed. Show one clear little drop falling vertically from the nearby umbrella rim as a visual bridge from the prior eave-drip scene. The doorway, covered landing and pillar on the RIGHT remain visible as the destination. Distant small umbrella is visible in the left depth. Do not clutter the opening with a fully visible second main man.

PANEL 05B (top right): EXACT SAME camera, focal length, roof, platform and pillar placement as 05A. Foreground large umbrella has moved toward and partly beyond the LEFT edge, exposing A clearly at middle-right. A is caught hurrying diagonally toward screen RIGHT into the shelter, right sleeve raised, torso slightly pitched forward. His lead foot is STILL ON THE WET STREET, about to step onto the low covered platform; neither foot has already completed the entry. His stride and clear empty path carry the eye to the dry landing. The near umbrella must not reverse direction or remain centered.

PANEL 06A (bottom left): cut during the entry movement to a CLOSER full-body view on the same side of the action axis, same screen-right direction and same storefront. A's SAME lead foot has now landed flat on the dry platform, his rear foot is still lifting over the drip boundary, knee naturally bent and body moving inward. One believable support foot, one moving foot: no extra limbs. His raised right sleeve is beginning to lower. Preserve the doorway and timber post on the RIGHT, with enough left-side rainy street to understand where he came from. The big foreground umbrella has already left this closer frame; do not reintroduce it. The distant little umbrella continues in the left background.

PANEL 06B (bottom right): EXACT SAME closer framing and landmarks as 06A. A has finished arriving and stopped. Both shoes now rest FLAT on the SAME covered paving surface inside the roof-drip boundary, separated in a relaxed stable stance; rear shoe comes alongside but not crossed over the other. No raised heel exposing a whole sole to camera, no airborne running foot. Body mass settles between the two feet, torso is upright, shoulders slightly relaxed; the previously raised right arm is lowered to roughly chest/waist height naturally, not still shielding the head. He quietly faces out toward the rain at screen-left only with a small head turn, while chest/hips retain the same generally screen-right orientation; do not rotate his whole body. The empty wet lane occupies the left half and the distant small umbrella has progressed leftward. Keep this ending quiet and spacious so the still figure, continuous rain and departing umbrella tell the feeling of a brief pause. No theatrical sadness, injury, falling, rescue, moral judgement or gestures to camera.

Continuity is more important than extra detail. Large umbrella moves left; main man moves right and then stops. 05A/05B share one stable view; 06A/06B share another stable closer view. Show the action sequence rather than four copies of the same running pose.
ANATOMY CONTINUITY LOCK: His RIGHT foot leads into the shelter in 05B/06A; his LEFT foot follows in 06A/06B. Track these same physical feet across the cut. Do not mirror the figure.

</details>

<a id="c2-rain-shelter-execution"></a>

### 路边躲雨：旧两镜五格与PSD修补记录（2026-11-06，已停止执行）

用户在阅读分镜资料后的方案基础上授权“开始解决”。本轮先在现有原件范围内落实动作和遮挡；保留05B宽景、05C收紧画面的俯视机位与建筑位置，不改整条街，不扩大到车轮、陆抬小院或章末演出。镜05的三格为同一固定机位的动作阶段；镜06的两格为同一较近画面的收步与停留，不据五格要求新建五张背景。

| 关键画格 | 画面与动作目标 | 台词／声音／切点 | 验收条件 |
| --- | --- | --- | --- |
| 镜05·接滴 | 近处伞沿接住前一镜水滴的注意位置；右侧仍可辨屋檐与石阶。赶檐人的肩和举袖先被近伞遮住。 | 夜廊上说完“他想起在青鸾国酒楼里听来的一个故事。”；“故事”落音后切入雨街，檐滴接雨打伞声。 | 不把已有叶尖挂滴当作已完成檐滴；不加陈平安在窗内观看的前景。 |
| 镜05·露人 | 机位不动，近伞向左平稳走开，逐渐露出抬袖遮雨、朝右侧檐下赶去的人。 | “撑伞的人在雨里，”；注意从伞转给无伞人。 | 以真实前后遮挡实现露人；不能只在原图上加箭头。伞客与赶檐者不互相穿过。 |
| 镜05·赶檐 | 同一空间继续。赶檐者前脚将跨上台阶，后脚仍在湿地；伞持续离开。 | 湿脚步略急，在跨入动作进行中接镜06。 | 来路与去向清楚，台阶前沿和檐柱不挡通路；切镜后不重复起步。 |
| 镜06·收步 | 同侧较近画面保留人物、檐柱与滴水边界。后脚收进，双脚落稳，肩背松一点，抬袖的手臂开始放下。 | “躲雨的人在檐下。”；脚步停，雨声继续。 | 能读成到达并停住，不能沿用后脚仍悬起的奔跑姿势冒充收步。 |
| 镜06·停留 | 继续停在檐下的人，边缘仍可见雨街与经过的伞；不另插入苦脸特写或新增事件。 | 本轮按建议在此承载第394行“也想起陆抬说过的‘留不住’……”完整旁白，实际原文不改。时长待配音确定。 | 人停而雨仍在；不因旁白提到陆抬就把他画成雨街现场人物。 |

**原件结构已核对，尚未修改。** Photoshop内只读打开[05B原PSD](<F:/project/JianlaiWhentheSwordArrives/game/lh/cpa/05B rain crowd effect.psd>)和[05C原PSD](<F:/project/JianlaiWhentheSwordArrives/game/lh/cpa/05C rain crowd effect.psd>)。两份均为三层：新增左／右路人各一层，其余合在背景中。05B为1159×649，陈平安过肩、主要近伞和赶檐人不在独立层；05C为1159×645，主行人及其脚部也合在背景。故下列处理属于局部补画，不能描述成简单隐藏人物层或挪动现成分件。

| 原件 | 本轮局部处理范围 | 必须保留 |
| --- | --- | --- |
| 05B | 沿陈平安前景轮廓补回被遮挡的窗边／街景；重排近伞的遮挡，使肩与举袖确实先被盖住、再向左露出。人物去除区约在左侧x0–315，须沿轮廓选择，不能整块矩形涂除。当前近伞约x350–500、y300–515；它的高度低于赶檐者头顶，不能只横移而忽略遮挡高度。 | 原画幅、建筑透视、门洞、檐柱、台阶、酒瓮和普通路人身份；已完成夜廊彩图不动。 |
| 05C | 赶檐者约x600–725、y205–425内调整后脚、重心及举袖臂；整理其附近檐下雨线、地面水纹和鞋底接触，明确滴水线内外。 | 原画幅、建筑、人物衣装发型朝向及既有相邻路人，不将整个平台抹成干白。 |

上述坐标来自原PNG目检，只用于圈定待核区域；实际操作须以PSD像素位置复核，不直接当作矩形填补范围。独立空间复核为 /root/rain_animation_reference：原机位与建筑可沿用；原05B只呈现露出后的状态，原05C只呈现跨入过程，两镜五格目前未通过。

**资料依据。** [Framed Ink](F:/中国古建筑学习资料_20261031/02_动画分镜/framed-ink_drawing-composition-for-visual-storytellers_Marcos_Mateu-Mestre.pdf)印页55、68–69（PDF56、69–70）：关注点衔接及固定机位中的动作构图。[电影镜头设计](<F:/中国古建筑学习资料_20261031/02_动画分镜/电影镜头设计 从构思到银幕 (Pdg2Pic etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf>)印页148、222、324–326（PDF170、244、346–348）：动作中切镜、兴趣中心转移、匹配连接与动作划变的区别。[动画分镜头设计](<F:/中国古建筑学习资料_20261031/02_动画分镜/动画分镜头设计 经典动画片解析 (刘辉，孙文博编著, 刘辉, 孙文博编著, 孙文博, Sun wen bo, 刘辉 etc.) (z-library.sk, 1lib.sk, z-lib.sk).pdf>)印页48、146–149（PDF56、154–157）：固定镜头、连接逻辑、相似形象与视线连接。以上为实际查阅页；具体场景安排是本项目应用，不冒称书中原例。

**当前执行状态（2026-11-06续做）。** 用户已明确允许“原PSD正常保存”，并要求先核验05B、无问题再保存，然后修改05C收步。05B局部生成两次未留下结果；内容识别试填出现街面误填到室内，已撤回。随后在原05B文档中以原图像素和局部填色重建遮挡区，当前四个编辑层为“05B foreground removal repair”“05B window jamb continuation”“05B sill and street continuation”“05B lower sill edge alignment”。最后一轮窗框／窗台接缝尚未完成视觉核验：电脑操作连接曾报“already has an active request”，刷新后截图仍返回其他窗口而非Photoshop画布。未执行保存，改动只留在Photoshop内存；不能标为通过或定稿。05C尚未修改。已请用户恢复Photoshop前台及处理待确认的其他电脑操作；不再要求重复批准正常保存。磁盘05B SHA256仍为f243beec698544258b3c81a633f7835bb3db9d6a501c5cbc1c5684db3c6852cf，05C仍为1e16a20b70ef8dce98c553aa77e77560fdad68b289a0dea56bcfb4efc28aa790。未另存图片、未接入游戏。

<details>
<summary>已撤回的车轮四镜建议（仅保留历史，不作为当前分镜或补图顺序）</summary>

以下为被用户最新脚本范围取代的旧建议；其中把第391–394行留在夜廊读完、先补车轮等安排均不再执行。

#### 已撤回的车轮四镜建议（历史文本）

本表依用户要求整理新四镜切入。范围止于现稿第394行“且慢行——慢一点，才看得见人间的苦。”句末；第398行开始的陆抬忆述属于下一段。沿用当前正文顺序，不提前搬用第419行崔东山的“历史车轮”台词。本轮仅整理此表，未改剧情、图片或运行调用。独立文字与连续性复核为 /root/intro_table_review。

镜号均指11月5日新四镜方案，与下方旧第09场镜01–04分别识别。前两镜是剪辑意象；第三镜回到现实夜廊。泥地上的折草与栏上的折草只以形状相接，不能表现为同一茎草移动或变形。

| 新镜号／镜名 | 画面与动作 | 对应台词（当前剧本） | 转场与声音设计 | 素材状态／缺图 |
| --- | --- | --- | --- | --- |
| 01｜车轮疾行 | 贴近路面的局部特写，普通木轮从左向右迅速掠过，轮缘大部分出框，路边草被压弯。镜内无人。 | **无对白。** 保留后文“历史车轮”的首次完整解释，不在这里提前朗读。 | 前段敬酒台词结束后，宴席声退去，短黑场中轮声先起，再切进木轮；轮声短而近，不用宏大配乐。 | **缺独立成图。** 已有四格概念线稿可作设计依据，不能算镜01成图。 |
| 02｜轮过折草 | 同一道路、同一低机位方向。轮已出画，停看泥地上受损的细草与叶尖水滴，让细物显出来。 | **无对白。** 给观众看清草的时间。 | 接轮子向右离开的方向；碾压声迅速远去，留一拍安静。镜尾用折草斜向和叶形准备切到镜03。 | **缺独立成图。** 需锁定轮辙与草的尺度，明确草落在泥地上。 |
| 03｜湿栏与手 | 叶形相接，画面已换为湿木栏；另一茎折草搁在栏上。陈平安的手与袖口在画右搭住栏沿，与草保持距离。脚步在画外渐停。 | [L387](../script_chapter2.rpy#L387)「雨已经停了，檐角还在滴水。」<br>[L389](../script_chapter2.rpy#L389)「陈平安沿着廊下慢慢走，一只手轻轻搭在栏杆上。」 | 02→03直接形状匹配切；泥纹变为木纹，檐滴、轻脚步和江声明确回到现实夜廊。手不碰草，不用草叶变形动画。 | **缺独立成图。** 以已完成镜04的栏杆透视、草叶形状、手与袖口位置为连续性依据。旧四格中草根似穿木的问题须修正，不能直接采用。 |
| 04｜扶栏看草 | 切到已完成彩图：陈在画右轻扶湿栏，低头看折草；远岸灯火与江面留在左侧。停在这个凝视结果上，承载随后忆述。 | [L390](../script_chapter2.rpy#L390)「走到灯下，一滴檐水落在他手边。他低头看了一眼。」<br>[L391](../script_chapter2.rpy#L391)「他想起在青鸾国酒楼里听来的一个故事。」<br>[L393](../script_chapter2.rpy#L393)「撑伞的人在雨里，躲雨的人在檐下。」<br>[L394](../script_chapter2.rpy#L394)「也想起陆抬说过的“留不住”，于是心里只剩一句话：且慢行——慢一点，才看得见人间的苦。」 | 03→04保持草左、手右、栏向与光向，切宽见人；以近处一声檐滴接低头的结果画面。青鸾故事由旁白回忆，画面留在夜廊凝视，不切回停用的旧雨街。第394行句末留一拍，作为切入段出口。 | **单张彩图已完成并采用。** 原图与项目图均保留。低头、檐滴落下、拉镜、水面动态均未制作；本图不能单独证明这些动作已完成。 |

**接出边界。** 下一段从 [L398](../script_chapter2.rpy#L398)「又记得陆抬曾经在飞鹰堡小院感慨，人间的遗憾，多是“留不住”三字。」开始，接第399–401行“且慢行／感同身受／措手不及”。保持旁白“陆抬·回忆”归属；是否切飞鹰堡小院、用哪些画面，另做下一段分镜。本表不自动采用旧镜07，也不把陆抬安排到当下夜廊。

**台词与画面核对。** 旧雨街画面停用不等于删去第391、393、394行正文；这些句子在新镜04的当下凝视画面上读完。第390行的“手边檐滴”与彩图中的“叶尖挂滴”是两处水：游戏静态呈现可用旁白和落水声承接结果图；短片若要实际拍出落滴或低头，需要另列局部动作制作，不能把叶尖挂滴当作已完成落滴。

**节奏与制作顺序。** 原25–30秒来自静默构图草案，不能直接套在加入全部现稿台词的版本。游戏按页阅读与停留，短片待配音后核定时长。当前缺镜01、02、03三张独立图，镜04不重画。此表确认后，建议先做与镜04直接相接的镜03，再完成镜01、02，最后验证四镜衔接；完整短片、章末CG和成就另行制作。

</details>

## 2026-10-30 当前执行与制作边界

- 当前487条对白／旁白／心声，按19个场头注释分段；保留2处显式自动存档、2处可点击无字停留、3句裴朱专用头像对白。19段是当前脚本的时间和空间定位，不等于已经完成19套分镜或19组美术。
- 当前引用37张背景／CG与4张独立立绘，共41个不同场景资源；另有两张专用头像。既有素材、稳定代号和A2／B2界面保留，挽臂CG及停用的裴朱场景人物层不重新启用。
- 当前278条正文处于黑场（此前280条，雨停看掌两句已有图），包含转场与待补图段落。此数不代表需要278张图片；收针后的溪边、宴前廊下、席间、雨夜、气府、灯下与离府仍需按下表补齐或复用稳定画面。
- 原T001–T226、V编号、11场／56单元及旧行号仅存在于下方历史折叠区，不作为当前正文编号。新稿不沿用旧T号逐项补图，不按旧“宴后双人夜谈”“现场善恶问答”制作。
- [第二章全章分镜工作簿](F:/图片素材/第二章全章分镜.xlsx)及10月12日并排阅读版仍是历史快照，本轮未回写。当前制作以本页和脚本为准；正式补图前再细化当前段落分镜。

## 当前段落定位与画面边界

| 当前段落（按脚本顺序） | 脚本入口 | 已有呈现 | 具体待补／归属边界 |
|---|---|---|---|
| 返乡途中·溪边 | [溪边开场](../script_chapter2.rpy#L5) · [收拾行装](../script_chapter2.rpy#L48) | 2026-11-01 核对：开场和坐谈沿用挑疱图。裴钱说完“往师父兜里装”后，切到收拾行装定稿 `c2_01_pack_v1`，只覆盖启程旁白，下一页入郡城。 | 坐谈图仍待采用；访友与宁姑娘计划是陈平安心声。[启程镜制作记录](../../work/art/chapter2/c2_creek_pack/record.json) |
| 黄庭国·御江畔郡城 | [L114](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:114) | 入城、观察、远处来人三图 | 剑修冲突是旧事与假设，未发生当场战斗；长段街面旧事的稳态仍需复核，不能把文字改动算作已补差分。 |
| 郡城·客栈门前 | [L178](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:178) | 邀请、思量、应允三图 | 陈平安因旧交情面答应短住；不能补成拒绝会导致吴懿受罚。 |
| 郡城江畔·登船 | [L229](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:229) | 首镜为华光楼码头朝西无人空镜，随后抛舟、化船、落符、搭板、升空 | 2026-11-01 确认首镜用左江右铺的新图，下一镜沿用左铺右江的四人抛舟图。先移开行人再变船，裴钱想买宝贝由旁白交代。 |
| 楼船·御江上空 | [L282](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:282) | 船上俯江CG | 故乡与楚夫人是联想和未来计划，不切成已经到达的场景。 |
| 紫阳府外·铁券河畔 | [L319](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:319) | 下船、拜谢、退场后交谈、引路四图 | 收舟、少女化符、符纸入河的因果已补文字，尚无专用动作差分；不把旧下船图记为已展示收舟结果。 |
| 沿河入府 | [L373](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:373) | 吴陈交谈、吴懿闭口近景、沿河引路 | 于禄龙气仅为吴懿心声，陈平安未获知；后续恢复现场对白。 |
| 紫阳府·府门 | [L420](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:420) | 府门迎接CG | 欢呼由众人发出；吴懿邀并肩是传音，陈平安的答话为现场对白。未实现完整人群跪起或前后换位动画。 |
| 暮色·客楼 | [L455](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:455) | 客楼、规矩、陈设、放箱、临窗五图，出廊后切黑 | 放箱的无字停留后接站稳画面；裴钱留在楼内看陈设，不进入陈朱廊下长谈。 |
| 宴前·四楼廊下 | [L509](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:509) | 黑场文字 | 需四楼临河廊下的暮色双人稳定画面；陈用养剑葫、朱用酒壶。不可复用室内含裴钱的图冒充廊下，不再制作旧稿的宴后雨夜双人长谈。 |
| 入夜·紫气宫长廊 | [L622](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:622) | 赴宴、询认、蜈蚣岭插镜、相认、拍肩、收手及陈孙独立立绘 | 旧事插镜由当下陈平安讲述；“小孙，边走边聊”归同行老者，之后催席才归紫阳府管事，二者均可在画外发声。 |
| 夜·雪茫堂 | [L758](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:758) | 黑场、迎客CG、堂口背景及裴朱专用头像；入席后切黑 | 挽臂由旁白承接，停用CG不复用。宾客席面、萧鸾三坛罚酒与再敬一坛、陈平安以坛回敬、孙登先杯饮均待正式分镜；堂口图不能冒充落座席面。 |
| 夜·返回客楼 | [L994](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:994) | 黑场文字 | 需散席返楼、雨中行路及独处读书的时间和空间承接；同行者各自回房后，廊下只有陈平安。当前雨声等仍由文字交代，未新增音频。 |
| 深夜·四楼廊下 | [L1031](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1031) | CG02·14·01覆盖[L1044](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1044)摊掌低看及其后河山句；其余仍黑场 | 用户仅批准看掌段接入，跃上栏杆前[L1049](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1049)退黑；栏杆行走与后续思索画面仍待补。雨已停，只留积水；崔东山并非现场出场。 |
| 返乡路上的旧日问答 | [L1130](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1130) | 黑场，具名陈朱回忆对白 | 这是过去路上的问答；不能把朱敛摆在当前夜廊。可在待补沉思底图上用明确回忆归属承接，不强制新增杀人情境或整场闪回。 |
| 当下·四楼廊下 | [L1152](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1152) | 黑场，陈平安心声与气府内心语分开 | 需陈在外部廊下、气府小人在体内的可辨状态；宁姑娘未在现场。小人急而不能明说的缘由、骂后笑及金光仍有所得均保留。 |
| 深夜·房内 | [L1238](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1238) | 黑场文字 | 需灯下读书稳态；陈重新翻开之前合上的书，油灯承接“不敢多想的一个人”。不提前画出顾璨已犯的事或替悬念定答案。 |
| 翌晨·辞别紫阳府 | [L1275](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1275) | 黑场文字 | 需清晨离府或返乡路结果图；保持三人、陈的竹箱、裴的行山杖连续。 |
| 同日·紫阳府 | [L1286](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1286) | 黑场文字，随后跳第三章 | 吴懿在客人离开后传讯；信息只给玩家。传讯媒介未定，不擅画具体法器或父亲接讯CG。 |

<a id="c2-scenes-09-10"></a>

## 第09、10场逐镜表

2026-11-06范围补充：用户确认已完成的夜廊切入止于第390行“他低头看了一眼”；第391行及镜05–06路边躲雨为下一制作段落。下列镜04同时列有第391行，不代表该句也已完成；本轮范围与素材状态以[最新表格](#c2-slow-attention-intro-table)为准。镜06细分动作和第394行接小院仍属分镜建议。

第09场「且慢行与善恶之问」分九组，镜01至镜51。第10场「宴后临窗夜谈」分一组，镜01至镜06。以下为分镜设计，画面、运镜和声音按设计列出。剧本中两场目前以黑场文字呈现。[雨停廊下](../script_chapter2.rpy#L387) · [路上问答的三个选项](../script_chapter2.rpy#L470) · [临窗入夜](../script_chapter2.rpy#L526) · [朱敛最后一问](../script_chapter2.rpy#L541)

### 第09场·第01组　紫阳府高楼檐下·扶栏缓行

紫阳府高楼，夜雨初停。近处是檐柱，远处是廊道尽头。楼外紧贴湖面。陈平安脚踩廊板，一只手搭着木栏，沿廊走一个来回。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜01 | **檐下空景。** 机位定住。檐角一滴水落过湿栏，栏外河面只透出两三点灯光。 | 先听檐水滴落和远处市声。廊内尚且无人，旁白起「雨已经停了，檐角还在滴水。」 |
| 第09场·镜02 | **人从柱后入画。** 陈平安从画左的柱后走来，草鞋踏着廊板，一只手轻轻搭上栏杆。镜头留在中远景，画右留出他要走的路。 | 旁白「陈平安沿着廊下慢慢走，一只手轻轻搭在栏杆上。」鞋底擦过廊板的声音很轻。 |
| 第09场·镜03 | **沿廊横移。** 镜头随他往右走一段，搭在栏上的手掠过一线水光。下一根柱子短暂遮住他的衣摆，柱外露出远岸灯影。 | 留一段没有旁白的路。柱后脚步仍接得上，间或听见檐滴。 |
| 第09场·镜04 | **灯下低头。** 机位定住。陈平安走到廊道尽头折返。经过灯下时，一滴檐水落在他手边的湿栏上。他低头。镜头落到指尖旁的水纹，栏外近处只有湖面。画面在这里停一拍。 | 旁白「走到灯下，一滴檐水落在他手边。他低头看了一眼。」「他想起在青鸾国酒楼里听来的一个故事。」第二句旁白在手边与湖面的画面上说完。“故事”落音，檐滴才接到青鸾国的伞沿。 |

镜04以[想起酒楼故事](../script_chapter2.rpy#L391)收住。镜05、06共用[撑伞与躲雨一句](../script_chapter2.rpy#L393)。[忆及陆抬的下一句](../script_chapter2.rpy#L394)从镜06跨到镜07，以“留不住”三字入小院。

**现实夜廊的画面参照。** 《春江水暖》用在镜01、03，先给空间时间，再让视线沿栏从近物移到远处。侯孝贤的固定长镜用在镜04，柱子先后两次遮住人，观众凭它认出他走回了原处。《鹿铃》的留白留给雨后的水汽与河面，远岸屋脊只显一截，近处湿木的边沿才落实笔。《剑来》的墨色变化落在同一件衣衫上，檐灯在深色柱影里留一豆暖光，他从灯前经过时衣褶稍清，走到廊端时衣摆渐淡在水汽里，折返后才重新清楚。

**镜01线稿记录（2026-11-02）。** [单张线稿原图](C:/Users/MSI/.codex/generated_images/01a1975a-1fa1-7d01-b992-4ed5dc477864/exec-55ab0add-6550-4ef8-b638-394ab63664f3.png)保留1672×941。已取回初稿笔触修整湿木扶手、横枋、柱脚倒影和远岸。扶手收进右端望柱，栏柱间距向右递减，檐下仍为无人空景。右端柱脚已补一笔短接触影，落点可辨，线稿待确认。书页依据及实际写入核验见[单图制作记录](../../work/art/chapter2/c2_09_01_empty/record.json)。

[镜04→05双格线稿](C:/Users/MSI/.codex/generated_images/01a1975a-1fa1-7d01-b992-4ed5dc477864/exec-bd440d80-231a-4b30-ae22-46346aeea503.png)上格里陈平安双脚踩在廊板上。上格收尾的小格取他手边的湿栏和栏外湖面，旁白在这里说完「他想起在青鸾国酒楼里听来的一个故事。」下格才俯看故事里的雨街。上格线稿待确认。[镜04单镜原画](C:/Users/MSI/.codex/generated_images/01a1975a-1fa1-7d01-b992-4ed5dc477864/exec-9a4a7c28-c3c8-40dd-8108-70867760168f.png)

### 第09场·第02组　酒楼听来的故事与飞鹰堡小院的旧话

空间/时间：回忆线，旧黄/水墨。

两拍都从陈平安的记忆展开。先见他在青鸾国酒楼听来的故事，再见他记得的陆抬。

**A拍　青鸾国酒楼·撑伞与檐下**

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜05 | **伞过，人躲雨。** 切入青鸾国酒楼里听来的故事，用街口的高机位俯看伞群。近伞的伞沿正落下一滴水，接着檐滴的位置和下落方向。机位定住。近处的路人一手持伞，一手提布包，朝画左走过。伞沿一点点让开，才看清后面抬袖遮头的人。他斜赶几步，前脚跨进画右的酒楼檐下。对街一把淡淡的小伞仍在往前走。 | 零落的檐滴声接成雨打伞面的细响。旁白接「撑伞的人在雨里，」。伞继续往街上走，几声急促的湿脚步靠近门口。 |
| 第09场·镜06 | **后脚收进檐下。** 低机位接同一个无伞路人：前脚已踩在干处，后脚从湿石板上提起，越过滴水线，落在前脚旁。他站定。檐水仍落在刚才鞋尖所在的地方。 | 后脚落地，湿脚步声停。旁白续「躲雨的人在檐下。」在这双停住的脚上起下一句「也想起陆抬说过的」。 |

动作参照：[英一蝶《雨宿り图屏风》](https://webarchives.tnm.jp/imgsearch/show/C0072048)看持伞者与掩头奔向屋檐者的身势；[《罗生门》开场镜5–8](https://thesuccessfulscreenwriter.com/wp-content/uploads/Rashomon-Continuity-Script.pdf)看路人涉水、上阶、在檐下收步回望的先后。《莎木》商店转角的伞客分在街角前后，近处行人手里的提篮让步子有了分量。《言叶之庭》漫画第一话以近伞遮住一角，对街的伞只留一小笔。镜05取这两层距离，露人的时机交给走过去的伞。[《莎木》街角截图](https://medium.com/@MoosaviAmir/what-s-shenmue-6145a484bbf1) · [《言叶之庭》漫画第一话](https://pocket.shonenmagazine.com/title/01951/episode/360947)

镜05B–05C同窗线稿（2026-11-04 原位修订，待修正）。本轮仅简化墙板、瓦面与窗槛细纹，补下格前脚外侧接触影；人物位置、双格构图和原窗框保留。窗框试改的接缝不合格，已撤回；干湿边界和水面碎反光尚未处理。两格沿用青鸾国酒楼二楼窗位，从路人露出全身接到跨入对街铺檐，以右侧檐柱和两只酒瓮定位。窗槛参马炳坚《中国古建筑木作营造技术》印页264图7-1，铺基、石板街和廊棚参《江南 水乡古镇》印页22及西塘章开篇。取构件关系，透视按本场模型试排。[双格线稿](C:/Users/MSI/.codex/generated_images/01a1975a-1fa1-7d01-b992-4ed5dc477864/exec-87ff2e72-f90c-4ebf-82cb-e71c93114276.png) · [三维窗位](../../work/art/chapter2/c2_09_rain_street_3d.html)

镜05B／05C 两张独立路人效果图（2026-11-04，待修正）：本轮修正05B左侧新增路人的比例，并补回05C的原前景伞客及左缘伞，保持窗槛遮挡和主动作可见。两名新增路人的衣装、手部和包袱差异仍未完成，已授权的 Firefly 局部填补被 Adobe 正版应用验证阻断，未生成结果。两张既有效果 PNG 已经 Photoshop 正常保存并回读核验，修订区外像素不变；原双格源图保留。仅供位置与连续性审阅，未接入游戏。[镜05B](C:/Users/MSI/.codex/visualizations/2026/11/01/01a1975a-1fa1-7d01-b992-4ed5dc477864/c2_09_05b_people_effect.png) · [镜05C](C:/Users/MSI/.codex/visualizations/2026/11/01/01a1975a-1fa1-7d01-b992-4ed5dc477864/c2_09_05c_people_effect.png) · [保存与核验记录](character_image_index.md#343-第二章第09场镜04--雨停扶栏2026-11-02)

**B拍　飞鹰堡小院·留不住**

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜07 | **“留不住”入小院。** 旁白念到“留不住”时，切到飞鹰堡小院。石桌旁是陆抬的侧影。镜头停在这里，让陈平安把念头想完。 | 旁白接「“留不住”，于是心里只剩一句话：且慢行——慢一点，才看得见人间的苦。」其中“留不住”是陆抬的旧话，“慢一点，才看得见人间的苦”是陈平安此刻的领会。随后旁白以“陆抬·回忆”忆述：「又记得陆抬曾经在飞鹰堡小院感慨，人间的遗憾，多是“留不住”三字。」「最深的肺腑之言，不过是对种种风景、种种人的一句“且慢行”。」 |
| 第09场·镜08 | 石桌上还剩半杯茶。一片落叶被风带出画面，镜头缓缓推向空处。 | 旁白仍以“陆抬·回忆”忆述：「陆抬又说，我们很难对世间诸多苦难，真正感同身受。」「所以当苦难临头，落在一个人的身上时，谁都会措手不及。」 |
| 第09场·镜09 | **回到夜廊。** 小院的旧色切回廊下的青灰。陈平安已经走过灯边，仍在廊板上沿栏朝左走。 | 小院最后一句说完，檐滴之间又听见鞋底轻擦廊板，接镜10。 |

要体现：不是只做“撑伞/躲雨”，必须补足飞鹰堡“留不住、且慢行、感同身受难、措手不及”。

### 第09场·第03组　观道观与光阴长河·尺度对照

空间/时间：抽象哲理段，回忆/意象混合。

功能：建立“可掌控一条光阴长河”与“四座天下洪流连道祖都拦不住”的尺度对照；抛出三教圣人为何要“慢”的设问。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜10 | 观道观全景：老道人立于观中，俯瞰藕花福地众生百态。福地如微缩盆景，人间烟火在其中流转。 | 旁白：“那座观道观的观主老道人，以藕花福地的众生百态观道。” |
| 第09场·镜11 | 意象镜头：一条细小光阴长河在福地中可快、可慢、可停滞；落叶悬停，雨滴倒回，行人定格。 | 旁白：“道法通天的无名老道人，显然可以掌控一座藕花福地的那条光阴长河，可快可慢，可停滞不前。” |
| 第09场·镜12 | 镜头猛拉开：四座天下的光阴洪流横贯画面，巨浪滔天；一只象征道祖的手或拂尘试图一拦，洪流仍不可阻挡。 | 旁白：“可是四座天下的光阴洪流，别说掌控，就是想要拦上一拦，据说连道祖都做不到。” |
| 第09场·镜13 | 水边空镜：逝水不舍昼夜。 | 旁白：“故而至圣先师曾经观水有悟：‘逝者如斯夫，不舍昼夜。’” |
| 第09场·镜14 | 回到廊下，陈平安仍沿栏慢慢走，心声起。 | 陈平安心声：“已经站得那么高、看得那么远的三教圣人，到底为何非要慢下来？至圣先师，佛祖，道祖，这三位有开天辟地之功的圣人，又到底在看什么？以至于一定要三座天下人间‘且慢行’。” |

要体现：尺度对照要清楚；设问要留悬念，不提前回答。

### 第09场·第04组　崔东山·历史车轮与稀烂花草

空间/时间：回忆线，黄庭国山巅。

功能：用强意象呈现“悲悯之言”，为陈平安的推理闭环蓄势。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜15 | 山巅，少年陈平安练拳，崔东山在旁笑言。镜头以拳风带起尘土。 | 旁白：“第一次与崔东山游历黄庭国，一次在山巅，崔东山陪着他一起练拳，曾经笑言——” |
| 第09场·镜16 | 意象切入：巨大历史车轮前行，碾过花草；花草稀烂特写，不血腥，但具体。 | 崔东山回忆：“历史的车轮前行之时，必然要碾碎许多花草。” |
| 第09场·镜17 | 车轮上方的马车阴影，车窗里隐约可见大人物轮廓；镜头仰拍，压迫感。 | 崔东山回忆：“这不是帝王心性的无情之语，而是一位中土醇儒的悲悯之言。” |
| 第09场·镜18 | 关键镜头：马车上的大人物低头看一眼车下稀烂花草。只给一个低头动作，不露全脸。 | 崔东山回忆：“那个读书人，希望所有看到这句话的掌权者，或是当时就坐在那辆马车上的大人物，能够低头看一眼那些稀烂的花草。” |
| 第09场·镜19 | 回到廊下，陈平安脚步稍顿，心声进入推理。 | 陈平安心声：“世道慢慢变好，需要担心吗？只要是变好，方向是对的，再慢都无所谓，当然不需要担心。” |

要体现：重点不是“无情”，是“低头看一眼”的悲悯；车轮与花草要成为后续“慢”的理由。

### 第09场·第05组　陈平安的思辨闭环与心田种子

空间/时间：现实夜廊 + 心田蒙太奇。

功能：补全陈平安自己的推理；把“念头是种子”泛化为世人皆然；明确他本人不知道，只当散步散心。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜20 | 陈平安继续在廊下缓行，心声继续。 | 陈平安心声：“若是世道在变得糟糕，比如历史车轮，以迅猛势头一碾而过，一路碾碎无数花草，哪怕有人想要低头去看一眼，也未必看得清楚。又何谈弥补？所以才要慢上一些？” |
| 第09场·镜21 | 关键落点：慢速镜头下，车轮偏入错误大道，又出现可修改的岔口；花草被避开一小片。 | 陈平安心声：“因为若是慢慢而行，哪怕是岔入了一条错误的大道，慢慢而错，是不是就意味着有了修改的机会？又或者，人间苦难可以少一些？” |
| 第09场·镜22 | 种子蒙太奇开始：心田土壤中，一粒粒念头种子抽芽；有的半路夭折，有的开花结果。 | 旁白：“陈平安并不知道，在一个人自己都浑然不觉的内心深处，每一个深刻的念头，就像心田里的种子。会抽芽，可能许多会半路夭折，可有些会在某天开花结果。” |
| 第09场·镜23 | 竹简特写：刻刀刻字；大太阳下裴钱晒竹简。 | 旁白：“那些以刻刀用心刻在竹简上的文字，那些被他反复咀嚼和念叨，甚至会在大太阳的天气里让裴钱去晒一晒的竹简文字……都是在他心田撒下的种子。” |
| 第09场·镜24 | 泛化群像蒙太奇：爹娘牢骚、夫子教诲、翻回再看的书上语句、听了很多遍蓦然开窍的老话、青山绿水、错过的心仪女子、走散的朋友。不具体指向宁姚。 | 旁白：“陈平安并不是孤例，事实上，世人一样会如此……皆是所有人心田里的一粒粒种子，等待着开花。” |
| 第09场·镜25 | 回到陈平安：他仍只是缓行，神情平常。 | 旁白：“陈平安哪里知道这些。他只当自己是在廊下散步散心。” |

要体现：推理闭环必须完整；种子蒙太奇是“世人皆然”，不是陈平安专属；不提前消费宁姚。

### 第09场·第06组　气府内景·金光不稳固的期待

空间/时间：人身小天地，气府内景。

功能：微观化“机缘将成未成”；建立金色小人的期待与陈平安仍缓行的悬念。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜26 | 水府内，绿衣小童们停下手中忙碌，一个个屏气凝神。 | 旁白：“人身小天地之中，拥有水字印的那座水府当中，绿衣小童们都停下了手头忙碌的事情，一个个屏气凝神。” |
| 第09场·镜27 | 金色文胆府邸外，真气火龙盘踞酣睡；镜头低机位，压迫又安静。 | 旁白：“而拥有金色文胆的那座府邸，外边盘踞着那条酣睡的真气火龙。” |
| 第09场·镜28 | 府邸内，金色儒衫小人负长剑、腰挂几本金色小书，金光凝练，熠熠生辉，如神祇塑金身。 | 旁白：“府邸里边，背负长剑、腰挂几本金色小书本的金色儒衫小人儿，一身金光越发凝练，熠熠生辉，如一尊神祇塑金身。” |
| 第09场·镜29 | 特写：金光虽亮，却有星星点点金色光彩流溢飘散，显然不稳固。 | 旁白：“只是从那个全身金光流淌的儒衫小人儿身上，不断有星星点点的金色光彩流溢飘散出去，显然并不稳固。” |
| 第09场·镜30 | 金色小人望向府门，充满期待，等陈平安停步；切回现实，陈平安仍在缓缓而行。 | 旁白：“他等着陈平安停下脚步，心里满是期待。可陈平安还在廊下慢慢走。” |

要体现：金光“凝练但不稳固”；期待越强，后面被“想姑娘”打断越好笑。

### 第09场·第07组　返乡路上·杀一人救更多人的问答

空间/时间：返乡路上，离开山崖书院后的回忆线。

功能：用道德难题呈现陈平安“给不了答案”的诚实；三分支为同场互动变体。线性版默认“我答不出”。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜31 | 返乡路上，陈平安、朱敛、石柔同行。陈平安开口问。 | 陈平安回忆：“如果杀一个无错的好人，可以救十人，救不救。” |
| 第09场·镜32 | 朱敛和石柔摇头。镜头给两人不同反应：朱敛沉稳，石柔先迟疑。 | 旁白：“两人摇头。” |
| 第09场·镜33 | 陈平安追问。 | 陈平安回忆：“那救千人呢？救万人呢？” |
| 第09场·镜34 | 石柔开始犹豫；特写她手指收紧或眼神游移。 | 旁白：“石柔开始犹豫了。” |
| 第09场·镜35 | 朱敛回答，镜头稳在他脸上。 | 朱敛回忆：“哪怕可以救整个天下人，我也不杀那个人。”<br>陈平安回忆：“为何？”<br>朱敛回忆：“我担心自己就是那个被杀的人。少爷，你呢。” |
| 第09场·镜36 | 互动分支处理：同一构图，只做微表情、停顿、口型差异；不改变后续镜头。 | — |

**第09场·镜36的三个选项**

| 分支 | 分镜处理 | 旁白/台词 |
| --- | --- | --- |
| 杀一个，救更多人 | 陈平安嘴唇微动，话到嘴边停住；镜头切他垂下眼。 | 陈平安回忆：“……”旁白：“话到嘴边，陈平安没有说出口。这个答案太轻了。” |
| 不杀 | 陈平安直视前方，说出后自己先沉默半拍。 | 陈平安回忆：“不杀。”旁白：“可这答案也未必经得起真正的处境。” |
| 我答不出（线性默认） | 陈平安沉默，镜头停在他被风吹动的衣袖上，直接接第09场·镜37。 | 无对白，保留呼吸声。 |

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜37 | 三分支统一接回：陈平安给出最终回答。 | 陈平安回忆：“我也给不了答案，或许只有真正走到那一步，我才可能知道我的本性和选择。” |
| 第09场·镜38 | 镜头拉远，三人继续前行；画面化回现实气府线。 | 转场：金色小人的焦急心声先入。 |

要体现：两人摇头、石柔犹豫的节奏不能省；分支只是互动变体，线性版仍为10组。

### 第09场·第08组　气府小人急跳脚·陈平安停步却想宁姚

空间/时间：气府内景 + 现实夜廊，交叉剪辑。

功能：全段反差喜剧高潮。分两拍：先“急”，再“停步揭示”。

**第一拍：气府内急**

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜39 | 气府内，金色儒衫小人急得几次想冲出府门；绿衣小童屏息看着。 | 旁白：“气府内，金色儒衫小人儿急得几次想冲出府门。” |
| 第09场·镜40 | 快切：金色小人跳脚，心声连发。 | 金色小人内心：“真想给那个陈平安几个大栗暴！你想岔了，想这些暂时注定没有结果的天大难题做什么？莫要不务正业，莫要与一桩千载难逢的机缘擦肩而过！” |
| 第09场·镜41 | 金光闪烁，金色小人指向“慢”字意象。 | 金色小人内心：“你先前所思所想的大方向，才是对的！快快将那个至关重要的‘慢’字，那个被世俗天地无比忽略的字眼，再想得更远一些，更深一些！只要想通透了，这就是你陈平安未来跻身上五境的大道契机！” |
| 第09场·镜42 | 旁白补叙事节制：这些内幕若直白告诉陈平安，反而会让他心境糟糕。画面给金色小人欲言又止。 | 旁白：“只是这些内幕，它若是直白告诉了陈平安，反而会让陈平安陷入一种无比糟糕的心境。” |

**第二拍：陈平安停步，绿衣小童哄笑，揭示想姑娘**

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜43 | 现实线：陈平安终于在栏边停下脚步。气府两座府邸的金色小人和绿衣童子都充满期待。 | 旁白：“陈平安终于在栏边停下脚步。两座府邸的金色儒衫小人和绿衣童子们，都充满了期待。” |
| 第09场·镜44 | 静一拍。然后绿衣小童们面面相觑，突然哄然大笑，满地打滚。 | 旁白：“然后绿衣童子们面面相觑，突然间哄然大笑起来。” |
| 第09场·镜45 | 陈平安心声揭示：他想念一个姑娘；下次剑气长城重逢，不能只是牵牵手，要胆子更大些。画面用少年脸红、手指蜷缩、栏杆雨滴等含蓄表现，不直给低俗画面。 | 陈平安心声：“原来陈平安站定之后，那一刻的纯粹心念，竟是开始想念一个姑娘了。而且想法特别不那么正人君子，竟是想着下次在剑气长城与她重逢，可不能只是牵牵手了，要胆子更大些。” |
| 第09场·镜46 | 继续心声：宁姑娘不愿意大不了被打一顿骂几句；万一她其实愿意，等他主动呢？大老爷们没气魄像话吗。 | 陈平安心声：“若是宁姑娘不愿意，大不了就是给打一顿骂几句，相信两人还是会在一起的。可如果万一宁姑娘其实是愿意的，等着他陈平安主动呢？你是个大老爷们啊，没点气魄，扭扭捏捏，像话吗？” |

要体现：先急后停，两拍不能压成一拍；喜剧来自“大道契机”被“想姑娘”打断，但表达要少年慌乱、含蓄。

### 第09场·第09组　转身回房·自我鼓气与气府收笑点

空间/时间：现实夜廊，接屋内。

功能：轻喜剧过渡；体现陈平安烟火气，不是高高在上的悟道者。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第09场·镜47 | 陈平安有了睡意，松开搭在栏上的手，转身沿廊走向房门。 | 旁白：“陈平安有些困了，便转身往房里走。他边走边用拳头轻击手掌，给自己鼓气。” |
| 第09场·镜48 | 以拳击掌特写，边走边自言自语。 | 陈平安：“不像话，肯定不像话！”<br>陈平安：“再说了，倒悬山那边，你又不是没抱过宁姑娘，只是那次光顾着发蒙了，啥个滋味都记不住，这怎么行？” |
| 第09场·镜49 | 他忽然停一下，自己把自己吓到。 | 陈平安：“亲个小嘴儿……陈平安找死啊，你？” |
| 第09场·镜50 | 继续走，强行拉回“慢”。 | 陈平安：“不能想这个，这个有些快了。你不刚想了那么多慢吗？与宁姑娘还是要慢些，文火慢炖，也是好的……”<br>陈平安：“好个屁的好……” |
| 第09场·镜51 | 气府内金色小人崩溃一句；绿衣小童捧腹大笑，满地打滚。 | 金色小人内心：“陈平安你大爷啊！”<br>旁白：“绿衣小童们一个个捧腹大笑，满地打滚。” |

要体现：节奏轻快；台词保留原文的自我拆台感；“慢”与“快”形成少年式反差。

### 第10场·第01组　宴后临河高楼·雨夜灯影与朱敛一问

空间/时间：宴散后，临河高楼，夜雨。

功能：收束留白；从玄妙大道落回人间生活；朱敛一问不补答。

| 镜号 | 画面与动作 | 旁白、台词与声音 |
| --- | --- | --- |
| 第10场·镜01 | 转场：宴散，回到临河高楼。裴钱已经睡下，窗外落着小雨。 | 旁白：“宴散，回到临河高楼。裴钱已经睡下，窗外落着小雨。” |
| 第10场·镜02 | 陈平安临窗坐着，望着河面散开的灯影；雨痕在窗上缓慢滑落。 | 旁白：“陈平安临窗坐着，望着河面散开的灯影。” |
| 第10场·镜03 | 朱敛入画。 | 朱敛：“少爷，还不歇着？”<br>陈平安：“还不困。坐会儿？” |
| 第10场·镜04 | 朱敛坐下；陈平安给他斟了杯酒，又望向窗外。酒杯轻响，雨声清楚。 | 旁白：“朱敛坐下。陈平安给他斟了杯酒，又望向窗外。” |
| 第10场·镜05 | 陈平安提崔东山旧事。 | 陈平安：“看着这条河，忽然想起崔东山说过的一件事。他说三教圣人都在试着各用各的办法，让那条注定势不可当的光阴长河，流得慢上一些。”<br>朱敛：“怎么个减慢？”<br>陈平安：“仙家山头是一物，人间城池是一物。战争，又是一物。能够让人心神沉浸其中的百家学问，好像也是。”<br>朱敛：“崔东山说得神神道道，老奴算是更迷糊了。”<br>陈平安：“我一样不懂。” |
| 第10场·镜06 | 朱敛问出最后一问；镜头不切陈平安正脸回答，而是停在被雨打散的河面灯影、酒杯边缘、陈平安侧脸眼神。 | 朱敛：“那么少爷想要懂得这些玄之又玄的大道吗？”<br>不收答。 画面停在雨、灯、酒、眼神上，淡出。 |

要体现：裴钱睡下、小雨灯影的生活质感；朱敛一问后留白；陈平安更在意人间具体的人与事，答案不急着说。

### 线性版与互动版

互动版在第09场·镜36呈现三个选项，三条分支统一接第09场·镜37。

线性版默认“我答不出”。第09场·第07组依次走镜31 → 32 → 33 → 34 → 35 → 37 → 38。

两版都保留10个镜组。全表共57个镜号，线性版跳过互动镜，走56镜。

### 雨停看掌之后的旧分镜记录

**画面分界（2026-11-01）。** 以陈平安独自默念的“且慢行。”（[剧本 L1066](../script_chapter2.rpy#L1066)）为界。第二章此后的场景图片与此前的场景图完全不同，须独立设计。具体采用怎样的画面形式仍待确定。

**当时未采用。** 2026-11-01，用户放弃本轮“陈平安回望四镜”。酒楼、飞鹰堡、山巅和夜廊折返的四镜方案、提示词及全部线稿一并停用。

停用稿存档 · [青鸾国酒楼听旧事](../../work/art/chapter2/c2_chen_memory_pov/01_qingluan_winehouse.png) · [飞鹰堡听陆抬说话](../../work/art/chapter2/c2_chen_memory_pov/02_feiying_lutai.png) · [黄庭国山巅低头](../../work/art/chapter2/c2_chen_memory_pov/03_huangting_summit.png) · [夜廊折返](../../work/art/chapter2/c2_chen_memory_pov/04_tiequan_return.png)

2026-11-01，用户停用10月31日晚制作的整套方案。从跃上栏杆到回房停翻书页（L1051–1272），旧18镜、四张线稿板和第03镜走马灯改稿一并归档。

<details>
<summary>2026-10-31 停用稿 · 镜头、线稿与制作记录</summary>

本版从 L1051 跃上栏杆起，到 L1272 书页停住为止，四段共18镜、81句。表中引号为原句或原句节选；行号指向现行剧本。每镜自所列首句起，保持到末句读完，镜内的姿态和光线变化随已有正文页推进。

**前镜伏笔（不计入18镜）。** 宴前 L515–523，陈、朱凭栏望铁券河。陈转述崔东山说要让“那条光阴长河，流得慢上一些”时，水面仍是寻常灯影。选靠近栏端的一根廊柱作位置标记，让观众认得灯影在柱影旁随水拖长的形状。深夜 L1044、1046 用已定稿的掌水图交代雨珠、夜河与青山；下一镜才把重心从掌心移到脚下。[宴前对白](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:515) · [雨停看掌定稿](../images/chapter2/c2_14_rain_after_v1.png)

这段光阴长河以陈平安亲历的往事呈现。铁券河的灯影引出溪水，溪边只看一眼，到了黄庭国山巅，留足崔东山说完旧话。陈平安在记忆里侧首，眼前重新见到今夜的廊灯。

**四段线稿（2026-10-31，停用）**　[01–06 栏上慢行与折返](../../work/art/chapter2/c2_slow_walk_boards/01_rail_01_06.png) · [07 山路旧问](../../work/art/chapter2/c2_slow_walk_boards/02_old_question_07.png) · [08–15 夜廊与气府](../../work/art/chapter2/c2_slow_walk_boards/03_corridor_08_15.png) · [16–18 灯下重读](../../work/art/chapter2/c2_slow_walk_boards/04_lamp_16_18.png)

第03镜在原线稿板内改成三格第一人称走马灯，依次为溪边、山巅、回望廊灯。第04镜在 L1089 同一句旁白内交代到栏端与转身后两格。旧稿共21格、18镜，均已停用，未接入游戏。[线稿核对及绘制提示词](../../work/art/chapter2/c2_slow_walk_boards/line_art_record.json)

#### 1　栏上慢行与折返（28句）

| 镜号 | 对应剧情 | 画面与切点 |
|---|---|---|
| 01 · 踏上栏顶 | [L1051–1063](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1051)　“陈平安跃上栏杆，慢慢走向另一头。”至“又总是措手不及。” | 廊内斜侧全身。取跃上之后脚已踏实的一步，栏顶在草鞋下，廊板在更低处，两者都露在对白框上方。左边几盏廊灯，右边夜河，栏上只有积水。青鸾国僧儒的旧事和陆抬说的“留不住”都在这一镜里读完；前方那截空栏始终留给他慢慢走。 |
| 02 · 人先想到“慢” | [L1066–1070](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1066)　陈平安心声“且慢行。”／“慢。” | 从行步全身切到肩后。近处留一角湿木和他的侧脸，越过他能看见远处柱影旁那道暖光。“慢。”单独占原有的一页，读完仍是普通的铁券河。 |
| 03 · 从溪边、山巅回望廊灯 | [L1073–1087](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1073)　“宴前同朱敛说过的那番话，也重新浮上心头。”至崔东山回忆“肯低头看一眼。” | **03a（L1073–1080）**　接02柱边的碎灯影，切到白日溪面的反光。陈平安从自己的眼睛看见水里的赤脚，左边裴钱正低头拨弄膝上的草鞋。**03b（L1083–1087）**　切到黄庭国山巅。自己缠腕的拳在左下，白衣崔东山在右，听他说完两句旧话。**03c（L1087句末接L1089起首）**　陈平安循声侧首，眼前已经是来路的廊灯、湿木栏与寻常夜河。 |
| 04 · 栏端折返 | [L1089–1116](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1089)　“夜廊寂静，陈平安走到栏杆尽头，转身往回走。”至“是不是也能少一些？” | **L1089 同一句内完成折返。** 接03c的主观视线，04a从廊内侧面看陈平安朝右停步。04b脚尖已转向左，沿栏走回。两格沿用原线稿，04a灯下水面仍有细弯痕。L1092“世道若是在变好”起留在现实夜廊，直到“那些被碾碎的花草”。 |
| 05 · 气府里有人在等 | [L1119–1123](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1119)　“气府之内，金色儒衫小人抬起头。”至“它静静等着。” | 切入体内。暗处的小人抬头，自身的金光向内聚，几粒散开，它守在原处。给气府留一个可辨的门口，供后面急劝时认回。心口的一点亮光随小人留在门内。 |
| 06 · 从花草想到一个人 | [L1125–1127](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1125)　“廊下的陈平安仍在往前走。”至“在路上问过朱敛的一个难题。” | 回到04的返程方向。先看见他仍独自在栏上走，让“离开山崖书院后”这句在现实夜廊说完。下一页陈平安开口问，才切去当年。 |

#### 2　返乡路上的旧问（10句）

| 镜号 | 对应剧情 | 画面与切点 |
|---|---|---|
| 07 · 十个人，和眼前这个人 | [L1131–1149](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1131)　陈平安旧问“若是杀一个没有做错事的好人，就能救十个人，杀不杀？”至“才知道自己的本心和选择。” | 山路自然天光，同行双人中景。陈平安侧头发问，朱敛在L1133轻轻摇头。问到一千、一万人，两个人在画面里的大小都不变。L1143“我担心自己就是那个被杀的人”留在朱敛平常的脸上，陈平安也在镜内听着；L1145朱敛转眼问“少爷，你呢？”，同镜留足他答“我也给不了答案”和末句。 |

#### 3　回到当下夜廊（28句）

| 镜号 | 对应剧情 | 画面与切点 |
|---|---|---|
| 08 · 旧问结束 | [L1153](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1153)　“夜色中的高楼上，陈平安仍是独自一人。” | 山路双人切回四楼单人全身，认回同一根廊柱、同一侧夜河。栏顶上只剩他的脚步。 |
| 09 · 门内急劝 | [L1155–1174](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1155)　“小人已经急得走到门边。”至气府心声“这可是你将来跻身上五境的大道契机！” | 切回05的气府，这次小人已到门边。让它的身体越过暗部、朝门外探出，脚仍在门内。五句急劝始终落在它身上；念到那个“慢”字时，看清它焦急的神色。 |
| 10 · 他听不见 | [L1177–1183](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1177)　“这些心语，陈平安一句也没有听见。”至“陈平安终于停下脚步。” | 切廊侧全身。他照原来的步子走，眼睛仍望向前方。旁白交代小人只能等；到“终于停下脚步”，陈平安的两脚在栏顶站定。 |
| 11 · 里面也停住 | [L1185](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1185)　“金色儒衫小人也站住了。” | 短切气府门内。接上一镜停步的姿势，小人也收住脚，脸上还带着急色。 |
| 12 · 想起宁姑娘 | [L1187–1198](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1187)　“廊下，陈平安忽然笑了一下。”至“可万一，她其实愿意呢？” | 回到陈平安侧脸。他先笑，后读到牵手的心声。身后空廊与夜河留在画面里，这一点笑意只给他自己。 |
| 13 · 下栏，给自己鼓气 | [L1201–1214](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1201)　“他跳下栏杆，朝房门走去。”至“这怎么行。” | 镜头放宽。用落地的一步交代高度变化，栏杆回到身侧。L1203走出两步，以拳轻击另一手掌；“又不是没抱过”以后双手松开，沿廊板向房门走。 |
| 14 · 门前又慢下来 | [L1217–1224](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1217)　“到了门口，他的脚步又慢了下来。”／“还是慢些。”／“与她，慢些也好。” | 门边侧身中景，让跨向门槛的下一步缓下来。这次“慢些”全留在鞋尖与门槛之间，灯光仍是日常的暖色。 |
| 15 · 余下的一点金光 | [L1227–1235](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1227)　“气府里的小人仰面倒了下去。”至“小人怔了一会儿，也笑了起来。” | 切气府。小人仰倒、骂出心声；L1233才把目光引向它心口仍凝着的一点金光。停在它低眼看光、回过味来的一笑。 |

#### 4　回房，灯下重读（15句）

| 镜号 | 对应剧情 | 画面与切点 |
|---|---|---|
| 16 · 同一盏灯，同一本书 | [L1242–1246](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1242)　“灯还亮着。”至“有些人的心，就像一面照妖镜。” | 由小人心口的一点金，切到桌上一小簇暖灯芯。第一眼仍能看到桌沿和合起的佛经，认出是先前离开的那间客房。L1244陈平安回到桌前重展书页，手指落在页边。 |
| 17 · 灯前想到家 | [L1248–1254](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1248)　“他看着灯火，却想起泥瓶巷的祖宅。”至“若有客人来，便也能看见。” | 从书边切到他的视线落处。近处一盏油灯，暖光照出桌面一点尘埃，房里更远处隐进暗里。祖宅窗台的草盆由旁白带出，画面守着这盏客灯。 |
| 18 · 书页停住 | [L1256–1272](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:1256)　“下巴搁在手背上，望着那点光亮。”至“他许久没有再翻页。” | 桌侧近中景，把手背、侧脸、摊开的书放在同一画面。L1262念及那一个人，眼睛仍朝着灯；L1265“天底下的道理，没有亲疏之别”作为心声。L1270灯芯轻响，手和书都不动，L1272整页留住同一画面，在这一次未完成的翻页上收束。 |

</details>

## 无字停留、头像与声音归属

- [L172](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:172)为客栈前远处来人的无参数`pause`；[L488](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:488)为放箱图的无参数`pause`。均由玩家控制继续，不宣称为连续动作动画；原挽臂无字停留仍取消。
- [L787](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:787)、[L789](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:789)、[L793](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:793)保留裴钱一次、朱敛两次专用头像；本轮未改变A2默认、B2可选的界面规则，也不把头像扩展给新配角。
- `wy_telepathy`是吴懿向陈平安传音；`wy_thought`是只向玩家呈现的吴懿心声。两者不可混用。
- `cpa_memory`、`zl_memory`、`cds_memory`保留回忆归属；`jssr_thought`只属于气府内部。心声／回忆结束后恢复普通对白标签，不让角色听见不属于现场的内容。
- `companion_elder`、`ziyang_steward`、`xiaoluan`、`ziyang_crowd`与积香庙小神分别承担各自发言，现阶段无新增配角头像、立绘或配音资产。

## 本轮核验入口

2026-10-30雨停图定稿、三处同名核对、仅两句接入范围与运行验证见[本图定稿接入记录](../../work/art/chapter2/c2_rain_after/finalization.json)。487条正文与顺序保持，仅新增显示与退黑两组演出语句；此次验证不扩展为全章验收。

当前文本对应、标签与跳转、图片引用及运行检查统一登记在[定稿接入记录](story_compression_record.md)的2026-10-29节。本页的段落表是脚本与素材状态登记，不替代游戏实机验收。487条文本映射及验证证据位于[本轮工作区](C:/Users/MSI/.codex/visualizations/2026/10/28/01a1827f-f8fa-7d52-ab18-1d96443336d9/chapter2_finalization_20261029/)。

## 历史分镜与验收记录（2026-10-12至2026-10-28）

下方原文保留旧稿分镜、素材决定及对应版本验收。其中所有“当前”、T／V编号、脚本行号、数量和“待补”均以当时版本为准；旧链接点击后可能已落到新版其他位置，不得作为当前制作依据。历史“善恶之问为现场问答”“宴后临窗长谈”已被本页上方的新稿顺序取代。

<details>
<summary>展开历史入口原文（旧T001–T226及56单元，非当前正文）</summary>

# 第二章当前分镜入口

更新：2026-10-26。记录当前脚本已经执行的文字顺序、归属、画面与缺项，供分镜维护及后续补图使用。

[第二章全章分镜工作簿](F:/图片素材/第二章全章分镜.xlsx) · [原文与改编并排阅读版（HTML）](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_review/第二章_原文与改编分镜对照.html) · [原文与改编并排阅读版（Excel）](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_review/第二章_原文与改编分镜对照.xlsx)

正文唯一权威是 [script_chapter2.rpy](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy)。本入口不重复完整对白；逐条文字、演出事件及原页对应见上述工作簿和阅读版。上述工作簿与阅读版仍为2026-10-12快照，本轮未回写外部导出；其中旧画面状态与行号不代表当前实现，后续补图以本项目分镜入口及当前脚本为准。图片稳定代号以 [image_catalog.json](F:/project/JianlaiWhentheSwordArrives/game/image_catalog.json) 为准；剧情改编与运行验收见 [压缩记录](F:/project/JianlaiWhentheSwordArrives/game/Codex/story_compression_record.md)。

## 统计与使用方式

- 原文253页保留为历史层，不作为当前文字页数；当前为226条文字（T001–T226）与2处无字停留（V01、V02），合计228个演出事件，覆盖11场、56个单元。
- 当前使用40张场景图片（原27张加第8场13张，含08-04五素材、08-05迎客CG及堂口背景；挽臂CG与四张裴朱场景人物层停用），另有08-05专用对白头像2张。56单元中，29个“已接入”、3个“复用已接入”、6个“已有图待补差分”、1个“部分接入”、17个“黑场待补图”。6个差分单元集中在第1场及第2场开头，可共用稳定状态，不等于必须新做6张图。
- 共91条文字显示在黑场：T107是第7场入夜过渡；T133及T138–T226共90条仍待补图。T134迎客与T135–T137裴朱头像对话已接入，挽臂CG已取消，08-05仍未整场完成。黑场条数不等于需要新增的图片张数。
- 表中T/V为当前实际事件编号；L为当前脚本正文或pause行号，范围包括中间演出指令。单元ID沿用原表，含05-02a、05-02b、06-01a/b/c、06-06，不重新编号。
- “已接入”表示当前脚本确实调用该图，不表示新增切法、动态镜头、分层人物或所有美术细节已经完成。“待补”列写具体当前缺口及可复用条件。

## 两处无字及归属

- **V01／02-04／L80**：客栈前切到CG02·02·03，陈、朱察觉远处吴懿；隐藏文字窗后点击继续，下一事件T041才说明来人身份。
- **V02／07-05／L271**：切到CG02·07·05，陈弯身放箱；隐藏文字窗后点击继续，再进入CG02·07·06站稳临窗的T105。
- 两处都是无参数pause，沿用点击、键盘、自动和快进规则；不是定时短停或连续动作动画。原**V03／08-05挽臂无字停留已于2026-10-26按用户要求取消**，编号保留为历史，不重新分配；T134迎客对白直接进入T135。
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

2026-11-06 接入更新：用户已确认的四人巨舟彩图以 `c2_03_reveal_v2.png` 接入03-03，沿用 **CG02·03·03**。先无字停留，点击后显示“水雾散开，三层楼船低悬在街面上”；画面只表示核舟悬空变大的终态。原图与运行素材逐字节一致，A2实机已核对终态与旁白恢复。此前删除的抛舟、落符、化人、搭板、登船后升空旧图仍缺失，因此连续整段未通过验收；下方旧“已接入”描述不代表缺失文件已恢复。接入与检查边界见[本图制作记录](../../work/art/chapter2/c2_03_throw_west/悬空巨舟_四人终态线稿.json)的 `game_integration_2026_11_06`。

实际次序为先疏散，再抛核舟、楼船化形、符纸化少女、搭板、登船后升空。核舟与楼船都位于干燥街面上方，升空图已能看到众人上船后的结果。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 03-01 | 来到开阔处 | T057<br>[L114](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:114) | CG02·03·01 | 已接入 | 无必需补图；不得将人物改记为站在水面或水中码头。 |
| 03-02 | 先让路，再抛出核舟 | T058–T059<br>[L116–121](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:116) | CG02·03·01 → CG02·03·02 | 已接入 | 让路动作由保留旁白交代，当前无必需补图。若要把让路改为无字，需要独立清场结果或挥袖差分；不能宣称已有移人动画。 |
| 03-03 | 楼船显形，低悬街面 | 无字停留＋原旁白<br>[L126](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:126) | CG02·03·03（四人巨舟定稿版） | 已定稿并接入／局部实机核对 | 2026-11-07用户查看完整彩图后确认定稿。1920×1080原图原样导入；先完整展示四人与巨舟，点击后恢复旁白。仅终态静帧，未制作连续变大动画；前后旧图缺失，连续流程未通过。 |
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

2026-10-16已接入08-01至08-03五张静态图：入夜赴宴、询认、认出笑意、拍肩、收手交谈。当前已按用户“全部替换”的要求统一为v2，孙登先身份与衣装采用已确认的 [彩色母版](F:/project/JianlaiWhentheSwordArrives/game/lh/sdx/sdx_master_v2.png)：灰绿斜襟叠裹短披肩、米白卷袖、左肩布结与深褐腰带。五张场景文件均为`_v2.png`，稳定代号CG02·08·01至CG02·08·05不变；旧v1文件保留并停用，旧v1调用别名兼容映射新图。T122 的拍肩、陈高兴和裴瞪眼作为08-03的触发动作；原P140及P141的历史映射保留，执行归属与原页出处分别记录。当次08-04前退黑；2026-10-18已补接08-04，现08-05保留T134迎客，并直接进入T135–T137裴朱头像对话；2026-10-26已取消V03挽臂CG，T133及T138以后仍待补图。226条正文与音频控制流不变；无字停留现为两处。

2026-10-17新增已确认的蜈蚣岭回忆图 `CG02·08·06`，仅覆盖T113–T114两句，在T115前回到原认出图。该次第8场共6张运行图，原五张与稳定代号保留；正文及音频不变。本次接入与验证见 [回忆插镜记录](../../work/art/chapter2/c2_08_memory_record.json)。

2026-10-18用户确认08-04彩图定稿，接入背景02·01与立绘01·01·02·01／09、立绘20·01·01·02／09，共五个独立素材。陈、孙分别使用固定左／右槽与同角色标签，按对白切换表情及轻微压暗，末句留空廊。接入与检查见 [08-04定稿记录](../../work/art/chapter2/c2_08_04_record.json)。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 08-01 | 入夜赴宴 | T108–T110<br>[L295–297](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:295) | CG02·08·01 | 已接入 | 夜廊建立图承接三人赴宴与陈停步，竹箱留在客楼。萧鸾身份继续由文字介绍，不将远处女性背影当成专属身份肖像；无必需新图。 |
| 08-02 | 廊下相认 | T111–T121<br>[L304–330](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:304) | CG02·08·02 → CG02·08·06 → CG02·08·03 | 已接入 | T111–T112夜廊询认；T113–T114切蜈蚣岭除妖后叮嘱的回忆图，仍由当下陈平安讲述；T115前回夜廊认出故人。T119–T121补叙保持夜廊、不重复插镜。无新增对白或无字停留，尚未拍肩。 |
| 08-03 | 拍肩与旁观 | T122–T127<br>[L336–347](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:336) | CG02·08·04 → CG02·08·05 | 已接入 | 拍肩图仅承载T122，T123起切手已收回的稳定群像，供裴、朱旁观及孙向同伴介绍陈；裴、朱内心仍由旁白注明，不当成当面对话，也不画出崔东山。无必需新图；静态切换不是连续拍肩动画。 |
| 08-04 | 催席同行 | T128–T132<br>[L356–374](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:356) | 背景02·01＋陈／孙独立立绘 | 已接入 | T128两人倾听，T129陈开口、孙略暗，T130孙开口、陈略暗，T131双方恢复倾听，T132撤下两人留空廊；修士全程画外。固定左右站位，不是行走动画；T133退黑。 |
| 08-05 | 吴懿相迎与众人揣测 | T133–T140<br>[L380–413](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:380) | 黑场 → CG02·08·07 → 背景03·01＋当前发言者柔边头像界面17·05／06（A2／B2对白，无场景人物立绘） → 黑场 | 部分接入 | T134吴迎客、陈听，随后直接进入头像对白；V03挽臂CG保持取消。T135用裴钱诧异头像，T136–T137换朱敛促狭头像，原界面17·01／02保留为身份源。A2／B2已接入，默认A2，设置可切B2并保存选择；本段为普通无头像规则的唯一专用头像例外。挽臂CG及四张场景人物层继续停用，原图和兼容定义保留；T138退黑，恢复无头像旁白及中性色板。T133与宾客镜头仍待补，剧情正文不改。当前实现与验收入口见[无头像对白制作记录](../../work/art/dialogue_no_portrait/record.json)的`game_integration`；P5及普通头像回退验证仅为历史。 |
| 08-06 | 举杯开席 | T141–T145<br>[L415–419](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:415) | 黑场 | 黑场待补图 | 补雪茫堂席面稳定群像与一个举杯关键状态；酒名和六十坛来历继续由对白承载。 |

2026-10-28对白界面接入：用户已授权从序章至目前完成内容统一使用A2／B2，默认A2，设置可切B2。普通对白、双人说话、心声与旁白均无对话区头像，仅本场T135–T137按句显示两张专用头像；场景CG人物和08-04独立立绘不因本轮UI接入移除。柔化遮罩界面17·03／04及头像17·05／06从已确认PSD导出，底色按当前背景派生中性／冷青／暖夜三类，黑场回退中性。Photoshop分层母版继续供用户UI与Codex API共同编辑；制作、验收证据与未验证项统一见上述`game_integration`。

以下按日期保留制作历史；当前运行范围以上表及2026-10-28接入记录为准。2026-10-27两套布局曾处于“已定稿、默认未定、待接入”阶段，历史决定见[08-05制作记录](../../work/art/chapter2/c2_08_05_record.json)的`portrait_layout_finalization_revision`，不再作为当前状态。

08-05宾客镜头的制作约定（2026-10-20用户批准，宾客部分尚未接入；当前前段演出以上表为准）：宾客属于堂内远景环境层；到T138–T140才切为堂口背景与安静的宾客远景，视点转向宾客不表示陈吴离场。三句均为叙述者概括，不把宾客当作轮流发言的角色，不追加姓名、口型或高亮。低对比通过尺度、灰阶和细节控制，人物保持实体，宴席尚未开始。新同框示意与透明层见[图片索引第3.36节](character_image_index.md#336-08-05堂口相迎与挽臂线稿2026-10-20)；同框图不是实际图层叠放，家具遮挡和边缘需在上色接入前继续核对。

2026-10-21空间修订：用户否定原小厅尺度，并指定按已展示的《庆余年》第一张夜宴截图改绘。当前背景线稿改为厅内占主体的宽阔宴堂，采用斜向宽中道、两侧连续分席、高梁架与远端主位屏风；人物和已上桌的菜肴移除，仍是未开席。旧小厅背景与同框宾客示意停用；宾客远景原则保留，原画布上的位置、大小及家具遮挡必须按新背景重排，不能把旧同框验收沿用到新背景。线稿未上色、未接入，游戏08-05仍为黑场，见[08-05制作记录](../../work/art/chapter2/c2_08_05_record.json)。

2026-10-21用户确认宽阔宴堂“可以非常不错”，并选择“陈吴主角画面与堂内宾客两种镜头分别预览”。已生成陈左吴右的挽臂前景同框示意，以及左一右三、席旁站立的匿名宾客远景示意；两镜分别呈现，不把全部人物同时铺满。空厅构图保持，人物镜头尚待审阅；宾客回望堂口的动作仍较轻。两图均为生成式构图预览，不是透明层实际叠放或游戏截图；新版宾客透明层尚未导出，旧小厅透明层停用，游戏仍退黑待补。见[图片索引第3.36节](character_image_index.md#336-08-05堂口相迎与挽臂线稿2026-10-20)。

2026-10-21线稿与3D往返修订（用户已授权，本轮候选待审）：迎客补“尚未挽臂”状态；裴朱镜头补闭口旁观与朱敛开口说话；宾客由椅凳区域移到席间中道侧可见空地，最近人物退回中景。出场顺序如下，切镜表示换取景，不表示画外人物离场或这时才到场。

| 拍点 | 画面与主客位置（2026-10-21主客修订） | 说话与连续性 |
|---|---|---|
| T133 | 堂口空间，人物画外 | 旁白已交代吴懿迎上来；不另加漫长走入或无字停留，也不表示全厅无人。 |
| T134 | 吴在画面左后、堂内侧朝外迎请；陈在右前、入口侧朝内回应，分开站立 | 吴懿迎客开口，陈平安闭口听；尚未挽臂。 |
| T135 | 吴右手挽陈左臂，两人转向左后内堂；吴略领前，陈随行 | 裴钱画外说“她竟然挽着师父”；陈吴闭口，不误给二人说话高亮。 |
| T136–T137 | 裴左、朱右，整组位于陈吴后方的入口侧；身体朝内，转头交谈 | 两句都是朱敛说，裴钱闭口听；二人原本就跟在后侧。 |
| T138–T140 | 左一右三匿名宾客远景 | 三句均为旁白；宾客无姓名、口型或逐人高亮，陈吴仍在画外，宴席未开始。 |

空间检查采用可旋转3D占位图，陈吴在入口附近，裴朱在其后侧，宾客在两侧席间；新增人物视角与斜侧视，避免主角出画或吴懿完全被遮住。模型内108项体量／深度组合检查未见人形与家具相交，最小净距约0.47m；数值只适用于估算模型。背景方向已向原画校准，但台阶、席案与柱距仍不是精确重建，不能据此宣布线稿等比透视通过。当前线稿、完整提示词、3D路径及验证记录见[图片索引第3.36节](character_image_index.md#336-08-05堂口相迎与挽臂线稿2026-10-20)与[制作记录](../../work/art/chapter2/c2_08_05_record.json)。本轮未改剧情脚本、图片注册或运行资产，尚未进行彩图、透明边缘及对白框实机验收。

2026-10-21后续反馈与当前重点：用户确认场景保持，指出线稿与3D人物均有贴图感。上轮无家具碰撞及说话状态检查只作为对应项目的结果，不构成场景融入验收。当前先用陈吴挽臂镜头做完整落地、共同灯位、接触阴影和线条协调的验证；[当前线稿](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-ebe48e24-acca-4fb6-95de-29cb0b2f48a8.png)为候选待审，旧主角同框保留为待修正动作／站位参考。人物实际出场关系和T133–T140说话顺序保持；全身是本次空间验证手段，不代表正式对白镜头必须全身。3D人物改进侧面厚度、关节及衣装体块，仍不作为正式角色模型。详见[制作记录](../../work/art/chapter2/c2_08_05_record.json)。

2026-10-21继续修订迎客与裴朱：按用户批准的陈吴融入方向，先补两组完整足点、共同灯位和地面投影；迎客保持吴开口、陈闭口、尚未接触，裴朱保持裴闭口听、朱说两句。裴朱首稿的裴钱偏高，已按05-03及02相邀回校整体体量，未设定新的厘米数或成人比例。当前[迎客线稿](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-11e9e660-8114-4a0d-a37f-5e3e838f6aff.png)与[裴朱线稿](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-c2b7cdf5-1598-4132-864e-fc87c8a5d74f.png)为候选待审；随后以原3D场景核对间距、前后和相对大小。宽厅建筑及T133–T140出场／说话顺序不变，仍未上色或接入；过程与空间检查统一见[制作记录](../../work/art/chapter2/c2_08_05_record.json)的`greeting_dialogue_integration_revision`。

2026-10-21主客调度修订（当前候选）：用户指出站位必须体现主人与客人，并明确“开始修改”。本场吴懿是迎请主人，陈平安是来客，裴钱与朱敛是随行者；左后主位为堂内方向、右前画外为入口方向。已重画[迎客](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-6f02539b-c7b9-49f0-8da1-770423ef0e56.png)、[挽臂转向堂内](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-8477785c-7ad1-4f13-bb4b-126b57a2c563.png)和[入口后侧裴朱交谈](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-60ddc8c1-4ef8-4cb5-924d-07a90dfc0cf8.png)。以上取代前述固定“陈左吴右”的旧调度作为当前评审入口；旧稿保留为待修正，不能用镜像旧立绘实现新转身。裴钱钱袋已修回自身左侧，陈玉簪参考沿用已确认的新方向稿；本轮未修改身份母版。

3D v5同步形成吴在堂内朝外、陈在入口朝内的迎接关系；挽臂后同向朝内、吴略领前，裴朱在陈后方入口侧并侧头交谈。主代理与独立复核已检查三张线稿及三镜空间截图；192人次占位检查无家具碰撞，未挽臂人物包围盒无相交，接触手袖按设计接触处理。建筑、家具、灯与机位保持。模型尺度只作估算，不构成原画的精确透视或正式身高标准。T133–T140文字、说话人及出场顺序保持，未接入游戏、未上色；完整输入、提示词与检查见[制作记录](../../work/art/chapter2/c2_08_05_record.json)的`host_guest_staging_revision`。

2026-10-22陈吴上色：用户批准吴懿与陈平安进入上色，并明确裴钱、朱敛先不改。已按上述主客线稿完成[迎客彩图](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-78a40155-15fc-40ac-9f3c-ecb46a714188.png)与[挽臂彩图](C:/Users/MSI/.codex/generated_images/01a14ee9-ccb2-7553-b578-b7b13b27159f/exec-3682efe5-aa02-4cfc-baf0-f45def9555e5.png)，上色阶段为候选，现已获用户定稿；吴青蓝／浅绿／暗红与陈灰蓝／灰白服色保持，同一暖灯和右侧冷夜色贯穿两镜。T134吴说陈听、T135裴钱画外说话、吴右手挽陈左臂及主客朝向不变。裴朱、宾客与3D v5未修改，完整上色过程见`chen_wu_color_revision`。

2026-10-22陈吴定稿接入（历史，后续采用范围见下）：两张彩图原始字节导入`images/chapter2/c2_08_greet_v1.png`与`c2_08_link_v1.png`，注册同基名`bg`定义并分别用于T134、T135；稳定代号为CG02·08·07／08。原生1672×941，运行时沿用1920×1080缩放，按完整CG展示；没有重新出图或拆透明层。T133与T136以后保留黑场，裴朱及宾客不提前采用。引用、切镜与局部实机验证统一记录于[定稿记录](../../work/art/chapter2/c2_08_05_record.json)的`finalization_revision`。

2026-10-22裴朱双人对话接入（历史）：用户批准挽臂CG先展示、点击后进入两人对话。T134既有迎客CG不改，挽臂CG移至新增V03无字停留；T135裴钱开口、朱敛闭口略暗，T136–T137交换开闭口及明暗，T138前退黑。采用独立堂口背景与四张RGBA人物层；两角色在陈吴后侧靠入口，裴在左、朱在右，使用原构图足点与相对体量。人物差分沿用同一变换；这是静态表情切换，不是连续口型。新增5素材的定义、文件基名、脚本调用及稳定代号对应；正文226条与音频不改。完整提示词、3D和叠放检查、运行验收见[08-05制作记录](../../work/art/chapter2/c2_08_05_record.json)的`pair_dialogue_revision`。

2026-10-25专用头像首轮接入（历史，后被下述采用修订替代）：用户否定上轮只靠场景人物明暗的效果，并指定应用此前讨论的独立头像对白方案。T135–T137保留场景人物表演，在底部只显示当前说话人的新绘胸像、姓名和台词；裴钱用界面17·01诧异开口，朱敛两句用界面17·02促狭说话。头像按句传入，不用持续场景开关；原图与UI尺寸分开，其他对白布局沿用原逻辑。T134和V03维持原CG，T138恢复普通旁白；226条正文、三处无字停留和3D v5保持。完整素材与该轮验收见08-05制作记录的 `speaker_portrait_revision`。

2026-10-25“仅背景与当前头像”采用修订（历史，当时仍含V03；当前范围见下文弃用修订）：用户明确08-05既有独立头像，就不再在场景中显示裴钱、朱敛立绘。T135–T137仅保留背景03·01，底部按句显示界面17·01／02及当前姓名、台词；四张场景人物层改为停用，原图、定义与兼容别名保留。T134、V03、T138边界及226条正文保持，不重绘场景或头像。本章当前场景图由45张降至41张，专用头像仍为2张；这是08-05的局部演出选择，不扩展为所有视觉小说场景的统一规则。采用与验证见 [08-05制作记录](../../work/art/chapter2/c2_08_05_record.json) 的 `portrait_only_revision`。

2026-10-25头像交互验收（历史）：正文226条、三处pause及原行号、音频和章节跳转保持；目录检查与隔离lint通过。常规布局与桌面强制small布局分别34/34断言通过，包含T134／V03／T138边界、当前发言者头像和姓名、三处引擎存读档、回退、回看、自动与快进。两种窗口已目检，无头像／姓名／正文重叠。small不是移动设备真机测试；旧档兼容、全章及手动存读档菜单未验证。原运行文件114份保持，陈吴定稿及3D v5保持。完整证据见制作记录 `speaker_portrait_revision`。

2026-10-26 P5式局部对白采用修订（历史试作，整套P5方案已弃用）：用户明确只按《女神异闻录5》方向制作08-05，并取消挽臂CG。T134迎客后直接进入T135–T137；背景03·01及两张专用头像原图沿用，当前说话人的头像放大并与黑白斜切框、错层姓名条组成界面，操作入口移至右侧，不混入纸墨风格，也不将胸像作为堂内人物层。`dialogue_comic.rpy`与`gui/dialogue/c2_08_comic_frame.svg`仅承载此段局部布局。挽臂CG标为停用，原文件、定义、稳定编号和别名保留；其他场景及3D v5保持。当前为226条正文、2处无字停留、40张场景图与2张头像；视觉待用户审阅，本轮隔离lint及常规37/37、桌面强制small/touch 34/34断言已通过（分批记录），初版采用和验收以[08-05制作记录](../../work/art/chapter2/c2_08_05_record.json)的`p5_dialogue_revision`为准。

2026-10-26底部按钮采用修订（历史试作，随P5方案停用）：按用户要求将六项快捷操作横排放回底部，桌面与触屏均保留回退、快进、自动、快存、快读、菜单。按钮使用黑白斜切边框及悬停／选中反色，随1920×1080场景区域等比缩放；面板、姓名与正文上移90逻辑像素，留出底部安全区。头像、背景、SVG原图及剧情均不改。视觉待用户审阅，本轮底栏常规与桌面强制small/touch分别55/55通过，含多窗口比例及六按钮实点；手机真机未测；当前采用与验证见[08-05制作记录](../../work/art/chapter2/c2_08_05_record.json)的`bottom_menu_revision`，上条37/37与34/34仅属于历史侧栏版本。

2026-10-26 P5方案弃用（历史）：P5的对话窗与它自身的人物、场景画风统一，但与本项目现有的人物和场景画风不协调；因此放弃整套P5式界面。当时撤下P5路由，临时恢复普通头像对白及原底部快捷菜单；两张头像、堂口背景、无场景人物立绘及取消挽臂CG的范围保持。P5源码与SVG仅保留停用历史，旧37/37、34/34及底栏55/55均为对应试作的历史验证，不作为当前布局验收。该轮隔离lint及普通头像回退实机25/25通过；仅确认当时回退可用，未确认新美术方案，原因与该阶段验证见[08-05制作记录](../../work/art/chapter2/c2_08_05_record.json)的`p5_rejection_revision`。

### 第9场：且慢行与善恶之问

本场全部仍是黑场文字。陈心声、崔东山回忆、陈朱真实问答、气府内心语依靠明确的说话人及副标区分，尚无对应专用图。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 09-01 | 且慢行 | T146–T151<br>[L422–429](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:422) | 黑场 | 黑场待补图 | 先明确本段与宴席及行走段的空间衔接，再补陈平安稳定沉思状态；伞、车轮等比喻不必逐一新增CG。 |
| 09-02 | 忆及崔东山所言 | T152–T153<br>[L433–434](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:433) | 黑场 | 黑场待补图 | 可共用09-01稳定沉思图，以回忆说话人标记区分即可；不必新增现实在场崔东山立绘。 |
| 09-03 | 慢与改过 | T154–T158<br>[L437–443](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:437) | 黑场 | 黑场待补图 | 共用09-01沉思图即可；种子是解释性意象，当前不必追加生长特效。 |
| 09-04 | 善恶之问 | T159–T164<br>[L445–454](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:445) | 黑场 | 黑场待补图 | 确认当前空间后补陈朱稳定双人交谈图，能清晰区别此处真实问答与前后心声；不需新增杀人情境图。 |
| 09-05 | 气府小人急劝 | T165–T171<br>[L457–465](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:457) | 黑场 | 黑场待补图 | 补可辨识为身体内部的气府空间及金色儒衫小人的着急稳定状态；若画冲门，仅作短相位并接站稳状态。 |
| 09-06 | 念及宁姑娘 | T172–T175<br>[L467–470](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:467) | 黑场 | 黑场待补图 | 复用陈的沉思或走路结果状态；宁姑娘并非当前在场，无必需新增宁姑娘出场图。 |
| 09-07 | 气府里的反应 | T176<br>[L473](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:473) | 黑场 | 黑场待补图 | 复用09-05待补气府与小人图即可；可选气急表情差分，非必须全新CG。 |

### 第10场：临窗雨夜长谈

本场全部仍是黑场文字。雨夜坐饮不能视作已经复用第7场的暮色站谈图；雨声、斟酒、雨歇目前由文字交代，没有本章新增音频调用。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 10-01 | 雨夜临窗入座 | T177–T181<br>[L480–487](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:480) | 黑场 | 黑场待补图 | 补同一客楼的雨夜双人坐饮稳定图，保持窗、箱与房间连续；斟酒可由保留旁白承接，不强制多帧倒酒动画。 |
| 10-02 | 河水与光阴长河 | T182–T190<br>[L489–504](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:489) | 黑场 | 黑场待补图 | 共用10-01待补雨夜坐谈图；河水与光阴概念由对白保留，不必补宇宙或光河特效。 |
| 10-03 | 马屁与酒 | T191–T195<br>[L506–514](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:506) | 黑场 | 黑场待补图 | 共用夜谈底图，补或复用陈转向朱、朱酒杯可见的稳定状态；若保留动作旁白可暂不做举杯动画。 |
| 10-04 | 远游与托付裴钱 | T196–T203<br>[L516–527](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:516) | 黑场 | 黑场待补图 | 共用夜谈图，保持裴房方向可交代；未来北俱芦洲与护送计划留语言，不补成当前旅途图。 |
| 10-05 | 朱敛说旧事 | T204–T215<br>[L529–544](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:529) | 黑场 | 黑场待补图 | 共用夜谈空间补朱讲述、陈倾听的稳定状态即可；不将整套少年朱敛风流闪回列为当前必补。 |
| 10-06 | 想起宁姑娘的心声 | T216–T220<br>[L547–551](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:547) | 黑场 | 黑场待补图 | 可共用夜谈图，以心声标记区分；可选陈分神表情，非必须新增宁姑娘立绘。 |
| 10-07 | 回神与雨歇 | T221–T224<br>[L554–560](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:554) | 黑场 | 黑场待补图 | 共用夜谈图，若要撤末旁白再补雨后窗景与杯酒减少的结果差分；当前保留旁白，不宣称已有音效。 |

### 第11场：翌晨离府与吴懿传讯

本场仍是黑场文字；翌晨离府和吴懿传讯后跳转第三章。传讯信息只向玩家交代，没有提前变成陈平安已知信息。

| ID | 当前标题 | 实际T/V与脚本行 | 当前画面代号 | 接入状态 | 具体待补／边界 |
|---|---|---|---|---|---|
| 11-01 | 翌晨辞府 | T225<br>[L565](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:565) | 黑场 | 黑场待补图 | 补可与第7场空间连续的清晨离府或返乡路结果图；保持三人及行装连续。 |
| 11-02 | 吴懿传讯 | T226<br>[L567](F:/project/JianlaiWhentheSwordArrives/game/script_chapter2.rpy:567) | 黑场 | 黑场待补图 | 补吴懿独处传讯的稳定图即可；传讯媒介未定，不擅画特定法器，也无需新增父亲接讯CG。 |

## 原文指代确认与仍待核项

- **“她竟然挽着师父”（2026-10-20已确认）**：用户明确指定吴懿挽着陈平安，当前脚本仅将此句“他”改为“她”，说话人仍为裴钱。挽臂接触与袖口遮挡按两人共同绘制处理；2026-10-22曾以完整CG接入T135，后改为V03无字展示；2026-10-26用户明确不需要挽臂CG，现已取消V03，T134迎客后直接进入T135裴朱头像对话。10月12日的原文快照与验收记录保留当时原词，不能据其旧待核项覆盖本次确认。
- **“紫气宫”与“雪茫堂”**：孙登先对白沿用“紫气宫”，当前赴宴地称雪茫堂；两者的空间或名称关系未核实，不擅自统一名称或拆成两个新地点。

现有整图无法证明的动作、时间和因果仍保留短旁白。第1场进行态、第2场开头迈步态、08-05的T133／T138–T140及第9–11场黑场是明确制作缺口；第7场暮色及08-01至08-03五图已经接入，不再列为待补。本文没有授权补写原作、删除更多对白、生成图片或把计划中的资产标记为完成。

## 数据来源与核验

本入口初版由2026-10-12快照 [actual_data.json](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_sync/actual_data.json) 的最终事件顺序与 [unit_visuals.json](C:/Users/MSI/.codex/visualizations/2026/10/12/01a1300d-d7a7-75a1-a5d0-d405431d07d9/chapter2_sync/unit_visuals.json) 的56单元现图核验整理。两份JSON及外部工作簿、阅读版仍保留该日状态；前者的历史字段保留原始来源。本轮以当前脚本逐条对齐原正文更新全部后移行号，并按 [第8场生成与接入记录](F:/project/JianlaiWhentheSwordArrives/work/art/chapter2/c2_08_record.json) 更新五图状态；226条正文与原文映射不变；2026-10-22曾按用户批准新增V03挽臂无字停留，2026-10-26已按后续要求取消。孙登先设计依据见 [当前身份标准](F:/project/JianlaiWhentheSwordArrives/game/lh/sdx/sdx_face_ref.md)。

| 来源 | SHA-256 |
|---|---|
| 历史script_chapter2.rpy（2026-10-22，挽臂V03与裴朱双人对话；当前脚本哈希见p5_rejection_revision） | `14589200642320401c3bd10bc2abbd1342f01c0c44596207060174960d2b115f` |
| 原文来源快照（baseline_sha） | `afa033c12b1c6fa57e712a3c6acb28b2a24e678ba07042a39aa225f4f813032c` |
| actual_data.json | `78787f79d0109b1786f39b6de3d7a1c75fbe60ebc3a3fc2a6072dda6d067fd4a` |
| unit_visuals.json | `5eeb4d1e11b56717e093ab9843fa03f54d22a07943eaefd11930d1b2ca9ffeb7` |

2026-10-16历史核验：56单元唯一且全覆盖；228个事件按当时脚本顺序归属；253原页保留历史映射；当时32张实际图片与两处无字停留可定位，黑场统计分出T107过渡。v2隔离lint退出0，主例66/66与稳定回看12/12合计78/78断言通过；覆盖五镜切换、三处存读档、跨镜回退、回看与当时08-04退黑，并核对1280×720及1867×1050窗口画面。主线程已目检五镜、大窗、退黑、回看及返回截图；111份原存档、缓存与rpyc文件哈希不变。该次依据独立的`scene8_sdx_v2_20261016/verification.json`，与旧v1同为78/78的验收分开记录，权威入口为上述第8场接入记录。

2026-10-18接入核验（历史记录）：加入回忆图与08-04五素材后，本章使用38张图片；第8场11个当前资源的定义、文件路径、调用及代号全部一致。08-04隔离lint退出0，实机65/65断言通过，覆盖五句对白的表情／亮暗／显隐、T127与T133边界、三处存读档、跨状态回退及回看返回。两种窗口1280×720及1867×1050下未见头顶裁切、脸被对白框遮挡或明显彩色残边；原图低alpha残边未作像素清理，换背景时仍需检查。114份原存档、缓存与rpyc文件哈希不变。当前正文226条、两处无字停留和音频控制流不变；行号与当前脚本逐条对齐。完整证据见[08-04定稿接入记录](../../work/art/chapter2/c2_08_04_record.json)。未验证完整十二章回归、旧版本存档迁移、移动端与物理1920×1080全屏；08-05起仍待补图，不宣称连续口型或行走动画。脚本或图片后续变更后，应重新核对行号、哈希及资产状态。

2026-10-20指代确认核验：本次正文仅将T135／L384裴钱对白中的“他”改为“她”，并更新紧邻注释。226条文字的说话人、顺序与数量、两处无字停留、演出／图片／音频指令及章节跳转均未改；08-05仍为黑场待补图。逐行静态核对通过，Ren'Py 8.5.3隔离lint退出0，仅有既存弃用及非ASCII文件名提示；原存档、cache与rpyc共114份哈希不变。未重跑实机或存读档，上述65/65验收只属于10月18日版本。六份素材已生成线稿，仍待确认、上色与接入，见[图片索引第3.36节](character_image_index.md#336-08-05堂口相迎与挽臂线稿2026-10-20)及[本轮制作记录](../../work/art/chapter2/c2_08_05_record.json)。

2026-10-22陈吴定稿核验（历史）：`bg_images.rpy`的63条背景定义（含5条兼容别名）及4条立绘定义核对通过，62个实际文件均存在且可解码；60处静态背景调用均已定义，无重复定义。4个既有标题前缀与5个v1→v2别名可正确解析。两张新图文件基名、定义名、脚本调用和稳定代号一致，分别只覆盖T134／T135；226条正文、说话人顺序、音频、两处停留及章节跳转保持。目录生成与`--check`通过。隔离SDK Python与主启动器均在启动前报WinError 623（系统DLL重定位），**本轮lint、实际切镜、存读档和回滚未执行**，无实机截图，不能沿用历史通过结果。原存档、缓存与rpyc 114/114哈希不变。完整静态证据与环境报告见[定稿记录](../../work/art/chapter2/c2_08_05_record.json)的`finalization_revision`。

2026-10-22裴朱双人对话验收（历史，非当前无场景人物版本）：72条图片定义解析到67个真实文件，第二章51处scene/show调用、5个新编号及目录派生产物一致；226条正文与接入前基线完全相同，当时45图片、91条黑场、3处无字停留。分镜56单元、54个T范围及V03行号均已对齐。隔离RenPy 8.5.3 lint退出0，仅既存弃用和非ASCII文件名提示；本轮已完成所需局部运行覆盖。主流程通过67条断言，余下自动/快进、两处对白读档及回看返回在独立补测中20/20通过，分批记数、不将重叠准备项相加冒充独立覆盖。验证涵盖V03点击/Enter/Space/自动/快进，T135–T137角色、口型、明暗及坐标，T138清场，V03/T135/T136三处存读档，T138回退至T134与history返回。已目检1280×720及1867×1050窗口中的脸、手势和对白窗，无明显透明洞、方框或错位。114份原存档、缓存与rpyc哈希不变。前次SDK启动623已在本轮隔离运行解决，历史失败记录仍保留；未做完整十二章回归、跨版本旧存档迁移、移动端或物理1080p全屏。完整证据见[08-05制作记录](../../work/art/chapter2/c2_08_05_record.json)的`pair_dialogue_revision`。


</details>
