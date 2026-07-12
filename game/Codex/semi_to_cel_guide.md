半写实身份图转赛璐璐 / 动画风精简流程

## 文档用途

本文件用于处理以下类型任务：

已有半写实角色身份图；
需要转为轻度赛璐璐 / 动画风；
需要继续扩展为三分之四侧、侧脸、回头镜头；
需要在同镜头、同光线、同角度下制作表情差分；
需要从脸部 / 半身身份图扩展为全身标准基准图；
需要迁移指定服装参考，但不能让服装参考带走脸部身份。

适用范围：

男性角色肩部以上近景；
角色脸部身份母版；
图生图风格转换；
局部重绘；
三分之四侧、侧脸、回头镜头；
同镜头表情差分；
全身标准基准图；
服装迁移；
立绘、表情差分、剧情 CG 的风格统一。
1. 核心问题

这类任务的核心矛盾主要有四条：

风格一推强，角色身份容易丢。
脸会滑向通用古风男主、国风美男、赛璐璐男主模板。
身份一锁太死，画面又会退回半写实。
如果只强调保持脸，模型可能不敢推风格，最后仍然像半写实原图。
角度或表情一变化，模型容易把“同一个人”重建成“新的一张脸”。
尤其是三分之四侧、侧脸、回头、微笑、委屈、小得意等变化，很容易触发新脸。
从近景扩展到全身时，服装、站姿、背景会重新触发“白衣仙侠贵公子 / 古风男主立绘”模板。
全身图里脸部占比变小，模型会更多依赖服装、发型、站姿、背景来理解人物，导致身份漂移。

一句话总括：

先保人，再推风格；先做桥接，再推角度；先锁镜头，再改表情；先定全身结构，再谈成图美感。

2. 总原则
2.1 必须遵守的原则
先锁身份，再轻度风格化。
先稳定正面，再做三分之四侧桥接，再做侧脸和回头。
表情差分不是重画角色，只能在同一帧里微调表情肌肉。
全身基准图不是宣传海报，而是后续差分的结构母版。
服装参考只负责衣服结构，不负责脸部身份。
每一轮只解决一个问题，不同时要求“更像、更侧、更赛璐璐、更好看、更全身、更有气质”。
只要跑偏，就退回上一张稳定图，不在错误底图上硬修。
2.2 不要做的事
不要一上来就写：
full anime redesign
strong cel-shaded style
complete 2D animation conversion
不要从正面直接跳纯侧脸或回头。
不要一次批量做多个表情。
不要用“开心、委屈、微笑”这类宽词让模型自由发挥。
不要把全身图做成剧情海报 / 宣传立绘。
不要让服装参考图同时影响脸、气质和身份。
不要在全身基准图阶段加入卷轴、剑、扇子、书本等剧情道具。
不要为了追求“书卷、古怪、清醒”而在全身图里反复改眼神和五官。
3. 标准流程
3.1 先做身份母版

先选一张最像、最稳的底图，要求至少满足：

脸型对；
眉眼关系对；
鼻嘴结构对；
眉心痣或身份特征稳定；
气质是同一个人；
没有明显美男模板化。

身份没稳之前：

不做风格转换；
不做跨角度；
不做表情差分；
不做全身服装迁移。
3.2 再做低强度风格化

第一次风格转换只做轻度整理，不追求一步到位。

推荐口径：

mild cel-shaded cleanup
lightly stylized
slightly cleaner linework
slightly clearer shadow blocks
slightly less realistic skin blending

避免口径：

full anime redesign
strong cel-shaded style
complete 2D animation conversion

目标不是彻底改脸，而是：

线条更干净；
阴影块面更明确一点；
皮肤和发丝少一点写实感；
整体更统一。
3.3 正面稳定后，先做三分之四侧桥接

三分之四侧不是终点，而是正面到侧脸之间的桥。

它主要验证：

转角度后还是不是同一个人；
眉眼关系是否还在；
鼻梁、嘴、人中、下巴是否开始漂；
眼神会不会滑向“回眸男主”；
下颌和脖颈连接是否仍符合身份。

三分之四侧的目标不是“越侧越好”，而是：

角度够用，身份稳定，男主感不过量，气质不阴沉。

3.4 再做标准侧脸

侧脸阶段重点不是好看，而是骨相一致。

必须重点看：

