# 单图制作记录与检查工具

记录采用 `assets/scene-record.template.json` 的 v2 结构。一张图一份记录，默认位于 `work/art/<scene_id>/record.json`；已有记录不重新初始化，不覆盖历史。只有用户范围允许新建文件时才创建记录、过程稿或快照；原位修改和禁止新文件的要求优先于本格式。旧 v1 可只读诊断，但不能继续制作或标为完成，补证边界见末节。

## 命令

从仓库根目录运行；将 `python` 替换为环境中可用的 Python 3 解释器。

```text
python .agents/skills/jianlai-scene-production/scripts/scene_record.py init work/art/c2_example/record.json --scene c2_example --request "按已确认场次制作候选图" --project .
python .agents/skills/jianlai-scene-production/scripts/scene_record.py init work/art/c2_prep/record.json --scene c2_prep --request "先完成出图前准备" --project . --stop-after space
python .agents/skills/jianlai-scene-production/scripts/scene_record.py fingerprint game/script_chapter2.rpy --role script
python .agents/skills/jianlai-scene-production/scripts/scene_record.py check work/art/c2_example/record.json
python .agents/skills/jianlai-scene-production/scripts/scene_record.py status work/art/c2_example/record.json
```

只有 `init` 写文件，而且拒绝覆盖。`fingerprint` 只输出路径、SHA256 和用途；`check`、`status` 只读。后两者都检查全份记录，不能通过只查末阶段绕开早期失败。退出码 0 表示没有记录错误或流程阻断，不表示图像合格或已经完成；必须同时看 `scope_complete`、`production_complete`、`next_stage`、`next_action` 和 `boundary`。

`next_action`：`start_stage` 开始指定阶段；`finish_attempt_and_review` 完成本次工作并送审；`finalize_stage` 把已经实际通过复核的阶段登记为 passed；`rework` 按明确问题修订；`resolve_record_errors` 修正记录或处理失效依据；`resolve_blocker` 需要处理阻断，不能继续抽图；`scope_complete` 表示用户指定的早期停止点已达到，不能继续后续阶段；`complete` 表示 delivery 也已完成。工具不调用生成器，不运行视觉模型，不启动游戏，不自动更改采用状态。

## 顶层字段

- `task`：`scene_id`、用户请求原文 `request`、绝对仓库路径 `project_root`、`scope`（`candidate` 或 `integrate`）、本次授权原文或可追溯位置 `authorization`、目标尺寸 `target_size`、`stop_after_stage` 停止边界（默认 delivery）。初始化默认 candidate；不能从“做一张图”推断允许替换游戏资产。用户只要求出图前准备时填 space，只要线稿时填 sketch；其他停止点按实际请求选择。边界后的阶段必须保持 pending 且没有尝试。达到早期边界时 scope_complete=true、production_complete=false、next_stage=null、can_continue=false；不能把它理解成可自动上色或出图。integrate 范围必须以 delivery 为终点。缺少此字段的旧记录兼容为 delivery，接手旧记录时仍须对照用户当前指令收窄边界。
- `sources`：剧本版本、任务单、角色标准、母版、相邻镜头、画风依据的文件指纹。优先引用已有权威文件，任务范围和验收条件须可追溯。允许新建文件时可保存批准范围的快照；禁止新文件时不能为填齐记录强建任务单或摘录。持续更新的素材索引不宜作固定制作输入，每次续做仍核对最新采用状态；母版或剧情变化须建立真实新基线，不能静默改写旧证据。
- `identity`：`characters` 为逐角色清单，每项含唯一 `id`、`face_master` 脸部母版指纹、`standard` 身份标准指纹、`visibility`（visible 或 not_visible）及 `visibility_reason` 字符串。母版和标准必须同时属于 sources。有角色时 `absence_reason` 为空；references 开始后无角色则必须填写该原因。not_visible 仅用于剧情背影或完整遮挡并解释原因，小脸或糊脸仍为 visible，验收不足记 unverified。
- `staging`：从有角色的 composition 开始锁定站位方案及证据，字段与摘要规则见下节。纯背景可保持模板空值，但不能跳过原有空间与光照检查。
- `constraints`：`locked` 固定项、`allowed_changes` 允许变化项、`uncertainties` 未解决且会改变制作的冲突。前两项必须在 brief 通过前填好；有实质冲突不得把 brief 标为通过。
- `retry_policy`：默认 `max_reworks: 2`，即每阶段首稿加两次自动返工。额外次数只通过 `extensions` 添加，结构为 `{ "stage": "sketch", "extra_reworks": 1, "authorization": "用户明确允许再修一次的原话/位置" }`。
- `stages`：固定为 brief、references、composition、space、sketch、color、preview、delivery。每项含 `status`、`required_checks`、`attempts`。`status` 只能是 pending、in_progress、passed、blocked。可以增加检查项，不能删掉模板中的必查项；所有阶段都有实际成果，不以“无需3D”为由跳过空间检查。
- `adoption`：`status` 为 candidate 或 confirmed；confirmed 必须有用户采用依据 `authorization`。`selected` 保存交付图指纹，必须对应某次实际制作输出。`asset_specs` 每项含 `asset` 指纹、实际 `width` / `height`、`format`（例如 PNG RGBA）、`display_treatment`（如原生1672×941，运行缩放到1920×1080）。交付完成时每张选中图必须有规格；用实际图片元数据读取结果填写，在 provenance 证据里保留核验结果，不能只复制目标尺寸。工具检查声明和绑定，不解码图片验证尺寸。`integration` 含 `status`（not_requested、pending、passed）、单独的接入授权 `authorization` 与实际验收文件 `evidence`。候选完成不代表用户定稿；integrate 范围必须等运行验收后才能标成完成。

