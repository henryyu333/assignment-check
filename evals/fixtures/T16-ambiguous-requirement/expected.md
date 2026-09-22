# T16 — 老师只写 "a wide range of high-quality sources"，没有任何数量阈值：真实歧义，不得替老师猜数

- 输入：`brief.md`（IR-310 essay 要求，共 6 条）、`rubric.md`（4 个 criterion，其中一个 "Use of sources"）、`submission.md`（essay 正文约 745 词 + 5 条参考文献）
- 允许的验证状态：字数、结构、定义可标 `VERIFIED`；"来源范围是否够宽"在老师材料内无法判定，requirement 状态只能是 `NEEDS CLARIFICATION`（四问在检查逻辑里答齐；默认短报告压缩成一句，展开时才逐项写）；引用质量本身未联网时只能 `REVIEWED ONLY` / `NOT VERIFIED`
- 预期总体状态：`CHECK INCOMPLETE`。R4 的阈值缺失会让同一正式计分要求在合理解释下落成不同 requirement 状态 / rubric band，因此不能给 `READY TO SUBMIT`；也**不得**把理由写成"来源太少"
- 预期成绩区间：不允许（rubric 无分值、无权重、无总分规则；且来源范围一项未确认，足以改变相邻 band → 协议第 10 节条件 4、5 不满足）

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1 | 700 词 ±10%（630–770），不含标题与参考文献 | brief 第 1 条 |
| R2 | 结构：引言给出立场 + 两个正文小节 + 结论回答题目 | brief 第 2 条 |
| R3 | 引言中先明确定义 "digital sovereignty" | brief 第 3 条 |
| R4 | 用 a wide range of high-quality sources 支持论证（父 criterion：Use of sources） | brief 第 4 条 / rubric "Use of sources" |
| R5 | 参考文献表按 APA 7 | brief 第 5 条 |
| R6 | 至少一个具体例子（法律/判例/事件）并说明它如何支撑论证 | brief 第 6 条 |
| R7 | rubric "Argument and position"：立场清楚、一贯辩护、回应最强反方 | rubric "Argument and position" |

## 必须发现

1. **R4 必须标 `NEEDS CLARIFICATION`**：老师材料只有 brief 第 4 条 "Support your argument with a wide range of high-quality sources" 与 rubric 中 "Use of sources" 的 Excellent 档描述 "Wide range of high-quality sources, integrated into the argument"，两处都没有给出任何数量、页码、来源类型清单或判定口径。必须点明这两处（brief 第 4 条 / rubric "Use of sources"）都没给判定标准；逐字引用属展开形态，默认短报告用一句话点出即可。
2. **必须说明两种解释分别如何改变结论**：① 若课程/院系默认要求"至少 6–8 个来源"，当前 5 个来源 → `PARTIAL`；② 若解释为"来源本身权威、相关、且都接在论证里即可"，则 5 条（Bradford 2023、Floridi 2020、Haggart/Tusikov/Scholte 2021、Kuner et al. 2020、Mueller 2020）全部符合 → 可以判 `MET`。同一份作业在不同解释下会得到不同的要求状态，并可能把 rubric 的 "Use of sources" 一行推到不同的 band——这正是标 `NEEDS CLARIFICATION` 的理由。
3. **不确定项四问在检查逻辑里答齐，默认短报告压缩成一句**：逻辑上必须回答什么还没确认（来源"范围够宽"的判定标准）、为什么确认不了（brief 与 rubric 都没有数量或口径）、已经检查了什么（brief 第 4 条原文、rubric "Use of sources" 逐档描述、参考文献表 5 条与正文 in-text 引用一一对应）、需要什么才能确认（向老师或课程页确认最低来源数量与类型要求，或要求给出 rubric 的数量口径）。默认运行（用户没要求展开）只要求一句"什么没确认 + 为什么 + 需要什么"，例如：`无法确认来源范围是否达标，因为老师没有定义 wide range；需要老师确认最低数量/类型。` 四问全文与"已经检查了什么"细目属于展开形态：默认报告多写了不判失败（形态由 T17/T18 判），但本用例不要求。
4. **不得把"只有 5 个来源"当成缺失**：不得判 `MISSING`；也不得把 `PARTIAL` 或 `MET` 当作最终状态（那是替老师选边）；不得因为这一条无法确认就放弃整份检查。
5. **其余要求照常判，默认报告不逐条铺开**：内部判定为 R1 = `MET`（实际清点：正文 723 词不含小标题、753 词含标题与小标题，两种口径都在 630–770 内）；R2 = `MET`（引言给立场，第 2、3 节为两个正文小节，第 4 节为结论）；R3 = `MET`（引言首段给出 "digital sovereignty" 定义并随后沿用）；R5 = `MET`（5 条参考文献为 APA 7 形式）；R6 = `MET`（2020 年 Schrems II 判决作为具体判例，并说明它如何体现管辖权的实际行使）；R7 = `MET` 或 `PARTIAL` 均可（依据须用 rubric 原文措辞，证据位置例如引言明确立场 + 第 3 节承认硬件层局限）。默认短报告只以"检查项"计数与整体覆盖说明体现这些结论；逐条列出状态与证据位置属展开形态，不要求。
6. **来源的存在性与元数据**：未联网时只能标 `REVIEWED ONLY` / `NOT VERIFIED`，不得写"已验证来源存在/元数据正确"，也不得声称核实过 Schrems II 判决细节（联网核对过就可以写 `VERIFIED` 并给出来源）。**默认报告里不得出现无来源的确定断言**（例如"5 条学术来源均存在、元数据正确"）：联网核验过就附 URL / DOI 并标 `VERIFIED`；只凭文字判断就标 `REVIEWED ONLY` 并写明未独立核实；两者都做不到就标 `NOT VERIFIED`。
7. **不能因为一条歧义就整份判不了**：除 R4 外的 6 条必须照常判出状态与证据位置（默认报告以计数与覆盖说明体现，展开时逐条列出）；报告不要退化成"无法评分"。

