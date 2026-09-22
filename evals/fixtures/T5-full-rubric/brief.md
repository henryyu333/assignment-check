# BUS 3420 — Operations and Information Systems

## Individual Case Study — 30% of the module mark

**Case:** Northwind Freight Group (NFG)
**Word limit:** 900 words (±10%), excluding the reference list, tables and figures
**Submission:** one file (PDF or Markdown) uploaded to the module site
**Deadline:** Friday 14 November 2026, 23:59

### Case background

Northwind Freight Group is a regional logistics operator based in Leeds. It employs 3,400 people across twelve depots and runs a fleet of 1,800 vehicles. Its core operational system, DispatchPro, was built in 2009 as a single on-premise application backed by one Oracle database running on two ageing servers in the company's own data centre.

DispatchPro handles order capture, route planning, driver dispatch and customer tracking. It is the system of record for every consignment NFG moves. The platform was never designed for the volumes the company now handles. In the 2025 peak season, volumes were 34% higher than the previous year; the nightly batch reconciliation ran past 04:00 on nineteen nights, and on three occasions the driver app was unavailable for more than two hours during morning dispatch. The customer-facing tracking page also failed twice during December, and two national customers raised formal service complaints.

Integration is equally dated. NFG maintains 47 point-to-point interfaces to customer and partner systems, each maintained separately and each a potential point of failure. Adding a new integration takes the IT team between six and nine weeks.

Elsewhere the company already runs a hybrid estate: finance and HR sit on a cloud SaaS platform, and the warehouse management system is hosted in a private cloud. The Board has asked the Chief Information Officer to bring a recommendation on the future of DispatchPro to its February 2027 meeting.

### The options on the table

**Option A — migrate DispatchPro to a cloud-native microservices architecture.** Rebuild the platform as independently deployable services on a public cloud: order capture, despatch, tracking, driver-app backend, plus a shared API gateway to replace the 47 point-to-point interfaces. Estimated as a two-phase programme of eighteen months.

**Option B — modernise the existing monolith in place.** Retain the application and the Oracle licence, replace the two servers in 2027, and address problems incrementally by tuning the batch process, adding read replicas, and patching individual integrations.

### Your task

You are advising the Board. Write a case study report that recommends one of the two options, or a clearly specified combination of them.

### Required structure

Your report must contain the following sections, with these headings, in this order:

1. **Executive summary** — a summary of your findings and recommendation, of no more than 150 words;
2. **Analysis** — the body of your argument;
3. **Recommendation** — what the Board should do;
4. **References** — a Harvard-style reference list.

### Required content

Your report must:

1. state clearly what decision the Board faces and why that decision matters to NFG;
2. analyse **both** options before recommending one;
3. include **at least one counter-perspective** — that is, state the strongest argument against the option you recommend, and respond to it;
4. give a clear recommendation and justify it with the evidence set out in your analysis;
5. cite **at least four** credible sources in Harvard style, both in the text and in the reference list;
6. include at least one figure or table presenting evidence, and keep every figure or table consistent with the numbers discussed in the text;
7. stay within the word limit.

### Guidance

Assume the Board is intelligent but not technical. Do not simply describe the case: your marks come from the quality of the argument you build from it. You may invent reasonable figures where the case does not supply them, but say where you have done so.

The report is marked against the rubric published on the module site.
