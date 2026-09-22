# Assignment Check v1 · Validation

日期：2026-09-22

## 结论

**v1 已完成受控回归、真实 harness 触发测试和两类盲测。最终性能补丁未发现新的阻断性问题。**

## 1 · 受控 fixture

T1–T20 覆盖：

- Essay 漏要求
- 数学答案正确但推导错误
- 代码漏行为要求
- 引用存在性 / 元数据 / 支持关系分层
- 完整 rubric
- 无 rubric
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

性能重构版完成了一次全量 T1–T20 回归：**20/20 的总体状态与预埋核心问题命中**。其中 T13 当时仍有默认短报告形态偏差，因此没有把那一次结果当成最终的引用分层稳定性证明。

最终补丁把引用三层提升为运行时 invariant 后，T13 连续独立运行 **2/2 PASS**：

- 来源存在性：独立 verification status
- 元数据：独立 verification status
- 是否支持主张：独立 verification status

两次都正确判为 `NEEDS REVISION`，并识别 Finn & Achilles 1999 的班级规模主张错配。

## 2 · 真实 Harness 触发

在真实 Agent Harness 中，以全量 Skill discovery、全新会话运行：

早期完整触发验收：

- 正例：**4/4 自动触发**
- 负例：**2/2 不误触发**

性能重构后又做了触发 smoke test：

- 正例：**2/2**
- 负例：**2/2**

触发验收以实际 Skill 加载行为为准，不依赖回答风格猜测。

## 3 · 真实感盲测

### Blind A — 写作 / Research

最终性能补丁后的独立运行：

- **PASS**
- runtime：约 **76 秒**
- 外部来源核验目标：**3 个**
- 总体：`NEEDS REVISION`

关键问题保持命中：

- MigrantVoice “70%” 统计来源质量问题，并识别链接 404；
- De Brauw 年份 / 主张错配；
- 无引用的 3,200 美元经验主张；
- 外部事实均保持可追溯来源。

最早同一类盲测约 596 秒；性能收敛后降到约 76 秒。该数字只代表本次测试环境，不是固定 SLA。

### Blind B — Code / Data

性能重构验收运行：

- **PASS**
- runtime：约 **183 秒**
- 总体：`NEEDS REVISION`

命中：

- 空值行处理问题；
- `dropped.log` 缺失；
- 汇总值重算不一致；
- summary 输出路径错误；
- README 缺失；
- 同时保留对正确部分的肯定。

## 4 · 安全与确定性

验收中持续检查：

- 不把解析失败当成 `MISSING`；
- 不在 brief / rubric 冲突时擅自选边；
- 危险代码不安全执行；
- 联网得到并用于 finding 的外部事实必须可追溯；
- 不满足条件时不输出 unsupported numeric grade；
- `READY TO SUBMIT` 不因为性能预算而放宽。

## 5 · 性能设计

最终运行核心采用：

1. **Pass 1：不联网的全要求覆盖扫描**
2. **Pass 2：只对高价值问题做定向验证**
3. **Fail fast：NEEDS REVISION + 3 个已验证 Top 问题后默认停止继续联网**
4. **READY 候选仍从严验证**
5. 结果、计数、文件证据在单次运行内复用，避免重复读取与重复计算
6. 完整 protocol 按需加载，不再每次启动都强制读入

当前 `SKILL.md` 约 **12 KB** mandatory runtime instructions；完整 protocol 保留为按需规格文件。

## 6 · 解释边界

- 受控 fixture 通过不代表真实作业不存在未知边界；
- 盲测通过不代表所有学科都达到专家级验证深度；
- 运行时间会随模型、网络、文件长度和外部来源数量显著变化；
- `READY TO SUBMIT` 不是成绩保证；
- 无法可靠读取或验证的内容应继续标为 `UNVERIFIED` / `NEEDS CLARIFICATION`。
