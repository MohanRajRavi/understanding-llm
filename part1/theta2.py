import numpy as np

# Dataset: houses with a hidden base cost
# True formula: price = 100 × size + 50,000  (the model doesn't know this)
sizes  = np.array([500, 1000, 1500, 2000, 2500, 3000, 3500], dtype=float)
prices = np.array([100000, 150000, 200000, 250000, 300000, 350000, 400000], dtype=float)

# Show why one theta isn't enough
best_single_theta = np.dot(sizes, prices) / np.dot(sizes, sizes)
print(f"Best single theta: {best_single_theta:.1f}")
print("Predictions with one theta:")
for sz, pr in zip(sizes, prices):
    pred  = best_single_theta * sz
    print(f"  {sz:.0f} sqft → predicted ${pred:,.0f}  actual ${pr:,.0f}  diff ${pred - pr:+,.0f}")
print("  Small houses are consistently off — one theta can't capture a base cost.\n")

# Two thetas: theta1 = price per sqft, theta2 = base price
theta1 = 150.0
theta2 = 0.0

# theta1's gradient is scaled by sizes (~500–3500) so it needs a smaller lr
# theta2's gradient is just mean(errors) — can move faster
lr1 = 1e-7
lr2 = 5e-4

num_iterations = 100_000

for i in range(num_iterations):
    errors    = (theta1 * sizes + theta2) - prices
    theta1   -= lr1 * np.mean(errors * sizes)
    theta2   -= lr2 * np.mean(errors)

print(f"After {num_iterations:,} iterations:")
print(f"  theta1 = {theta1:.2f}  (expected: 100)")
print(f"  theta2 = {theta2:,.0f}  (expected: 50,000)\n")

print("Predictions:")
for sz, pr in zip(sizes, prices):
    pred = theta1 * sz + theta2
    print(f"  {sz:.0f} sqft → ${pred:,.0f}  (actual ${pr:,.0f})")

# Predict new houses
print("\nNew predictions:")
for sz in [800, 1200, 2200, 4000]:
    print(f"  {sz} sqft → ${theta1 * sz + theta2:,.0f}")