额头到鼻梁的线；
鼻梁长度和鼻头结构；
人中和嘴唇厚薄；
下巴收束；
下颌到脖颈连接；
耳朵位置；
发束方向。

注意：

眉心痣在侧脸可能弱化或不可见，这不一定是错；
但不能被乱改成额饰、花钿或新装饰。
3.5 再做回头镜头

回头镜头必须放在侧脸之后。

这一阶段最容易跑偏成：

回眸美男；
温柔男主；
恋爱向镜头；
仙气海报。

目标应该是：

有剧情状态；
有观察或判断；
有警觉或回望动作；
不是“给观众看的美男回眸”。
3.6 当前镜头稳定后，再做表情差分

表情差分的前提：

当前镜头可留；
当前角度可留；
当前身份可留；
当前光线可留；
当前气质可留。

表情差分只能做：

眉毛；
上下眼睑；
眼神张力；
嘴角；
轻微脸颊张力。

不要改：

镜头；
光线；
头部角度；
发型；
衣服；
背景；
脸型；
鼻嘴结构。

推荐顺序：

认真；
疑惑；
微笑；
小得意；
委屈。

原因很简单：越往后越容易男主化、幼态化或恋爱向。

3.7 再做全身标准基准图

全身阶段的目标不是“做一张好看的宣传图”，而是：

把已经锁住身份的同一个人，扩展成可复用的全身结构母版。

全身基准图主要解决：

全身比例；
站姿；
服装结构；
袖子、腰封、下摆、鞋子；
身体轮廓；
后续动作差分底图。

全身基准图不适合单独承担：

脸部锁定；
表情差分；
眼神差分；
眉心痣最终判断。

所以全身图稳定后，必须配套做：

同服装半身 / 腰上基准图。

推荐顺序：

近景锁脸图
→ 轻度风格化
→ 三分之四侧桥接
→ 表情差分验证
→ 全身标准基准图
→ 同服装半身基准图
→ 全身动作差分
→ 半身表情差分
4. 全身基准图经验回溯
4.1 这次遇到的问题

本轮任务的目标是：

从已经稳定的肩部以上近景 / 三分之四侧近景，重新扩展成全身标准基准图。

但过程中反复出现几个问题。

问题一：全身图一旦变远，脸部身份立刻变弱

近景里能看清：

脸型；
眼型；
鼻嘴；
眉心红籽；
表情；
气质。

但全身图里脸占比太小，模型会转而依赖：

服装；
发型；
站姿；
背景；
整体轮廓。

于是角色容易从“锁定人物”滑向“白衣古风男”。

问题二：“清瘦、书卷、古怪”容易让模型重新造人

原本只是想补气质，但模型会把这些词理解成新角色设定。

高风险词包括：

thin
bookish
slightly odd
clear-headed
observant
harder to read

结果容易变成：

另一个清瘦白衣书生；
普通白蓝书生袍角色；
冷淡、文弱、清秀男主；
脸型、眼型、鼻嘴全部重建。
问题三：全身图里一动眼神，就容易换脸

以下词在全身图阶段风险很高：

observant gaze
clear-headed eyes
quietly judging
harder to read
sharp gaze
intelligent eyes
subtle strange expression

模型容易把它们执行成：

更锐利的眼睛；
更冷峻的脸；
更标准的男主五官；
更强的“判断感男主”。

你想要的是：

原脸基础上，眼神轻微清醒一点。

但模型可能执行成：

重新画一个清醒、冷峻、有判断感的白衣男主。

问题四：服装迁移容易两头失衡

服装迁移时会出现两种极端：

第一种：

白衣太干净；
袍边纹样太精细；
腰饰太贵；
垂饰太漂亮；
袖子太仙；
整体像白衣仙侠贵公子。

第二种：

压贵气压太狠；
服装变成普通白蓝书生袍；
腰部、垂饰、层次全部消失；
角色服装识别度被削掉。

正确方向不是“越素越好”，而是：

保留白衣层次和读书人结构，减少仙侠门派公子感。

问题五：v9 开始已经变脸

后面继续修 v10、v11、v12 时，脸一直回不来。

原因不是提示词不够强，而是：

v9 开始，底图脸已经漂移。

后续再写：

keep the same face
do not change identity

模型只会理解成：

保持 v9 的错误脸。

所以这类情况不能继续硬修，必须回退。

4.2 难点是什么

全身图的难点不在于“画不出全身”，而在于：

脸部身份、服装结构、人物气质、全身构图四者会互相拉扯。

