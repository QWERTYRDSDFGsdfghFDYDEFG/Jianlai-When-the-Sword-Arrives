# 半写实身份图转赛璐璐 / 动画风的稳定流程文档

## 用途

本文件用于总结并规范：
当已有一张半写实角色身份图，需要转换成赛璐璐 / 二维动画风格时，如何避免角色身份丢失、脸部模板化、风格与身份互相拉扯的问题。

适用于：

* 男性角色肩部以上近景
* 角色脸部身份母版
* 半写实转动画风
* 图生图风格转换
* 局部重绘
* 立绘、表情差分、剧情 CG 的风格统一

---

# 1. 核心问题

这类任务的核心问题不是单纯“画风不对”，而是：

**半写实身份图转赛璐璐时，风格转换会吃掉角色身份。**

具体表现为：

* 一强化赛璐璐 / 动画风，脸就变成通用二次元古风男主；
* 一强化身份锁定，画面又退回半写实；
* 赛璐璐块面推进太强时，脸部阴影会变硬、变突兀；
* 风格推进太弱时，又只是半写实图稍微清理了一下。

一句话概括：

**风格对了，人容易丢；人回来了，风格又容易退。**

---

# 2. 常见初期问题表现

最初从半写实身份图转成赛璐璐风格时，出现了以下问题。

## 2.1 脸部身份丢失

一旦提示词里出现较强的：

```text
anime style
cel-shaded style
2D animation style
```

模型就会优先调用“通用动画美型脸”。

结果是：

* 脸型变成标准动画美型脸；
* 眼睛变成通用二次元男主眼；
* 鼻子和嘴被简化成模板零件；
* 下颌变得过顺、过干净；
* 表情变成“漂亮冷淡”；
* 人物看起来像通用古风动画男主，而不是原来的同一个人。

这类失败可以概括为：

**风格出来了，但人没了。**

---

## 2.2 风格仍然偏半写实

当提示词改成强力锁脸后，模型又会保留半写实身份图的质感。

结果是：

* 皮肤仍然有真实灰阶；
* 鼻梁高光偏写实；
* 嘴唇有真实体积；
* 头发仍然是丝状写实；
* 衣服材质偏真实；
* 画面像半写实数字绘，而不是明确的赛璐璐。

这类问题可以概括为：

**人回来了，但风格又回去了。**

---

# 3. 任务难点

这类任务的真正难点不是“怎么写赛璐璐”，而是：

**如何在不重画脸的前提下做风格转换。**

---

## 3.1 难点一：模型会把“风格转换”理解成“重新设计人物”

图像模型在执行“转成赛璐璐 / 动画风”时，往往不会只改渲染方式，而会顺手改掉：

* 眼型；
* 鼻子；
* 嘴；
* 下巴；
* 脸部比例；
* 头发分组；
* 表情气质。

因此它生成的不是“同一个人换画风”，而是“符合该画风审美的新角色”。

---

## 3.2 难点二：身份参考图本身带有强写实质感

半写实身份图既包含身份信息，也包含渲染方式。

模型在参考它时，会同时吸收：

* 真实皮肤质感；
* 真实鼻梁高光；
* 真实头发丝；
* 半写实光影；
* 厚涂式体积。

所以身份锁得越强，画面越容易被拖回写实。

---

## 3.3 难点三：男性古风角色容易掉进美男模板

该类角色通常有多个高风险元素：

* 白衣；
* 长发；
* 眉心红痣；
* 冷静眼神；
* 肩部以上近景；
* 蓝灰夜景背景；
* 少年 / 青年脸；
* 古风服装。

这些元素一组合，模型很容易自动收敛成：

* 清冷男主；
* 国风美男；
* 恋爱游戏可攻略男主；
* 二次元古风帅哥；
* 素雅版古偶男主。

因此，这不是单纯风格问题，也涉及**男性角色反模板问题**。

---

# 4. 解决思路

最终有效的解决方式不是一步转风格，而是分阶段推进。

总原则：

**先锁身份，再轻度风格化；不能先强转赛璐璐，再试图救脸。**

