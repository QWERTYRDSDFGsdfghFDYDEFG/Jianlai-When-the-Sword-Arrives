# script.rpy Ren'Py 演出脚本执行表

> 用途：把 [script逐场分镜表.md](E:\新建文件夹\When the Sword Arrives\game\script逐场分镜表.md:1) 继续细化成 `script.rpy` 可直接照着调整的 Ren'Py 演出口径。  
> 目标：让序章每一场都知道该怎么写 `scene / show / hide / with / voice`，并知道图片该如何复用。  
> 原则：先保证可跑、可读、可补图，再逐步加精细站位与差分。

---

## 通用口径

### 背景

- 每次切新图直接用 `scene bg xxx`。
- 同一图下的连续对白尽量不重复 `scene`。
- `midnight_lake` 系列建议后续拆成“母图 + 金色法术 overlay”的做法，减少重画。

### 立绘

- 当前文件几乎全靠整张背景图推进，后续重做时也不必强行把每场改成立绘对话。
- 需要补立绘的场优先放在 `序-01 / 序-02 / 序-09 / 序-13 / 序-14`。
- 戏台段和演剑段可以继续以整张剧情图为主，立绘只做辅助。

### 转场

- 序章开场、收尾：`with fade`
- 喜剧表演、人物亮相：`with dissolve`
- 奇观、演剑、章节高潮：`with Dissolve(1.0)`

### 配音

- 继续沿用现有 `voice voice_id("voice.xxx")`。
- 不新增假配音路径，不在文档里发明不存在的音频 id。
- 长句需要拆音时，只拆文本节奏，不改 scene 结构。

### 推荐占位命名

- 李宝瓶：`lbp standard`
- 崔东山：`cds standard`
- 李槐：`lh hero`
- 裴钱：`peiqian standard` / `peiqian sword`
- 陈平安：`cpa standard` / `cpa sword_robe`
- 朱敛：`zl standard` / `zl bandit`
- 石柔：`sr standard` / `sr bandit`
- 于禄：`yl scholar`
- 谢谢：`xx musician`

---

## 序章

### 序-01 深夜庭院得知离别

**执行骨架**

```renpy
scene bg prologue_courtyard_night
with fade

show lbp standard at left_medium
show cds standard at right_medium
with dissolve
```

**脚本口径**

- 开场先留 `1` 句环境感，不急着切复杂调度。
- 李宝瓶先说，再补崔东山进场，更有“人不见了”的空落。
- 本场结束后直接切湖边夜景，不需要额外 `hide all`。

### 序-02 湖边夜谈

```renpy
scene bg prologue_midnight_lake
with fade

show lbp standard at left_medium
show cds standard at right_medium
with dissolve
```

- 套 `双人夜谈`，整场以固定双人构图为主。
- 李宝瓶情绪起时，可以短暂切 `show lbp standard at center_medium`。
- 这一场是湖区母图，后续几场都尽量从这套环境延展。

### 序-03 李槐持鹿登场

```renpy
scene bg prologue_lihuai_ring_path
with Dissolve(1.0)

show lh hero at center_medium
show milu standard at right_back
with dissolve
```

- 这一场核心是“亮相”，不需要堆对白镜头。
- 先让旁白把金色雷池说清楚，再放李槐台词。
- 如果资源紧，可以只做整图，不单独做人鹿分层。

### 序-04 戏台匪寇铺垫

```renpy
scene bg prologue_stage_far
with dissolve

show zl bandit at left_medium
show sr bandit at right_medium
show yl scholar at left_back
show lsy scholar at right_back
with dissolve
```

- 本场作用是把戏台搭起来，节奏要快，别陷入逐句调度。
- 朱敛、石柔站前，两个“文弱书生”在后景即可。
- 下一场直接切近景版戏台，形成同场推进。

### 序-05 李槐英雄救场

```renpy
scene bg prologue_stage_near
with dissolve

show lh hero at center_medium
show zl bandit at left_medium
show sr bandit at right_medium
with dissolve
```

- 李槐的几句台词可以全部留在同一张近景图内。
- 朱敛、石柔不要抢戏，重点是把李槐的“真信自己是大侠”演出来。
- 结尾崔东山响指后直接切下一张抒情图，形成喜剧后的收气。

### 序-06 湖边琴笛对景

```renpy
scene bg prologue_duet_lakeside
with fade
```

- 这场可以只靠整张背景图加旁白完成，不强求立绘进出。
- 左右人物轮廓要清楚，但不需要强对话感。
- 作用是缓一口气，给裴钱演武做垫步。