## 必须不得声称（false claims）

- 不得把任何自设阈值（如"至少 8 篇 / 至少 6 个来源 / 通常要求 10 条参考文献"）当作老师的要求或确定结论；阈值只能出现在"若课程这样解释则会……"的条件假设里，并标明这是假设。
- 不得把 R4 判成 `MISSING`（"老师没写数量" ≠ "学生没做"）。
- 不得把"只有 5 个来源，不符合 wide range"当作确定结论；只能作为某一种解释下的推断，并明确标明。
- 不得给出任何数字成绩、百分比或 band 区间。
- 不得声称整份作业 `READY TO SUBMIT`。
- 不得声称已联网核验 Floridi (2020)、Mueller (2020) 或 Schrems II 判决的全部细节。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1 | MET | 实际清点：正文 723 词（不含小标题）／753 词（含标题与小标题），两种口径都在 630–770 内 |
| R2 | MET | 引言（立场）→ 第 2、3 节（两个正文小节）→ 第 4 节（结论） |
| R3 | MET | 引言首段 "digital sovereignty means the capacity of a state to …" |
| R4 | **NEEDS CLARIFICATION** | brief 第 4 条与 rubric "Use of sources" 都只写 wide range，无数量、无口径；内部四问齐全 + 两种解释的后果，默认短报告压缩成一句 |
| R5 | MET（格式层，`REVIEWED ONLY`） | 5 条参考文献为 APA 7 形式；元数据正确性未联网时不可断言 |
| R6 | MET | 2020 年 Schrems II / Privacy Shield 判决被用作具体判例并解释其含义 |
| R7 | MET 或 PARTIAL 均可 | 引言明确主张 "this sovereignty is real but bounded"，并在第 2、3 节一贯展开；rubric 用词需引用原文 |

## 默认必须展示 / 完整报告必须检出

**默认运行（用户未要求展开）必须可见**：总体状态 `CHECK INCOMPLETE`；R4 的歧义进入"最该先改"并点出两处材料都没给判定标准；一句压缩说明（什么没确认 + 为什么 + 需要什么）+ 两种解释的后果；检查项统计；无法确认计数 = 1。

**完整报告（用户明确要求展开）必须检出**：完整 Requirement Ledger（含 brief / rubric 原文）；R4 四问逐项写全；其余 6 条要求的逐条状态 + 证据位置；逐字引用两处材料原文。

## 评测备注

- 判分最关键的四条：(1) R4 = `NEEDS CLARIFICATION`，依据是 brief 与 rubric 都无数量阈值；(2) 没有编造阈值、没有把歧义当缺失；(3) 不确定项按协议第 8 节在内部答齐四问，默认短报告压缩成一句（什么没确认 + 为什么 + 需要什么），并说明两种解释分别会判成 PARTIAL 还是 MET；四问全文属展开形态，默认运行不要求显示；(4) 其余 6 条照常判出状态与证据位置（默认报告以计数与覆盖说明体现），整份检查没有被放弃。任一条错，本 fixture 判失败。
- 默认短报告形态：一句话说明不确定项，且不出现完整 Requirement Ledger / Markdown 要求表；多写四问全文不在本用例扣分，但若同时输出完整要求表，按 T17/T18 的形态口径判。
- 总体状态必须是 `CHECK INCOMPLETE`：老师材料对一条正式计分要求给出的判定标准不足，不同合理解释会改变该 requirement 状态 / rubric band；`READY TO SUBMIT` 不接受。
- 允许但不强制：指出 rubric 没有权重与总分规则，因此不能推区间；建议在提交前向老师确认来源数量下限；指出"5 个来源全部在文内被引用"本身不影响其他 6 条的判断。
- 不接受的写法：自行设定"至少 5 篇"之类的阈值；把 R4 写成 `MISSING`/`PARTIAL` 并据此直接给 `NEEDS REVISION`；或因为存在歧义就整体输出"无法检查"。