---

# 5. 解决流程

## 5.1 第一步：确认身份优先级高于风格

首先必须让模型明确：

```text
This is not a redesign.
Do not change the face.
Do not change the face shape, eye shape, nose, mouth, jawline, forehead mole, expression.
```

这一阶段的目标是：

**防止人物变成新角色。**

如果脸已经不对，风格再好也不能保留。

---

## 5.2 第二步：把“强赛璐璐”改成“轻度赛璐璐清理”

不要直接写：

```text
turn it into anime style
make it cel-shaded
convert to full 2D animation style
```

这会让模型进入强风格重绘模式。

更稳定的写法是：

```text
only apply a mild cel-shaded cleanup
do not redesign the face
preserve exact face identity
keep 80% of the current portrait and apply only 20% stylization
```

这一阶段的目标不是“彻底转动画”，而是只做：

* 稍微清理线条；
* 稍微减少写实皮肤；
* 稍微增加块面阴影；
* 稍微减少写实发丝；
* 稍微统一画面。

核心原则：

**不要让风格权重高过身份权重。**

---

## 5.3 第三步：如果脸跑了，立即退回上一张稳定图

如果生成结果已经变成：

* 通用动画男主；
* 标准二次元古风美男；
* 漂亮冷淡男主脸；
* 跟原身份不像的新角色；

不要继续在这张跑偏图上修。

正确做法是退回：

* 最后一张身份稳定的图；
* 或原半写实身份底图。

原则：

**宁可风格弱一点，也不要在错误身份上继续加工。**

---

## 5.4 第四步：如果风格太弱，只动渲染，不动脸

当身份稳定但仍偏半写实时，不要再写“change face”或“make more anime”。

应明确：

```text
This edit is only for rendering style, not for face redesign.
Do not change the face shape, eyes, nose, mouth, jawline, expression, or forehead mole.
Only make the linework cleaner and the shadow blocks slightly clearer.
```

目标是：

* 保留脸；
* 只减写实质感；
* 只推一点二维块面。

---

## 5.5 第五步：如果阴影过硬，只修阴影形状

当赛璐璐块面推进后，可能出现脸颊大三角阴影、贴片式阴影等问题。

此时不要继续写：

```text
more cel-shaded
stronger anime shading
```

否则阴影会更硬。

正确写法是：

```text
refine shadow shapes
make cheek shadows natural
avoid pasted-on triangular shadows
keep shadows fitted to the face structure
```

目标是：

**让赛璐璐块面服从骨相，而不是把脸变成图形拼贴。**

---

## 5.6 第六步：最后只做微调，不再大改

当身份、眉心痣、脸型、眼神、整体气质已经稳定后，进入最后阶段。

此时提示词应变成：

```text
final micro-adjustment
do not make major changes
keep this exact same person
slightly cleaner
slightly flatter
slightly more unified
slightly less semi-realistic
```

最后阶段不追求明显变化，只追求：

* 更统一；
* 更干净；
* 更少一点写实；
* 不破坏身份。

---

# 6. 解决过程中出现的新问题

## 6.1 风格强了，脸会变模板

强赛璐璐化后，容易出现：

* 标准动画美型脸；
* 标准动画眼；
* 标准动画鼻；
* 标准动画嘴；
* 理想化下颌；
* 漂亮冷淡表情。

这说明：

**强风格转换会吞掉身份。**

---

## 6.2 身份强了，风格会退回半写实

当提示词过度强调原脸身份时，模型会带回：

* 半写实皮肤；
* 真实鼻梁高光；
* 真实嘴唇体积；
* 真实发丝；
* 半写实布料。

这说明：

**身份参考越强，写实质感越容易被带回来。**

---

## 6.3 轻赛璐璐推进时，阴影会变硬

当要求更明显块面阴影时，脸颊可能出现：

* 大面积三角阴影；
* 阴影边界过硬；
* 阴影像贴片；
* 阴影不顺脸部骨相。

这说明：

