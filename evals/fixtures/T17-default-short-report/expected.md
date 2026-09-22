# T17 — 默认短报告：有明确缺口，但不能把完整 ledger 全铺出来

- 输入：`brief.md`、`submission.md`
- 测试台词：`检查一下这份作业能不能交。`
- 预期总体状态：`NEEDS REVISION`
- 目的：专门检查**默认输出形态**，不是检查复杂学科事实。

## Ledger 基准

| ID | 要求 | 预期状态 |
|---|---|---|
| R1 | 明确写出 decision question | MET |
| R2 | 解释 electric shuttle buses | MET |
| R3 | 解释 expanded bike-share | MET |
| R4a | 比较两者的 cost | MET |
| R4b | 比较两者的 implementation time | MISSING |
| R5 | 给出 recommendation，并由比较支撑 | MET |

## 必须发现

唯一需要进入 Top fixes 的核心缺口：提交物只比较了 upfront cost，没有比较两种方案的 implementation time。

## 默认形态必须满足

最终回答应保持短报告：

1. 标题 / 总体状态
2. 最多 1–3 条“最应该先改”
3. 检查项统计
4. 如有不确定项才给一句摘要；本 fixture 没有必须出现的不确定项

允许用自然语言压缩，但**不得默认输出完整 Requirement Ledger、逐条 Markdown 表、完整 finding 六要素、长篇优点列表或完整 protocol 解释**。

建议形态类似：

```text
Assignment Check

NEEDS REVISION

最应该先改：
1. 老师要求比较 cost 和 implementation time；你只比较了 cost，implementation time 还没比较。

检查项：5 完成 · 1 缺失
```

## 不得声称

- 不得给数字成绩或分数区间
- 不得判 `READY TO SUBMIT`
- 不得因为没有 rubric 而拒绝检查
- 不得把“两个方案都介绍了”当成已经完成双维度 compare
