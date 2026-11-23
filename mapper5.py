#!/usr/bin/env python3
import sys, csv

# Output fields:
# total_txns, total_amount, success_count, failed_count,
# high_value_count, successful_amount

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))
        if not row:
            continue
        if row[0].strip().lower() in ("txnid", "transaction id"):
            continue
        if len(row) != 7:
            raise ValueError("Expected 7 columns")

        txn_id, customer_id, category, qty, unit_price, status, payment = [x.strip() for x in row]
        if not customer_id:
            raise ValueError("Missing CustomerID")

        qty = float(qty)
        unit_price = float(unit_price)
        if qty < 0 or unit_price < 0:
            raise ValueError("Negative quantity or unit price")

        amount = qty * unit_price
        status = status.upper()
        if status not in ("SUCCESS", "FAILED"):
            raise ValueError("Invalid transaction status")

        success = 1 if status == "SUCCESS" else 0
        failed = 1 if status == "FAILED" else 0
        high_value = 1 if amount >= 50000 else 0
        successful_amount = amount if success else 0

        values = [1, amount, success, failed, high_value, successful_amount]
        print(customer_id + "\t" + ",".join(str(v) for v in values))
    except Exception as exc:
        print("Skipping malformed row: " + str(exc), file=sys.stderr)
