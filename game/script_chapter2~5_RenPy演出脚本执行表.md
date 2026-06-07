# script_chapter2 ~ script_chapter5 Ren'Py 演出脚本执行表

> 用途：把 [script_chapter2~5逐场分镜表.md](E:\新建文件夹\When the Sword Arrives\game\script_chapter2~5逐场分镜表.md:1) 继续细化成 Ren'Py 实际可落地的演出脚本口径。  
> 目标：每一场都知道该怎么写 `scene / show / hide / with / voice`。  
> 原则：少切图、稳复用、先保证可跑，再补精修演出。

---

## 通用口径

### 背景

- 新场切入：`scene bg xxx`
- 同背景下连续对话：尽量不重复 `scene`
- 轻环境版：优先用 `scene bg xxx_mist` 或统一加 very light 氛围底图

### 立绘

- 单人：`show cpa standard at center_medium`
- 双人：`show cpa standard at left_medium` / `show wy standard at right_medium`
- 三人：左、中、右固定，不乱飞
- 未发言角色：若后续有系统支持，可切 `dim` 版；当前文档先用“压暗未发言角色”作为实现目标

### 转场

- 日常切入：`with dissolve`
- 压抑停顿：`with fade`
- 奇观或章节收束：`with Dissolve(1.0)` 或较慢淡入淡出
- 同场对话小切换：尽量不频繁加转场

### 配音

- 已有配音时：`voice voice_id("voice.xxx")`
- 暂无配音时：文本先行，不占位假路径
- 长讲理段：按语义拆成短句，每句单独 `voice`

### 推荐占位命名

以下为执行表里的推荐占位名，后续可以按实际素材名替换：

- 背景：
  - `bg chapter2_mountain_path`
  - `bg chapter2_huangting_city`
  - `bg ziyangfu_gate`
  - `bg ziyangfu_banquet`
  - `bg ziyangfu_treasure_tower`
  - `bg mountain_road_dusk`
  - `bg war_torn_official_road`
  - `bg antique_shop`
  - `bg shujianhu_lake`
  - `bg qingxia_road`
- 立绘：
  - `cpa standard`
  - `cpa shujianhu`
  - `wy standard`
  - `zl standard`
  - `peiqian standard`
  - `gc standard`
  - `mud_loach human`
  - `assassin kneel`

---

## Chapter 2

### 2-01 返乡山路与溪涧歇脚

**执行骨架**

```renpy
scene bg chapter2_mountain_path
with fade

show cpa standard at left_medium
show peiqian standard at right_medium
show zl standard at left_back
show shirou standard at right_back
with dissolve
```

**脚本口径**

- 开头 2 到 3 句旁白直接铺背景，不急着切人。
- 陈平安回乡念头开始后再 `show cpa`.
- 裴钱挑水疱和朱敛插话，用双人或三人固定构图，不频繁进出场。
- 本场结尾不 `hide`，直接接入入城场更顺。

### 2-02 黄庭郡城入城

```renpy
scene bg chapter2_huangting_city
with dissolve

show cpa standard at left_medium
show peiqian standard at right_medium
show zl standard at left_back
with dissolve
```

- 以旁白交代旧事与黄庭国变化。
- 裴钱“回家咯”时可短暂把陈平安缩到 `center_medium`，突出“离家更近”的心绪。

### 2-03 吴懿现身相邀

```renpy
show wy standard at right_medium
with dissolve
```

- 不切背景，直接在郡城主街上引入吴懿。
- 对话主轴只保留 `cpa` 与 `wy` 两人前景。
- 其他人若实现压暗，则保留后景；若未实现，直接不显示。

### 2-04 核雕小舟化楼船

```renpy
hide cpa
hide wy
hide peiqian
hide zl
with dissolve

scene bg chapter2_city_boat_magic
with Dissolve(1.0)
```

- 这场优先做成背景奇观图或特效图，不建议靠立绘硬演。
- 裴钱惊叹后，再把角色切回。

### 2-05 楼船上眺望御江

```renpy
scene bg shujianhu_lake_mist
with fade

show cpa standard at left_medium
show peiqian standard at right_medium
with dissolve
```

- 用 very light 雾气版最稳。
- 这场旁白多，人物少说。
- 结尾“紫阳府到了”前不切人，靠旁白过渡。

