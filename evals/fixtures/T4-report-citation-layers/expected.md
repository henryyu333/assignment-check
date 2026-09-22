# T4 — Report：论点合理，引用分三层出问题（元数据 / 支持关系 / 来源类型）＋一处主要论断无引用

- 输入：`brief.md`（MGT3101 report 要求）、`submission.md`（学生 report，正文 769–776 词 + 参考文献表）
- 允许的检查深度：内部可判项（正文年份 vs 参考文献年份、来源类型不符、无引用论断、scope 是否匹配）→ `VERIFIED`；外部事实（文献是否存在、真实期刊与年份）→ 联网核实后可标 `VERIFIED`，不联网则必须标 `REVIEWED ONLY` 或 `UNVERIFIED`，并在内部按协议第 8 节答齐四问（默认短报告一句：没确认什么 + 为什么 + 需要什么）。两种都接受
- 预期总体状态：`NEEDS REVISION`
- 预期成绩区间：不允许（无 rubric、无分值/权重/performance band）

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1 | 对"remote work 是否提高 productivity"给出明确立场并用证据支持 | brief 第 1 条 |
| R2 | 至少引用 3 个来源 | brief 第 2 条 |
| R3 | 其中至少 2 个为 peer-reviewed（期刊论文或同行评审会议论文） | brief 第 2 条 |
| R4 | 正文引用与参考文献表均按 APA 7 | brief 第 3 条 |
| R5 | 讨论所依赖证据的局限 | brief 第 4 条 |
| R6 | 每个主要论断都能追溯到参考文献表中的来源 | brief「Marking notes」第 2 条 |
| R7 | 正文 750–850 词（不含参考文献表） | brief 头部「Length」 |

## 必须发现

1. **必须把引用检查分成三层分别写**："来源是否存在" / "元数据是否正确" / "来源是否支持该主张"，三层不得合并成一句"引用有问题"。
2. **元数据层（内部可判，必须发现）**：正文写 `(Bloom, Liang, Roberts & Ying, 2015)`，参考文献表同一文献写 2013 年 → 同一文献年份前后不一致。位置：正文「The strongest experimental evidence」第 1、2 段；参考文献表第 1 条。
3. **元数据层（期刊名，联网则必须指出）**：该文献真实出处为 *The Quarterly Journal of Economics*, 130(1), 165–218（2015），DOI 10.1093/qje/qju032；参考文献表写成 *Journal of Labor Economics*, 33(1), 165–218（2013），期刊名、年份（卷号）均错。**若未联网，必须把"期刊名与卷号是否正确"标 `UNVERIFIED`/`REVIEWED ONLY`，并说明没确认什么、为什么、需要什么（内部四问答齐；默认短报告一句即可，展开时逐项写全）；不得凭空断言期刊名正确。**
4. **支持层（纯文本可判，必须发现）**：正文用 Bloom et al. 的呼叫中心实验（中国旅行社接线/录入岗位、按人均吞吐量计产出）去支撑"remote work clearly strengthens collaborative innovation in knowledge-based teams"。该研究的对象与产出指标都不涉及团队协作或创新，主张超出证据范围。位置：正文「The strongest experimental evidence」第 2 段（"Because the Bloom et al. experiment shows a 13% productivity gain…"）。
5. **来源类型层（内部可判，必须发现）**：正文称 "A peer-reviewed study from Deloitte Insights (2022)"，参考文献表把该 consultancy 出版物排成期刊文章（*Deloitte Insights, 14*(2), 45–58，无 DOI）。brief 明确把 consultancy publication 排除在 peer-reviewed 之外 → 类型标注不符。
6. **无引用论断（内部可判，必须发现）**：正文「Survey evidence」段末 "Remote work reduces voluntary turnover by about a third." 是带具体数字的主要论断，句上没有任何引用，段落里其他句子都有引用 → 违反 R6。
7. 必须给出总体状态 `NEEDS REVISION`，且不得写"引用检查通过"。
8. 三条内部可判问题（第 2、4、5、6 点）必须至少给出 3 处，且每处标出所属层次与位置。

## 必须不得声称（false claims）