### 序-07 裴钱踏湖演武

```renpy
scene bg prologue_peiqian_run
with Dissolve(1.0)

show peiqian sword at center_medium
with dissolve
```

- 这一场主要靠旁白推动动作。
- 不建议为了“武戏”切太多图，一张动势足的主图比多张半成品更有效。
- 金色花朵、湖面踏点、竹刀竹剑是识别重点。

### 序-08 湖心高台收势

```renpy
scene bg prologue_platform_pose
with dissolve

show peiqian sword at center_medium
with dissolve
```

- 这是上一场的收势图，建议跟 `序-07` 同套角色造型。
- 台词还没真正开始前，先让姿势立住。
- 如果制作节奏紧，这张可以从 `序-07` 主图裁切派生。

### 序-09 湖上对唱唤剑仙

```renpy
scene bg prologue_platform_duet
with dissolve

show peiqian sword at left_medium
show cds standard at right_medium
with dissolve
```

- 全段尽量保持双人构图，不要一句一换位。
- 崔东山的胡说八道要轻快，但画面底色不能太闹。
- 最后一句“小师叔”之前不要切图，让呼唤落在同一构图里。

### 序-10 陈平安踏湖现身

```renpy
scene bg prologue_cpa_arrival
with Dissolve(1.0)

show cpa sword_robe at center_medium
with dissolve
```

- 这张要做成真正的出场大图，尽量不要被立绘切碎。
- 旁白先走完“从山顶一掠而来”的势，再接崔东山那句“走你”。
- 这一场和后两场要统一服装、湖面、剑气方向。
- `cpa sword_robe` 在这三场里明确指“金醴法袍白衣版”，不是陈平安日常暖天行路装。
- 原文已写明“不背负那把剑仙，只是腰间挂了一只养剑葫”，因此本图不要带书箱，不要背剑。

### 序-11 陈平安演剑上段

```renpy
scene bg prologue_cpa_sword_01
with dissolve

show cpa sword_robe at center_medium
with dissolve
```

- 这里是第一段昂扬，不必急着做终极高潮。
- 长台词建议按语义拆句，但画面不换。
- 如果后续要做轻微镜头推进，可用同图缩放，不必另切新图。
- 服装继续锁定上一场的“金醴法袍白衣版”，不要切回日常行路装。

### 序-12 陈平安演剑下段

```renpy
scene bg prologue_cpa_sword_02
with Dissolve(1.0)

show cpa sword_robe at center_medium
with dissolve
```

- 这是演剑收顶，建议比上一张更开、更亮一点。
- 整段结束后直接切书院门口，形成“表演结束，回到真正告别”的落地感。
- 这一段只需要一张足够有气势的收束图。
- 继续保留白衣法袍、单个朱红养剑葫和同一方向的剑势，三联图要看起来像同一段连续演出。


### 序-13 书院门口正式送别

```renpy
scene bg prologue_academy_gate_farewell
with fade

show cpa standard at center_medium
show peiqian standard at left_medium
show zl standard at left_back
show sr standard at right_back
show lh hero at right_medium
show lbp standard at left_front
with dissolve
```

- 这是多人送别场，重点是“关系站位”而不是每个人都出满戏。
- 茅小冬可以只用一句台词，不必强求立绘。
- 本场结束后切官道图，直接收束为两人送行。

### 序-14 大隋官道师生送行

```renpy
scene bg prologue_autumn_road_sendoff
with fade

show cpa standard at left_medium
show cds standard at right_medium
with dissolve
```

- 这场就是 `同路夜谈 + 收章`，双人固定构图最稳。
- 崔东山长段说理不用频繁切角度，靠文本节奏和停顿就够。
- 最后一句“愿先生心境，四季如春”后可直接 `jump chapter2_start`，不必再补别的画面。

---

## 图片复用建议

- `prologue_midnight_lake` 作为湖区母图，可派生 `lihuai / duet_lakeside / peiqian / platform_duet`。
- `prologue_stage_far` 与 `prologue_stage_near` 做成同一戏台远近景。
- `prologue_peiqian_run` 与 `prologue_platform_pose` 建议共用同一人物造型与水面体系。
- `prologue_cpa_arrival / prologue_cpa_sword_01 / prologue_cpa_sword_02` 必须作为连续三联图设计。
- `prologue_courtyard_night / prologue_academy_gate_farewell / prologue_autumn_road_sendoff` 是序章首尾情绪三锚点，优先保证完成度。
