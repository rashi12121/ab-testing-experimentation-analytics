# Experiment Summary

## Objective
Evaluate whether the redesigned checkout experience increases conversion.

## Primary KPI
Conversion rate = converted users / experiment users.

## Statistical Framework
- Null hypothesis (H0): treatment conversion rate <= control conversion rate.
- Alternative hypothesis (H1): treatment conversion rate > control conversion rate.
- Significance level: alpha = 0.05.
- Report both statistical and practical significance.

## Interpretation Template
Run `python src/analysis.py` to populate the exact observed metrics. The analysis reports:
- control and treatment conversion rates
- absolute and relative lift
- z-test p-value
- chi-square p-value
- bootstrap 95% confidence interval
- device-level treatment behavior

## Important Caveats
- Segment analyses are exploratory and involve multiple comparisons.
- Statistical significance does not automatically imply business significance.
- Before a full rollout, monitor guardrail metrics such as refund rate, average order value, latency, and customer support contacts.