- 不得声称 Bloom et al. (2015) 这篇文献不存在或"查无此文"（它真实存在，问题是元数据写错）。
- 不得声称引用检查通过、所有来源都支持其主张、或三条引用都没问题。
- 不得声称 Choudhury et al. (2021) 的元数据有误（该条是规范的：*Strategic Management Journal, 42*(4), 655–683，DOI 10.1002/smj.3251）。
- 不得声称已联网核实却不给出可核验的来源/DOI；声称 `VERIFIED` 必须附来源。
- 不得声称报告没有立场或立场不清（R1 明确给出了"条件性收益"的立场）。
- 字数表述必须与实测口径一致，且不得凭空判"超限"：按空白分词、不拆连字符为 738（不含小标题）/ 762（含小标题），拆连字符为 750 / 774；`R7` 判 `MET`（含标题口径）或 `NEEDS CLARIFICATION`（口径跨线）均可接受，但都必须写明口径与实测值。**不许写"远超上限"或"明显不足"。**
- 不得给出数字成绩、百分比或分数区间。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1 | MET | 第 1 段与结论段明确给出"条件性、任务相关的小幅提升"这一立场，并用三项证据展开 |
| R2 | MET | 参考文献表 3 条（Bloom et al.、Choudhury et al.、Deloitte Insights） |
| R3 | MET（Bloom 与 Choudhury 均为同行评审期刊论文） | 若 agent 因 Deloitte 误标而判 `PARTIAL`，只要同时说明仍有两篇合格来源，可接受；判 `MISSING` 不接受 |
| R4 | `PARTIAL` | 参考文献表结构基本符合 APA 7，但同一文献年份前后不一致、把 consultancy 出版物排成期刊文章；若联网，期刊名/卷号错误也是 APA 元数据错误 |
| R5 | MET | 「Discussion」明确讨论样本、任务类型、产出指标不可加总、时间跨度等局限 |
| R6 | `PARTIAL` | 多数论断有引用，但 turnover 那句带具体数字的主要论断无引用；协作创新主张的引用不支持该主张 |
| R7 | MET | 实际清点（按空白分词、不拆连字符）：正文含小标题 762 词、不含小标题 738 词；拆连字符口径为 774 / 750。brief 要求 750–850 → 是否计入小标题会改变达标结论 |

## 评测备注

- 最关键的四条：(1) 三层分开写；(2) 内部可判的年份不一致被发现；(3) 支持层（scope 不匹配）被发现；(4) 无引用论断被发现。四条都出现才算完成本 fixture 的核心要求。
- (b) 的 scope 问题必须**只靠文本**就能判出：句子本身把"人均吞吐量 +13%"当成"知识型团队协作创新"的证据，不需要外部资料。
- 严重度参考：支持层问题标"重要"（影响 R6/R1 的证据链）；元数据年份不一致与来源类型误标可标"重要"或"小问题"（后者仅在 agent 同时说明这是引用诚信问题时才成立）；无引用论断标"重要"。标"严重"必须给齐位置、证据、理由、影响、验证状态、修改方向，否则降级。
- **外部事实可追溯**：若联网核实了 Bloom et al. 的真实出处（*The Quarterly Journal of Economics*, 130(1), 165–218, 2015，DOI 10.1093/qje/qju032），同一 finding 里必须附可追溯来源（DOI / 稳定 URL），即使只标 `REVIEWED ONLY`；给不出来源时只能把"期刊名与卷号是否正确"标 `UNVERIFIED` 并说明需要什么，不得直接断言真实出处。
- 允许但不强制：指出正文 4 作者在 APA 7 中应写作 `(Bloom et al., 2015)`；指出 Deloitte 条目缺 DOI 与"consultancy 出版物通常无卷期页"的矛盾。这些属于同一根因的下游表述，按协议第 6 节不得另计为独立 finding。
- 允许但不强制：把「The strongest experimental evidence」第 2 段"先说明任务狭窄、紧接着又下推广结论"的内部不一致作为支持层 finding 的证据（同一根因，不另计）。
- 不接受：只写"部分引用需要核实"而不分层、不给位置；或**因为无法联网**就整体判 `CHECK INCOMPLETE`（内部可判项足以支撑 `NEEDS REVISION`）。若 `CHECK INCOMPLETE` 来自字数口径跨线（`R7` 在两种口径下分别达标/不达标）并写明理由，则接受。
