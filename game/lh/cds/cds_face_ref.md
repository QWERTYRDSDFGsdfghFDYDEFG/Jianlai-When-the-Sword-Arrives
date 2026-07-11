# 崔东山固定脸部身份与当前服装标准

> 适用范围：崔东山（`cds`）的近景、半身、全身立绘、表情差分、动作差分与剧情 CG。
> 当前版本：`2026-07-11`，依据现有四张正式参考图重写。
> 方法参考：`Codex/semi_to_cel_guide.md`。
> 核心原则：先锁同一个人，再改变角度、表情、动作和场景；近景负责锁脸，全身图负责锁体型与服装结构。

---

## 1. 正式参考图与职责

| 优先级 | 文件 | 固定职责 | 不承担的职责 |
| --- | --- | --- | --- |
| 1 | `lh/cds/cds-v1.png` | 正面偏微角、肩部以上近景；最高优先级脸部身份母版 | 不单独推断全身比例和衣摆结构 |
| 2 | `lh/cds/cds_exp_34_v1.png` | 三分之四侧近景；锁定转角后的骨相、眉眼、鼻口和下颌关系 | 不用其局部表情覆盖正面母版的五官结构 |
| 3 | `lh/cds/cds_face_34_cand_v1.png` | 同镜头、同光线、同角度的中性差分基底；用于认真、疑惑、微笑、委屈、小得意等表情差分 | 不允许借表情重画脸、改机位或改光线 |
| 4 | `lh/cds/cds_full_base_v11.png` | 全身体型、站姿、发型大轮廓、当前服装层级、配色和鞋履母版 | 不作为近景五官细节的最高判据 |

冲突裁决顺序：

1. 脸型、眉眼、鼻口、眉心痣、年龄感：以 `cds-v1.png` 为准。
2. 三分之四侧的透视与骨相：以 `cds_exp_34_v1.png` 为准。
3. 表情差分的机位、光线、构图和衣领：以 `cds_face_34_cand_v1.png` 为固定底板。
4. 身高比例、肩宽、袍服层级、腰带、垂绦和鞋：以 `cds_full_base_v11.png` 为准。
5. 全身图因脸部占比小而丢失的细节，必须回贴近景身份，不能反向改写近景母版。

以上四张图共同构成当前正式标准。旧候选表、旧失败样例和其他来源图片不得覆盖本组标准，除非本文件再次明确修订。

---

## 2. 一句话身份结论

**崔东山是眉心有痣、冷白肤色、黑色高束长发的清瘦白衣少年；外形年轻克制，眼神清醒而略带审视感，不能画成甜净、温柔、浪漫或仙侠贵公子式的通用古风男主。**

人物气质允许聪明、机敏、似笑非笑和一点小得意，但这些只能通过细微表情表现，不能重新设计五官。

---

## 3. 固定脸部身份

### 3.1 年龄、脸型与骨相

- 外观年龄稳定在少年后期，约 `16-18` 岁；年轻但不幼态。
- 脸型为偏窄、略长的椭圆脸，面中修长，轮廓干净。
- 颧区平顺但有真实转折，不鼓、不宽，也不能磨成无骨感的平面脸。
- 下颌线清晰、向下自然收束；下巴窄而有圆钝末端，不做尖锐 V 脸。
- 正面偏微角时左右脸存在自然透视差，禁止强行镜像成完全对称。
- 三分之四侧时，远侧脸收窄，近侧颧颊与下颌仍保持同一套骨相，不能变成另一张更尖、更冷的脸。

### 3.2 眉与眉心痣

- 黑色长眉，眉毛浓度中等偏浓，眉头自然聚拢，眉峰和眉尾略有上扬走势。
- 眉形利落但保留真实毛流，不做细弯柳叶眉，也不做夸张剑眉。
- 两眉之间略上方有一颗小而清楚的朱红色圆痣。
- 眉心痣是一级身份锚点：位置、大小和颜色必须稳定，不能消失、偏移、变黑、变成花钿或装饰纹样。

### 3.3 眼睛与眼神

