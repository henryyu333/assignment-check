"""Order reporting script for COMP9001 Assignment 2.

Usage:
    python orders.py <orders.csv> <rates.json>
"""

from __future__ import annotations

import csv
import json
import sys


def load_orders(path):
    """Read a CSV export and return a list of parsed order records.

    Each record is a dict with keys ``id``, ``amount`` and ``currency``.
    """
    orders = []
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for line_no, row in enumerate(reader, start=2):
            try:
                order_id = row["id"].strip()
                if not order_id:
                    raise ValueError("blank id")
                amount = float(row["amount"])
                currency = row["currency"].strip().upper()
                if not currency:
                    raise ValueError("blank currency")
            except (KeyError, TypeError, AttributeError, ValueError) as exc:
                raise ValueError(f"row {line_no} is malformed: {row!r}") from exc
            orders.append({"id": order_id, "amount": amount, "currency": currency})
    return orders


def total_by_currency(orders):
    """Sum the amounts of ``orders`` per currency code."""
    totals = {}
    for order in orders:
        code = order["currency"]
        totals[code] = totals.get(code, 0.0) + order["amount"]
    return totals


def convert(totals, rates):
    """Convert totals into the target currency using ``rates``.

    Raises KeyError if a currency in ``totals`` has no rate.
    """
    return {code: total * rates[code] for code, total in totals.items()}


def main(argv):
    if len(argv) != 3:
        print("usage: python orders.py <orders.csv> <rates.json>", file=sys.stderr)
        return 2

    with open(argv[2], encoding="utf-8") as handle:
        rates = json.load(handle)

    orders = load_orders(argv[1])
    converted = convert(total_by_currency(orders), rates)

    width = max(len(code) for code in converted)
    for code, total in sorted(converted.items(), key=lambda item: item[1], reverse=True):
        print(f"{code:<{width}}  {total:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
