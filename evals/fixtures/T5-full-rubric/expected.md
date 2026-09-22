# T5 — 带完整 Rubric 的 case study：反方视角缺失 + 来源数量不足

- 输入：`brief.md`、`rubric.md`、`submission.md`
- 允许的检查深度：`VERIFIED` / `REVIEWED ONLY` 均可接受（所有材料可读；表格数字可重算，属 `VERIFIED`；论证质量属 `REVIEWED ONLY`。本用例不应出现 `UNVERIFIED` 作为主要判断）
- 预期总体状态：`NEEDS REVISION`
- 预期成绩区间：**允许但非必需**（rubric 有权重与 band，四条 criterion 都可读，每条的 band 都有证据；若给出，必须标注为估计并说明未验证部分）

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1 | 明确陈述 Board 面临的决定，并说明该决定为何重要 | brief「Required content」第 1 条 |
| R2 | Executive summary，不超过 150 词 | brief「Required structure」第 1 项 |
| R3 | 报告含四个规定章节且顺序正确：Executive summary / Analysis / Recommendation / References | brief「Required structure」 |
| R4 | 在给出推荐之前分析 **both** options（Option A 与 Option B） | brief「Required content」第 2 条 |
| R5 | **至少一个 counter-perspective**：给出反对自己推荐的最强论证并回应 | brief「Required content」第 3 条 |
| R6 | 给出明确 recommendation，并用分析中的证据论证 | brief「Required content」第 4 条 |
| R7 | 至少 4 个可信来源，Harvard 格式，正文与参考文献都要有 | brief「Required content」第 5 条 |
| R8 | 至少一张图或表，且与正文数字一致 | brief「Required content」第 6 条 |
| R9 | 900 词 ±10%（810–990 词，不含参考文献、图表） | brief「Required content」第 7 条 / 页首 Word limit |
| R10 | Rubric **Criterion A — Problem framing (20%)** | rubric row 1 |
| R11 | Rubric **Criterion B — Analysis (40%)**：复合，含 B1 清晰论证 / B2 counter-perspective / B3 结论有证据支持 | rubric row 2 |
| R12 | Rubric **Criterion C — Use of evidence (25%)**：复合，含 C1 至少四个来源 / C2 图表与正文一致 | rubric row 3 |
| R13 | Rubric **Criterion D — Presentation (15%)**：结构、Harvard 格式、字数 | rubric row 4 |

R5 是 R11（Criterion B）的子项；R7、R8 是 R12（Criterion C）的子项；R2、R3、R9 与 R13（Criterion D）相关。子项只能用于检查覆盖，不得各算成一个 criterion，也不得重复计入权重。

## 必须发现

1. **R5 / Criterion B 的 B2 子项缺失**：全文没有任何反方视角——没有出现"反对迁移的最强论证"，也没有对这类论证作出回应；推荐方向自始至终没有被挑战过。必须把它挂在 **Criterion B** 名下，说明 B 只能落在「65–79」档（"the counter-perspective is weak, partial or absent"），即 `PARTIAL`。
2. **R7 / Criterion C 的 C1 子项不足**：参考文献只有 3 条（Chen and Patel, 2023；Deloitte, 2024；Sharma, 2022），少于老师要求的 4 条。必须给出"只有 3 条"这一可核查的事实，并说明 C 只能 `PARTIAL`。
3. **复合结构不得被拆散或重复计分**：Criterion B 的三个子项、Criterion C 的两个子项必须作为一个 criterion 内部的分项呈现；不得推出第 5、第 6 个 criterion，也不得把 20/40/25/15 的权重重复累加（四项权重之和必须仍是 100%）。
4. **总体状态为 `NEEDS REVISION`**：因为存在明确未完成的要求（R5 缺失、R7 不足）。
5. **判分依据必须引用 rubric 原文措辞**：例如引用 "the counter-perspective is weak, partial or absent"、"Fewer than four credible sources" 等原文，而不是自造描述。

## 必须不得声称（false claims）

