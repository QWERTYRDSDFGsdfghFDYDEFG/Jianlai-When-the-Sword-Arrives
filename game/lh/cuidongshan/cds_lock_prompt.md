# 崔东山锁脸专用最终提示词模板

适用对象：崔东山后续全部立绘、半身像、场景状态图、双人同场图、动作差分图。

唯一身份锚点：

- `lh/cuidongshan/cuidongshan_face_locked_identity_sheet_02.png`

配套参考：

- `lh/cuidongshan/CUIDONGSHAN_FACE_IDENTITY_STANDARD.md`
- `lh/cuidongshan/cds_face_test.md`

---

## 1. 先记住一条总规则

后续所有崔东山出图，不要再把任务写成：

- “生成一个崔东山风格角色”
- “画一个白衣少年谋士”

必须写成：

- “基于已提供母版图，保持同一人物身份，只改变场景 / 表情 / 动作 / 视线”

一句话口径：

`这不是重新设计角色，而是让同一个崔东山进入不同场景。`

---

## 2. 必须锁死的身份项

每次都要明确写进提示词的固定项：

- 男性
- 黑色长发
- 长发半束 / 半挽高髻
- 眉心有小而凝的红籽
- 窄长收束的年轻脸型
- 偏收、略长、不圆不甜的眼睛
- 细直鼻梁
- 偏薄嘴唇
- 白色外袍
- 淡青蓝内衫
- 修长、轻、不壮的读书人体态
- 手持卷轴或保留卷轴口径
- 外轻内重、清醒克制、孤独深情

---

## 3. 最终通用主模板

适合大多数单人图。

```text
Use case: identity-preserve
Asset type: visual novel character or scene art
Primary request: Starting from the provided reference image of Cui Dongshan shown in the conversation, create a new scene while preserving the exact same character identity.
Input images: Image 1 is the reference image and identity anchor for Cui Dongshan. Preserve the exact same person.
Scene/backdrop: 【填写场景】
Subject: Cui Dongshan from the reference image, male, same face, same black half-tied long hair, same small red brow mark, same white outer robe and pale blue inner robe, same slim scholar body proportions, holding a scroll or keeping the same scholar-like hand logic
Style/medium: match the reference image's semi-realistic Chinese illustration style, restrained, human, not glamorous
Composition/framing: 1920x1080 landscape, 【填写景别和构图】, single-character scene unless otherwise specified, no duplicate faces
Lighting/mood: 【填写光线与情绪】
Color palette: low saturation, restrained Song-dynasty-inspired Eastern fantasy palette, white and pale blue for Cui Dongshan
Materials/textures: believable cloth, natural hair, real paper/wood/stone/water textures depending on the scene
Constraints: keep Cui Dongshan exactly male and identical to the reference image; preserve the exact face shape, eye shape, nose, mouth, brow mark, hairstyle silhouette, clothing silhouette, body proportions, and restrained temperament; do not redesign him; only change scene, expression, action, gaze direction, and shot distance; his eyes must still feel intelligent, observant, and carrying weight, not empty and not softened into a sweet male lead.
Avoid: female character, red hair, glamorous costume, exposed legs, jewelry, high heels, face collage, duplicate heads, round face, wide jaw, mature male lead face, noble prince face, big sweet eyes, thick lips, idol styling, xianxia game style, standard costume-drama pretty-boy face, ornate crown, luxury clothing, redesigning features, generic handsome-face beautification.
No text, no watermark.
```

---

## 4. 单人图推荐写法

这是最稳的版本，优先级最高。

### 4.1 单人立绘 / 半身图

把这几项替换进去：

- `【填写场景】`：plain warm off-white background / quiet interior study / lakeside at night / academy courtyard
- `【填写景别和构图】`：full-body portrait with generous empty space / medium shot for VN dialogue / half-body with stable framing
- `【填写光线与情绪】`：soft even light, calm and restrained / quiet lamplight, thoughtful / cool moonlit night, restrained sadness

最稳附加句：

```text
Single-character scene only. Do not add any second figure.
```

---

## 5. 双人图推荐写法

双人图最容易串味，所以必须把崔东山写成主角色，把另一人写成次级配角。