具体表现：

想保脸 → 模型容易退回近景或半身；
想做全身 → 脸部身份权重下降；
想补书卷感 → 容易变普通书生；
想补古怪感 → 容易变阴沉、冷峻、反派或男主化；
想压贵气 → 服装容易过度简化；
想保服装识别度 → 又容易回到仙侠贵公子。

所以全身图不能同时承担所有任务。

正确分工应该是：

近景 / 半身图：负责脸、眼神、表情、古怪感
全身图：负责比例、服装、站姿、整体轮廓
4.3 实际解决过程
第一阶段：直接从近景扩展全身

最开始直接根据近景身份和服装参考做全身，能得到完整人物，但常见问题是：

背景像海报；
服装太仙侠；
站姿太男主；
脸部身份变弱。

所以后续开始压：

not a cinematic poster
not a noble xianxia prince
not a generic handsome ancient-style male lead
full-body standard base portrait
simple blue-gray studio background

这一步解决了海报感和背景抢戏问题。

第二阶段：尝试补“清瘦、书卷、古怪”

后来发现全身图太端正、太标准，于是尝试补：

thin
bookish
slightly odd
clear-headed
observant
harder to read

但问题是，这些词在全身图里风险很高。

模型会把它们理解成：

重新生成一个清瘦、书卷、冷淡的白衣少年。

于是出现：

脸型变了；
眼型变了；
鼻嘴关系变了；
发型变柔；
服装变成普通书生袍；
原本身份被替换。

这说明：

全身图阶段不适合用抽象气质词强行修身份。

第三阶段：发现 v9 已经是断点

后面继续修 v10、v11、v12 时，脸一直回不来。

原因不是提示词不够强，而是：

v9 开始，底图脸已经漂移。

后续再写：

keep the same face
do not change identity

模型只会理解成：

保持 v9 的错误脸。

所以这类情况不能继续硬修，必须回退。

第四阶段：重新回到全身版，接受“全身图只负责全身”

最后重新做全身版时，不再试图在全身图里解决所有脸部细节，而是把目标改成：

全身完整；
服装清楚；
构图稳定；
背景干净；
身形偏清瘦；
有基本书卷感；
不追求近景级别锁脸。

最终定稿图的价值在于：

它是一张可用的全身标准基准图，而不是最终脸部身份母版。

4.4 解决后又出现了什么问题
1. 脸部不会像近景那样稳定

全身图里脸太小，不能要求它承担：

表情差分；
眼神差分；
眉心红籽精确检查；
脸型细节锁定。

这些应该交给同服装半身图 / 肩部以上近景。

2. 服装仍有一定“漂亮立绘感”

全身图为了保留白衣层次和视觉完成度，不可能完全去掉：

白衣公子感；
立绘感；
清俊角色感。

只要不滑到“仙侠贵公子 / 古偶男主海报”，就可以接受。

3. “古怪感”在全身图里只能很轻

全身图不适合强做古怪感。

如果强行做，模型容易通过以下方式错误表达：

改眼神；
改脸；
低头变阴沉；
嘴角变邪魅；
姿态变反派。

所以全身图里的“古怪”只能是轻微气质，不要当作主要目标。

5. 全身基准图原则
5.1 明确参考图职责

服装参考图只负责：

服装结构；
袍子层次；
配色；
长袍轮廓；
袖子形状；
全身服装比例。

服装参考图不负责：

脸部身份；
五官比例；
表情；
年龄感；
眼神气质；
人物性格。

核心句：

Use lh/lcds/崔东山.png only for clothing structure and full-body costume reference, not face identity.
5.2 全身基准图不是宣传海报

全身基准图要避免：

山水夜景抢戏；
大雾气；
电影感光影；
英雄式站姿；
仙侠海报气氛；
剧情道具；
大风吹衣摆；
夸张袖摆。

全身基准图应该：

背景简单；
全身完整；
站姿中性；
服装结构清楚；
人物占比适中；
不带剧情动作；
不用道具固定手部姿势。

核心句：

This is a reusable full-body standard character base image, not a cinematic poster.
5.3 人物大小

全身图里人物不能太小。

经验值：

全身完整入画，但人物尽量占画面高度的 75%–85%。

人物太小会导致：

脸部身份弱；
眉心痣不清楚；
眼型嘴型难判断；
后续差分不稳。

人物太大又容易：

