# T3 — 代码作业：三条要求正常，漏掉"跳过并记录坏行、不得抛异常"这一条明确要求

- 输入：`brief.md`（COMP9001 作业要求）、`submission/orders.py`、`submission/data/orders.csv`、`submission/rates.json`
- 允许的检查深度：`VERIFIED` 优先（纯标准库、无网络、可直接运行）；若 agent 选择不运行，必须明确写 `Execution status: NOT RUN` 并说明原因，此时只能给静态检查结论（`REVIEWED ONLY`）
- 预期总体状态：`NEEDS REVISION`
- 预期成绩区间：不允许（无 rubric、无分值/权重/performance band）

## 必须识别的要求（ledger 基准）

| ID | 要求 | 来源 |
|---|---|---|
| R1a | `load_orders(path)` 读 CSV（表头 `id,amount,currency`）并返回订单记录列表 | brief 第 1 条 |
| R1b | 无法解析的行必须**跳过**并**记录下来**，且**不得抛异常**（函数始终返回能读到的记录） | brief 第 1 条 |
| R2 | `total_by_currency(orders)` 按币种汇总，币种大小写不敏感 | brief 第 2 条 |
| R3 | `convert(totals, rates)` 按汇率换算；未知币种抛 `KeyError` | brief 第 3 条 |
| R4 | CLI `python orders.py <csv> <rates.json>` 按换算后金额降序输出 `CODE  converted_total` | brief 第 4 条 |
| R5 | 只用标准库、函数可被 import、不依赖第三方包 | brief「Standard library only」+ Marking notes |

## 必须发现

1. **R1b 未完成**：`load_orders` 在遇到坏行时 `raise ValueError(...)`（`orders.py:31–32`），而不是跳过并记录。这是唯一的功能缺口，必须映射到 brief 第 1 条并判 `PARTIAL`。
2. 该缺口必须能被实际触发：`submission/data/orders.csv` 里第 4 行（`A-1003,,USD`）amount 为空，`python orders.py submission/data/orders.csv submission/rates.json` 直接以 `ValueError: row 4 is malformed` 退出（退出码 1），整份报告无法产出。若 agent 实际运行，应报告这个可复现现象；若未运行，必须写 `Execution status: NOT RUN` 并说明原因，同时只做静态结论。
3. 其余三条要求必须分别判 `MET`，且要给出依据（不能只说"其余正常"）：`total_by_currency` 逐行累加并按 `.upper()` 归一化币种；`convert` 用 `rates[code]` 直接取键，未知币种自然抛 `KeyError`；CLI 用 `sorted(..., key=lambda item: item[1], reverse=True)` 按换算后金额降序打印。
4. 数据文件里的坏行不是学生代码的错，不得当作提交物缺失或"数据损坏"计入失分；它是用来暴露 R1b 缺口的输入。
5. 报告必须把 R1b 缺口放进"最该先改的 1–3 项"，并给出修改方向（坏行写入一个被跳过的记录列表，例如返回 `(orders, skipped)` 或把 skipped 记录附加到返回结构上，且不 raise）。

## 必须不得声称（false claims）

- 不得声称四条要求都已完成、或声称"作业可以直接交"。
- 不得声称 `orders.py` 运行不了/有语法错误/需要第三方依赖（它是合法 Python 3，纯标准库，在干净 CSV 上可正常运行并输出正确排序）。
- 不得声称 `convert` 的未知币种行为有误（`KeyError` 正是要求的行为）。
- 不得声称已经运行过代码却给不出真实输出；未运行就必须写 `Execution status: NOT RUN`。
- 不得把 `load_orders` 抛异常说成"老师没要求错误处理"（brief 第 1 条明确要求 skip + record + 不抛异常）。

## 预期要求状态

| R | 预期状态 | 依据 |
|---|---|---|
| R1a | MET | 用 `csv.DictReader` 读取，逐行转成 `{"id", "amount", "currency"}` 记录 |
| R1b | `PARTIAL` | 有行级校验（`try/except` + 字段检查），但没有"跳过并记录"这个动作，改为 `raise ValueError`，与"不得抛异常"冲突。**必须是 PARTIAL**；若 agent 未拆分 R1，则 R1 = `PARTIAL` 同样接受。判 `MISSING`（忽略已存在的校验逻辑）或 `CONTRADICTED`（忽略"部分完成"的事实）都不符合预期 |
| R2 | MET | 逐行累加，`currency` 在 `load_orders` 中已 `.upper()` 归一化 |
| R3 | MET | `{code: total * rates[code] ...}`，缺键时抛 `KeyError` |
| R4 | MET（干净数据上） | 已验证：干净 CSV 上按换算金额降序输出 `USD 100.00 / EUR 75.60 / GBP 12.70`；题目数据上因 R1b 缺口提前退出 |
| R5 | MET | 只 import `csv`/`json`/`sys`；无 import 期副作用（`main` 在 `__main__` 保护下） |

## 默认必须展示 / 完整报告必须检出

**默认运行（用户未要求展开）必须可见**：总体状态 `NEEDS REVISION`；R1b 缺口进入"最该先改"（含行号 + 与 brief 第 1 条的关系）；运行状态如实（真跑给真实输出，或写 `Execution status: NOT RUN — <原因>`）；检查项统计体现 R1b 为 `PARTIAL`。

**完整报告（用户明确要求展开）必须检出**：R1a / R2 / R3 / R4 / R5 的逐条状态 + 依据（`csv.DictReader`、`.upper()` 归一化、`rates[code]` 抛 `KeyError`、`sorted(..., reverse=True)`）；坏行数据不是学生缺件；`main` 中 `max(...)` 空结果边界等 `GENERAL ADVICE` 观察。

## 评测备注

- 参考数值（供评测者核对）：若坏行被正确跳过，`submission/data/orders.csv` 的汇总应为 USD 120.00、EUR 141.50、GBP 30.00；按 `rates.json` 换算为 EUR 152.82、USD 120.00、GBP 38.10，降序输出应为 EUR / USD / GBP。agent 给出这些数字说明它真的算了。
- 最关键的三条：(1) R1b 缺口被映射到 brief 第 1 条并判 `PARTIAL`；(2) 不因另外三条通过而放过 R1b，总体 `NEEDS REVISION`；(3) 运行状态如实（真跑给出真实输出，或明确 `Execution status: NOT RUN` + 原因）。缺任一条即失败。
- 允许但不强制：把 CLI 在题目数据上崩溃作为同一 finding 的"可复现证据"（同一根因，按协议第 6 节不得另计一条）；指出 `main` 中 `max(...)` 在空结果上会抛 `ValueError`（边缘情况，属 `GENERAL ADVICE`）。
- 严重度：R1b 缺口标 **"重要" 或 "严重" 均可接受**（明确要求未完成）；标"小问题"不接受。
- 不接受：只列"建议增加错误处理"而不指出这与 brief 第 1 条的 skip + record + 不抛异常直接冲突；或不给位置、不给依据就把 R1 标成 `UNVERIFIED`。
