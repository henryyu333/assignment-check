# Assignment Check v1 · Validation

日期：2026-09-22

## 结论

公开仓库当前包含 **T1–T20 共 20 个独立 fixture**。其中 T17 / T18 在公开审计后补成独立的输出形态 fixture。

公开仓库现在可直接复核的是 fixture、验收口径与结构校验。开发阶段曾完成受控回归、真实 Harness 触发测试与两类 blind test；但原始 harness transcript / logs 没有随公开仓库发布。因此下面的通过率与耗时是**开发阶段记录**，不是当前公开仓库可一键复现的 benchmark。

## 1 · 公开 fixture

当前 `evals/fixtures/`：

- T1–T16
- T17 — 默认短报告形态
- T18 — 用户明确要求完整报告
- T19 — recheck ID 复用
- T20 — MATCH UNCERTAIN

合计：**20 个独立 fixture 目录**。

它们覆盖：

- Essay 漏要求
- 数学答案正确但推导错误
- 代码漏行为要求
- 引用存在性 / 元数据 / 支持关系分层
- 完整 rubric / 无 rubric
- 只有提交物
- 无法验证的来源数据
- brief / rubric 冲突
- “分别描述”但没有真正 compare
- prompt injection
- PDF 图表未抽取
- 引用真实但不支持主张
- 危险代码
- 修改后回归
- 要求歧义
- 默认短报告 / 完整报告
- recheck ID 复用与 MATCH UNCERTAIN

> T17 / T18 是在公开审计后补成的 standalone fixture。补齐后，当前版本**尚未重新执行一次完整的 20-case harness 回归**，因此这里不把“当前版本 = 20/20”作为新的可复核结论。

### 自动结构校验

`.github/workflows/validate.yml` 会在 push / pull request 时检查：Skill 核心文件、frontmatter 关键字段、20 个 fixture 与各自 `expected.md`、T14 危险代码保持不可执行 `.txt` 形式、README 当前预览图路径，以及已知旧资产 / 旧用户名残留。

这个 workflow 只验证**公开仓库结构与安全约束没有退化**，不声称代替真实 Agent Harness 的行为评测。

## 2 · 历史开发阶段受控回归

性能重构阶段曾记录一次全量回归：**20/20 的总体状态与预埋核心问题命中**。

该次运行中，T13 的默认短报告形态仍有偏差；后续补丁把引用三层提升为运行时 invariant 后，T13 又做了两次独立运行并记录为 **2/2 PASS**。

这些结果来自开发阶段 harness 记录。公开仓库保留 fixtures 与验收口径，但**不包含当时的完整 transcript / runner logs**，因此第三方目前可以审阅测试设计，不能仅凭仓库内容独立复核这些历史通过率。

## 3 · 历史真实 Harness 触发

开发阶段记录：

- 早期完整触发验收：正例 **4/4**，负例 **2/2**
- 性能重构后 smoke test：正例 **2/2**，负例 **2/2**

触发证据当时基于实际 Skill 加载行为，而不是仅凭回答风格判断。原始事件流未随公开仓库发布。

## 4 · 历史 blind test

### Blind A — Writing / Research

开发阶段最终记录：

- PASS
- runtime：约 **76 秒**
- 外部来源核验目标：3 个
- 总体：`NEEDS REVISION`

记录的关键命中包括来源质量、年份 / 主张错配与无引用经验主张。

### Blind B — Code / Data

开发阶段记录：

- PASS
- runtime：约 **183 秒**
- 总体：`NEEDS REVISION`

记录的关键命中包括空值处理、`dropped.log` 缺失、重算不一致、输出路径错误与 README 缺失。

> 以上耗时只代表当时测试环境，不是固定 SLA，也不是当前仓库可直接复现的 benchmark。

## 5 · 安全与确定性

公开规格要求：

- 不把解析失败当成 `MISSING`
- 不在 brief / rubric 冲突时擅自选边
- 危险代码在安全条件不足时不运行
- 联网得到并用于 finding 的外部事实必须可追溯
- 不满足条件时不输出 unsupported numeric grade
- `READY TO SUBMIT` 不因为性能预算而放宽

**边界：**这些是 Skill 对宿主 Agent 的行为约束。真正的沙箱、网络隔离、文件权限、进程限制和凭据保护由宿主环境提供；Assignment Check 本身不实现运行时沙箱。

## 6 · 性能设计

运行核心采用：

1. Pass 1：不联网的全要求覆盖扫描
2. Pass 2：只对高价值问题做定向验证
3. Fail fast：`NEEDS REVISION` + 3 个已验证 Top 问题后默认停止继续联网
4. READY 候选仍从严验证
5. 单次运行内复用结果、计数与文件证据
6. 完整 protocol 按需加载

当前 `SKILL.md` 约 12 KB；完整 protocol 保留为按需规格文件。

## 7 · 解释边界

- fixture 通过不代表真实作业不存在未知边界
- 历史 harness 记录不等于公开可复现 benchmark
- blind test 通过不代表所有学科都达到专家级验证深度
- 运行时间会随模型、网络、文件长度和外部来源数量显著变化
- `READY TO SUBMIT` 不是成绩保证
- 无法可靠读取或验证的内容应继续标为 `UNVERIFIED` / `NEEDS CLARIFICATION`