### 2-06 紫阳府千人迎接

```renpy
scene bg ziyangfu_gate
with Dissolve(1.0)

show wy standard at center_medium
show cpa standard at left_medium
show peiqian standard at right_medium
show zl standard at left_back
with dissolve
```

- 迎接人海优先放在背景里，不单独做大量角色立绘。
- 吴懿邀陈平安并肩时，切双人主构图。
- 陈平安拒绝并肩那一句，适合前景只留 `cpa` 与 `wy`。

### 2-07 多宝高楼安置

```renpy
scene bg ziyangfu_treasure_tower
with dissolve

show wy standard at right_medium
show cpa standard at left_medium
show peiqian standard at center_small
with dissolve
```

- 裴钱惊叹可用更靠前的小比例站位，增加“抻着脖子看”的感觉。
- 章节收尾前 `hide wy`，只留陈平安一行更自然。

---

## Chapter 3

### 3-01 宴前重逢孙大侠

```renpy
scene bg ziyangfu_corridor
with fade

show cpa standard at left_medium
show sdx standard at right_medium
with dissolve
```

- 先双人，后补 `peiqian` / `zl` 在后景。
- 这场的重点是“认出来了”，不是复杂调度。

### 3-02 雪茫堂入席

```renpy
scene bg ziyangfu_banquet
with dissolve

show wy standard at center_medium
show cpa standard at left_medium
show peiqian standard at right_medium
show zl standard at left_back
with dissolve
```

- 宴席阶段背景固定，不要频繁切。
- 吴懿挽陈平安时，可让吴懿更靠近中心，陈平安偏左半步。

### 3-03 “且慢行”

```renpy
hide peiqian
hide zl
with dissolve

show cpa standard at center_medium
with dissolve
```

- 长讲理段时，优先单人中景。
- 若有配音，必须拆句。
- 结尾再把听众切回。

### 3-04 杀一人救天下的问答

```renpy
show zl standard at right_medium
show cpa standard at left_medium
with dissolve
```

- 说完问题后留 1 到 2 句空拍旁白或短停顿。
- 朱敛回答时不要切背景。

### 3-05 宴后夜谈

```renpy
scene bg mountain_road_dusk
with fade

show cpa standard at left_medium
show zl standard at right_medium
with dissolve
```

- 全段以双人走路对话为主。
- 只在话题转换明显时，切一次更远的背景即可。

### 3-06 去往嫁衣女鬼府邸前

```renpy
scene bg mountain_road_dusk
with dissolve
```

- 可以不重摆太多，只把语气往“悬念”收。
- 章节末尾建议 `hide all` 再 `with fade`。

---

## Chapter 4

### 4-01 红烛镇前计划分流

```renpy
scene bg hongzhu_town_stop
with fade

show cpa standard at left_medium
show zl standard at right_medium
with dissolve
```

- 这是纯计划戏，保持双人固定构图最省成本。

### 4-02 石毫国战乱车队

```renpy
scene bg war_torn_official_road
with fade

show slz standard at left_medium
show lmx standard at right_medium
with dissolve
```

- 先由旁白铺乱世，再切人。
- 这场重点靠背景，不靠复杂人物。

### 4-03 阮秀与宋郎中

```renpy
scene bg carriage_interior
with dissolve

show rx standard at center_medium
show slz standard at left_medium
with dissolve
```

- 徐铉芹只作为进出场补位。
- 阮秀尽量居中，体现她的静和稳。

### 4-04 古董铺入场

```renpy
scene bg antique_shop
with fade

show cpa disguise at left_medium
show lzg standard at right_medium
with dissolve
```

- 伪装版陈平安单独用 `cpa disguise` 占位最清楚。
- 古董铺信息量大，背景一次到位后不再切。

### 4-05 掌柜讲书简湖

```renpy
show cpa disguise at left_medium
show lzg standard at right_medium
```

- 延续上一场，不切背景。
- 这是“信息灌注段”，不要再加多余角色。

### 4-06 顾璨楼船初现

```renpy
scene bg shujianhu_lake
with Dissolve(1.0)

show gc standard at center_medium
show thj standard at left_back
show mud_loach human at right_back
with dissolve
```

- 顾璨居中最重要。
- 如果还没有群像立绘，后景人物可以先不做。

