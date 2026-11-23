#!/usr/bin/env python3
import sys

current_customer = None
totals = [0.0] * 6

def emit(customer_id, values):
    total_txns, total_amount, success_count, failed_count, high_count, success_amount = values
    if success_amount >= 1000000000 and success_count >= 50000:
        classification = "PREMIUM_FREQUENT"
    elif success_amount >= 1000000000:
        classification = "PREMIUM"
    elif success_count >= 50000:
        classification = "FREQUENT"
    else:
        classification = "NORMAL"

    # Amounts in this dataset are whole rupees; format without decimal places.
    print("{}\t{}\t{:.0f}\t{}\t{}\t{}\t{:.0f}\t{}".format(
        customer_id, int(total_txns), total_amount, int(success_count),
        int(failed_count), int(high_count), success_amount, classification
    ))

for line in sys.stdin:
    try:
        customer_id, raw = line.rstrip("\n").split("\t", 1)
        values = [float(x) for x in raw.split(",")]
        if len(values) != 6:
            raise ValueError("Expected 6 aggregation fields")
    except Exception as exc:
        print("Skipping malformed intermediate row: " + str(exc), file=sys.stderr)
        continue

    if current_customer is None:
        current_customer = customer_id

    if customer_id != current_customer:
        emit(current_customer, totals)
        current_customer = customer_id
        totals = [0.0] * 6

    totals = [a + b for a, b in zip(totals, values)]

if current_customer is not None:
    emit(current_customer, totals)
