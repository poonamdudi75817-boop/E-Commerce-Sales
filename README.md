# Hadoop E-Commerce Activity

Contents:
- `code/mapper.py`: reads transaction rows and emits customer-level partial statistics.
- `code/combiner.py`: locally sums mapper output fields.
- `code/reducer.py`: final customer aggregation and classification.
- `output/customer_analysis.csv`: locally computed expected output for all customers.
- `REPORT.md`: methodology, dataset summary, commands, validation, and report template.

Start with `REPORT.md`. Hadoop execution has not been run in this environment; run the commands on your Hadoop setup and add your own runtime, shuffle-counter values, and screenshots.
