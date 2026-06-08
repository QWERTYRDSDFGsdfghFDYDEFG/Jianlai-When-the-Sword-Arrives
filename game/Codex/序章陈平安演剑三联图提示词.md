# 序章陈平安演剑三联图提示词

用途：专门用于序章三张关键图的出图提示词准备，不直接出图。

适用场次：

- 序-10 陈平安踏湖现身
- 序-11 陈平安演剑上段
- 序-12 陈平安演剑下段

---

## 1. 这组三联图的特别口径

这三张图不是陈平安日常行路立绘，也不是书简湖日常版。

它们属于原脚本明文指定的序章演出特例，服装必须服从 `script.rpy` 原文：

- 一抹雪白身影
- 一身金醴法袍飘荡不已
- 如一位白衣仙人站在幽幽镜面
- 不背负那把剑仙
- 腰间挂一只养剑葫
- 长剑由崔东山临时取出

结论：

- 脸部身份继续严格锁定 `cpa_face_standard_01`
- 但服装不能使用 `cpa_outfit_variant_06_warm_weather`
- 本组三联图改用“金醴法袍白衣版”作为场景特例服装

---

## 2. 共用硬约束

以下约束三张图都必须一起带上：

```text
1920x1080, horizontal composition, visual novel key art, anime-style CG, clean linework, cel shading, low saturation, restrained color design, cinematic but not photorealistic.

Strictly lock Chen Ping'an's face identity to cpa_face_standard_01: slim long young male face, stable facial bone structure, stable proportions of eyebrows, eyes, nose and mouth, age 20-22, calm, reliable, self-controlled, resilient, not boyish, not old, not idol-like.

This is the prologue special costume version, not the warm-weather travel outfit. He must wear a white Jinli robe with subtle dignified texture, flowing robe hem and sleeves, the overall impression of a white-robed immortal standing on the dark lake surface. Keep only one single vermilion sword-nourishing gourd at the waist. Do not carry the bamboo book box. Do not carry the sword on his back before the sword is drawn.

The lake worldbuilding must stay unified across all three images: night lake, dark mirror-like water surface, distant mountain silhouette, faint cold moonlight, restrained golden spiritual energy, same lighting direction, same robe logic, same face identity.
```

---

## 3. 共用负面约束

```text
Do not redesign the face, do not make the jaw wider, do not make the eyes bigger, do not make him younger, do not make him older, do not turn him into an idol-style pretty male lead, do not add makeup, do not make him flirtatious, demonic, overly elegant, or aristocratic.

Do not use the warm-weather travel outfit, do not add the bamboo book box, do not add a back-carried sword, do not add a second gourd, do not change the gourd into a bottle or ornament, do not add luxurious gold accessories, do not make the robe into exaggerated xianxia streamer costume, do not overdecorate.

Do not make the environment too busy, do not let the background overpower the character, do not switch to photorealism, do not switch to thick painting, do not make it look like a random fantasy male instead of Chen Ping'an.
```

---

## 4. 场次 序-10 提示词

对应图名：`bg prologue_cpa_arrival`

### 中文主提示词

```text
陈平安从东华山顶一掠而来，落在夜色湖面之上，作为序章“送别表演”的核心亮相画面。画面是中近景的英雄登场 key art，人物位于中前方，脚下是幽幽如镜的湖面，远处山影低压，夜色深而不脏。陈平安必须严格保持 cpa_face_standard_01 的固定脸部身份：20-22 岁青年，窄长脸，五官比例稳定，沉静、可靠、自持、坚韧，带一点收着的少年意气。

本图服装不是日常行路装，而是原文明确指定的金醴法袍白衣版：白色法袍，袍摆与长袖在夜风中扬起，质地有克制而贵重的法袍感，但不能华丽浮夸，整体第一眼像“白衣仙人立于幽幽镜面”。他不背剑仙，不背青竹书箱，腰间只挂一个朱红养剑葫。长剑尚未完全进入主动作，可以表现为即将接剑、将要出剑的前一瞬。崔东山如需出现，只能作为弱辅助，不能抢主视觉。

整体是《剑来》气质的视觉小说主视觉：克制、清冷、稳、亮相感强，夜湖压暗，人物提亮，白衣与黑湖形成明确对照，少量金色灵气只作点缀。纯动画风格，赛璐璐分色，线条干净，1920x1080 横版。
```

### 英文压缩提示词

```text
Chen Ping'an lands on the dark mirror-like lake at night after leaping from Donghua mountain, prologue hero entrance key art, medium-close shot, centered foreground figure, distant mountain silhouette, restrained moonlit night lake. Strictly keep cpa_face_standard_01 identity: slim long young male face, stable features, age 20-22, calm, reliable, self-controlled, resilient, slight youthful spirit.

He wears the prologue special white Jinli robe, not the travel outfit: flowing white ceremonial robe with restrained noble texture, sleeves and robe hem moving in the wind, the overall impression of a white-robed immortal standing on a dark lake. No bamboo book box, no sword on the back, only one vermilion sword gourd at the waist. Sword action is about to begin, not full swing yet. Cui Dongshan may appear only as minor support. Anime visual novel key art, cel shading, clean linework, 1920x1080.
```