- 眼型横向偏长，开度克制，上眼睑线较明确，下眼睑较轻。
- 内眼角自然，外眼角微收，整体不是圆眼、下垂眼或夸张上挑狐狸眼。
- 虹膜为深灰褐至近黑色，瞳孔与虹膜不过度高亮。
- 双眼大小与间距自然，不放大，不增加浓睫毛和卧蚕妆感。
- 常态目光稳定、清醒、略带审视；不是凶狠瞪视，也不是温柔含情。
- 表情变化时，眼型骨架不变，只调整眼睑开合、注视张力与极轻微的眼尾状态。

### 3.4 鼻、口与下巴

- 鼻梁细直、长度适中，起点自然；鼻尖小而有体积，鼻翼克制。
- 三分之四侧必须保留参考图中连续、清楚的鼻梁—鼻尖轮廓，不能削成尖翘假体鼻。
- 嘴唇宽度中等偏窄，唇峰克制，上唇略薄、下唇稍有体积。
- 常态闭口，嘴角接近水平或极轻微下压，不能默认带营业式微笑。
- 唇色为低饱和灰粉，不做鲜红、亮泽或柔软嘟唇。
- 下巴与下唇之间保留自然凹面，不拉长、不削尖。

### 3.5 肤色与表面质感

- 肤色为偏冷的自然白皙，受蓝灰环境光影响，但仍保留微弱血色。
- 皮肤是半写实、轻度赛璐璐整理：结构清晰、过渡克制，可见轻微真实纹理。
- 禁止奶油磨皮、瓷白发光、油亮高光、重妆、明显眼线和偶像精修质感。
- 眼下可有极轻的自然阴影，用来支撑清醒与克制，不能画成病弱黑眼圈。

---

## 4. 固定发型

- 发色为自然黑色，冷光下可出现蓝黑高光，不得变成纯蓝、灰发或棕发。
- 长发高束，顶部以简洁束带固定成高马尾；余发直落至腰背区域。
- 头顶与发冠区域有明确体积，但不做夸张仙侠高冠。
- 中央偏自然分缝，额前和两侧保留若干细长碎发；碎发位置可以随动作轻微变化，整体轮廓不能换型。
- 鬓发贴近面侧，帮助说明头部转角；不得改成齐刘海、厚刘海、披发或精致偶像卷发。
- 发丝表现以成束结构为主、少量细丝为辅，避免每根发丝都油亮分明。

---

## 5. 当前体型与全身比例

以 `cds_full_base_v11.png` 为准：

- 身形高挑清瘦，骨架轻，肩宽适中偏窄，不健壮、不柔弱、不女性化。
- 头身比例修长自然；颈部较直，肩线平缓，腰身不刻意收紧。
- 常态站姿安静、自然，重心有轻微偏移；不摆英雄姿势、战斗姿势或海报式回眸。
- 双臂自然下垂，宽袖遮住部分手腕和手部；露出的手指比例真实、姿态放松。
- 全身母版必须完整保留头、衣摆和双脚，人物宜占画面高度约 `75%-85%`。

---

## 6. 当前固定服装

### 6.1 总体结构

- 当前服装为白色宽袖外袍、浅冰蓝交领内袍、白灰中层襟边、蓝灰复层腰带、长垂绦与浅色布靴。
- 结构属于克制的书生/修士袍服，不是贫寒粗布，也不是华贵仙门礼服。
- 服装固定为多层交领：贴颈白色内领带细蓝边，其外为浅冰蓝交领，再外叠白灰窄纹襟边与白色长外袍。
- 外袍前襟自肩胸垂直到脚踝附近，左右长襟形成清楚的纵向框架。

### 6.2 外袍与袖型

- 外袍为冷白、灰白，不是纯亮白；布料有柔和重量和自然垂坠。
- 袖型宽大、长而下垂，袖口呈自然弧形，不能飘成无重力仙袖。
- 外袍襟边与袖缘带同色低对比的细密暗纹，纹样只作为材质细节，不能抢脸或变成金银华纹。
- 肩部自然落肩，胸腰处不过度贴身，不塑造贵公子式窄腰。

### 6.3 内袍、腰带与垂绦

- 内袍主色为低饱和浅冰蓝，长及脚面，前身有自然纵向褶皱和极轻暗纹。
- 腰间为蓝灰与浅灰白多层软带，束法清楚但不夸张，右前侧形成简洁结扣。
- 右前侧保留数条细长垂绦：蓝灰绳、少量小型银灰连接件、深蓝灰流苏。
- 垂绦是当前服装识别点之一，但必须克制；不得增加玉佩群、金属法器、发光饰品或过量珠串。