裁头；
裁脚；
裁衣摆；
丢失全身结构。
5.4 背景要压干净

全身基准图背景最好是：

简单蓝灰；
轻微纹理；
不抢戏；
不要山水；
不要浓雾；
不要剧情场景；
不要海报光。

背景越复杂，模型越容易把它当成剧情图。

5.5 服装贵气只能小幅压

服装迁移时常见问题是：

白衣太干净；
袍边纹样太精细；
腰饰太贵；
垂饰太漂亮；
袖子太仙；
整体像白衣仙侠贵公子。

正确修法是：

less luxurious, less fantasy-like, more restrained scholar clothing

不要写成：

old, poor, dirty, rough, torn

因为这样会破坏服装设定。

目标不是把衣服改破旧，而是：

保留白衣层次和读书人结构，减少仙侠门派公子感。

5.6 道具先不要加

全身基准图阶段不要加：

卷轴；
扇子；
剑；
书；
法器；
手势动作。

道具会导致：

固定手部姿态；
画面变成剧情图；
后续差分困难；
手部动作被锁死。

先做干净母版，后面再做道具差分。

5.7 全身图不是锁脸图

全身图主要负责：

身高比例；
体型轮廓；
发型大方向；
服装结构；
袖子、腰带、下摆、鞋子；
站姿；
基础背景。

全身图不负责：

眼神细节；
复杂表情；
精准眉眼关系；
嘴角差分；
古怪感细节；
近景级别身份判断。
5.8 不要在全身图里强修眼神

以下词在全身图里高风险：

observant gaze
clear-headed eyes
quietly judging
harder to read
sharp gaze
intelligent eyes
subtle strange expression

它们容易导致：

换眼型；
换脸；
变冷峻男主；
变反派；
变另一个白衣书生。

全身图里如果要补气质，只能写更安全的整体描述：

slightly quieter body presence
less standard male-lead aura
more restrained scholar-like bearing
robe hangs naturally on a lean body
5.9 不要让“书卷、古怪”变成新角色设定

错误写法：

make him a thin, bookish, slightly odd young scholar

模型会理解成：

重新生成一个清瘦书生。

正确写法：

keep the same character, same face, same costume, same composition;
only make the overall body presence slightly more restrained and scholar-like

重点是：

不要把气质词写成角色定义，要写成微调方向。

6. 常用提示词模板
6.1 轻度赛璐璐模板
Use the current image as the only base image.

This is not a redesign.
Do not change the face shape, eye shape, nose, mouth, jawline, forehead mole, hairstyle, clothing, angle, or composition.

Only apply a mild cel-shaded cleanup.
Preserve exact face identity.

Make the linework slightly cleaner,
make the shadow blocks slightly clearer,
make the skin blending slightly less realistic,
make the hair rendering slightly less strand-based.

Do not turn him into a generic handsome anime male lead.
Do not beautify the face.
6.2 表情差分固定前缀
Use the current image as the only base image.

This is an expression variation, not a new character image.
Do not redesign the character.
Do not change the camera angle, head angle, lighting, hairstyle, robe, background, body posture, face shape, eye shape, nose, mouth structure, jawline, forehead mole, or character identity.

Keep the exact same shot, same lighting, same face identity, same hairstyle, same robe, and same background.

Only adjust facial expression muscles very subtly:
eyebrows, eyelids, gaze tension, mouth corners, and slight cheek tension.

Do not beautify the face.
Do not make him softer, younger, prettier, more romantic, or more like a generic handsome male lead.
This must look like the same frame with only the expression changed.

通用负面词：

different person, face redesign, changed angle, changed lighting, changed hairstyle, changed clothing, changed background, changed face shape, changed eye shape, changed nose, changed jawline, generic handsome male lead, romance game male lead, pretty-boy face, over-beautified, larger eyes, glossy lips, different identity
6.3 侧脸补充句
This is a side-profile identity study, not a beautiful side-profile poster.
Keep the same person and the same bone structure.
Do not turn him into a generic elegant side-profile male.
6.4 回头补充句
This is not a romantic looking-back shot.
Do not make him look like a handsome male lead turning back.
Do not make the gaze soft, inviting, or emotionally posed.
6.5 表情目标短语

可在固定前缀后追加：

认真：calm, serious, focused, attentive, clear-headed
疑惑：subtle doubt, questioning, observant, restrained skepticism
微笑：very faint restrained smile, knowing, not warm, not romantic
小得意：subtle smugness, quiet confidence, slight mischief, restrained
委屈：restrained grievance, slight stubbornness, not fragile, not romantic

