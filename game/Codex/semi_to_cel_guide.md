# 半写实身份图转赛璐璐 / 动画风精简流程

## 1. 用途

用于把已锁定身份的半写实角色图转换为轻度赛璐璐风，并继续制作：

- 三分之四侧、侧脸和回头镜头；
- 同镜头表情差分；
- 全身标准基准图与同服装半身图；
- 服装迁移、立绘和剧情 CG。

核心目标：保持角色身份，只改变必要的风格、角度、表情或身体结构。

## 2. 核心原则

- 先保人，再推风格。
- 先稳定正面，再做三分之四侧，最后做侧脸和回头。
- 表情差分只调整表情肌肉，不重画角色。
- 全身图负责比例、服装和站姿；近景或半身图负责脸、眼神和表情。
- 服装参考只负责衣服结构，不负责脸部身份。
- 每轮只解决一个问题，不同时要求更像、更侧、更美、更动画化。
- 一旦身份漂移，立即退回上一张稳定图。

禁止直接使用以下强转换口径：

```text
full anime redesign
strong cel-shaded style
complete 2D animation conversion
```

## 3. 标准流程

### 3.1 锁定身份母版

底图至少应满足：

- 脸型、眉眼、鼻嘴和下颌关系正确；
- 眉心痣等身份特征稳定；
- 年龄、阶层和气质一致；
- 没有滑向通用古风男主或美型模板。

身份未稳定前，不做风格转换、跨角度、表情差分或全身扩展。

### 3.2 轻度风格化

第一次只整理线条、阴影和材质，不重新设计五官。

推荐口径：

```text
mild cel-shaded cleanup
lightly stylized
slightly cleaner linework
slightly clearer shadow blocks
slightly less realistic skin blending
```

### 3.3 跨角度

固定顺序：

1. 正面身份母版；
2. 三分之四侧桥接；
3. 标准侧脸；
4. 回头镜头。

三分之四侧重点检查眉眼、鼻嘴、下巴和下颌连接；侧脸重点检查额头至鼻梁、嘴唇、人中、下巴、耳位和发束方向。

回头镜头应表现观察、判断或警觉，避免恋爱向“美男回眸”。

### 3.4 表情差分

只有当前镜头、角度、身份和光线都稳定后才制作。

允许调整：

- 眉毛；
- 上下眼睑；
- 眼神张力；
- 嘴角；
- 轻微脸颊张力。

禁止改变镜头、光线、头部角度、发型、衣服、背景、脸型和鼻嘴结构。

建议按风险从低到高制作：认真、疑惑、微笑、小得意、委屈。表情成立后立即停止。

### 3.5 全身标准基准图

全身图是可复用结构母版，不是宣传海报。

它主要负责：

- 身高与体型比例；
- 中性站姿；
- 服装层次、袖子、腰封、下摆和鞋子；
- 身体轮廓及后续动作差分基础。

要求：

- 完整显示头到脚，人物占画面高度约 75%–85%；
- 使用简单、低饱和的蓝灰背景；
- 不使用剧情道具、英雄式站姿和大幅飘动衣摆；
- 不加入山水、浓雾或海报式戏剧光；
- 服装保持清楚、克制，既不仙侠奢华，也不简化成普通书生袍。

全身图稳定后，应补做同服装半身或腰上基准图，用于锁脸和表情差分。

## 4. 高风险问题

### 4.1 全身图变脸

全身图中脸部占比变小，模型容易依据服装、站姿和背景重新造人。不要在此阶段强行加入以下眼神或气质词：

```text
observant gaze
clear-headed eyes
quietly judging
harder to read
sharp gaze
intelligent eyes
subtle strange expression
```

安全写法是强调微调整体姿态，而不是重新定义角色：

```text
keep the same character, same face, same costume, same composition;
only make the overall body presence slightly more restrained and scholar-like
```

### 4.2 服装迁移带走身份

服装参考只可提供配色、袍服层次、袖形、腰部结构和全身轮廓。

项目中的示例口径：

```text
Use lh/cds/崔东山.png only for clothing structure and full-body costume reference, not face identity.
```

压低贵气时使用：

```text
less luxurious, less fantasy-like, more restrained scholar clothing
```

不要使用 `old`、`poor`、`dirty`、`rough`、`torn`，以免破坏服装设定。

### 4.3 错误底图无法继续修正

如果某一版已经变脸，`keep the same face` 只会继续保持错误脸。应退回最后一张身份正确的图，或使用正确近景参考执行脸部回贴。

## 5. 常用提示词

### 5.1 轻度赛璐璐转换

```text
Use the current image as the only base image.

This is not a redesign.
Do not change the face shape, eye shape, nose, mouth, jawline,
forehead mole, hairstyle, clothing, angle, or composition.

Only apply a mild cel-shaded cleanup.
Preserve exact face identity.
Make the linework slightly cleaner,
the shadow blocks slightly clearer,
the skin blending slightly less realistic,
and the hair rendering slightly less strand-based.

Do not beautify the face or turn him into a generic handsome anime male lead.
```

### 5.2 表情差分固定前缀

