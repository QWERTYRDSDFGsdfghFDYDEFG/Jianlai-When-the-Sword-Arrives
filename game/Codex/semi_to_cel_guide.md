# 半写实身份图转赛璐璐 / 动画风精简流程

## 用途

本文件用于处理这类任务：

* 已有半写实角色身份图
* 需要转为轻度赛璐璐 / 动画风
* 需要继续扩展为三分之四侧、侧脸、回头镜头
* 需要在同镜头下做表情差分
* 需要从脸部 / 半身身份图扩展为全身基准图
* 需要迁移指定服装参考，但不让服装参考带走脸部身份

适用范围：

* 男性角色肩部以上近景
* 角色脸部身份母版
* 图生图风格转换
* 局部重绘
* 三分之四侧、侧脸、回头镜头
* 同镜头表情差分
* 全身标准基准图
* 服装迁移
* 立绘、表情差分、剧情 CG 的风格统一

---

# 1. 核心问题

这类任务的核心矛盾有四条：

1. 风格一推强，角色身份容易丢，脸会滑向通用古风男主。
2. 身份一锁太死，画面又会退回半写实。
3. 角度或表情一变化，模型就容易把“同一个人”重建成“新的一张脸”。
4. 从近景扩展到全身时，服装、站姿、背景会重新触发“白衣仙侠贵公子 / 古风男主立绘”模板。

一句话总括：

**先保人，再推风格；先做桥接，再推角度；先锁镜头，再改表情；先定全身结构，再谈成图美感。**

---

# 2. 总原则

* 先锁身份，再轻度风格化。
* 先稳定正面，再做三分之四侧桥接，再做侧脸和回头。
* 表情差分不是重画角色，只能在同一帧里微调表情肌肉。
* 全身基准图不是宣传海报，而是后续差分的结构母版。
* 服装参考只负责衣服结构，不负责脸部身份。
* 每一轮只解决一个问题，不同时要求“更像、更侧、更赛璐璐、更好看、更全身、更有气质”。
* 只要跑偏，就退回上一张稳定图，不在错误底图上硬修。

不要做的事：

* 不要一上来就写 `full anime redesign`、`strong cel-shaded style`
* 不要从正面直接跳纯侧脸或回头
* 不要一次批量做多个表情
* 不要用“开心、委屈、微笑”这类宽词让模型自由发挥
* 不要把全身图做成剧情海报 / 宣传立绘
* 不要让服装参考图同时影响脸、气质和身份
* 不要在全身基准图阶段加入卷轴、剑、扇子、书本等剧情道具

---

# 3. 标准流程

## 3.1 先做身份母版

先选一张最像、最稳的底图，要求至少满足：

* 脸型对
* 眉眼关系对
* 鼻嘴结构对
* 眉心痣或身份特征稳定
* 气质是同一个人
* 没有明显美男模板化

身份没稳之前：

* 不做风格转换
* 不做跨角度
* 不做表情差分
* 不做全身服装迁移

---

## 3.2 再做低强度风格化

第一次风格转换只做轻度整理，不追求一步到位。

推荐口径：

```text
mild cel-shaded cleanup
lightly stylized
slightly cleaner linework
slightly clearer shadow blocks
slightly less realistic skin blending
```

避免口径：

```text
full anime redesign
strong cel-shaded style
complete 2D animation conversion
```

目标不是彻底改脸，而是：

* 线条更干净
* 阴影块面更明确一点
* 皮肤和发丝少一点写实感
* 整体更统一

---

## 3.3 正面稳定后，先做三分之四侧桥接

三分之四侧不是终点，而是正面到侧脸之间的桥。

它主要验证：

* 转角度后还是不是同一个人
* 眉眼关系是否还在
* 鼻梁、嘴、人中、下巴是否开始漂
* 眼神会不会滑向“回眸男主”
* 下颌和脖颈连接是否仍符合身份

三分之四侧的目标不是“越侧越好”，而是：

**角度够用，身份稳定，男主感不过量，气质不阴沉。**

---

## 3.4 再做标准侧脸

侧脸阶段重点不是好看，而是骨相一致。

必须重点看：

* 额头到鼻梁的线
* 鼻梁长度和鼻头结构
* 人中和嘴唇厚薄
* 下巴收束
* 下颌到脖颈连接
* 耳朵位置
* 发束方向

注意：

* 眉心痣在侧脸可能弱化或不可见，这不一定是错
* 但不能被乱改成额饰、花钿或新装饰

---

## 3.5 再做回头镜头

回头镜头必须放在侧脸之后。

这一阶段最容易跑偏成：

* 回眸美男
* 温柔男主
* 恋爱向镜头
* 仙气海报

目标应该是：