6.6 阴影过硬修正模板

当轻度赛璐璐化产生脸颊大三角阴影、贴片式阴影或不服从骨相的硬边时，不要继续增加赛璐璐强度，只修阴影形状：

```text
This edit is only for shadow-shape refinement.
Do not change the face, identity, expression, angle, lighting direction, hairstyle, clothing, or composition.

Refine the shadow shapes.
Make cheek shadows natural.
Avoid pasted-on triangular shadows.
Keep every shadow fitted to the face structure.
Do not make the cel shading stronger or harder.
```

6.7 详细表情差分模板

以下内容应接在“表情差分固定前缀”之后使用。每轮只选择一个目标，不要一次生成多个表情。

认真 v1：

```text
Expression target: serious and focused.

Only change the expression slightly:
make the gaze more focused and attentive,
lower the upper eyelids very slightly,
bring the brows slightly closer with mild concentration,
make the mouth flatter and more restrained,
reduce any soft or pretty male-lead feeling.

The expression should feel calm, serious, clear-headed, and observant.
Do not make him angry, gloomy, or villain-like.
Do not change the face structure.
```

认真 v2（只在 v1 识别度不足时使用）：

```text
Expression target: serious v2.

The current result is close, but the serious expression needs to be slightly clearer.
Only adjust the facial expression very subtly:
make the gaze a little more focused and concentrated,
lower the upper eyelids slightly more,
bring the brows slightly closer with mild concentration,
add a little more attentive tension around the eyes,
keep the mouth flat and restrained.

The expression should feel calm, serious, attentive, clear-headed, and observant.
Do not make him angry, gloomy, villain-like, romantic, or soft.
Do not make major changes.
This must still look like the same frame with only a slightly clearer serious expression.
```

认真做到 v2 后应停止；继续加强容易滑向严肃、不悦或阴沉。

疑惑 v1：

```text
Expression target: subtle doubt and questioning.

Only change the expression slightly:
raise one eyebrow very subtly,
make the eyes look more questioning and observant,
add a slight skeptical tension around the eyelids,
keep the mouth closed and restrained,
make the mouth corners slightly tighter.

The expression should feel like quiet doubt, clear-headed questioning, and subtle judgment.
Do not make him cute or childishly confused.
Do not tilt the head or change the face structure.
```

微笑 v1：

```text
Expression target: very faint restrained smile.

Only change the expression slightly:
lift the mouth corners very subtly,
make the smile thin, restrained, and barely visible,
keep the eyes calm, clear-headed, and observant,
do not soften the gaze too much,
keep a slight self-aware feeling.

The expression should feel like a quiet, subtle, knowing smile.
Not warm, romantic, cute, openly happy, or like a gentle male lead.
Do not change the face structure.
```

小得意 v1：

```text
Expression target: subtle smugness.

Only change the expression slightly:
make one corner of the mouth lift just a little,
add a faint self-aware smugness,
make the eyes look calm, clever, and slightly amused,
keep the expression restrained and controlled.

The expression should feel like quiet confidence and slight mischief.
Do not make him evil, arrogant, flirtatious, or villain-like.
Do not make the smile wide or change the face structure.
```

委屈 v1：

```text
Expression target: restrained grievance.

Only change the expression slightly:
lower the gaze just a little,
make the eyelids slightly heavier,
make the mouth corners slightly pressed down,
add a restrained feeling of being wronged,
but keep the expression controlled and self-aware.

The expression should feel like quiet, restrained grievance, with a little stubbornness.
Do not make him cry, soft, cute, childish, fragile, or romantic.
Do not make the eyes watery or change the face structure.
```

表情建议按风险从低到高依次制作：认真、疑惑、微笑、小得意、委屈。表情一旦成立就停止，不追求更强识别度。

6.8 全身基准图通用模板
Use the current locked face identity as the highest-priority identity standard.

This is not a character redesign.
This is the same person expanded into a full-body standard base portrait.

Use lh/lcds/崔东山.png only for clothing structure, robe layers, color arrangement, full-body costume silhouette, and restrained scholar-like costume reference.
Do not use lh/lcds/崔东山.png as a face identity reference.

Keep the same established face identity:
same face shape, same eye shape, same nose, same mouth, same jawline, same forehead mole, same age impression, same restrained temperament.

