# Author: 23f1002718@ds.study.iitm.ac.in
# Customer Analytics: CLV vs Acquisition Cost Analysis

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate synthetic dataset
# -----------------------------
np.random.seed(42)

n = 250
acquisition_cost = np.random.uniform(20, 300, n)  # $20–$300 per customer
clv = acquisition_cost * np.random.uniform(2.5, 6.0, n) + np.random.normal(0, 100, n)

data = pd.DataFrame({
    "Acquisition_Cost": acquisition_cost,
    "Customer_Lifetime_Value": clv
})

# -----------------------------
# 2. Styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # clean, presentation-ready font sizes

# -----------------------------
# 3. Scatterplot
# -----------------------------
plt.figure(figsize=(8, 8))  # ensures 512x512 px at dpi=64
sns.scatterplot(
    data=data,
    x="Acquisition_Cost",
    y="Customer_Lifetime_Value",
    palette="viridis"
)

plt.title("Customer Lifetime Value vs Acquisition Cost", fontsize=18)
plt.xlabel("Acquisition Cost ($)")
plt.ylabel("Customer Lifetime Value ($)")

# -----------------------------
# 4. Export figure (exact 512x512 px)
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
plt.close()