所有指纹统一为 `{ "path": "绝对路径或相对记录所在目录的路径", "sha256": "64位摘要", "role": "这份文件负责证明什么" }`。selected 仅接受已通过阶段的末次输出，旧失败稿不能混入；游戏运行通过状态不得早于 preview 通过。不把凭证或包含凭证的文件纳入资料包。

## 站位方案与版本绑定

`staging` 保持在现有记录中，不要求额外计划文件：

```json
{
  "camera": "本镜机位、俯仰及观看方向",
  "anchors": "主要地标、地面高差与可站立区域",
  "action_target": "谁执行什么动作、朝向哪一个对象或区域",
  "action_space": "动作及后续器物展开所需范围、边界",
  "route": "入口、去向和需保留的通道；无移动时说明",
  "continuity": "前后镜的地标及行动对应、机位变化；无邻镜或仅有分镜时说明依据与未验范围",
  "evidence": [],
  "characters": [
    {
      "character_id": "cpa",
      "position": "相对地标和同伴的位置",
      "footing": "足点、地面高差或接触支撑",
      "facing": "头肩、躯干、骨盆和脚的朝向关系",
      "gaze": "具体观看对象",
      "scale_depth": "校正景深与姿态后的体量依据",
      "occlusion": "前后遮挡及需保留的关键轮廓"
    }
  ]
}
```

有角色且 composition 或以后阶段已开始时，六个场景字段必须非空，角色名单与 identity 精确一致，每人的六个位置字段必须齐全。evidence 非空且属于 sources，绑定实际背景、确认剧情/分镜及已有相邻镜的依据。示例空列表不能作为通过证据。brief/references 准备期间可暂空；纯背景的 staging 检查可 not_applicable。这里要求具体的关系描述，不强制未经证实的坐标或尺度。

调用 `check` / `status` 得到 `staging_sha256`（无角色时为 null）。摘要按完整 staging 对象的规范 JSON 计算，等价于脚本的 `staging_digest`：UTF-8、ensure_ascii=False、sort_keys=True、separators=(',', ':') 后做 SHA256。从 composition 到 delivery，每次 attempt 和 review 都写入该值，attempt.inputs 包含 staging.evidence。实际绘图提示词或原位操作必须表达这份计划的动作目标与站位条件；摘要本身不替代传达计划。

更改机位、地标、人物、目标或任一计划字段都会使旧尝试/复核的摘要失效；不得只更新旧摘要来恢复通过。保持 v2 结构，缺少这些字段的旧 v2 也须实际补证，不能凭原来的身份通过继续制作。不自动修改历史记录，不强制另存文件。

## 每次尝试

```json
{
  "id": "sketch-01",
  "kind": "image",
  "producer": "实际制作者的代理标识",
  "tool": "实际使用的生成或编辑工具",
  "prompt": "本次实际提交的完整提示词",
  "inputs": [],
  "outputs": [],
  "review": null
}
```

`kind` 为 plan、image 或 verification。任何实际图像生成、重绘或像素修改均记 image，不能用 plan/verification 包装改图；前四阶段只做规划，不允许 kind=image。inputs / outputs 都是指纹列表；执行前登记输入，生成或写作后补齐成果，再送审。brief 输入至少绑定一个 sources 文件，其余阶段至少绑定上一阶段最新输出，防止拿无关资料跳过依赖。只有末次 in_progress 尝试可以暂时没有输出或 review；已审尝试必须有输出。同一既有图跨阶段可重复登记同路径、同哈希的成果，无需创建新文件；同一阶段重试仍不得复用输出路径。用户要求原位修改时，不为满足此约定创建候选或用新文件替换原件。若原位写入使历史文件指纹失效，旧通过必须失效，不改写历史哈希冒充原检查仍有效。规划阶段可以用任务单、站位文字或 SVG，不强制生成图片。实际生成过程原生尺寸、目标尺寸偏差、工具失败等在成果或检查观察中明确记录。

