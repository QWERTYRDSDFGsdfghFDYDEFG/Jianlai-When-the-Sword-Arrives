# Ren'Py 接图执行清单

适用范围：本项目所有图片、配音、角色、场次演出的 Ren'Py 接入工作。

用途：把“图已经有了，怎么安全、快速、统一地接进工程”变成固定清单，减少漏资源、错命名、断调用和黑屏报错。

建议使用方式：

1. 单场出图前先填 `Codex/single_scene_image_brief_template.md`
2. 图确认可用后，再按本清单执行接入

---

## 0. 接图前先确认

- [ ] 这张图已经确认可用，不是纯废弃测试图
- [ ] 已明确它属于 `test / cand / master` 中哪一级
- [ ] 已明确这是背景图、事件图、CG 还是仅角色参考图
- [ ] 已明确本次是否要真正接入脚本，而不是只存档留底

如果还没回答清楚，先不要接。

---

## 1. 文件与目录检查

### 1.1 文件名检查

- [ ] 全小写
- [ ] 只含字母、数字、下划线
- [ ] 没有空格
- [ ] 没有双下划线
- [ ] 没有中英文混杂命名
- [ ] 版本号明确

推荐格式：

`c章节号_场次号_主体或动作_v版本号`

示例：

- `c1_07_pq_run_v1`
- `c2_02_cpa_pq_v1`

### 1.2 尺寸检查

- [ ] 图片尺寸为 `1920 x 1080`

### 1.3 目录检查

- [ ] Chapter 1 放入 `images/chapter1/`
- [ ] Chapter 2 放入 `images/chapter2/`
- [ ] Chapter 3 放入 `images/chapter3/`
- [ ] 其他章节按同规则放置

---

## 2. 图片导入

优先使用项目现成脚本导入：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\import_generated_image.ps1 -ImageName c1_07_pq_run_v1
```

常用写法：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\import_generated_image.ps1 -ImageName c2_02_cpa_pq_v1 -Chapter 2
```

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\import_generated_image.ps1 -ImageName c1_08_pq_pose_v1 -SourcePath "C:\path\to\image.png"
```

导入后确认：

- [ ] 文件已进入正确目录
- [ ] 文件名和预期一致
- [ ] 没出现多份近似重名文件

---

## 3. `bg_images.rpy` 接入

### 3.1 是否需要补 `image bg`

以下情况一般需要：

- [ ] 背景图
- [ ] 事件构图图
- [ ] 作为整场 `scene bg` 使用的 CG

以下情况一般不在 `bg_images.rpy` 里接：

- [ ] 仅角色参考图
- [ ] 尚未决定实装的测试图

### 3.2 新增定义

在 [bg_images.rpy](/E:/新建文件夹/When%20the%20Sword%20Arrives/game/bg_images.rpy:1) 补：

```renpy
image bg c1_07_pq_run_v1 = im.Scale("images/chapter1/c1_07_pq_run_v1.png", 1920, 1080)
```

检查：

- [ ] `image bg` 名与文件同基名
- [ ] 路径真实存在
- [ ] 路径使用正斜杠
- [ ] 章节目录写对
- [ ] 宽高为 `1920, 1080`

### 3.3 兼容旧别名

只有历史脚本大量依赖时，才临时保留别名。

检查：

- [ ] 是否真的有必要保留旧别名
- [ ] 是否已明确哪个才是主名
- [ ] 后续是否计划收敛回一个主名

---

## 4. 脚本中的 `scene bg` 接入

在对应脚本里统一写：

```renpy
scene bg c1_07_pq_run_v1
```

检查：

- [ ] `scene bg` 名与 `image bg` 名一致
- [ ] 没有多写或漏写下划线
- [ ] 没写成旧的临时别名
- [ ] 同一场里没有重复无意义 `scene`

如果只是同背景下连续对白：

- [ ] 尽量不要重复 `scene bg`

---

## 5. 立绘与人物接入

### 5.1 角色变量检查

在 [characters.rpy](/E:/新建文件夹/When%20the%20Sword%20Arrives/game/characters.rpy:1) 确认：

- [ ] 所有说话角色变量都已定义
- [ ] 新角色在脚本发言前已完成定义

### 5.2 立绘调度检查

常规骨架：

```renpy
show cpa standard at left_medium
show peiqian standard at right_medium
with dissolve
```

检查：

- [ ] 当前场次是否真的适合立绘推进
- [ ] 多人场是否只保留关键角色
- [ ] 未发言角色是否需要压暗
- [ ] 站位是否符合分镜表与执行表

### 5.3 `A3` 场次检查

如果本场是事件场，不要用普通站姿硬演。

检查：

- [ ] 是否应先 `hide` 当前立绘
- [ ] 是否应切整张事件图
- [ ] 是否应在事件图后再恢复对白结构

示例：

```renpy
hide cpa
hide peiqian
with dissolve