### 6.4 鞋履

- 鞋为浅灰白布靴/软履，低帮至中低帮轮廓，鞋面有低对比暗纹。
- 鞋底薄而实用，颜色略深于鞋面；不得改成黑靴、厚底战靴或华丽仙靴。

### 6.5 配色与材质

- 主色：冷白、灰白。
- 辅色：浅冰蓝、雾蓝灰。
- 深色强调：垂绦末端的深蓝灰；眉心朱痣是脸部唯一明确暖色识别点。
- 材质以细织布、旧丝或柔软棉麻混合质感表现；干净但不发光，不使用金边、亮银甲片或透明纱。

---

## 7. 表情差分固定规则

表情差分统一以 `cds_face_34_cand_v1.png` 的镜头为基底，并参考 `cds_exp_34_v1.png` 校验三分之四侧骨相。

必须保持完全一致：

- 画幅、景别、相机位置、焦段感与裁切。
- 头部朝向、下巴高度、肩线和身体姿态。
- 主光方向、亮度、色温、阴影形状与蓝灰背景。
- 发型轮廓、碎发、衣领层级和纹样位置。
- 脸型、眉心痣、眼型、鼻形、唇部结构、下颌与年龄感。

只允许微调：眉毛高度与内外侧张力、上下眼睑开合、注视张力、嘴角、唇缝、轻微面颊与下颌肌肉。

### 7.1 认真

- 双眉轻微向内收，眉峰不夸张下压。
- 上眼睑略压，注视更集中。
- 嘴角收平，唇缝稳定，下颌有轻微定住感。
- 不能变成愤怒、冷酷或反派瞪视。

### 7.2 疑惑

- 一侧眉峰极轻抬起，另一侧基本保持。
- 眼睑略放松，目光出现短暂停顿感。
- 唇缝可极轻松开，或单侧嘴角出现微小偏移。
- 不歪头、不改头部角度，不做夸张问号脸。

### 7.3 微笑

- 嘴角小幅上提，可带极轻的单侧先动感。
- 眼睑只轻微放松，眼神仍清醒。
- 原则是“知道但不说破”，不露齿、不大笑、不甜、不含情。

### 7.4 委屈

- 眉头轻向内上方靠拢，下眼睑轻提。
- 嘴角极轻下压，唇部保持克制。
- 表现“有点不服又暂时忍住”，不是哭泣、撒娇、可怜或柔弱。
- 不加泪光、泪痕、红鼻头和夸张八字眉。

### 7.5 小得意

- 单侧嘴角小幅上提，眉尾略扬。
- 眼神增加一点灵动和自知，但眼睛不放大。
- 不抬头、不改机位、不露齿，不做反派邪笑或油滑挑逗。

差分验收底线：第一眼必须像同一帧只动了表情肌。如果更换了脸、角度、光线或衣领，即使情绪更鲜明也判定失败。

---

## 8. 风格锁定

- 项目统一方向：东方幻想、宋代审美、半写实、沉静克制、自然情绪光影、低饱和高级灰、真实材质结构。
- 本角色当前图像风格：半写实东方人物向轻度赛璐璐整理过渡，保留真实骨相，线条更干净，阴影适度分组。
- 风格化只能改变渲染语言，不能改变脸部比例、年龄、肤色关系、发型或服装。
- 不追求强赛璐璐、纯动画脸、厚重描边或高饱和二次元上色。

禁止方向：仙侠网游、古偶电视剧、恋爱游戏男主、页游海报、二次元萌系、流行修仙爽文男主、过度精修国风美男。

---

## 9. 生成与编辑固定口径

### 9.1 通用身份前缀

```text
Use the provided locked references as one identity set for Cui Dongshan, the same character.
This is not a redesign and not a new handsome ancient-style male.

Face identity priority: cds-v1.png.
Three-quarter bone structure and perspective: cds_exp_34_v1.png.
Expression-shot camera, lighting and composition: cds_face_34_cand_v1.png.
Full-body proportions, hairstyle silhouette and current costume structure: cds_full_base_v11.png.

Preserve the same narrow slightly long oval face, restrained long eyes, straight fine nose,
thin muted lips, naturally tapered jaw with a softly blunt chin, cold fair natural skin,
small vermilion mole above the brows, black high-tied long hair, and youthful restrained age impression.
Do not beautify or romanticize him.
```