### 每次图片操作的身份输入

有角色的 `kind=image` 尝试必须把全部 `face_master` 放进 `inputs`，并记录 `identity_input`，二选一：

- 生成或生成式修图：`{ "method": "reference_images", "call_id": "实际调用标识或可定位的调用事件", "arguments": { "prompt": "实际完整提示词", "referenced_image_paths": ["实际提交的绝对路径"] } }`。arguments 保存真实请求参数，可包含其他工具参数；prompt 必须与 attempt.prompt 一致，全部脸部母版路径须同时在请求和 inputs 中。不要把登记过母版、打开过母版或文字写着锁脸当成已传图。
- 非生成的局部编辑或像素复用：`{ "method": "preserved_pixels", "source": "原图指纹对象", "evidence": ["实际写入记录或脸区差分的文件指纹"] }`。source 必须属于 inputs，仍需输入母版用于核对。此方式须有工具能力和实际写入依据，不能用于把生成式重画包装成原像素保留，也不能把保留旧脸直接判为身份通过。

调用前登记且 outputs 为空、review 为 null 时，call_id 或像素保留 evidence 可暂空；取得输出或送审后必须补齐实际调用/写入证据，不能把计划输入当成已调用。

上述示例中的“指纹对象”应填写完整对象，不是占位字符串。检查器核对所登记请求与 inputs 的一致性，不能证明记录真实或工具确实使用了参考；保留可追溯调用事件，复核者仍须看本次结果。

第二次及以后尝试增加 `rework`：

```json
{
  "from_attempt": "sketch-01",
  "finding_ids": ["F1"],
  "change": "只修正已指出的行进方向",
  "preserve": "人物身份、服装、其余站位和背景结构"
}
```

只能引用上一轮真实存在的问题，不能用“更好看”替代返工原因。完成的尝试与原复核意见作为历史保留；不要把旧失败改写成通过。图像生成失败且没有输出时，保留工具错误证据作为该次 outputs，kind 按实际操作填写，复核记为 rework 或 blocked，不伪造图片。

## 复核与证据

`review` 结构为：

```json
{
  "reviewer": "实际独立复核代理标识",
  "verdict": "rework",
  "checks": [
    {"id": "identity", "result": "pass", "observation": "对照母版的具体观察", "evidence": []}
  ],
  "findings": [
    {"id": "F1", "severity": "hard", "state": "open", "problem": "问题位置及表现", "required_change": "必须修什么", "preserve": "不能动什么", "evidence": []}
  ],
  "character_checks": []
}
```

例子中的空 evidence 不能提交为已检查记录：每条须填写实际检查过的文件指纹，一轮复核的证据合计至少包含本次输出。视觉证据须指向实际图像；内存预览或局部放大可绑定原图，在观察中记录实际查看事件和位置，不强制另存截图。名称不同不能证明代理独立，工具仅检查填写关系。sketch、color、preview、delivery 均需独立复核；有角色的 space 也需独立空间复核，其他规划阶段可由协调者自检。

这四个阶段的 required_checks 均包含 `identity`，有角色时 `review.character_checks` 必须逐人填写，无遗漏或重复。每项结构为：

```json
{
  "character_id": "cpa",
  "result": "pass",
  "observation": "本轮同一人物的判断及不确定处",
  "view": "头部角度、原图局部位置、整图和局部的实际查看事件",
  "image": {"path": "被检查图", "sha256": "64位摘要", "role": "本轮身份检查对象"},
  "evidence": [],
  "comparisons": {
    "face_shape": "脸型、下颌与母版的具体对照",
    "features": "可见五官比例和位置的具体对照",
    "age": "年龄感的具体对照",
    "hair": "发际线和发型轮廓的具体对照"
  }
}
```

- evidence 至少绑定该角色母版与被检查图。image 必须为图像文件指纹，同一次复核的全部角色必须指向同一张图。有图片 outputs 时必须核对该次输出图；没有图片 outputs 的内存预览或交付，image 必须属于本次 inputs，且与上一已通过视觉阶段 character_checks 中实际被验图一致，不能以该阶段的 JSON 输出代替图像来源。
- 有角色时 adoption.selected 必须只包含 delivery 末次逐人核对的那张图，且与每个角色的 image 指纹相同，不能拼凑多人各自通过的不同图。相同指纹可沿用真实独立复核观察并写明出处，不必重画；若 preview 输出带 UI 截图、delivery 交付原 CG，则在 delivery outputs 登记那张既有 CG 并逐人核对，登记不要求新建图片。
- pass 必须有四项具体观察，不能只写“像同一人”。fail 或 unverified 不能汇总为通过；逐人 not_applicable 仅允许 visibility=not_visible，仍填写 view 和遮挡原因。无可见脸时全局 identity 可 not_applicable，但不表示脸部已验证。

