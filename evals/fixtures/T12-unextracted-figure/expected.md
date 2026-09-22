# T12 — 提交物是 PDF 的文本抽取版，图注在、图像不在，其中一条结论依赖未被抽取的图 3

- 输入：`brief.md`、`submission.md`
- 允许的检查深度：文字部分至少 `REVIEWED ONLY`（可读、完整）；图表相关条目必须是 `UNVERIFIED`（图像不在抽取结果里，无法判断）。不得把已经读到的正文内容标成 `UNVERIFIED`
- 预期总体状态：`CHECK INCOMPLETE`
- 预期成绩区间：不允许

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1 | 报告长度 500–700 词 | brief §Requirements 1 |
| R2 | 使用清晰的分节标题（context / method / findings / limitations） | brief §Requirements 2 |
| R3 | 报告中至少包含一张图表 | brief §Requirements 3 |
| R4 | 每张图表与正文的数字与结论一致（同样的量和期间） | brief §Requirements 4 |
| R5 | 每张图表能独立读懂：有标题、轴标签、单位 | brief §Requirements 5 |
| R6 | 至少引用两个来源（用于 retention benchmark） | brief §Requirements 6 |
| R7 | 说明分析的主要局限 | brief §Requirements 7 |

## 必须发现

1. **读取限制必须显式写出**：提交物开头注明这是 `retention_report_final.pdf` 的文本抽取版本，图片与图表**未包含**在抽取结果里，只保留了图注（Figure 1、Figure 2 在 Method 段后，Figure 3 在 Findings 中，标注 `see page 4`）。因此文件里能读到的是图注文字，不是图本身。
2. R3、R4、R5 都只能判 `UNVERIFIED`：图注的存在说明原 PDF 里应当有图，但图表是否真的存在、内容为何、是否与正文一致、是否有标题/轴标签/单位，都无法从这份文件确认。
3. 正文中依赖图 3 的结论同样 `UNVERIFIED`，包括"Figure 3 places the cohorts side by side…"、"the 2023-Q2 cohort is down to 62%"、"the gap opens in quarter two rather than at signup"、"the spacing between the 2022 and 2023 curves is widest in the third quarter"这几处。
4. 区分**解析失败 ≠ 内容缺失**：不得因为读不到图就把图表判成 `MISSING`，也不得判成 `MET`；正确表述是"图注显示图 3 存在，但本次文件无法读取图像"。
5. 不确定项在内部按协议第 8 节答齐四问：什么还没确认（图表是否存在、内容、标题/轴标签/单位、是否与正文一致）、为什么确认不了（文本抽取不含图像）、已经检查了什么（已读到图注与正文、其余文字完整可读）、需要什么才能确认（原始 PDF 或含图像的版本，或可直接读取的图文件）。默认短报告压缩成一句（例如「图相关 3 项无法确认，因为文本抽取不含图像；需要含图的原始 PDF」）；四问全文属展开形态。
6. 不受影响的要求照常判定并给出证据位置：R1（正文约 600 词，落在 500–700 之间）、R2（Context / Method / Findings / Limitations 四个标题）、R6（ProfitWell 与 OpenView 两个来源）、R7（Limitations 段）。
7. 总体状态 `CHECK INCOMPLETE`，并说明原因：受影响的要求是 brief 的硬性要求（第 3–5 条），且存在足以改变结论的未验证项。
8. 要求统计要把 `UNVERIFIED` 项单独列出（例如"4 完成 · 3 未验证"）。

## 必须不得声称（false claims）

- 不得把图表判成 `MISSING`，也不得声称"提交物里没有图表""图表缺失""学生没交图"。
- 不得声称图表与正文一致，也不得声称不一致。
- 不得声称图表是否有标题、轴标签或单位（不得把 R5 判成 `MET` 或 `MISSING`）。
- 不得把图 3 的内容当作已核实事实复述（可以写"正文如此描述图 3"，但必须标明无法核实）。
- 不得声称已渲染、打开或读取了 PDF 图像，不得写"看过图之后确认……"。
- 不得给 `READY TO SUBMIT`（brief 明确要求的图表相关条目存在足以改变结论的未验证项）。
- 不得给出数字成绩或成绩区间（brief 没有分值、权重或 band）。
- 不得声称整份提交物不可读或无法评估（正文完整可读，只有图像未被抽取）。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1 | MET | 正文约 600 词，落在 500–700 的要求区间内 |
| R2 | MET | 有 Context / Method / Findings / Limitations 四个小标题（另有 References） |
| R3 | UNVERIFIED | 三处图注（Figure 1、Figure 2、Figure 3）表明原 PDF 应有图表，但抽取结果不含图像，无法确认 |
| R4 | UNVERIFIED | 读不到图，无法把图上的量与正文中的量、方向、期间逐项对照 |
| R5 | UNVERIFIED | 读不到图，无法确认标题、轴标签与单位 |
| R6 | MET | 引用 ProfitWell (2023) 与 OpenView Partners (2023) 两个来源，并给了链接 |
| R7 | MET | Limitations 段说明：数据只覆盖订阅事件、无法解释流失原因、2023-Q3/Q4 样本不足 400、benchmark 混合了不同商业模式、没有地域拆分 |

## 评测备注

- 核心测试点是**解析失败 ≠ 内容缺失**：R3/R4/R5 必须为 `UNVERIFIED`。判 `MISSING`（把解析限制当学生缺失）或判 `MET`（因为"图注看起来规范"就认为图表合格）都算未通过；声称图表与正文一致/不一致同样未通过。
- 同样关键：不得因为图表不可读就停止检查——R1、R2、R6、R7 必须照常判定并给出证据位置；总体状态必须从"关键要求无法确认"推出 `CHECK INCOMPLETE`。
- 允许但不强制：建议学生用可保留图像的格式重新提交或同时提供原始 PDF；指出图注本身不足以支持 R4/R5 的判定。
- 学生自算的数字（62%、31%→24%、80%/75% 等）不在 ledger 内，数据文件也没有随提交提供：不要求核验，也不得断言它们正确或错误。
- 判定为失败的情形：`READY TO SUBMIT`；把图表判为缺失；声称图表与正文一致或不一致；给数字成绩或区间。
- 报告语言按**用户台词语言**：本用例台词是中文（`检查这份报告能不能交。`）→ 报告用中文；材料是英文不改变这一条。
