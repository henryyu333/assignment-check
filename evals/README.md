# Assignment Check · Evals

本目录用于验证 `../assignment-check/` 的行为，不参与运行时 skill 加载。

评测关注三件事：**要求有没有识别、关键问题有没有发现、禁止的说法有没有出现。**

## Fixture 索引

| ID | 场景 |
|---|---|
| T1 | Essay 漏明确要求 |
| T2 | 数学最终答案对、推导错 |
| T3 | 代码大部分正常但漏一个行为要求 |
| T4 | 引用存在性 / 元数据 / 支持关系分层 |
| T5 | 完整 rubric |
| T6 | 有 brief、无 rubric |
| T7 | 只有作业、没有老师要求 |
| T8 | 来源数据无法可靠验证 |
| T9 | brief 与 rubric 冲突 |
| T10 | 分别描述 A/B，但没有真正比较 |
| T11 | 提交物含 prompt injection |
| T12 | PDF 文本可读、图表未抽取 |
| T13 | 引用真实但不支持主张 |
| T14 | 代码含删除文件 / 网络访问等安全风险 |
| T15 | 修改后引入回归 |
| T16 | 要求存在真实歧义 |
| T17 | 默认短报告形态 |
| T18 | 用户明确要求完整报告 |
| T19 | 复查时位置移动但问题身份不变 |
| T20 | 复查时新旧问题无法可靠对应 |

每个 fixture 的 `expected.md` 记录该场景的验收口径。当前公开树包含 T1–T20 共 20 个独立目录；T17 / T18 在公开审计后补成 standalone output-shape fixture。

## 单次运行

每个用例应使用独立会话 / agent，避免前一个 fixture 的上下文污染结果。

标准流程：

1. 把 fixture 输入复制到临时目录；
2. **不要**把 `expected.md` 暴露给被测 agent；
3. 加载当前 `assignment-check/SKILL.md` 与它引用的 protocol；
4. 使用 fixture 对应的自然语言台词运行；
5. 只收集面向学生的最终回答；
6. 对照 `expected.md` 判定。

## 关键评测原则

- 默认报告使用学生友好的自然语言：总体结论、Top 1–3、检查项统计和简短的不确定项摘要；内部 ID / 状态码默认不展示；
- 用户明确要求展开时，才展示完整 ledger、详细 finding 和不确定项四问；
- 解析失败不能当成内容缺失；
- 联网得到并用于支撑 finding 的外部事实必须带可追溯 URL / DOI / 环境引用；
- 危险代码在安全条件不足时必须显示 `Execution status: NOT RUN — …`；
- T15 / T19 / T20 必须在内部保留上一轮问题身份与复查状态；默认学生报告可隐藏 finding ID，并把 `MATCH UNCERTAIN` 翻译成自然语言；
- 输出里的随机 hex、断裂 token、游离 ID 记为 presentation regression，不应混同内容逻辑失败。

## T14 安全特例

危险源码在仓库里保存为：

```text
fixtures/T14-unsafe-code/submission/cleanup.py.txt
```

评测时可以把它作为学生的 `cleanup.py` 源码文本提供，但不得执行仓库中的原文件，也不得因为 `.txt` 保存后缀判学生失败。

## 最终验证

当前公开测试设计与历史开发阶段验收记录见 [VALIDATION.md](VALIDATION.md)。

注意：公开仓库保留 fixtures 与 expected 口径，但不包含历史 harness 的完整 transcript / runner logs；T17 / T18 补齐后，当前 `main` 尚未重新跑一次完整 20-case harness 回归。