### 9.2 表情差分固定前缀

```text
Use cds_face_34_cand_v1.png as the only base frame for camera, head angle, lighting,
background, hairstyle, robe, crop and pose.
Use cds-v1.png and cds_exp_34_v1.png only to verify the locked face identity.

This is an expression variation, not a new portrait.
Change only subtle facial muscles: eyebrows, eyelids, gaze tension, mouth corners,
lip seam and slight cheek tension.
Keep the exact same shot, same light, same angle and same person.
```

### 9.3 全身与动作差分固定前缀

```text
Use cds_full_base_v11.png for the full-body proportions, standing silhouette,
robe layers, white and pale icy-blue color arrangement, wide sleeves, layered sash,
restrained hanging cords and pale cloth shoes.
Use cds-v1.png as the highest-priority face identity reference.

Keep the same character and the same current costume.
Do not turn the full-body image into a cinematic poster, xianxia prince portrait,
romantic male-lead illustration or heroic pose.
```

### 9.4 固定负面约束

```text
different person, face redesign, changed age, generic handsome ancient-style male lead,
romance-game male lead, costume-drama idol, noble xianxia prince, sweet innocent boy,
sharp V-shaped chin, enlarged eyes, heavy eyelashes, glossy lips, porcelain skin,
beautified symmetry, warm romantic gaze, seductive smile, villain smirk,
missing forehead mole, displaced forehead mole, decorative forehead mark,
changed hairstyle, ornate crown, loose hair, luxurious robe, gold trim,
glowing white costume, fantasy armor, excessive ornaments, dramatic poster lighting,
heroic pose, cropped feet, changed camera, changed lighting, changed background
```

---

## 10. 验收清单

### 10.1 脸部

- 是否第一眼仍是 `cds-v1.png` 中的同一个人？
- 脸是否偏窄略长，而非尖 V 脸或宽短脸？
- 眉心朱痣的位置、大小、颜色是否稳定？
- 眼睛是否横向偏长、开度克制，没有放大或偶像化？
- 鼻、唇、下颌和少年年龄感是否保持？
- 是否避免了奶油肌、浓妆、亮唇和恋爱感眼神？

### 10.2 三分之四侧与表情

- 是否保持 `cds_exp_34_v1.png` 的三分之四侧透视关系？
- 差分是否与 `cds_face_34_cand_v1.png` 同镜头、同光线、同角度、同裁切？
- 是否只改变表情肌，没有换脸、歪头、改发型或改衣领？
- 情绪是否成立但仍克制，没有夸张漫画表情？

### 10.3 全身与服装

- 身形是否高挑清瘦、肩宽克制、站姿自然？
- 白外袍、浅冰蓝内袍、多层交领、宽袖、复层腰带、垂绦和浅色布靴是否齐全？
- 暗纹是否低对比，服装是否干净克制而非奢华发光？
- 全身图是否完整显示头到脚，没有道具、英雄姿势和海报背景？
- 近景五官若有漂移，是否回贴 `cds-v1.png`，而不是在错误脸上继续修？

---

## 11. 最终记忆点

1. `cds-v1.png` 锁“是谁”。
2. `cds_exp_34_v1.png` 锁“三分之四侧仍是同一个人”。
3. `cds_face_34_cand_v1.png` 锁“同一帧只换表情”。
4. `cds_full_base_v11.png` 锁“体型、站姿和当前服装”。
5. 眉心朱痣不可丢，长眼、窄长脸、冷白肤色和黑色高束长发不可漂移。
6. 表情只能微调肌肉，不能借情绪重新设计脸。
7. 全身图只负责结构；脸部细节冲突时永远回到近景母版。
8. 白衣要冷、净、克制、有层次，不要仙、贵、亮、飘。
9. 风格可以轻度赛璐璐化，身份不能动画男主模板化。
10. 如果新图更漂亮却不像同一个崔东山，直接判定失败。
