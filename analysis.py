import numpy as np
import pandas as pd
from scipy.stats import proportions_ztest, chi2_contingency
import matplotlib.pyplot as plt

DATA = "data/ab_test_users.csv"

def bootstrap_lift(control, treatment, iterations=5000, seed=42):
    rng = np.random.default_rng(seed)
    control = np.asarray(control)
    treatment = np.asarray(treatment)
    diffs = np.empty(iterations)
    for i in range(iterations):
        c = rng.choice(control, len(control), replace=True).mean()
        t = rng.choice(treatment, len(treatment), replace=True).mean()
        diffs[i] = t - c
    return np.quantile(diffs, [0.025, 0.975])

def main():
    df = pd.read_csv(DATA)

    # Validation
    assert df["user_id"].is_unique, "user_id must be unique"
    assert df["converted"].isin([0, 1]).all(), "converted must be binary"
    assert set(df["experiment_group"]) == {"control", "treatment"}

    c = df.loc[df.experiment_group == "control", "converted"]
    t = df.loc[df.experiment_group == "treatment", "converted"]

    c_rate, t_rate = c.mean(), t.mean()
    abs_lift = t_rate - c_rate
    rel_lift = abs_lift / c_rate

    count = np.array([t.sum(), c.sum()])
    nobs = np.array([len(t), len(c)])
    z_stat, p_value = proportions_ztest(count, nobs, alternative="larger")

    table = pd.crosstab(df["experiment_group"], df["converted"])
    chi2, chi_p, _, _ = chi2_contingency(table)

    boot_low, boot_high = bootstrap_lift(c, t)

    print("\n=== A/B TEST SUMMARY ===")
    print(f"Control users:   {len(c):,}")
    print(f"Treatment users: {len(t):,}")
    print(f"Control CVR:     {c_rate:.4%}")
    print(f"Treatment CVR:   {t_rate:.4%}")
    print(f"Absolute lift:   {abs_lift:.4%}")
    print(f"Relative lift:   {rel_lift:.2%}")
    print(f"Z-statistic:     {z_stat:.3f}")
    print(f"One-sided p-val: {p_value:.6g}")
    print(f"Chi-square p-val:{chi_p:.6g}")
    print(f"Bootstrap 95% CI for absolute lift: [{boot_low:.4%}, {boot_high:.4%}]")

    decision = (
        "Recommend rollout: statistically significant positive effect."
        if p_value < 0.05 and abs_lift > 0
        else "Do not roll out yet: evidence is insufficient or effect is negative."
    )
    print(decision)

    # Segment analysis
    segment = (
        df.groupby(["device", "experiment_group"], observed=True)["converted"]
        .agg(["count", "mean"])
        .reset_index()
    )
    print("\n=== DEVICE SEGMENTS ===")
    print(segment.to_string(index=False))

    # Simple visualization
    rates = df.groupby("experiment_group", observed=True)["converted"].mean()
    ax = rates.mul(100).plot(kind="bar", figsize=(7, 4))
    ax.set_ylabel("Conversion rate (%)")
    ax.set_title("A/B Test Conversion Rate")
    ax.set_xticklabels(["Control", "Treatment"], rotation=0)
    plt.tight_layout()
    plt.savefig("reports/conversion_rate.png", dpi=160)
    plt.close()

if __name__ == "__main__":
    main()