**赛璐璐阴影不是越硬越好，必须符合脸部结构。**

---

## 6.4 最终版本可能不是纯赛璐璐

最终稳定结果通常是：

* 身份稳；
* 眉心痣稳；
* 脸没有跑；
* 有轻度二维整理；
* 但仍保留一点半写实质感。

这不是失败，而是这类任务里较安全的结果。

因为如果继续强推纯赛璐璐，很可能再次回到模板脸。

---

# 7. 推荐的标准工作流

以后遇到类似“半写实身份图转赛璐璐 / 动画风”的问题，按以下顺序处理。

---

## 7.1 先做身份母版

先选一张最像的图作为身份底图。

身份母版必须满足：

* 脸型正确；
* 眉眼关系正确；
* 鼻嘴结构正确；
* 眉心痣 / 身份特征稳定；
* 气质是同一个人；
* 没有明显美男模板化。

身份没稳之前，不做风格转换。

---

## 7.2 再做低强度风格化

第一次风格转换不要追求明显赛璐璐。

使用口径：

```text
mild cel-shaded cleanup
lightly stylized
slightly cleaner linework
slightly clearer shadow blocks
slightly less realistic skin blending
```

不要使用强指令：

```text
full anime redesign
strong cel-shaded style
complete 2D animation conversion
```

---

## 7.3 每一轮只解决一个问题

不要一轮同时要求：

* 更像；
* 更赛璐璐；
* 更好看；
* 更清冷；
* 更反模板；
* 更有气质。

一轮只解决一个问题：

* 脸不像：只修身份；
* 风格太弱：只动渲染；
* 阴影太硬：只修阴影形状；
* 眉心痣淡：只强化眉心痣；
* 嘴太柔：只减嘴唇柔感。

---

## 7.4 跑偏后不要硬救

如果一张图已经变成通用动画男主，不要继续在它上面修。

应立即退回上一张身份稳定图。

判断跑偏的标准：

* 第一眼不像同一个人；
* 眼睛变成标准动画男主眼；
* 鼻嘴变成通用零件；
* 下巴美型化；
* 表情变成漂亮冷淡；
* 裁成头像后像恋爱游戏男主头像。

只要这些明显成立，就不要继续用该图作为底图。

---

# 8. 推荐提示词结构

以后可使用以下结构作为基础模板。

```text
Use the current image as the only base image.

Do not redesign the character.
Do not change the face shape, eye shape, nose, mouth, jawline, forehead mole, hairstyle, clothing, angle, or composition.

This is only a mild style cleanup, not a full anime redesign.

Keep the exact same face identity.
Only adjust the rendering:
cleaner linework,
slightly clearer shadow blocks,
slightly flatter color transitions,
slightly less realistic skin blending,
slightly less realistic hair detail.

Preserve 80% of the current portrait and apply only 20% stylization.

Do not turn him into a generic anime male lead.
Do not make him prettier, softer, younger, or more romantic.
```

---

# 9. 当风格仍偏写实时的提示词

```text
Use the current image as the only base image.

Do not change the face identity, face shape, eyes, nose, mouth, jawline, expression, forehead mole, hairstyle, clothing, angle, or composition.

This edit is only for rendering style, not for face redesign.

Only push the rendering slightly further toward clean 2D cel-shaded animation:
cleaner linework,
clearer shadow boundaries,
more defined shadow blocks,
slightly flatter skin color transitions,
less painterly blending,
less realistic skin texture,
less realistic hair-strand rendering.

Preserve about 85% of the current face identity and structure.
Apply only about 15% additional cel-shaded stylization.

The final image should look like the same portrait, with the same person and same mood, but with slightly cleaner 2D animation-style linework and more visible cel-shaded block shadows.
```

---

# 10. 当阴影过硬时的提示词

