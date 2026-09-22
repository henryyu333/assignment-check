# T1 — Essay：四条要求都写在 brief 里，学生漏掉"必须给出自己的判断"这一条

- 输入：`brief.md`（PSY2004 作业要求）、`submission.md`（学生 essay；按不同合理标题口径，正文为 601–646 个空白分词 token + 参考文献表）
- 允许的验证状态：字数必须实际清点并标 `VERIFIED`；命题内容判断可标 `REVIEWED ONLY`
- 预期总体状态：`NEEDS REVISION`
- 预期成绩区间：不允许（无 rubric、无分值/权重/performance band，不满足协议第 10 节任何条件）

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1a | 用自己的话定义 dual-process theory（不得照抄讲义或字典定义） | brief 第 1 条 |
| R1b | 给出一个日常例子，说明两种加工的差异 | brief 第 1 条 |
| R2 | 说明 Kahneman 传统与 Gigerenzer 传统在"启发式是否有用"上的分歧，写出各自主张 | brief 第 2 条 |
| R3 | 在 predictive accuracy 维度上判断哪一派更有说服力，并给出理由 | brief 第 3 条 |
| R4a | 至少引用两篇 peer-reviewed 来源 | brief 第 4 条 |
| R4b | 参考文献表按 APA 7 列出 | brief 第 4 条 |
| R5 | 正文 600–750 词（不含参考文献表） | brief「Format」节 |

（R1a/R1b 是 brief 第 1 条拆出的原子要求；R4a/R4b 是第 4 条拆出的原子要求。允许拆得更细或合并为 R1/R4，但四条 brief 要求必须全部出现，且 R3 必须作为独立条目可辨识。）

## 必须发现

1. **R3 完全缺失**：全文没有任何一处回答"哪一派更有说服力"。第 5 节结尾只写 Both perspectives have merit，属于回避判断，不构成第 3 条要求的"判断 + 理由"。
2. R3 的缺失必须映射到 brief 第 3 条（predictive accuracy 维度上的判断），并说明缺席位置：第 5 节（结论段）以及全文。
3. 字数必须实际清点并说明口径。按空白分词：References 前全部内容（含文档标题和小标题）646；去掉文档总标题 636；去掉所有 Markdown 标题 601。三种合理口径都落在 600–750 内 → R5 = `MET`。不得制造“可能低于 600”的假风险；只凭感觉估算、或把参考文献表算进正文导致判超限，都算未完成检查。
4. 两条 peer-reviewed 来源判为真实存在且够数：Tversky & Kahneman (1974, *Science*) 与 Gigerenzer & Gaissmaier (2011, *Annual Review of Psychology*) → R4a = `MET`；Kahneman (2011) 是专著，不计入"两篇 peer-reviewed"。
5. 定义（第 1 节）与日常例子（第 2 节，开车回家／儿童冲上马路）都是学生自己的表述，且第 2 节确实对应"两种加工的差异" → R1a/R1b = `MET`。
6. 两派分歧（第 3、4 节）分别写出 Kahneman/Tversky 的"捷径导致系统性偏差"与 Gigerenzer 的"生态理性、少即是多" → R2 = `MET`。

## 必须不得声称（false claims）

- 不得声称学生给出了"哪一派更有说服力"的判断，或声称 R3 只是"论述不够充分"（该动作完全缺席）。
- 不得声称"没有 rubric，所以无法检查 / 无法判断"——老师材料（brief 四条要求）足以建立 ledger 并给总体状态。
- 不得给出任何数字成绩、百分比、分数区间或估算得分。
- 不得声称参考文献格式存在实质错误并因此扣 R4b（示例的 APA 7 格式是规范的）；若提 minor 排版偏好，必须标 `GENERAL ADVICE` 且不作为失分依据。
- 不得声称已运行计算/查重/AI 检测类工具。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1a | MET | 第 1 节用自己的话描述两种加工（快/自动/无意识 vs 慢/刻意/可检查），无照抄痕迹 |
| R1b | MET | 第 2 节开车回家 + 儿童冲上马路的例子，落在 System 1 / System 2 的切换上 |
| R2 | MET | 第 3 节写 Kahneman/Tversky 视启发式为系统性误差来源；第 4 节写 Gigerenzer 的生态理性与少即是多 |
| R3 | `MISSING` | 全文无任何立场判断；第 5 节以"双方各有道理"收尾。**必须是 MISSING，不得写成 PARTIAL、UNVERIFIED 或 NEEDS CLARIFICATION** |
| R4a | MET | 两条同行评审期刊论文（Science 1974；Annual Review of Psychology 2011） |
| R4b | MET | 参考文献表符合 APA 7（作者、年份、刊名斜体、卷号斜体、页码、DOI） |
| R5 | MET | 实际清点：646（含全部标题）/ 636（不含文档总标题）/ 601（不含全部 Markdown 标题），所有合理口径都在 600–750 内 |

## 默认必须展示 / 完整报告必须检出

**默认运行（用户未要求展开）必须可见**：总体状态 `NEEDS REVISION`；R3 缺失进入"最该先改"（含位置与理由）；检查项统计里体现该缺失（`1 缺失` 或等价的缺失计数）。

**完整报告（用户明确要求展开）必须检出**：字数三种口径的实际清点（601 / 636 / 646）与 `R5 = MET`；R1a / R1b / R2 / R4a / R4b 的逐条状态 + 证据位置；两条同行评审来源的认定（Kahneman 2011 是专著，不计入）。

## 评测备注

- 最关键的三条：(1) R3 = `MISSING` 且进入"最该先改的前 3 项"；(2) 字数被实际清点后判 `MET`，且不得声称存在低于 600 的合理计数；(3) 总体状态为 `NEEDS REVISION`。任何一条错，本 fixture 判失败。
- 短报告形态：总体状态 + 最该先改的 1–3 项 + 要求统计（此处应为 6 完成 · 0 部分完成 · 1 缺失）+ 无法确认项数。要求统计里出现"1 缺失"是 R3 被正确识别的直接证据。
- 允许但不强制：指出第 5 节的模糊结论是"回避判断"而非"判断较弱"；建议在 predictive accuracy 维度上给出可比较的标准（如预测效度研究、实验室 vs 野外的外部效度）。这些属于修改方向，不是新 finding。
- 判定 R3 时的边界：第 4 节"a one-reason decision rule matches or beats a regression model in forecasting tasks"是在**转述 Gigerenzer 一方的主张**（brief 第 2 条要求的内容），不是学生自己的判断，不能算作 R3 的部分完成；把这句话当作 R3 = `PARTIAL` 的依据判失败。
- 允许但不强制：把 R3 缺失标为"严重"（核心要求未完成）或"重要"（影响某个 criterion）。两种都接受，但必须给出位置 + 证据 + 理由 + 修改方向。
- 不接受的写法：只在报告里提"论述可以更深入"而没把 R3 映射到 brief 第 3 条；或把"两种观点各有道理"当成分歧讨论的完成（那只满足 R2，不满足 R3）。
