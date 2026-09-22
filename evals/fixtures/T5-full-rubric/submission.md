# Cloud or On-Premise: The Future of DispatchPro at Northwind Freight Group

## Executive summary

This report examines whether Northwind Freight Group should migrate DispatchPro, its 2009 on-premise dispatch platform, to a cloud-native microservices architecture (Option A) or modernise the existing application in place (Option B). The two options are compared on five-year cost, peak-season reliability and integration effort. On all three dimensions Option A performs better: its five-year cost is £9.8m against £12.4m, it removes the single points of failure behind the December 2025 outages, and it replaces 47 point-to-point interfaces with a managed API gateway. The report recommends that the Board approve a phased migration beginning in Q1 2027, with the legacy platform retired by the end of 2028.

## Analysis

### What the Board is deciding

The Board must decide whether NFG replaces the architecture of DispatchPro or continues to run and patch it. The decision matters because DispatchPro is the system of record for every consignment the company moves. When the platform is unavailable, drivers are despatched on paper, customer tracking goes dark, and contractual service levels are missed. The 2025 peak season produced three morning-dispatch outages and two failures of the customer tracking page. The two national customers who raised formal complaints together represent 18% of NFG's revenue, and both contracts run to 2029. Three retail customers also operate service-level agreements that carry credits of up to 4% of monthly charges for tracking downtime, and those credits were claimed in January 2026. The choice, therefore, is not a routine IT refresh but a decision about whether the company can keep its service commitments at its current rate of growth.

### Option A: cloud-native microservices

Option A rebuilds DispatchPro as independently deployable services on a public cloud, with order capture, despatch, tracking and the driver-app backend able to scale separately (Sharma, 2022). This addresses the 2025 failures directly: in those incidents, route planning saturated the same database that served the driver app, so a slow batch job took the drivers down with it. Separating those workloads means a surge in route planning can no longer starve despatch. The migration also replaces the 47 point-to-point interfaces with a shared API gateway, which the IT team estimates would cut the time needed to add a customer integration from six to nine weeks to roughly two weeks. Phase one would move despatch and tracking, while order capture stays on-premise until phase two, so that a fault in the new stack cannot interrupt order intake during the transition year. The programme is costed as two phases over eighteen months, with a dual-run period in which the legacy platform remains available.

### Option B: modernising the monolith in place

Option B retains the application and the Oracle licence and addresses the symptoms. The 2027 server replacement would cost £0.64m, read replicas would reduce contention on the reporting database, and the reconciliation window could be shortened by parallelising the route-planning step. These measures are real, but bounded. The monolith still deploys as a single unit, so any change to despatch logic still requires a full regression test and a weekend release. The batch job still runs against one database, so the 04:00 overrun returns whenever volumes grow by another third. It also leaves the 47 integrations untouched, so every new customer still requires bespoke work, and most of the integration knowledge sits with two long-serving engineers who are both eligible to retire before 2028. Option B buys time rather than solving the problem.

### Comparing the two options

Table 1 sets out the five-year cost of each option.

**Table 1. Five-year cost comparison (£ millions)**

| Cost item | Option A (migration) | Option B (modernise) |
|---|---|---|
| Implementation | 4.2 | 1.1 |
| Infrastructure and licensing | 3.5 | 5.9 |
| Maintenance and support | 2.1 | 5.4 |
| **Total** | **9.8** | **12.4** |

Option B is cheaper in the first year, at £1.1m against £4.2m, because the migration carries most of its cost up front. Over five years, however, Option A is £2.6m cheaper: the Oracle licence, the 2027 hardware replacement and the higher support burden together outweigh the migration cost. Published cost studies of comparable mid-sized operators put the crossover point between the third and fourth year of a migration (Chen and Patel, 2023), which is the pattern Table 1 shows. Because the company's two largest contracts run to 2029, a five-year horizon matches the period over which the Board has to guarantee service. The comparison also assumes NFG's recent volume growth of roughly 30% a year continues; on that assumption the on-premise estate would need a second hardware replacement before 2032, while the cloud services would absorb the extra volume within the existing subscription bands.

## Recommendation

The Board should approve Option A and begin a phased migration in Q1 2027. The recommendation follows from the comparison above: Option A is £2.6m cheaper over the contract horizon, removes the failure mode that caused the 2025 outages, and cuts integration effort from weeks to days, the same pattern reported across European freight operators that have completed comparable migrations (Deloitte, 2024). Two conditions should be attached. First, the API gateway should be delivered in phase one rather than last, because it carries the largest operational benefit for the least risk. Second, the legacy platform should remain in dual run until the driver app has completed one full peak season on the new architecture, so that the December 2027 peak is covered by both systems. The Board should also ask the CIO to report progress against the phase-one milestones at six-month intervals.

## References

Chen, R. and Patel, S. (2023) 'Platform modernisation in mid-sized logistics firms: a five-year cost study', *Journal of Transport Technology*, 14(2), pp. 88–104.

Deloitte (2024) *The cloud imperative in European freight and logistics*. London: Deloitte Insights.

Sharma, A. (2022) 'Monoliths and microservices in operational systems: a review of the trade-offs', *Information Systems Frontiers*, 24(6), pp. 1801–1819.
