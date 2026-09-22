> **Note on this file:** this is the text-extraction version of my submitted report
> `retention_report_final.pdf`. Images and figures are **not** included in this extraction.
> Figure captions have been preserved. Full document: 6 pages.

# Retention at LinguaLoop: What the Cohort Data Shows

## Context

LinguaLoop is a subscription language-learning app with a freemium funnel: free trial, then a monthly or annual plan. Over the last three years the team has reported healthy acquisition numbers while revenue growth has been flat, which suggests the problem sits after signup rather than before it. This report uses the quarterly cohort file to check that story. The product had roughly 90,000 paying subscribers at the end of 2023, split about 60/40 between monthly and annual plans; the annual plan carries the larger revenue per user, so most of what follows is read through that lens.

## Method

I grouped users by signup quarter and tracked the share still subscribed at the end of each following quarter, so every cohort is compared at the same age. Retention is the standard subscription measure: active paid subscribers at the end of quarter *n* divided by the cohort size at signup, as a percentage. Cohorts are kept in the file even when they are small, and their sample size is flagged where it matters. Free-trial users who never converted are excluded from the denominator of every retention figure below, since they are tracked separately in the funnel view. I compared the Q4 retention of the cohort with two external benchmarks: ProfitWell's SaaS retention study and the consumer-subscription figures in the 2023 OpenView SaaS Benchmarks report.

[Figure — image not included in the text extraction]

*Figure 1: Cohort retention curves, 2021–2024 (see page 3).*

[Figure — image not included in the text extraction]

*Figure 2: Activation rate vs Q4 retention by cohort (see page 3).*

## Findings

Acquisition grew steadily, but retention did not follow. Early cohorts from 2021 stabilise near 80% at quarter four, which is close to the SaaS benchmark; cohorts from 2022 drift down to roughly 75%; and the 2023 cohorts sit clearly below both.

[Figure — image not included in the text extraction]

*Figure 3: Quarterly retention by cohort (2021–2024) — see page 4.*

Figure 3 places the cohorts side by side over their first four quarters and shows where the decline actually starts. The 2021 cohorts hold above 80% at Q4, while the 2023-Q2 cohort is down to 62%, and the gap opens in quarter two rather than at signup. Reading the same figure across quarters, the drop is concentrated in the annual-plan segment, which is consistent with the pricing change made in early 2023. The spacing between the 2022 and 2023 curves is widest in the third quarter, where the annual-plan renewals cluster, and narrowest in quarter one; if the gap were driven by acquisition quality alone it would be widest at the start of a cohort's life, so the shape of the curves matters as much as their endpoints.

Two secondary observations. First, the cohorts that activate above 55% (users who complete at least one lesson streak in week one) also retain better at Q4, which is the pattern Figure 2 was built to show. Second, the share of trial users who convert on the annual plan fell from 31% to 24% between 2021 and 2023.

## Limitations

The cohort file only covers the subscription event. It says nothing about why people left, so the 2023 decline is consistent with the pricing change but not proven by it. Sample sizes for the 2023-Q3 and 2023-Q4 cohorts are also under 400 users each, which makes their quarter-to-quarter movement noisy. Finally, the benchmark comparison mixes business models, since the OpenView figures include sales-led products with very different retention dynamics. The file also has no geographic breakdown, so I cannot test whether the decline is concentrated in one market or spread evenly across all of them.

## References

- ProfitWell (2023). *SaaS retention benchmarks: how retention rates differ by revenue band.* profitwell.com/recur/.
- OpenView Partners (2023). *2023 SaaS Benchmarks Report: consumer and prosumer subscription retention.* openviewpartners.com/2023-saas-benchmarks/.
