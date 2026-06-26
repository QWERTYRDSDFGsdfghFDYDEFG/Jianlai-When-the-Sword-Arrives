# 崔东山新聊天起手模板

> 本文件只保留“新聊天怎么起手”。  
> 角色标准以 `lh/cds/cds_face_ref.md` 为准。

---

## 1. 使用顺序

1. 先提供 `lh/cds/cds_face_ref.md`
2. 再提供镜头方案：
   - `lh/cds/cds_pose_guide.md`
3. 当前优先候选图：
   - `lh/cds/cds_exp_sheet_cand_v2.png`
   - `lh/cds/cds_34_sheet_cand_v2.png`
   - `lh/cds/cds_turn_sheet_cand_v2.png`
   这三张可以继续作为当前迭代参考，但仍然不是正式锁脸母版。
4. 如果后续正式资产已经补齐，再附上：
   - `lh/cds/cds_face_close_master_v1.png`
   - `lh/cds/cds_face_34_master_v1.png`
   - `lh/cds/cds_turn_sheet_v1.png`
   - `lh/cds/cds_exp_sheet_v1.png`
5. 最后只补这次要变化的变量：表情 / 动作 / 场景 / 景别 / 光线

---

## 2. 可直接复制的起手模板

```text
这次不是重新设计角色，而是基于现有标准继续生成同一个崔东山。

请先严格读取并遵守：
- lh/cds/cds_face_ref.md
- lh/cds/cds_pose_guide.md

如果当前正式资产已经补齐，请把以下文件作为正式参考：
- lh/cds/cds_face_close_master_v1.png
- lh/cds/cds_face_34_master_v1.png
- lh/cds/cds_turn_sheet_v1.png
- lh/cds/cds_exp_sheet_v1.png

如果当前仍在测试阶段，请优先附上当前候选：
- lh/cds/cds_exp_sheet_cand_v2.png
- lh/cds/cds_34_sheet_cand_v2.png
- lh/cds/cds_turn_sheet_cand_v2.png

如果需要告诉模型“不要再往旧版跑偏”，可额外附上失败样例：
- lh/cds/cds_exp_sheet_cand_v1.png
- lh/cds/cds_34_sheet_cand_v1.png
- lh/cds/cds_turn_sheet_cand_v1.png

本次只允许变化：
- 表情：[填写]
- 动作：[填写]
- 场景：[填写]
- 景别：[填写]
- 光线：[填写]

要求：
- 人物必须仍然是同一个崔东山
- 必须保留眉心痣、白衣儒衫结构、少年外形但心性老辣的底色
- 优先服从现有标准，不重新设计脸、发型和服装方向
- 不要沿用 `cand_v1` 图里已经出现的俊秀、对称、白净、精修男主脸
- 如果新图更好看但不像现有标准里的同一个崔东山，直接判定失败
- 默认尺寸 1920x1080 横版
```

---

## 3. 最稳的起手值

- 表情：认真 / 微笑 / 小得意
- 动作：标准接话 / 三分之四侧接话 / 轻回头
- 场景：留白背景 / 书院夜色 / 金色雷池 / 官道送行
- 景别：肩部以上近景 / 中近景
- 光线：冷色柔光 + 极轻暖补

---

## 4. 当前批次的额外禁令

在首批正式母版 `cds_face_close_master_v1.png`、`cds_face_34_master_v1.png` 出来之前：

- 不要把 `cds_exp_sheet_cand_v1.png` 当脸部母版
- 不要把 `cds_34_sheet_cand_v1.png` 当脸部母版
- 不要把 `cds_turn_sheet_cand_v1.png` 当脸部母版
- `cds_exp_sheet_cand_v2.png`、`cds_34_sheet_cand_v2.png`、`cds_turn_sheet_cand_v2.png` 可以继续作当前过渡参考，但仍不能替代正式 `master`

原因很简单：

- 它们可以帮我们看“镜头组织大概可用”
- 但不能帮我们锁定“崔东山到底长什么样”

先补出真正能锁脸的近景正式母版，再谈表情页和回头页的精修。
