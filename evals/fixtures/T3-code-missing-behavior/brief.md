# COMP9001 Programming Assignment 2 — Order Reporting Script

**Due:** Week 9, Friday 23:59 (submit via the unit's submission portal)
**Language:** Python 3.10+
**Standard library only.** The marking machine has no third-party packages: `pandas`, `numpy`, `requests` and similar are not installed. A solution that imports them will not run.

## Task

Write a single file `orders.py` that turns a dirty order export into a currency report. Your program must satisfy the four numbered requirements below.

1. **`load_orders(path)`** — read the CSV at `path` (header row `id,amount,currency`) and return a list of order records. Real exports are dirty: some rows have a missing or non-numeric `amount`, a missing `currency`, or a blank `id`. `load_orders` must **skip** every row that cannot be parsed and **record** it, so the caller can see what was dropped. Malformed input must **not** raise an exception: the function must always return the records it could read.
2. **`total_by_currency(orders)`** — return a dictionary mapping each currency code to the total `amount` in that currency. Currency codes are case-insensitive on input (`eur` and `EUR` are the same currency).
3. **`convert(totals, rates)`** — take the dictionary from (2) and a dictionary of exchange rates (`{"USD": 1.0, "EUR": 1.08, ...}`, where the rate is the number of target-currency units per 1 unit of that currency) and return a new dictionary of converted totals. If a currency in `totals` has no entry in `rates`, raise `KeyError`.
4. **Command line interface** — `python orders.py <csv> <rates.json>` must print one line per currency, sorted by the **converted** amount from largest to smallest, in the form `CODE  converted_total`.

## Marking notes

- Each of the four requirements is checked separately. Do not leave a requirement half-done: a function that fails on dirty data does not earn the credit for requirement 1 even if it works on clean data.
- Keep the functions importable. The marker imports `orders.py` and calls `load_orders`, `total_by_currency` and `convert` directly, so the module must not do work at import time.
- Include the CSV and the rate file you tested with in your submission folder.
- Comments explaining your error handling are welcome but not required.
