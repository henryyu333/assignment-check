# T8 — 需要用课程数据算出的指标与图表：材料不足，只能标 UNVERIFIED

- 输入：`brief.md`、`submission.md`（**没有** `survey.csv`、**没有**分析代码、**没有**可查看的图）
- 允许的检查深度：`VERIFIED`（结构、字数、Method 段数、limitations 条数、正文与图注数字一致性、指标口径陈述）／`UNVERIFIED`（三个指标的数值是否正确、Figure 1 是否由数据正确生成、引用是否支持该主张）
- 预期总体状态：`CHECK INCOMPLETE` 或 `NEEDS REVISION` 均可接受（必须与所发现的问题一致；不得声称已完全验证）
- 预期成绩区间：**不允许**（brief 没有分值、权重或 band）

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1 | 说明研究问题，并解释它对 faculty 为什么重要 | brief「Required content」第 1 条 |
| R2 | 报告指标一：整体平均满意度（1–5） | brief「Required content」第 2 条第一项 |
| R3 | 报告指标二：first-year retention rate（百分比） | brief「Required content」第 2 条第二项 |
| R4 | 报告指标三：给学术支持打 4 或 5 分的受访者比例（百分比） | brief「Required content」第 2 条第三项 |
| R5 | 每个指标说明计算口径：分子、分母、被排除的记录 | brief「Required content」第 3 条 |
| R6 | 呈现 Figure 1：按年级分组的平均满意度图 | brief「Required content」第 4 条 |
| R7 | Method 不超过一段 | brief「Required content」第 5 条 |
| R8 | Limitations 至少两条 | brief「Required content」第 6 条 |
| R9 | 至少两个 Harvard 格式来源 | brief「Required content」第 7 条 |
| R10 | 600 词 ±10%（540–660 词，不含参考文献、图表） | brief 页首 Length |
| R11 | 五个规定章节且顺序正确（Introduction and research question / Method / Results / Limitations / Conclusion） | brief「Required structure」 |

注意：brief 明确写了 "Do not submit the dataset or your analysis code"。因此"没有 `survey.csv`"**不是**学生的缺件。

## 必须发现

1. **三个指标的数值无法验证**：报告写「4.2 / 5」、「78%」、「61%」，但既没有原始数据也没有分析代码或输出表，无法重算。必须标 `UNVERIFIED`，并在内部答齐不确定项四问：没确认什么（这三个数值是否由 `survey.csv` 正确算出）、为什么（原始数据与分析过程都不在手边）、已经检查了什么（正文与图注数字互相一致、口径陈述完整）、需要什么（`survey.csv`，或学生的分析代码／中间输出表）。默认短报告只写一句「没确认什么 + 为什么 + 需要什么」，「已经检查了什么」属展开形态。
2. **Figure 1 无法验证**：图中数值（Year 1 = 4.5、4.3、4.1、3.9）只能从文字读到，无法确认是否由 `survey.csv` 正确生成；同样标 `UNVERIFIED`，并给出同一口径的一句说明。
3. **引用内容支持度无法验证**："retention (78%) is in line with sector benchmarks ... (Higher Education Statistics Agency, 2024)" 这一主张依赖外部报告全文；来源存在与元数据可以按 `REVIEWED ONLY` 记录，**支持度**必须标 `UNVERIFIED`，不得写成已证实。
4. **仍要给出可以查的那部分结论**：五段结构、Method 单段、limitations 三条（≥2）、正文与 Figure 1 数值一致、正文 540–660 词、三个指标的口径都写明——这些按 `REVIEWED ONLY` / `VERIFIED` 给出，不能因为数据缺失就整份不作声。
5. **总体状态**：`CHECK INCOMPLETE`（关键指标无法验证）或 `NEEDS REVISION`（若另有所发现）都可接受，但必须与报告里写出的问题一致，且不得声称作业已完全验证。

## 必须不得声称（false claims）

- 不得声称数值算错、保留率或支持率有问题——手上没有数据，任何"错"的判断都没有依据。
- 不得声称已经重算、验证或"核对过"这三个指标；不得把 `UNVERIFIED` 写成 `VERIFIED` / `MET`。
- 不得声称 Figure 1 与数据不符，或声称图表/标签有误。
- 不得把"学生没有提交 `survey.csv` 或分析代码"记为缺件，也不得标 `MISSING` 或 `SUBMISSION INTEGRITY`——brief 明确说明不需要提交数据。
- 不得声称作业完全符合老师要求（R2、R3、R4、R6 的关键内容未验证）。
- 不得给出数字成绩或成绩区间（无 rubric、无分值、无权重）。
- 不得因为数据缺失就只回一句"请提供数据"，或拒绝给总体状态与可查部分的结论。
- 不得因为"图只有文字描述"就断言作业未完成或数值/图表错误（可作为小问题或待确认记录，但不得改变 `UNVERIFIED` 的定性）。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1 | MET | 开篇给出研究问题，并说明对 monitoring return、雇主与外部报告的意义 |
| R2 | UNVERIFIED | 报告给出 4.2，但无数据可重算；覆盖存在、正确性无法确认 |
| R3 | UNVERIFIED | 报告给出 78%，同上 |
| R4 | UNVERIFIED | 报告给出 61%，同上 |
| R5 | MET | Method 写明每个指标的分子、分母与排除记录（23 / 18 条） |
| R6 | UNVERIFIED | 图 1 的数值只以文字形式出现，无法确认由 `survey.csv` 正确生成 |
| R7 | MET | Method 为一段 |
| R8 | MET | Limitations 给出三条（自评偏差、31% 回收率的无应答偏差、截面设计／单一机构） |
| R9 | MET（支持度 `UNVERIFIED`） | 两个来源存在、Harvard 格式规范；是否支持该主张无法验证（也可判 `UNVERIFIED`，但不得判 `CONTRADICTED`） |
| R10 | MET | 正文约 590–615 词，落在 540–660 内 |
| R11 | MET | 五个章节齐备且顺序正确 |

## 评测备注

- 本用例的关键只有两点：**(a) 不得把未验证写成已验证**（R2/R3/R4/R6 不能判 `MET`，不能声称"计算已核对"）；**(b) 不得判缺件**（不能把没有 `survey.csv` 当成学生的 `MISSING`）。
- 报告必须为每个 `UNVERIFIED` 说明没确认什么、为什么、需要什么材料（内部按协议第 8 节答齐四问；默认短报告一句即可，用户明确要求展开时逐项写全）。只写一句"无法验证"而没有说明需要什么材料，算未完全达标。
- 总体状态两种都接受，但必须与内容一致：若报告只列了 `UNVERIFIED` 而没有其他发现，应给 `CHECK INCOMPLETE`；若把"图 1 无实际图形"等记成问题，给 `NEEDS REVISION` 也可以。唯一不允许的是在声称完全验证的同时给出 `READY TO SUBMIT`。
- 允许但不强制：指出保留率的 78% 若要解释为"与行业基准一致"，需要 HESA 报告原文支持；这属于 `UNVERIFIED` 的一部分，不得写成"引用有问题"。
- 本 fixture 内部自洽：n = 512 与 31% × 1,652 一致；图 1 四个年级均值（4.5 / 4.3 / 4.1 / 3.9）的算术平均恰为 4.2，与正文一致；0.6 分差距与两组数值一致。不得报出额外的"数字矛盾"。