---

## 5. 场次 序-11 提示词

对应图名：`bg prologue_cpa_sword_01`

### 中文主提示词

```text
陈平安在夜湖之上持剑演出第一段高潮，对应“我偏要逆流而上，撞一撞那南墙”的昂扬段落。画面为近景主视觉，陈平安位于中前偏左，剑势已经展开，但还不是最终高潮，重点是第一波气势被真正拉开。人物必须继续严格锁定 cpa_face_standard_01 的固定脸部身份：窄长脸，五官关系不变，20-22 岁，沉静底色里生出明亮、昂扬、向上的锋芒，但不能变成热血少年漫男主。

服装必须完整延续上一张同一套金醴法袍白衣版，不能换装，不能回到暖天行路装。白色法袍在挥剑动作中拉出清晰动线，袖摆、袍摆与剑势共同形成由左向右或由下向上的推进感。腰间仍只保留一个朱红养剑葫，不带书箱，不背剑。湖面仍是同一片夜湖，同一套冷色月光与轻微金色灵气，画面更近、更有呼吸感，但世界观不能变化。

整体应是“主角讲理 + 演剑”的视觉小说演出图，克制中见昂扬，清楚、好读、可直接承担长台词，不做花哨特效堆叠。纯动画风格，赛璐璐分色，线条干净，1920x1080 横版。
```

### 英文压缩提示词

```text
Chen Ping'an performs the first rising sword movement on the night lake, corresponding to “I will go against the current and crash into that wall”, close-up key visual, figure slightly left of center, sword force unfolding but not yet the final climax. Strictly keep cpa_face_standard_01 identity: slim long young face, unchanged proportions, age 20-22, calm core with bright upward determination, not shonen-hotblooded.

Keep the exact same white Jinli robe from the previous image, not the travel outfit. The robe sleeves and hem must follow the sword motion and create a clear dynamic line. One vermilion sword gourd at the waist only, no bamboo book box, no sword on the back. Same night lake, same cold moonlit lighting, slight restrained golden spiritual energy. Anime visual novel CG, cel shading, clean linework, 1920x1080.
```

---

## 6. 场次 序-12 提示词

对应图名：`bg prologue_cpa_sword_02`

### 中文主提示词

```text
陈平安在同一片夜湖上把演剑推到顶点，对应“书中自有剑仙意”后的高潮收束。画面为中近景到半特写，构图比上一张更开、更高一点，陈平安仍是绝对主体，剑气与人物气势一起向上抬起，形成真正的收顶感。人物必须继续严格保持 cpa_face_standard_01 的固定脸部身份：窄长脸、稳定五官、20-22 岁、沉静可靠、自持坚韧；这张可以更开阔、更风流一点，但绝不能变成轻佻、妖俊或古偶男主。

服装继续锁定同一套金醴法袍白衣版，整组三联图要看起来像同一段连续演出。白色法袍在更开的构图里形成向上扬起的轮廓，和剑势共同完成第二层高潮。仍然不背剑，不带书箱，只保留单个朱红养剑葫。夜湖、山影、月光方向、灵气逻辑、白衣与黑湖对照关系都必须与前两张一致，只是这一张更开、更亮一点。

整体是《剑来》序章高潮收束图：不是炫技，不是玄幻海报堆料，而是一个真正能把“白衣仙人立湖面、演剑成势”压住的视觉小说主视觉。纯动画风格，赛璐璐分色，线条干净，1920x1080 横版。
```

### 英文压缩提示词

```text
Chen Ping'an pushes the sword performance on the same night lake to its peak, the closing climax after “there is sword-immortal intent in the book”, medium-close to half-close key visual, slightly higher and more open composition than the previous image, upward sword force and upward character momentum. Strictly preserve cpa_face_standard_01 identity: slim long face, stable features, age 20-22, calm, reliable, self-controlled, resilient; slightly more open and graceful, but never flirtatious or idol-like.

Keep the same white Jinli robe as a continuous three-panel sequence. The robe silhouette rises with the sword motion to complete the second climax. No sword on the back, no bamboo book box, only one vermilion sword gourd. Same night lake, same mountain silhouette, same moonlight direction, same restrained spiritual energy logic, just more open and slightly brighter. Anime visual novel key art, cel shading, clean linework, 1920x1080.
```

---

## 7. 使用建议

- 真正出图时，先贴“共用硬约束”。
- 再贴对应场次的主提示词。
- 最后补“共用负面约束”。
- 三张图应视为连续三联图生成，不要分别当成互不相关的单图。

如果后续要正式把这套白衣法袍版纳入陈平安标准体系，建议再单独建立一个文档，例如：

- `lh/cpa/CPA_PROLOGUE_SWORD_ROBE_STANDARD.md`

这样以后序章再重做时，就不会再和日常暖天行路装打架。
