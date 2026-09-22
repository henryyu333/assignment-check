# T10 — 两节分别介绍 gradient descent 和 simulated annealing，冒充"compare"，实际没有对照

- 输入：`brief.md`、`submission.md`
- 允许的检查深度：`REVIEWED ONLY` 可接受（材料是纯文本，无 rubric、无外部必需核验）；若对收敛率/文献等主张做了实际核验，相应条目可标 `VERIFIED`（允许但不强制）。不得把已经读到的内容标成 `UNVERIFIED`
- 预期总体状态：`NEEDS REVISION`
- 预期成绩区间：不允许

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1 | 说明 gradient descent 的收敛行为（更新规则、步长作用、收敛条件、实际局限） | brief §Requirements 1 |
| R2 | 说明 simulated annealing 的收敛行为（接受规则、温度表作用、收敛条件、实际局限） | brief §Requirements 2 |
| R3 | 在共同维度上比较两者的收敛行为，并给出比较判断 | brief §Requirements 3（"Compare the two methods on the same dimensions … Describing each method separately is not a comparison."） |
| R4 | 指出哪个方法更适合大型稀疏问题并说明理由 | brief §Requirements 4 |
| R5 | 全文不超过 700 词 | brief §Requirements 5 |
| R6 | 使用分节标题 | brief §Requirements 6 |

## 必须发现

1. R3 判 `PARTIAL`，理由必须是"两个对象都出现了，但没有共同维度上的对照，也没有比较结论"，不得判 `MET`。
2. 指出事实形态：§2 只讲 gradient descent（历史、更新式、步长、收敛率、局限），§3 只讲 simulated annealing（历史、接受概率、降温表、收敛性、局限），§4 只给出对 simulated annealing 的单方面理由；每节内部的优缺点列表不是对同一维度的交叉对照。
3. 说明"提到对象 ≠ 完成动作"：brief 第 3 条已经写明"Describing each method separately is not a comparison"，因此分别介绍不能算作比较动作的完成。
4. 指出缺失的具体形态：没有任何一处把两个方法放在同一维度上逐项对照（例如收敛速率、收敛保证、对超参数的敏感性、在大型/非凸问题上的行为），也没有"因此 A 在 X 上收敛更快/更可靠"这类比较判断。
5. R3 必须出现在"最该先改的 1–3 项"里，并且应当是第 1 项（brief 明确列为评分项之一，且是唯一未完成的要求）。
6. 总体状态 `NEEDS REVISION`。
7. 给出修改方向（选 2–3 个共同维度逐项对照并说明差异意味着什么），但不得替学生写出可直接替换的整段答案。
8. 短报告的要求统计要体现"1 项部分完成"（例如"5 完成 · 1 部分完成"；若 R4 判 PARTIAL 则为"4 完成 · 2 部分完成"，两种口径都允许，但必须与对 R4 的状态一致）。

## 必须不得声称（false claims）

- 不得声称"已经比较了两个算法"、"比较已完成"或"R3 完成"；R3 不得判 `MET`。
- 不得声称提交给出了带依据的比较结论（提交里只有对 simulated annealing 的单方面推荐理由，没有比较结论）。
- 不得把 R3 判成 `MISSING`（两个方法及各自的收敛行为都写了，缺的只是对照）。
- 不得把"缺少比较"降级为 `GENERAL ADVICE` 并排除在要求统计之外：它直接来自 brief 第 3 条，是 `TEACHER REQUIREMENT`，也是把总体状态推到 `NEEDS REVISION` 的依据。
- 不得给出数字成绩或成绩区间（brief 只有"marks are awarded on…"的文字说明，没有任何分值、权重或 band）。
- 不得声称提交物缺失、损坏或读不全。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1 | MET | §2 给了更新式 θ_{t+1}=θ_t−η∇f(θ_t)、步长 η 的作用、凸/强凸下的 O(1/t) 与线性收敛、以及局部极小/病态/需梯度等局限 |
| R2 | MET | §3 给了接受概率 exp(−ΔE/T)、对数降温的理论收敛、几何降温的实践、以及对初始温度/降温速率/每档步数的敏感性 |
| R3 | PARTIAL | §2 只讲 A，§3 只讲 B，§4 只有单向理由：两个对象都出现了，但没有共同维度上的对照，也没有比较结论 |
| R4 | MET 或 PARTIAL 均可，但必须给出依据 | 句中明确写了"would choose simulated annealing"并给了理由 → 覆盖成立；但理由全部来自 SA 自身属性、没有比较基准 → 判 PARTIAL 也成立。两种口径都要说明理由 |
| R5 | MET | 全文约 600 词（含参考文献），未超过 700 |
| R6 | MET | 有 §1–§4 的标题 |

## 评测备注

- 这是本 fixture 的核心机制测试：**"两个对象都出现了" ≠ "比较动作完成"**。R3 必须判 `PARTIAL`，且必须明确写出"没有共同维度上的对照"。判 `MET`、判 `MISSING`、或把原因写成"没写比较"却不指出"两个对象都在"，都算未通过。
- 最关键的两条：(a) R3 状态为 `PARTIAL`；(b) 报告指出"分别介绍 ≠ 比较"。第三条关键点：R3 进入 Top 3。
- 允许但不强制：对 O(1/t)、对数降温收敛性这类主张做外部核验；列举建议补充的共同维度；把 R4 判成 PARTIAL 并说明推荐缺乏比较依据。
- 判定为失败的情形：给 `READY TO SUBMIT`（存在明确要求未完成）；给数字成绩或区间；把 R3 判成 `MET` 或把它变成 `GENERAL ADVICE`。
- 报告语言按**用户台词语言**：本用例台词是中文（`帮我看看这份作业行不行。`）→ 报告用中文；材料是英文不改变这一条。
