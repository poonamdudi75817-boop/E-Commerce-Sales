#!/usr/bin/env python3
import sys

for line in sys.stdin:
    try:
        customer_id, raw = line.rstrip("\n").split("\t", 1)
        values = [float(x) for x in raw.split(",")]
        if len(values) != 6:
            raise ValueError("Expected 6 aggregation fields")
        print(customer_id + "\t" + ",".join(str(v) for v in values))
    except Exception as exc:
        print("Skipping malformed intermediate row: " + str(exc), file=sys.stderr)