Create a clean full-body standing base portrait.
Show the entire figure clearly from head to feet.
Use a simple blue-gray background.
Do not make this a cinematic poster or dramatic scene illustration.

Keep the white outer robe and light blue inner garment,
with layered scholar robe structure and wide sleeves,
but reduce the generic handsome male-lead aura, xianxia-prince feeling, and overly luxurious fantasy costume feeling.

The robe should feel restrained, structured, and scholar-like,
not fairy-like, not overly noble, not a costume-drama poster outfit.

Keep the standing pose neutral and natural.
Do not add props.
Hands should be relaxed and natural, partially covered by sleeves if appropriate.

Do not make him prettier, softer, more romantic, more noble, or more elegant.
Do not redesign the face.
Do not turn him into a generic handsome ancient-style male lead.

全身基准图负面词：

face redesign, different person, loss of identity, generic handsome ancient-style male, costume-drama poster hero, elegant xianxia prince, noble refined aura, immortal prince costume, luxurious robe, fantasy robe, overly pristine clothing, delicate decorative patterns, excessive ornaments, fairy-like elegance, overly graceful sleeves, stiff hands, default character-sheet hands, dramatic prop, scroll, cinematic poster, dramatic background, heavy mist, cropped body, cropped feet
6.9 全身基准图安全模板

以后从近景身份图扩展全身，优先用这版：

Use the provided locked close-up identity references as the highest-priority identity standard.

Create a full-body standard base portrait of the same character.
This is not a redesign and not a new character.

Keep the same face identity as much as possible:
same face shape, same eye shape, same nose, same mouth, same jawline, same age impression, same hairstyle direction, and the same small forehead mole if visible.

Show the full body clearly from head to feet.
Use a simple desaturated blue-gray studio background with only a subtle floor shadow.
No scenic background, no cinematic poster, no dramatic clouds, no props.

The pose should be neutral and natural:
standing calmly, relaxed arms, slight natural asymmetry, not heroic, not romantic, not noble-prince-like.

Clothing:
white outer scholar robe over pale icy-blue inner layers,
long wide sleeves,
layered robe panels,
subtle woven trim,
simple waist sash,
a few restrained hanging cords.
The robe should be clean and readable, elegant but restrained.

Character feeling:
slim, youthful, lightly built, scholar-like.
A calm, restrained, slightly aloof presence.
Do not overdo the oddness in the full-body version.

Do not turn him into a generic handsome ancient-style male lead.
Do not turn him into a noble xianxia prince.
Do not make him a romantic game protagonist.
Do not over-beautify the face.
Do not make the robe overly luxurious.
Do not simplify the costume into a plain generic scholar robe.

Style:
semi-realistic to lightly cel-shaded anime illustration,
clean linework,
gentle grouped shadows,
slightly simplified rendering,
but the identity must remain faithful to the close-up references.

全身安全负面词：

new character, different person, changed face, face redesign, changed eyes, sharper gaze, judging gaze, generic handsome ancient-style male lead, romance-game male lead, noble xianxia prince, immortal prince, heroic pose, glamorous elegance, poster composition, cinematic background, dramatic clouds, added props, plain generic scholar robe, over-simplified costume, luxurious robe, ornate prince robe, feminine body, sickly body, exaggerated eccentricity
6.10 错误脸回贴模板

当全身图结构可用、但脸已经跑偏时，不要继续普通微调。
应改成“脸部身份回贴”。

使用前提：

当前全身图只保留身体、服装、构图；
同时提供正确的近景锁脸参考；
明确声明当前脸是错的，不要保留。

模板：

Use the current full-body image only for the body, clothing, pose, composition, and background.

Use the established locked close-up face reference as the only face identity reference.

Replace only the face identity in the current full-body image.
Do not change the body, clothing, hairstyle direction, pose, composition, or background.

The current face is wrong and must not be preserved.
Restore the established locked character face:
same narrow slightly long face,
same restrained eye shape,
same nose and mouth structure,
same jawline,
same forehead mole,
same age impression,
same clear-headed, slightly odd temperament.

Do not redesign the full-body image.
Do not change the costume.
Do not change the pose.
Only correct the face identity.

注意：

如果没有正确近景锁脸图，只靠错误脸底图，基本救不回。

7. 跑偏信号与修正原则
7.1 通用跑偏信号

只要出现以下任意明显情况，就应退回上一张稳定图：