```text
Use the current image as the only base image.

Do not change the face identity, face shape, eye shape, nose, mouth, jawline, forehead mole, hairstyle, clothing, angle, or composition.

Keep the current mild cel-shaded style, but refine the shadow shapes.

The large hard triangular shadow on the cheek is too unnatural and too graphic.
Make the facial shadow blocks more natural and better fitted to the cheekbone and face structure.
Keep cel-shaded shadow boundaries, but make them less oversized, less triangular, and less pasted-on.

Unify the rendering style:
reduce the overly realistic nose highlight slightly,
keep cleaner 2D shadow blocks,
but do not add heavy painterly blending.

Preserve the same person and same expression.
Do not beautify the face.
Do not make the eyes larger, softer, prettier, or more anime-standard.
Do not redesign the face into a generic anime male lead.
```

---

# 11. 最后一轮微调用提示词

```text
Use the current image as the only base image.

Do not redesign the character.
Do not change the face shape, eye shape, eyebrow-eye relationship, nose structure, mouth shape, jawline, forehead mole, hairstyle direction, clothing structure, camera angle, or composition.

Keep this exact same person and this exact same identity.

This is only a final micro-adjustment.
Do not make major changes.
Do not restyle the image aggressively.

Keep the current mild cel-shaded / lightly stylized look, but refine it slightly:

- reduce realism only a little more
- keep the same facial structure and expression
- make the rendering slightly cleaner and more unified
- make the shadow shapes slightly cleaner and more consistent
- keep the face shadows natural and fitted to the facial structure
- slightly reduce overly soft skin blending
- slightly reduce realistic hair-strand detail
- keep hair grouped a little more cleanly, but do not change the hairstyle
- slightly simplify the robe shading and keep the folds clean
- keep the blue-gray background soft and simple

Do not beautify the face.
Do not make him prettier, softer, younger, or more romantic.
Do not turn him into a generic anime male lead.
Do not enlarge the eyes.
Do not sharpen the jaw into a V-line.
Do not change the nose into a standard anime nose.
Do not change the mouth into a pretty anime male mouth.

Keep the current restrained, calm, slightly heavy expression.
Keep the small forehead mole clear and stable.

The final result should look almost the same as the current image, with only a very small final cleanup:
slightly cleaner,
slightly flatter,
slightly more unified,
slightly less semi-realistic,
but still clearly the same portrait and the same person.
```

---

# 12. 通用负面词

```text
face redesign, different person, generic anime male lead, handsome anime protagonist, romance game male lead, pretty-boy face, idealized anime face, sharp V-line jaw, larger eyes, prettier face, softer face, younger face, romantic expression, standard anime nose, standard anime mouth, over-stylized cel shading, full anime redesign, loss of identity, exaggerated shadow blocks, pasted-on cheek shadow, harsh unnatural face shadow, painterly realism, realistic skin texture, realistic hair rendering
```

---

# 13. 验收标准

生成后按以下顺序验收：

1. 是否还是同一个人；
2. 脸型有没有变；
3. 眼型有没有变成标准动画男主眼；
4. 鼻子和嘴有没有变成通用动画零件；
5. 下颌有没有变成理想化 V 脸；
6. 眉心痣是否清楚稳定；
7. 表情是否仍然克制、沉、清醒；
8. 是否变成恋爱游戏可攻略男主头像；
9. 风格是否有轻度二维整理；
10. 阴影是否自然贴合脸部骨相。

如果第 1 项失败，整张失败。
如果第 2 到第 6 项里有两项明显失败，应退回上一张稳定图。
如果只是风格不够强，可以继续低强度微调。
如果只是阴影不自然，只修阴影，不动脸。

---

# 14. 通用经验总结

这套流程说明：

**强赛璐璐会吃身份；强锁脸会回写实；正确做法是低强度、多轮微调，只动渲染，不动五官。**

以后遇到类似问题，不要一步到位转画风。

正确路线是：

1. 先找一张身份最稳的底图；
2. 锁住脸型、五官、眉心痣和神态；
3. 只做轻度赛璐璐清理；
4. 每轮只解决一个问题；
5. 跑偏就退回，不在错误图上硬修；
6. 最后阶段只做微调，不再大改。

一句话总原则：

**不是先转风格再救脸，而是先锁脸，再一点点推风格。**