```text
Use the current image as the only base image.

This is an expression variation, not a new character image.
Keep the exact same shot, lighting, face identity, hairstyle, robe,
background, body posture, face shape, eyes, nose, jawline, and forehead mole.

Only adjust facial expression muscles very subtly:
eyebrows, eyelids, gaze tension, mouth corners, and slight cheek tension.

Do not beautify, soften, rejuvenate, or romanticize the character.
This must look like the same frame with only the expression changed.
```

表情目标短语：

- 认真：`calm, serious, focused, attentive, clear-headed`
- 疑惑：`subtle doubt, questioning, observant, restrained skepticism`
- 微笑：`very faint restrained smile, knowing, not warm, not romantic`
- 小得意：`subtle smugness, quiet confidence, slight mischief, restrained`
- 委屈：`restrained grievance, slight stubbornness, not fragile, not romantic`

### 5.3 侧脸与回头补充句

```text
This is a side-profile identity study, not a beautiful side-profile poster.
Keep the same person and the same bone structure.
Do not turn him into a generic elegant side-profile male.
```

```text
This is not a romantic looking-back shot.
Do not make him look like a handsome male lead turning back.
Keep the gaze observant, restrained, and story-driven.
```

### 5.4 阴影形状修正

```text
This edit is only for shadow-shape refinement.
Do not change the face, identity, expression, angle, lighting direction,
hairstyle, clothing, or composition.

Make cheek shadows natural and fitted to the face structure.
Avoid pasted-on triangular shadows.
Do not make the cel shading stronger or harder.
```

### 5.5 全身基准图

```text
Use the locked close-up references as the highest-priority identity standard.
Create a full-body standard base portrait of the same character.
This is not a redesign or a new character.

Keep the same face shape, eyes, nose, mouth, jawline, age impression,
hairstyle direction, and forehead mole if visible.

Show the complete figure from head to feet.
Use a simple desaturated blue-gray studio background and subtle floor shadow.
Use a neutral natural standing pose with relaxed arms.
No scenic background, cinematic poster, dramatic clouds, or props.

Keep the layered white and pale-blue scholar robe readable and restrained.
Do not make it overly luxurious or simplify it into a generic scholar robe.

Use lightly cel-shaded semi-realistic rendering with clean linework
and gentle grouped shadows.
Identity must remain faithful to the close-up references.
```

### 5.6 错误脸回贴

使用当前全身图保存身体、服装、姿势、构图和背景，同时提供正确的近景锁脸参考。

```text
Use the current full-body image only for the body, clothing, pose,
composition, and background.
Use the locked close-up reference as the only face identity reference.

The current face is wrong and must not be preserved.
Replace only the face identity.
Restore the established face shape, eyes, nose, mouth, jawline,
forehead mole, age impression, and restrained temperament.

Do not change the body, costume, pose, composition, or background.
```

没有正确近景参考时，不要继续在错误脸底图上硬修。

### 5.7 通用负面词

```text
different person, new character, face redesign, changed angle,
changed lighting, changed hairstyle, changed clothing, changed background,
generic handsome male lead, romance-game male lead, pretty-boy face,
noble xianxia prince, over-beautified face, larger eyes, glossy lips,
cinematic poster, heroic pose, dramatic background, added props,
cropped body, cropped feet
```

## 6. 跑偏处理

出现以下任一情况，立即退回上一张稳定图：

- 第一眼不像同一个人；
- 眼睛、鼻嘴或下巴变成通用美型零件；
- 三分之四侧或回头变成古风男主镜头；
- 表情差分改变了角度、光线或身份；
- 全身图变成宣传海报或仙侠贵公子；
- 服装参考带走脸部身份；
- 服装被过度简化；
- 道具锁死手势或让画面变成剧情图。

修正时遵守单变量原则：

- 脸不像，只修身份；
- 风格太弱，只动渲染；
- 阴影太硬，只修阴影形状；
- 表情太弱，只微调表情肌肉；
- 背景太重，只压背景；
- 人物太小，只调整人物占比；
- 服装太贵，只轻微压低贵气；
- 手部太僵，只修手部，不加道具。

## 7. 验收清单

### 7.1 身份与风格

- 是否仍是同一个人；
- 脸型、眼型、鼻嘴、下颌和身份特征是否稳定；
- 是否避免通用动画男主、古偶或恋爱游戏脸；
- 风格是否只是轻度二维整理；
- 阴影是否服从骨相。

### 7.2 角度与表情

- 跨角度后骨相是否一致；
- 回头镜头是否避免恋爱向回眸；
- 表情差分是否保持镜头、光线、角度、发型、衣领和背景；
- 嘴部是否只改变表情，没有更换结构；
- 表情成立后是否及时停止。

### 7.3 全身基准图

- 是否完整显示头到脚；
- 人物比例、站姿和服装结构是否清楚；
- 背景是否简单且没有道具；
- 是否避免海报感、英雄感和仙侠贵公子感；
- 脸部是否没有明显漂移；
- 是否可用于后续动作差分；
- 是否配套准备同服装半身图。

## 8. 最终记忆点

先锁脸，再推风格；先做桥接，再跨角度；先锁镜头，再改表情。

全身图负责比例、服装和站姿，半身图负责脸、眼神和表情。

每轮只改一个变量；一旦变脸，立即回退，不在错误底图上继续修。