```text
Use case: identity-preserve
Asset type: visual novel two-character scene art
Primary request: Starting from the provided reference image of Cui Dongshan shown in the conversation, create a two-character scene while preserving the exact same character identity for Cui Dongshan.
Input images: Image 1 is the reference image and identity anchor for Cui Dongshan. Preserve the exact same person.
Scene/backdrop: 【填写场景】
Subject: Cui Dongshan from the reference image, male, same face, same black half-tied long hair, same small red brow mark, same white outer robe and pale blue inner robe, same slim scholar body proportions, holding a scroll or keeping the same scholar-like hand logic, positioned on the right side of the composition. 【另一角色名字】 may appear on the left as a clearly secondary figure in plain traditional clothing, smaller in visual weight.
Style/medium: match the reference image's semi-realistic Chinese illustration style, restrained, human, not glamorous
Composition/framing: 1920x1080 landscape, stable two-character VN composition, Cui Dongshan is the identity focus, the second character is smaller and secondary, no extra figures, no duplicate faces, no large foreground face insert
Lighting/mood: 【填写光线与情绪】
Constraints: keep Cui Dongshan exactly male and identical to the reference image; preserve the exact face shape, eye shape, nose, mouth, brow mark, hairstyle silhouette, clothing silhouette, body proportions, and restrained temperament; do not redesign him. The second character must not alter Cui Dongshan's design and must remain visually secondary.
Avoid: extra male face in background, face collage, multiple heads, female styling for Cui Dongshan, red hair for Cui Dongshan, glamorous costume, exposed legs, jewelry, high heels, round face, wide jaw, mature male lead face, noble prince face, big sweet eyes, thick lips, idol styling, xianxia game style, standard costume-drama pretty-boy face, redesigning features, generic handsome-face beautification.
No text, no watermark.
```

双人图额外加一句最有用：

```text
The second character must remain clearly secondary and must not contaminate or alter Cui Dongshan's identity.
```

---

## 6. 高压场景模板

适合夜景、逆光、轻俯视、轻仰视、动作状态。

```text
Keep Cui Dongshan identical to the reference image even under difficult cinematic conditions.
Preserve the same jaw width, same face length, same eye structure, same brow mark, same age, and same male scholar identity under this lighting and angle.
Do not let the dramatic lighting, perspective, or motion redesign his face.
```

高压图必须额外禁止：

```text
Do not widen the jaw, do not mature the face, do not enlarge the eyes, do not beautify into a generic handsome lead.
```

---

## 7. 中文短模板

如果你用中文提示词，可以直接用这一版：

```text
以已提供的崔东山母版图为唯一身份锚点，保持完全同一人物，不重新设计角色。
崔东山，男性，黑色长发半束，眉心有小而凝的红籽，窄长收束的年轻脸型，偏收略长的眼睛，细直鼻梁，偏薄嘴唇，白色外袍，淡青蓝内衫，修长偏轻的读书人体态，手持卷轴。

这是他在【场景】中的【画面类型】。只允许变化场景、表情、动作、视线、景别和轻微光线关系，不允许改变脸型、五官比例、年龄感、发型轮廓、服装轮廓和人物气质。

气质必须保持：外轻内重，清醒克制，孤独深情，像总比别人多看一步，但不是反派脸，也不是温柔男主脸。

画风保持半写实东方人物、宋代审美、山水志怪、人间烟火、低饱和高级灰、自然情绪光影。

不要女性化，不要红发，不要华丽服装，不要露腿，不要首饰，不要高跟鞋，不要圆脸，不要宽下颌，不要大眼甜感，不要厚唇，不要偶像风，不要古偶男主感，不要仙侠网游风，不要重新设计五官，不要更完美更对称的主角脸。
无文字，无水印。
```

---

## 8. 最推荐的变量填写方式

为了最稳，变量尽量短，不要写成长篇剧情。

推荐这样填：

- `【场景】`：书院深夜庭院 / 湖边夜谈 / 官道送行 / 屋内案前 / 湖心高台夜色
- `【画面类型】`：单人中景 / 半身近景 / 双人中景 / 单人立绘
- `【光线与情绪】`：冷月夜色、压着情绪 / 暖灯安静、若有所思 / 夜色克制、似笑非笑

不推荐这样填：

- 一大段剧情说明
- 把关系、世界观、情绪、动作全塞进一句话
- 给模型太多“重新设计”的空间

---

## 9. 使用顺序

后续每次出图都按这个顺序：

1. 先贴母版图。
2. 再用“最终通用主模板”。
3. 再补场景变量。
4. 如果是双人图，改用“双人图推荐写法”。
5. 如果是高压角度或逆光图，再补“高压场景模板”。

---

## 10. 一句话最终版

如果只记一句，就记这句：

`以母版图为唯一身份锚点，保持完全同一人物，只换场景和状态，不重新设计崔东山。`