* 有剧情状态
* 有观察或判断
* 有警觉或回望动作
* 不是“给观众看的美男回眸”

---

## 3.6 当前镜头稳定后，再做表情差分

表情差分的前提：

* 当前镜头可留
* 当前角度可留
* 当前身份可留
* 当前光线可留
* 当前气质可留

表情差分只能做：

* 眉毛
* 上下眼睑
* 眼神张力
* 嘴角
* 轻微脸颊张力

不要改：

* 镜头
* 光线
* 头部角度
* 发型
* 衣服
* 背景
* 脸型
* 鼻嘴结构

推荐顺序：

1. 认真
2. 疑惑
3. 微笑
4. 小得意
5. 委屈

原因很简单：越往后越容易男主化、幼态化或恋爱向。

---

## 3.7 再做全身标准基准图

全身阶段的目标不是“做一张好看的宣传图”，而是：

**把已经锁住身份的同一个人，扩展成可复用的全身结构母版。**

全身基准图主要解决：

* 全身比例
* 站姿
* 服装结构
* 袖子、腰封、下摆、鞋子
* 身体轮廓
* 后续动作差分底图

全身基准图不适合单独承担：

* 脸部锁定
* 表情差分
* 眼神差分
* 眉心痣最终判断

所以全身图稳定后，必须配套做：

**同服装半身 / 腰上基准图。**

推荐顺序：

```text
近景锁脸图
→ 轻度风格化
→ 三分之四侧桥接
→ 表情差分验证
→ 全身标准基准图
→ 同服装半身基准图
→ 全身动作差分
→ 半身表情差分
```

---

# 4. 全身基准图原则

## 4.1 明确参考图职责

服装参考图只负责：

* 服装结构
* 袍子层次
* 配色
* 长袍轮廓
* 袖子形状
* 全身服装比例

服装参考图不负责：

* 脸部身份
* 五官比例
* 表情
* 年龄感
* 眼神气质
* 人物性格

核心句：

```text
Use lh/lcds/崔东山.png only for clothing structure and full-body costume reference, not face identity.
```

---

## 4.2 全身基准图不是宣传海报

全身基准图要避免：

* 山水夜景抢戏
* 大雾气
* 电影感光影
* 英雄式站姿
* 仙侠海报气氛
* 剧情道具
* 大风吹衣摆
* 夸张袖摆

全身基准图应该：

* 背景简单
* 全身完整
* 站姿中性
* 服装结构清楚
* 人物占比适中
* 不带剧情动作
* 不用道具固定手部姿势

核心句：

```text
This is a reusable full-body standard character base image, not a cinematic poster.
```

---

## 4.3 人物大小

全身图里人物不能太小。

经验值：

**全身完整入画，但人物尽量占画面高度的 75%–85%。**

人物太小会导致：

* 脸部身份弱
* 眉心痣不清楚
* 眼型嘴型难判断
* 后续差分不稳

人物太大又容易：

* 裁头
* 裁脚
* 裁衣摆
* 丢失全身结构

---

## 4.4 背景要压干净

全身基准图背景最好是：

* 简单蓝灰
* 轻微纹理
* 不抢戏
* 不要山水
* 不要浓雾
* 不要剧情场景
* 不要海报光

背景越复杂，模型越容易把它当成剧情图。

---

## 4.5 服装贵气只能小幅压

服装迁移时常见问题是：

* 白衣太干净
* 袍边纹样太精细
* 腰饰太贵
* 垂饰太漂亮
* 袖子太仙
* 整体像白衣仙侠贵公子

正确修法是：

```text
less luxurious, less fantasy-like, more restrained scholar clothing
```

不要写成：

```text
old, poor, dirty, rough, torn
```

因为这样会破坏服装设定。

目标不是把衣服改破旧，而是：

**保留白衣层次和读书人结构，减少仙侠门派公子感。**

---

## 4.6 道具先不要加

全身基准图阶段不要加：

* 卷轴
* 扇子
* 剑
* 书
* 法器
* 手势动作

道具会导致：

* 固定手部姿态
* 画面变成剧情图
* 后续差分困难
* 手部动作被锁死

先做干净母版，后面再做道具差分。

---

# 5. 常用提示词模板

## 5.1 轻度赛璐璐模板

```text
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
```

---

## 5.2 表情差分固定前缀

```text
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
```

可配合的通用负面词：

```text
different person, face redesign, changed angle, changed lighting, changed hairstyle, changed clothing, changed background, changed face shape, changed eye shape, changed nose, changed jawline, generic handsome male lead, romance game male lead, pretty-boy face, over-beautified, larger eyes, glossy lips, different identity
```

---

## 5.3 侧脸补充句