第一眼不像同一个人；
眼睛变成标准动画男主眼；
鼻嘴变成通用零件；
下巴开始理想化、V 脸化；
表情变成漂亮冷淡；
三分之四侧变成回眸美男；
侧脸变成古风侧颜杀；
回头镜头变成恋爱向海报；
表情差分变成新脸；
全身图变成宣传海报；
全身图变成白衣仙侠贵公子；
服装参考图带走脸部身份；
道具让全身图变成剧情图。
7.2 修正原则
脸不像，只修身份；
风格太弱，只动渲染；
阴影太硬，只修阴影形状；
男主感回潮，只压嘴、眼、气质；
过阴，只回一点清醒和自然感；
表情太弱，只轻微加强表情肌肉；
表情太重，回退上一张，不继续加压；
背景太重，只压背景，不动人物；
全身人物太小，只放大人物，不改服装和脸；
服装太贵，只小幅压贵气，不改成破旧；
手部太僵，只修手部自然度，不加道具。
7.3 全身基准图跑偏信号

只要出现以下情况，就要回退，不要继续硬修：

脸型开始变窄、变顺、变美型；
眼型变成冷峻男主眼；
鼻嘴关系变成另一套五官；
眉心红籽消失或变成装饰点；
服装被简化成普通白蓝书生袍；
腰部、垂饰、层次全部消失；
背景变成剧情海报；
人物变成竖版新立绘；
“书卷感”变成文弱；
“古怪感”变成阴沉或邪魅；
“清醒感”变成冷峻男主；
写了 keep same face 但其实是在保留错误脸。

尤其注意：

一旦发现某一版已经变脸，就不能继续在这张图上修。必须回退到脸正确的版本。

8. 验收清单
8.1 通用验收
还是不是同一个人；
脸型有没有变；
眼型有没有变成标准男主眼；
鼻子和嘴有没有变成通用零件；
下颌有没有理想化；
眉心痣或身份特征是否稳定；
表情是否仍克制、清醒；
是否像恋爱游戏可攻略男主头像；
风格是否只是轻度二维整理；
阴影是否贴合脸部骨相。
8.2 三分之四侧验收
是否真的比正面更侧；
是否还没跳成纯侧脸；
鼻梁、嘴、下巴是否仍符合身份；
眼神是否开始“回眸男主化”；
气质是否过阴、过沉、反派化；
是否能作为正面到侧脸之间的桥。
8.3 表情差分验收
镜头有没有变；
光线有没有变；
头部角度有没有变；
发型有没有变；
背景和衣领有没有变；
脸型、眼型、鼻子有没有变；
嘴是不是只在做表情变化，而不是换了结构；
身份有没有跑；
表情是否成立。

如果表情已经成立，就停，不继续追求更强识别度。

8.4 全身基准图验收

全身图定稿前检查：

是否完整显示头到脚；
背景是否干净；
是否没有道具；
是否不是海报；
服装结构是否清楚；
服装是否既不太仙，也不过度简化；
身形是否偏清瘦；
是否仍像同一个角色；
脸部是否没有明显跑偏；
发型大方向是否保留；
站姿是否自然但不英雄化；
是否可以作为后续全身动作差分底图；
是否需要另做同服装半身图来补锁脸。

如果全身图：

服装和比例可用；
脸没有明显跑偏；
背景干净；
站姿可复用；

就可以定稿。

不要为了追求更强的“古怪感”继续修全身。

9. 最终记忆点

以后遇到这类任务，只记住下面这些：

先找最稳的身份底图。
先锁脸，再推风格。
风格只做轻推，不做强转。
正面之后先做三分之四侧桥接。
侧脸和回头都要防“古风男主模板”。
表情差分不是重画角色，只是微调表情肌肉。
全身基准图不是宣传图，而是结构母版。
服装参考只参考衣服，不参考脸。
全身图负责比例和服装，半身图负责脸和表情。
一旦跑偏，立刻回退，不在错误图上硬修。
全身图不要强修眼神。
“清瘦、书卷、古怪”不能写成新角色设定。
一旦变脸，立刻回退，不要在错误脸上继续修。
全身图只要服装、比例、构图稳定，就可以定稿。
古怪感、表情、眼神，放到同服装半身图里解决。
不要为了全身图里的气质，把已经稳定的脸修坏。
最终全身基准图是“可复用结构母版”，不是“最强脸部身份图”。
