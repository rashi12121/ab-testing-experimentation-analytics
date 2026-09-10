# A/B Testing & Experimentation Analytics

A production-style, end-to-end A/B testing project using Python, SQL, Pandas, SciPy, and statistical inference.

## Business Problem

An e-commerce product team launched a redesigned checkout experience and wants to know whether it improves user conversion without relying on random fluctuations.

**Experiment**
- Control: existing checkout
- Treatment: redesigned checkout
- Primary metric: conversion rate
- Secondary metrics: revenue per user, average order value
- Decision rule: combine statistical significance with practical business impact

## Questions Answered

1. Is the treatment conversion rate higher than control?
2. What is the absolute and relative lift?
3. What is the 95% confidence interval for the treatment effect?
4. Is the result statistically significant?
5. Is the observed lift practically meaningful?
6. Does the treatment behave consistently across device, country, and traffic source?
7. What risks should be considered before rollout?

## Methods

- Data validation and experiment balance checks
- Conversion-rate estimation
- Absolute and relative lift
- Two-proportion z-test
- Chi-square test of independence
- 95% confidence intervals
- Bootstrap confidence interval for lift
- Revenue-per-user comparison
- Segment-level analysis
- Multiple-comparison caution for exploratory segments

## Repository Structure

```text
ab_testing_experimentation_analytics/
├── data/
│   └── ab_test_users.csv
├── notebooks/
│   └── ab_testing_analysis.ipynb
├── reports/
│   └── experiment_summary.md
├── sql/
│   └── experiment_metrics.sql
├── src/
│   ├── analysis.py
│   └── generate_notebook.py
├── requirements.txt
└── README.md
```

## Run Locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python src/analysis.py
```

The project uses a deterministic random seed, so the dataset and analysis are reproducible.

## Example Resume Bullet

**A/B Testing & Experimentation Analytics | Python, SQL, Statistics**
- Designed and analyzed a 50K-user randomized A/B test for an e-commerce checkout redesign, measuring conversion and revenue impact.
- Applied two-proportion z-tests, chi-square testing, confidence intervals, and bootstrap resampling to quantify treatment lift and statistical uncertainty.
- Performed segment-level analysis across device, geography, and acquisition channel to identify heterogeneous treatment effects and support rollout recommendations.


