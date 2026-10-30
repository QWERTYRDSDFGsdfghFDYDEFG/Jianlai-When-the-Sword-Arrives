# 单图制作记录与检查工具

记录采用 `assets/scene-record.template.json` 的 v1 结构。一张图一份记录；同一场次的独立背景、人物差分可分别建记录，用 `sources` 互相引用已确认依据。默认记录放 `work/art/<scene_id>/record.json`，图片过程稿仍留生成器工作区，不复制进 `game/`。已有记录不要重新初始化或覆盖。

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
- `sources`：剧本版本、任务单、角色标准、母版、相邻镜头、画风依据的文件指纹。任务单须真实写成文件，包含剧情范围和验收条件；至少登记它及适用的权威依据。对内容将继续修改的文档，另存本次批准范围的快照，避免把旧证据静默改写。
  尤其是 `character_image_index.md`：任务输入使用相关条目的冻结摘录或权威依据快照，并注明来源路径与原始文件哈希；持续更新的素材登记、索引日志本身不作为制作输入，避免例行登记使本次记录自行失效。每次续做仍须核对最新权威来源；母版或剧情的实质变更必须建立新基线，不能用快照掩盖变化。
- `constraints`：`locked` 固定项、`allowed_changes` 允许变化项、`uncertainties` 未解决且会改变制作的冲突。前两项必须在 brief 通过前填好；有实质冲突不得把 brief 标为通过。
- `retry_policy`：默认 `max_reworks: 2`，即每阶段首稿加两次自动返工。额外次数只通过 `extensions` 添加，结构为 `{ "stage": "sketch", "extra_reworks": 1, "authorization": "用户明确允许再修一次的原话/位置" }`。
- `stages`：固定为 brief、references、composition、space、sketch、color、preview、delivery。每项含 `status`、`required_checks`、`attempts`。`status` 只能是 pending、in_progress、passed、blocked。可以增加检查项，不能删掉模板中的必查项；所有阶段都有实际成果，不以“无需3D”为由跳过空间检查。
- `adoption`：`status` 为 candidate 或 confirmed；confirmed 必须有用户采用依据 `authorization`。`selected` 保存交付图指纹，必须对应某次实际制作输出。`asset_specs` 每项含 `asset` 指纹、实际 `width` / `height`、`format`（例如 PNG RGBA）、`display_treatment`（如原生1672×941，运行缩放到1920×1080）。交付完成时每张选中图必须有规格；用实际图片元数据读取结果填写，在 provenance 证据里保留核验结果，不能只复制目标尺寸。工具检查声明和绑定，不解码图片验证尺寸。`integration` 含 `status`（not_requested、pending、passed）、单独的接入授权 `authorization` 与实际验收文件 `evidence`。候选完成不代表用户定稿；integrate 范围必须等运行验收后才能标成完成。

所有指纹统一为 `{ "path": "绝对路径或相对记录所在目录的路径", "sha256": "64位摘要", "role": "这份文件负责证明什么" }`。selected 仅接受已通过阶段的末次输出，旧失败稿不能混入；游戏运行通过状态不得早于 preview 通过。不把凭证或包含凭证的文件纳入资料包。

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

`kind` 为 plan、image 或 verification。前四阶段只做规划，不允许 kind=image。inputs / outputs 都是指纹列表；执行前登记输入，生成或写作后补齐成果，再送审。brief 输入至少绑定一个 sources 文件，其余阶段至少绑定上一阶段最新输出，防止拿无关资料跳过依赖。只有末次 in_progress 尝试可以暂时没有输出或 review；已审尝试必须有输出。不同尝试的成果使用不同文件路径，不能覆盖上一张。规划阶段可以用任务单、站位文字或 SVG，不强制生成图片。实际生成过程原生尺寸、目标尺寸偏差、工具失败等在成果或检查观察中明确记录。

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
  ]
}
```

例子中的空 evidence 不能提交为已检查记录：每条必须填写实际检查过的文件指纹，如原图、对照图、局部截图、布局说明、运行截图或日志；一轮复核的证据合计必须至少包含本次输出，不能只引用旧图或需求文档。视觉检查的证据须指向图像，只有文字声明不能代替看图。核证者必须真的查看原始需求和图像；名称不同并不能从技术上证明代理独立，工具仅检查填写关系。sketch、color、preview 必须由独立代理复核；规划和交付登记允许协调者自检。

- `verdict` 为 pass、rework、blocked；检查结果为 pass、fail、unverified、not_applicable。
- 每次复核须覆盖该阶段全部 required_checks。pass 不能含 fail、unverified 或未解决的 hard 问题。hard 不能靠 accepted 绕过。
- not_applicable 仅用于条件项：空背景的 identity_basis / identity / anatomy；无接触或足点的 grounding；单张扁平CG的 actual_composite；明确非游戏用途的 dialogue_safe_area。观察里必须说明为何不适用并附场景依据。
- 问题 `severity` 为 hard 或 soft，`state` 为 open、resolved、accepted。soft 可由复核说明限制后保留，不把模型偏好冒充用户认可。rework 必须有具体 finding。
- 在需要独立复核的三个阶段，独立代理不可用时保持 review 为 null 或 verdict 为 blocked，据实交付“独立复核未执行”，不要给同一代理另起名字。

## 续做、失效与回退

每次生成前和交接前运行 status。它会重新核对 sources、所有尝试的 inputs / outputs 及复核 evidence；文件消失、哈希变化或前一阶段未通过时停止后续流程。恢复时按 next_action 继续，不重新初始化，不重复已经通过的阶段。

如果剧本、母版、任务约束发生真正变更，或需要退回一个已经通过的上游阶段：先冻结旧记录和旧成果，建立带递增后缀的新记录，添加顶层 `previous_record` 文件指纹与 `revision_reason` 变更说明，scene_id 保持相同，sources 登记新的依据。已完成的目标阶段及下游不得直接沿用通过状态；仍有效的上游成果可以复用，但需要按新任务重新核对再记录，不能复制原尝试冒充本轮复核。工具沿 previous_record 链验证记录指纹，累计每阶段已经消耗的尝试和已授权扩展额度；不能通过新建续做记录刷新预算。新记录的 extensions 只写本次新授权，不复制旧额度。重复授权、循环引用或超过63次续做均会阻断。工具不自动迁移或信任旧通过结论。旧尝试用于审计，不能把更改后的文件重新算哈希后继续沿用旧复核。

自动重试耗尽时记录保持有效但 can_continue=false；超额写入尝试、缺失授权或跳阶段属于记录错误。工具不能提供不可篡改审计，记录仍是普通 JSON；append-only 是工作约定，跨版本可用仓库差异或保留快照核对。

## 维护验证

运行 `python -B .agents/skills/jianlai-scene-production/tests/test_scene_record.py`。测试资料写到系统临时目录并保留，或用环境变量 `SCENE_RECORD_TEST_ROOT` 指定已存在的工作区目录；不自动删除任何目录。测试只验证流程行为和证据绑定，不进行实际出图或游戏验收。