scene bg c2_04_magic_boat_v1
with Dissolve(1.0)
```

---

## 6. 转场接入

默认口径：

- 日常切入：`with dissolve`
- 压抑停顿：`with fade`
- 奇观 / 收束：`with Dissolve(1.0)`

检查：

- [ ] 转场类型是否符合场次气质
- [ ] 同场对白中是否加了过多转场
- [ ] 是否误用过强、过花哨的转场

---

## 7. 配音接入

脚本中统一写：

```renpy
voice voice_id("voice.xxx")
```

不要直接写硬路径。

在 [audio_index.rpy](/E:/新建文件夹/When%20the%20Sword%20Arrives/game/audio_index.rpy:1) 检查：

- [ ] 新 `voice_id` 已加入 `VOICE_INDEX`
- [ ] 映射路径真实存在
- [ ] 路径使用正斜杠
- [ ] 脚本中的 key 与索引中的 key 完全一致

---

## 8. 心境系统接入

涉及情绪节点时优先使用：

```renpy
$ story_mood_event("a", "separation")
```

```renpy
$ story_mood_choice("a", "listen")
```

必要时才直接写：

```renpy
$ set_mood("a", 60, "detail")
```

检查：

- [ ] 当前场次是否真的有 mood 节点
- [ ] key 是否对应正确角色
- [ ] event / choice 映射是否存在

---

## 9. 脚本静态检查

接完图后，逐项检查：

- [ ] 引号全部闭合
- [ ] 没有跨行字符串错误
- [ ] `label` / `jump` 没断链
- [ ] 新角色变量已定义
- [ ] `scene bg` / `show` / `hide` 顺序合理
- [ ] 不存在明显重复、无效调用

---

## 10. 资源静态检查

- [ ] 图片路径存在
- [ ] 音频路径存在
- [ ] `bg_images.rpy` 已同步
- [ ] `scene bg xxx` 与 `image bg xxx` 一致
- [ ] 文件名、版本号、下划线无误
- [ ] 没把测试图误当正式图接入主流程

---

## 11. 演出正确性检查

- [ ] 这场到底是立绘场还是事件场，判断没错
- [ ] 景别选对
- [ ] 站位服务对白
- [ ] 留白足够
- [ ] 多人场没塞满
- [ ] 本场的画面焦点和剧情焦点一致
- [ ] 项目统一风格没有跑偏

---

## 12. 最小可跑骨架确认

每场接图至少要能缩成下面的最小骨架：

```renpy
scene bg __________________
with __________________

show __________________ at __________________
show __________________ at __________________
with __________________

voice voice_id("__________________")
```

确认：

- [ ] 我知道这场最小可跑骨架是什么
- [ ] 我知道哪些效果是“先跑通再补”
- [ ] 我没有在第一轮就塞太多花哨演出

---

## 13. 可玩验收

至少确认：

- [ ] 新游戏从 `label start` 进入不报错
- [ ] 场景切换不黑屏、不停滞
- [ ] 新图能正常显示
- [ ] 配音能正常播放
- [ ] 快进、回看、存档、读档没有被破坏

---

## 14. 文档同步判断

最后再判断一次：

- [ ] 这次只是测试图接入，不更新角色标准文档
- [ ] 这次只是候选图接入，不更新角色标准文档
- [ ] 这次正式替换主母版，需要同步标准文档
- [ ] 这次正式新增表情页 / 动作页，需要同步相关文档或索引

原则：

出图是高频动作，改角色标准文档是低频动作。不要混成一步。

---

## 15. 交付记录

- 接入文件：
- 修改脚本：
- 修改的 `image bg`：
- 修改的 `voice_id`：
- 是否涉及 mood：
- 是否需要后续补图：
- 是否需要后续重构旧别名：

备注：

`____________________________________________`