```text
This is a side-profile identity study, not a beautiful side-profile poster.
Keep the same person and the same bone structure.
Do not turn him into a generic elegant side-profile male.
```

---

## 5.4 回头补充句

```text
This is not a romantic looking-back shot.
Do not make him look like a handsome male lead turning back.
Do not make the gaze soft, inviting, or emotionally posed.
```

---

## 5.5 表情目标短语

可在固定前缀后追加：

* 认真：`calm, serious, focused, attentive, clear-headed`
* 疑惑：`subtle doubt, questioning, observant, restrained skepticism`
* 微笑：`very faint restrained smile, knowing, not warm, not romantic`
* 小得意：`subtle smugness, quiet confidence, slight mischief, restrained`
* 委屈：`restrained grievance, slight stubbornness, not fragile, not romantic`

---

## 5.6 全身基准图模板

```text
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
```

全身基准图负面词：

```text
face redesign, different person, loss of identity, generic handsome ancient-style male, costume-drama poster hero, elegant xianxia prince, noble refined aura, immortal prince costume, luxurious robe, fantasy robe, overly pristine clothing, delicate decorative patterns, excessive ornaments, fairy-like elegance, overly graceful sleeves, stiff hands, default character-sheet hands, dramatic prop, scroll, cinematic poster, dramatic background, heavy mist, cropped body, cropped feet
```

---

# 6. 跑偏信号

只要出现以下任意明显情况，就应退回上一张稳定图：

* 第一眼不像同一个人
* 眼睛变成标准动画男主眼
* 鼻嘴变成通用零件
* 下巴开始理想化、V 脸化
* 表情变成漂亮冷淡
* 三分之四侧变成回眸美男
* 侧脸变成古风侧颜杀
* 回头镜头变成恋爱向海报
* 表情差分变成新脸
* 全身图变成宣传海报
* 全身图变成白衣仙侠贵公子
* 服装参考图带走脸部身份
* 道具让全身图变成剧情图

修正原则：

* 脸不像，只修身份
* 风格太弱，只动渲染
* 阴影太硬，只修阴影形状
* 男主感回潮，只压嘴、眼、气质
* 过阴，只回一点清醒和自然感
* 表情太弱，只轻微加强表情肌肉
* 表情太重，回退上一张，不继续加压
* 背景太重，只压背景，不动人物
* 全身人物太小，只放大人物，不改服装和脸
* 服装太贵，只小幅压贵气，不改成破旧
* 手部太僵，只修手部自然度，不加道具

---

# 7. 验收清单

## 7.1 通用验收

* 还是不是同一个人
* 脸型有没有变
* 眼型有没有变成标准男主眼
* 鼻子和嘴有没有变成通用零件
* 下颌有没有理想化
* 眉心痣或身份特征是否稳定
* 表情是否仍克制、清醒
* 是否像恋爱游戏可攻略男主头像
* 风格是否只是轻度二维整理
* 阴影是否贴合脸部骨相

---

## 7.2 三分之四侧验收

* 是否真的比正面更侧
* 是否还没跳成纯侧脸
* 鼻梁、嘴、下巴是否仍符合身份
* 眼神是否开始“回眸男主化”
* 气质是否过阴、过沉、反派化
* 是否能作为正面到侧脸之间的桥

---

## 7.3 表情差分验收

* 镜头有没有变
* 光线有没有变
* 头部角度有没有变
* 发型有没有变
* 背景和衣领有没有变
* 脸型、眼型、鼻子有没有变
* 嘴是不是只在做表情变化，而不是换了结构
* 身份有没有跑
* 表情是否成立

如果表情已经成立，就停，不继续追求更强识别度。

---

## 7.4 全身基准图验收

* 全身是否完整入画
* 人物是否占画面高度约 75%–85%
* 背景是否简单、不抢戏
* 是否像基准图，而不是剧情海报
* 是否去掉了不必要道具
* 服装结构是否清楚
* 服装是否仍符合参考结构
* 服装是否过贵、过仙、过华丽
* 手部是否自然
* 脸部身份是否至少没有明显跑偏
* 是否需要另做同服装半身图来补锁脸

---

# 8. 最终记忆点

以后遇到这类任务，只记住下面十句：

1. 先找最稳的身份底图。
2. 先锁脸，再推风格。
3. 风格只做轻推，不做强转。
4. 正面之后先做三分之四侧桥接。
5. 侧脸和回头都要防“古风男主模板”。
6. 表情差分不是重画角色，只是微调表情肌肉。
7. 全身基准图不是宣传图，而是结构母版。
8. 服装参考只参考衣服，不参考脸。
9. 全身图负责比例和服装，半身图负责脸和表情。
10. 一旦跑偏，立刻回退，不在错误图上硬修。