- 不得声称报告包含反方视角，或把 Criterion B 判为 `MET` / 落在 80–100 档。
- 不得声称来源数量达到 4 个及以上，或把 Criterion C 判为 `MET`。
- 不得添加 rubric 之外的 criterion（如"文笔流畅度""创新性""图表美观度"）。
- 不得把 Criterion B / C 的子项各算成一个独立 criterion，或按子项重复累加权重（不得出现 20+40+25+15 之外的计分结构）。
- 不得给出单一精确分数冒充老师的最终成绩；若给区间，必须标明是估计，并说明未验证部分。
- 不得声称 Table 1 与正文不一致或算术有误（表内 4.2+3.5+2.1=9.8、1.1+5.9+5.4=12.4，正文引用的 £9.8m / £12.4m / £2.6m 均一致）。
- 不得声称字数超限或章节缺失（正文约 880 词，含表格行约 906 词，均落在 810–990 内；四个章节齐全）。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1 | MET | 「What the Board is deciding」明确写出决定内容，并给出重要性（系统地位、2025 停机、18% 收入、SLA credits） |
| R2 | MET | Executive summary 约 106 词，未超 150 |
| R3 | MET | 四个章节齐备且顺序正确 |
| R4 | MET | Analysis 分别给出 Option A、Option B，并用 Table 1 在同一成本维度上直接对照 |
| R5 | MISSING | 全文无任何反方视角或对反对意见的回应 |
| R6 | MET | 「Recommendation」给出明确动作（approve Option A、Q1 2027 起分阶段迁移）并回指 Table 1 的对比 |
| R7 | PARTIAL | 只有 3 个来源，少于 4 个；格式本身规范 |
| R8 | MET | Table 1 存在且与正文一致 |
| R9 | MET | 正文约 880 词（不含表格与参考文献），落在 810–990 内 |
| R10 | MET | 问题陈述与重要性都具体（Criterion A 的复合两项均满足） |
| R11 | PARTIAL | 三个子项中 B1、B3 满足，B2 完全缺失 → 落在 65–79 档 |
| R12 | PARTIAL | 子项 C1 不足（3 < 4），C2 满足 → 落在 50–64 或 65–79 之间的表述均可，但必须 `PARTIAL` |
| R13 | MET | 结构、Harvard 格式、字数三项均满足（若判 `PARTIAL`，必须给出具体依据，例如把 R7 的来源数量算进 D；但 D 的 text 只涉及 structure / citation format / word count） |

## 默认必须展示 / 完整报告必须检出（T17 / T18 共用）

**T17（默认短报告）必须可见**：总体状态 `NEEDS REVISION`；两项核心问题进入"最该先改"（反方视角缺失、来源少于 4 个）；检查项统计；无法确认项数或一句压缩说明；不得出现完整要求表 / Markdown ledger。

**T18（用户明确要求展开）必须检出**：完整 Requirement Ledger（含 rubric 原文措辞）；四个 criterion 的分档判断挂在父 criterion 名下、权重只算一次（20/40/25/15 = 100%）；全部详细问题六要素；未验证事项按协议第 8 节四问逐项写全；优点 1–3 条；成绩依据（给出时必须标明为估计并说明未验证部分）。

## 评测备注

- 本 fixture 的 **brief 里有两条「要求 6 / Guidance」相关的要求**，submission 在这两处也确有真实缺陷（非本次故意预埋，但属于真实发现，命中不算错、不命中也不判失败）：
  - 表中数字（18% revenue、4% SLA credits、£0.64m、2027 硬件更换等）是按 brief 允许的方式虚构的，但 **brief 要求「say where you have done so」，submission 没有标注**；
  - 正文写交叉点「在第三到第四年……which is the pattern Table 1 shows」，而 Table 1 只有五年合计，**表里看不出任何交叉年**。

- 判分重点只有两条：(a) 反方视角缺失是否被发现；(b) 是否把它正确挂在 **Criterion B** 下、把来源不足正确挂在 **Criterion C** 下，并且没有把子项拆成独立 criterion 或重复计分。
- 报告必须用 rubric 原文措辞说明当前 band 与差距（例如 "the counter-perspective is weak, partial or absent"、"Fewer than four credible sources"），这是本用例的硬性检查点。
- 成绩区间允许但不强制：给区间时必须标明是估计；不给区间、只给 readiness 与修改优先级同样通过。出现"最终成绩 X 分"这类表述即失败。
- R13 判 `MET` 与判 `PARTIAL` 都可接受（`PARTIAL` 需给出依据）；R10 若判 `PARTIAL` 也可接受，条件是必须引用 Criterion A 原文说明差在哪一项。
- 本用例不测试默认短报告形态（那是 T17）；也不测试复查（那是 T19/T20）。