### 4-07 柳树边与龙泉郡平行切

```renpy
scene bg lakeside_willow
with fade

show middle_aged_man standard at center_medium
with dissolve

scene bg yang_shop
with dissolve

show rq standard at left_medium
show ylt standard at right_medium
with dissolve
```

- 这是平行切，关键是“切得稳”，不是切得快。

---

## Chapter 5

### 5-01 渡口重逢

```renpy
scene bg shujianhu_dock
with fade

show cpa shujianhu at left_medium
show gc standard at right_medium
show mud_loach human at right_back
with dissolve
```

- 这里开始优先用 `cpa shujianhu`，与返乡版区分。

### 5-02 去青峡岛的路上

```renpy
scene bg qingxia_route
with dissolve

show cpa shujianhu at left_medium
show gc standard at right_medium
with dissolve
```

- 一路沉默感主要靠顾璨说、陈平安不接。
- 中段可短暂 `hide gc` 再 `show gc`，模拟顾璨追上来继续说。

### 5-03 刺客妇人求饶

```renpy
scene bg boat_deck
with fade

show cpa shujianhu at left_medium
show gc standard at right_medium
show assassin kneel at center_small
show mud_loach human at right_back
with dissolve
```

- 妇人跪姿必须低位，才能成立压迫感。

### 5-04 “为什么不只是杀了她？”

```renpy
hide assassin
with dissolve

show cpa shujianhu at left_medium
show gc standard at right_medium
show mud_loach human at right_back
```

- 问题抛出后，画面应更干净。
- 最好只剩陈平安、顾璨、小泥鳅。

### 5-05 “一家人就要齐齐整整”

```renpy
show cpa shujianhu at center_medium
hide mud_loach
with dissolve
```

- 这一句建议切单人或双人近一些。
- 说完后留白一拍。

### 5-06 顾璨与小泥鳅私下说话

```renpy
scene bg boat_side_corner
with fade

show gc standard at left_medium
show mud_loach human at right_medium
with dissolve
```

- 这场是补顾璨内心层，不要加陈平安。

### 5-07 去见婶婶前先把话说完

```renpy
scene bg qingxia_road
with dissolve

show cpa shujianhu at left_medium
show gc standard at right_medium
with dissolve
```

- 双人走路构图，稳定即可。

### 5-08 “对不起，是我来晚了”

```renpy
show cpa shujianhu at center_medium
hide gc
with dissolve

show gc standard at right_medium
with dissolve
```

- 先给陈平安一句，再让顾璨反应进来。
- 这是整章最该留停顿的一句之一。

### 5-09 长谈上半

```renpy
scene bg qingxia_road
with dissolve

show cpa shujianhu at left_medium
show gc standard at right_medium
with dissolve
```

- 全段不建议反复切景。
- 重点靠表情差分：疲惫、讲理、低头听。

### 5-10 长谈下半

```renpy
show cpa shujianhu at left_medium
show gc standard at right_medium
```

- 若要强调“来一个我杀一个”，可短暂将陈平安切 `center_medium`。

### 5-11 并肩前行收束

```renpy
scene bg qingxia_road_far
with fade

show cpa shujianhu at left_medium
show gc standard at right_medium
with dissolve
```

- 最后一场适合稍远一点的收束构图。
- 不建议做成和解笑脸，维持“路还在走”的状态。

---

## 建议优先补的 Ren'Py 辅助资源

### 立绘位置 transform

建议后续统一封装：

- `left_medium`
- `right_medium`
- `center_medium`
- `left_back`
- `right_back`
- `center_small`

### 表情差分优先级

陈平安优先保证：

- 平静聆听
- 准备讲理
- 看穿不说破
- 压着疲惫
- 轻度警觉
- 极轻微温和

顾璨优先保证：

- 热情
- 讨好
- 愣住
- 慌乱
- 嘴硬
- 低头听

### 执行顺序建议

1. 先按本文把 `chapter2` 与 `chapter5` 跑通  
2. 再补 `chapter3` 的宴席与夜谈  
3. 最后补 `chapter4` 的多线切换  

原因：

- `chapter2` 最适合建立基础演出口径  
- `chapter5` 最能验证陈平安与顾璨的核心戏  
- `chapter3` 和 `chapter4` 信息量更大，更适合在基础流程稳后再补

