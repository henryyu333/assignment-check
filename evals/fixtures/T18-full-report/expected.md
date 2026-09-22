# T18 — 用户明确要求完整报告：必须展开 ledger 与 finding

- 输入：`brief.md`、`submission.md`
- 测试台词：`给我完整报告，逐条列出老师要求、证据、状态和所有问题。`
- 预期总体状态：`NEEDS REVISION`
- 目的：专门检查**用户明确要求展开时**，输出不能仍停留在默认短报告。

## Ledger 基准

| ID | 要求 | 预期状态 | 证据 |
|---|---|---|---|
| R1 | 明确写出 decision question | MET | `## Decision` 首段 |
| R2 | 解释 electric shuttle buses | MET | `## Option A` |
| R3 | 解释 expanded bike-share | MET | `## Option B` |
| R4a | 比较两者的 cost | MET | `## Comparison`：bike-share upfront spending lower |
| R4b | 比较两者的 implementation time | MISSING | 全文无两者 implementation time 对照 |
| R5 | recommendation 并由比较支撑 | MET | `## Recommendation` 以 upfront cost 为理由推荐 bike-share |

## 完整报告必须展示

- 总体状态 `NEEDS REVISION`
- 完整 Requirement Ledger：R1–R5（其中 compare 拆为 R4a / R4b）
- 每条 requirement 的状态与证据位置
- 对 R4b 的完整 finding：位置、问题、证据、为什么重要、受影响要求、验证状态、修改方向
- 明确说明无 rubric，因此不输出数字成绩
- 可以给有证据的优点，但不能用优点冲淡 R4b 缺口

## R4b finding 最低要求

- 来源：`TEACHER REQUIREMENT`
- 要求状态：`MISSING`
- 验证状态：至少 `REVIEWED ONLY`；若宿主对全文做了可复核定位，也可 `VERIFIED`
- 修改方向：补一个共同维度，直接对照 shuttle 与 bike-share 各自需要多久才能部署 / 上线，而不是继续分别介绍

## 不得声称

- 不得给数字成绩或成绩区间
- 不得判 `READY TO SUBMIT`
- 不得只输出默认四块然后停止
- 不得虚构老师没有给出的 implementation-time 阈值
