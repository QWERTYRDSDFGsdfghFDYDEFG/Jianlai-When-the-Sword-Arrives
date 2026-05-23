# 00_MASTER_PROMPT - Codex 工程入口规则

## 读取顺序

Codex 进入本工程后，默认先读取根目录 `README.md`。

在开始任何修改前，继续读取：

1. `Codex/00_MASTER_PROMPT.md`
2. `GDD.md`
3. `Codex/01_FIRST_PLAYABLE.md`
4. 与任务直接相关的 `.rpy`、美术、音频或数据文件

其中 `Codex/01_FIRST_PLAYABLE.md` 只负责定义“第一版可玩原型”的目标、范围、验收与测试流程；通用规则以本文档为准。

如果用户明确指定额外文件，则以用户指定文件为准，并在发现路径不存在时说明实际情况。

## 项目定位

本项目是基于《剑来》书简湖篇改编的 Ren'Py 视觉小说原型。

开发目标不是自由重写一个新项目，而是在现有工程结构内逐步补齐：

- 剧情章节
- 角色对白
- 背景与立绘演出
- 音频氛围
- 选择与状态反馈
- 存档、读档和基础 UI 流程

## 执行原则

- 先保证项目可运行，再增强表现。
- 优先沿用现有 Ren'Py 脚本结构和角色定义。
- 不一次性重写目录结构。
- 不擅自删除已有素材、章节或系统文件。
- 改剧情时保持书简湖篇的慢节奏、沉静感、压抑感和问心主题。
- 文本进入 `.rpy` 时，拆成适合视觉小说阅读的短旁白和短对白。
- 新增角色名必须先确认或补充到 `characters.rpy`。
- 发现设计不清楚时，先记录问题或在回复中说明，不擅自偏离核心方向。

## 长会话工作策略

Codex can get dumber and slower on long sessions.

Here's the fix:

1. Run Process_narration=false

This will stop Codex from showing you all the planning steps, resulting in saving a lot of output tokens.

2. Prompt: "Act as an orchestrator. Use parallel agents to do the research and execution work. Write detailed tasks for each parallel agent and force them to act, iterate, get their tasks done, and bring back an in-depth report. Your job is to deeply analyze the agents' work, provide feedback, and provide them with continuous tasks."

This prompt offloads the majority of the context-burning work to agents, and each agent has its own context window. So you can utilize 5 agents (5 context windows).

3. Add this hard rule: "Measure twice, cut once policy."

Debugging and patching is messy work. Force Codex to plan first, act after (don't use plan mode; it's just overcomplicated). Ask it to make a task list for every task so it can track progress and iterate better.

4. Add this hard rule: "Keep the codebase clean, no tmp files, no dead code, no dead files. Stay organized all the time. No unnecessary folders, subfolders, or files."

## 每次任务交付

完成修改后，说明：

- 修改了哪些文件
- 实现了什么
- 做过哪些验证
- 哪些验证因为缺少工具或环境无法执行

如果 Ren'Py 可执行环境不可用，至少进行静态检查，例如：

- 引号是否闭合
- label / jump 是否存在明显断链
- 角色变量是否已定义
- 是否存在明显乱码、TODO、占位符或跨行字符串错误
