# 崔东山立绘母版提示词

用途：用于生成崔东山当前阶段的正式立绘母版，方向为“空手正常走路”的可复用 Ren'Py 站立立绘。

## 最终提示词

```text
Use case: illustration-story
Asset type: Ren'Py character standing portrait master for project use
Primary request: Create the final canonical master standing portrait of Cui Dongshan for the project, based on the accumulated test results. This is the reusable sprite master to save into the project.
Scene/backdrop: almost blank pale parchment backdrop with the faintest ink-wash paper atmosphere only, no scenery detail, no floor plane, no props, no shadows distracting from the figure.
Subject: Cui Dongshan only, East Asian young man age 18-21, narrow slightly long youthful face, restrained long eyes, fine straight nose bridge, thin lips, tiny clear red mark at the brow center, black long hair half tied in a simple high half-bun with slight loose strands, slim scholar build, white outer robe over gray-blue inner robe, black cloth shoes.
Style/medium: semi-realistic Eastern fantasy character illustration, Song-dynasty aesthetic, restrained and understated, subtle ink-wash influence combined with clean production-quality character rendering, low saturation, natural fabric structure, not anime-cute, not idolized, not xianxia game glamour.
Composition/framing: 1920x1080 landscape, full body from head to shoes, centered slightly to the right with generous empty space, clean silhouette, suitable as a reusable Ren'Py standing portrait master.
Lighting/mood: soft neutral diffuse light, calm, quiet, intelligent, inwardly heavy but outwardly light.
Color palette: off-white, gray-blue, ink gray, muted skin tones, black hair.
Materials/textures: layered scholar robes with broad sleeves, natural folds, lightly worn cloth, simple understated details.
Action/pose: empty hands, natural normal walking pose, one foot slightly forward, the other trailing naturally, arms relaxed with a subtle walking swing, torso upright, head facing slightly to the side as if quietly moving forward, expression restrained and unreadable.
Constraints: strictly preserve the same Cui Dongshan identity from the reference image; preserve the white outer robe and gray-blue inner robe structure; preserve the slim scholarly body type and half-tied hairstyle silhouette; preserve the tiny brow red mark; keep this as the canonical master portrait for later expression and pose variants; no hand props; no extra characters; no text; no watermark.
Avoid: round face, wide jaw, mature male lead face, noble young master styling, big sweet eyes, thick lips, makeup look, ornate crown, luxurious gold ornaments, floating immortal costume, theatrical pose, exaggerated robe motion, busy background, bright saturated colors.
```

## 当前结论

- 方向锁定为：空手、正常走路、白色外袍、灰蓝内衫、半写实宋韵、低饱和留白背景。
- 当前环境里内置 `image_gen` 能生成会话预览，但未提供可直接复制到项目目录的本地文件路径。
- 后续如具备可落盘路径，应优先使用本提示词直接生成正式母版文件，例如命名为 `cds_master_walk_v1`。