- `verdict` 为 pass、rework、blocked；检查结果为 pass、fail、unverified、not_applicable。
- 每次复核须覆盖该阶段全部 required_checks。pass 不能含 fail、unverified 或未解决的 hard 问题。hard 不能靠 accepted 绕过。
- not_applicable 仅用于条件项：无角色的 identity_basis / anatomy / staging、无可见脸的 identity、无接触或足点的 grounding、单张扁平CG的 actual_composite、明确非游戏用途的 dialogue_safe_area。观察里须说明原因并附场景依据。
- 问题 `severity` 为 hard 或 soft，`state` 为 open、resolved、accepted。soft 可由复核说明限制后保留，不把模型偏好冒充用户认可。rework 必须有具体 finding。
- 在需要独立复核的阶段（含有角色的 space），独立代理不可用时保持 review 为 null 或 verdict 为 blocked，据实说明“独立复核未执行”，不要给同一代理另起名字。

### 同图站位复核

composition、space、sketch、color、preview、delivery 都有必查项 `staging`。有角色时不得将它设为 not_applicable，复核绑定当前方案摘要：

- `review.checks` 中 id=staging 的检查仍填写 result、observation、evidence；pass 还必须有 `observations` 对象，含 camera、action_target、action_space、route、continuity 五项具体对照。evidence 包含 staging.evidence；在四个视觉阶段还必须包含逐人检查的同一张被验图，不能验旧布局交新彩图。
- 四个视觉阶段的每个 character_checks 增加 `placement` 对象，沿用同一 image、view 和图像证据，无需重复保存图片：

```json
{
  "result": "pass",
  "observation": "本轮位置判断及未确定处",
  "observations": {
    "position": "实际站位与计划地标关系的对照",
    "footing": "实际支撑与地面高差的对照",
    "facing": "头身脚朝向是否共同成立",
    "gaze": "实际视线与指定目标的对照",
    "scale_depth": "校正景深及姿态后的体量对照",
    "occlusion": "实际遮挡与关键轮廓的对照"
  }
}
```

placement.result 为 pass、fail 或 unverified；pass 必须有完整六项观察，不能只验足点。画外足点等局部不适用在对应字段说明，不可豁免整个人的位置检查；没露脸的角色同样填写。任何 placement 为 fail/unverified 时，全局 staging 与总 review 均不能 pass。位置与脸分别判定，脸正确不能补偿错误站位。全景的通道、动作目标和占用空间也须独立通过。

## 续做、失效与回退

每次生成前和交接前运行 status。它会重新核对 sources、所有尝试的 inputs / outputs 及复核 evidence；文件消失、哈希变化或前一阶段未通过时停止后续流程。恢复时按 next_action 继续，不重新初始化，不重复已经通过的阶段。

旧 v1 只保留为诊断与历史依据，检查器阻止 can_continue 和完成状态，不自动改写。不能只改 schema_version 或复制旧 pass 来迁移；须根据真实调用、逐角色绑定与实际独立复核补证。允许新建文件时，使用 v2 续做记录并以 previous_record 引用旧 v1，继续累计旧重试预算；禁止新文件时不强建快照，也不擅改历史，在原位限制内无法补齐可核验记录就明确保留阻断。

如果剧本、母版、任务约束发生真正变更，或需要退回已经通过的上游阶段：在允许新文件时冻结旧记录和成果，建立带递增后缀的新记录，添加顶层 `previous_record` 文件指纹与 `revision_reason` 变更说明，scene_id 保持相同，sources 登记新的依据。已完成的目标阶段及下游不得直接沿用通过状态；仍有效的上游成果可以复用，但需要按新任务重新核对再记录，不能复制原尝试冒充本轮复核。工具沿 previous_record 链验证记录指纹，累计每阶段已经消耗的尝试和已授权扩展额度；不能通过新建续做记录刷新预算。新记录的 extensions 只写本次新授权，不复制旧额度。重复授权、循环引用或超过63次续做均会阻断。工具不自动迁移或信任旧通过结论。旧尝试用于审计，不能把更改后的文件重新算哈希后继续沿用旧复核。

自动重试耗尽时记录保持有效但 can_continue=false；超额写入尝试、缺失授权或跳阶段属于记录错误。工具不能提供不可篡改审计，记录仍是普通 JSON；append-only 是工作约定，跨版本可用仓库差异或保留快照核对。

## 维护验证

运行 `python -B .agents/skills/jianlai-scene-production/tests/test_scene_record.py`。测试使用内存资料，不创建临时、备份或候选文件；只验证流程行为和证据绑定，不进行实际出图、脸部相似性或站位正确性判断，也不进行游戏验收。
