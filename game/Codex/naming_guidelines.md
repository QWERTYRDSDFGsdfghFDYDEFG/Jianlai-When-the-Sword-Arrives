# 命名规范

适用范围：`game/` 工程内的图片、音频、文档、角色资料、脚本中的资源调用名。

这份规范的目标只有两个：

1. 文件名尽量短，便于人工管理。
2. 文件名、`image bg` 定义名、脚本调用名保持一致，避免 Ren'Py 灰底占位图。

---

## 1. 总原则

### 1.1 尽量短，不写成一句话

不要再使用这种名字：

- `CUIDONGSHAN_FACE_IDENTITY_STANDARD.md`
- `prologue_platform_pose_v1.png`
- `cpa_scene_ch2_01_homecoming_opening_04_black_peiqian_bamboo_box_cleaner.png`

推荐改成短名：

- `cds_face_ref.md`
- `c1_08_pq_pose_v1.png`
- `c2_01_rest_v1.png`

### 1.2 默认只用小写英文字母、数字、下划线

统一使用：

- `a-z`
- `0-9`
- `_`

不要使用：

- 空格
- 连字符 `-`
- 中文标点
- 双下划线 `__`
- 混用大小写

正确示例：

- `c1_07_pq_run_v1.png`
- `c2_02_cpa_pq_v1.png`
- `cds_face_ref.md`

### 1.3 一个资源，尽量一个基名

同一个背景资源，三处名字应尽量一致：

1. 图片文件名
2. `bg_images.rpy` 里的 `image bg xxx`
3. 脚本里的 `scene bg xxx`

推荐写法：

```renpy
image bg c1_07_pq_run_v1 = im.Scale("images/chapter1/c1_07_pq_run_v1.png", 1920, 1080)
```

```renpy
scene bg c1_07_pq_run_v1
```

不要再出现：

- 文件叫 `prologue_peiqian_run_v1.png`
- 定义叫 `prologue_peiqian_run`
- 脚本里写 `scene bg peiqian`

这种三套名字并行最容易出错。

---

## 2. 图片命名规范

### 2.1 背景图统一格式

格式：

`c章节号_场次号_主体或动作_v版本号.png`

示例：

- `c1_01_lbp_return_v2.png`
- `c1_02_midnight_lake_v1.png`
- `c1_07_pq_run_v1.png`
- `c1_08_pq_pose_v1.png`
- `c1_09_platform_duet_v1.png`
- `c1_10_cpa_arrival_v1.png`
- `c2_01_rest_v1.png`
- `c2_02_cpa_pq_v1.png`

说明：

- `c1` 表示第一章
- `01` 表示该章内第 1 张主要背景
- 主体/动作尽量 2 到 4 段词以内
- `v1`、`v2`、`v5` 表示版本

### 2.2 主体命名缩写建议

角色/主体优先使用项目内已有短变量：

- 陈平安：`cpa`
- 崔东山：`cds`
- 裴钱：`pq`
- 李宝瓶：`lbp`
- 李槐：`lh`
- 朱敛：`zl`

场景动作词保持简短：

- `run`
- `pose`
- `duet`
- `return`
- `rest`
- `arrival`
- `farewell`
- `sendoff`

### 2.3 图片文件名长度建议

建议控制在：

- 24 个字符以内更好
- 最长尽量不要超过 32 个字符（不含扩展名也一样尽量短）

像下面这种就偏长了：

- `prologue_platform_pose_v1.png`

更推荐：

- `c1_08_pq_pose_v1.png`
- 如果场景已明确，也可以进一步缩成 `c1_08_pose_v1.png`

---

## 3. Ren'Py 背景定义规范

### 3.1 `image bg` 名称默认跟文件同基名

推荐：

文件：

- `images/chapter1/c1_07_pq_run_v1.png`

定义：

```renpy
image bg c1_07_pq_run_v1 = im.Scale("images/chapter1/c1_07_pq_run_v1.png", 1920, 1080)
```

调用：

```renpy
scene bg c1_07_pq_run_v1
```

### 3.2 允许保留兼容别名，但只能临时用

如果旧脚本很多，短期可以保留别名：

```renpy
image bg pq_run = im.Scale("images/chapter1/c1_07_pq_run_v1.png", 1920, 1080)
image bg c1_07_pq_run_v1 = im.Scale("images/chapter1/c1_07_pq_run_v1.png", 1920, 1080)
```

但目标仍然应该是最终只保留一个主名。

### 3.3 不要出现这些情况

- `image bg` 名和文件名不一样，但没有记录
- 文件改名了，`bg_images.rpy` 没改
- `scene bg` 里多写一个下划线
- 同一张图同时存在 `cpa`、`chengpinan`、`c1_10_cpa_arrival_v1` 三套叫法却没人知道主名是哪一个

---

## 4. 文档命名规范

### 4.1 文档文件名不要过长

像这种太长：

- `CUIDONGSHAN_FACE_IDENTITY_STANDARD.md`

推荐改成：

- `cds_face_ref.md`
- `cds_face_standard.md`

### 4.2 文档命名格式

格式：

`主体_用途.md`

推荐用途词：

- `ref`
- `standard`
- `guide`
- `checklist`
- `notes`
- `index`

示例：

- `cpa_face_ref.md`
- `cds_face_ref.md`
- `pq_pose_guide.md`
- `chapter1_bg_index.md`

### 4.3 文档名长度建议

建议：

- 16 个字符以内最好
- 24 个字符以内可接受

---

## 5. 目录级别约定

### 5.1 图片按章节放

继续保持：

- `images/chapter1/`
- `images/chapter2/`
- `images/chapter3/`

### 5.2 文档按用途放

建议：

- 项目规则文档：`Codex/`
- 角色参考资料：`lh/角色缩写/`
- 通用说明：项目根目录或 `Codex/`

---

## 6. 新增资源时的执行步骤

每次新增背景图，按下面顺序处理：

1. 先确定短文件名。
2. 图片放到对应章节目录。
3. 在 `bg_images.rpy` 里用同名基名定义 `image bg`。
4. 在脚本里用同一个名字 `scene bg xxx`。
5. 最后静态检查三处是否一致。

检查模板：

- 文件：`images/chapter1/c1_07_pq_run_v1.png`
- 定义：`image bg c1_07_pq_run_v1 = ...`
- 调用：`scene bg c1_07_pq_run_v1`

三者完全一致才算通过。

---

## 7. 当前推荐的统一方向

### 7.1 背景图

后续新背景图尽量统一成：

- `c1_01_xxx_v1.png`
- `c1_02_xxx_v1.png`
- `c2_01_xxx_v1.png`

### 7.2 角色参考文档

后续角色资料尽量统一成：

- `cpa_face_ref.md`
- `cds_face_ref.md`
- `pq_face_ref.md`

不要继续新增：

- `XXX_FACE_IDENTITY_STANDARD.md`

---

## 8. 一句话版

以后尽量执行这一条：

`文件名短 + 全小写下划线 + 文件名 = image bg 名 = scene bg 名`
