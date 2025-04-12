# Same logic as before, but removing ace_tools and using only native print statements and matplotlib.
# This version uses monthly values from the slide chart and prints full summary of water savings.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Monthly water loss estimates in millions of gallons (based on Slide chart)
baseline_monthly_loss = np.array([
    8600, 8300, 8700, 10800, 13000, 14900,
    16800, 17900, 18500, 18800, 19200, 19500
])  # millions

goldilocks_monthly_loss = np.array([
    5400, 5100, 5200, 7100, 9800, 11000,
    12400, 13200, 13700, 13900, 14200, 14500
])  # millions

# Convert to billions for reporting
baseline_monthly_loss_b = baseline_monthly_loss / 1000
goldilocks_monthly_loss_b = goldilocks_monthly_loss / 1000
monthly_savings_b = baseline_monthly_loss_b - goldilocks_monthly_loss_b

# Totals
total_baseline = baseline_monthly_loss_b.sum()
total_goldilocks = goldilocks_monthly_loss_b.sum()
total_saved = monthly_savings_b.sum()
efficiency_gain = (total_saved / total_baseline) * 100

# Print formatted summary
print("\n---------------------------------------------")
print("2024 Water Loss Summary (Real Monthly Data)")
print("---------------------------------------------")
print(f"Total Water Lost (Baseline):    {total_baseline:.2f} billion gallons")
print(f"Total Water Lost (Goldilocks):  {total_goldilocks:.2f} billion gallons")
print(f"Total Water Saved:              {total_saved:.2f} billion gallons")
print(f"Efficiency Improvement:         {efficiency_gain:.1f}%")

# Print breakdown table
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

print("\nMonthly Breakdown (in Billions of Gallons):")
print(f"{'Month':<5} {'Baseline':>10} {'Goldilocks':>14} {'Saved':>10}")
for i in range(12):
    print(f"{months[i]:<5} {baseline_monthly_loss_b[i]:>10.2f} {goldilocks_monthly_loss_b[i]:>14.2f} {monthly_savings_b[i]:>10.2f}")

# Visualization
x = np.arange(len(months))
width = 0.3

plt.figure(figsize=(12, 6))
plt.bar(x - width, baseline_monthly_loss_b, width=width, label='Baseline Loss', color='gray')
plt.bar(x, goldilocks_monthly_loss_b, width=width, label='Goldilocks Loss', color='green')
plt.bar(x + width, monthly_savings_b, width=width, label='Saved', color='blue')

plt.xticks(x, months)
plt.ylabel("Water Loss (Billions of Gallons)")
plt.title("Monthly Water Loss Comparison - Baseline vs Goldilocks")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()