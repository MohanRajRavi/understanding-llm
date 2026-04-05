import numpy as np

# Dataset: house sizes (sq ft) and their prices
# Pattern: every 1 sq ft adds $100  →  price = 100 × size
sizes  = np.array([500, 1000, 1500, 2000, 2500], dtype=float)
prices = np.array([50000, 100000, 150000, 200000, 250000], dtype=float)

# Starting guess — deliberately wrong so we can watch it learn
theta = 150.0

learning_rate  = 1e-7
num_iterations = 10_000

print("Before training:")
for sz, pr in zip(sizes, theta * sizes):
    print(f"  {sz:.0f} sqft → predicted ${pr:,.0f}  (actual ${sizes[list(sizes).index(sz)] * 100:,.0f})")

mse_before = np.mean((theta * sizes - prices) ** 2)
print(f"  MSE: {mse_before:,.0f}\n")

# Gradient descent — nudge theta toward the correct value each iteration
for i in range(num_iterations):
    errors   = theta * sizes - prices
    gradient = np.mean(errors * sizes)
    theta    = theta - learning_rate * gradient

print(f"After {num_iterations:,} iterations:  theta = {theta:.2f}  (expected: 100.00)")

predictions = theta * sizes
for sz, pred, actual in zip(sizes, predictions, prices):
    print(f"  {sz:.0f} sqft → ${pred:,.0f}  (actual ${actual:,.0f})")

mse_after = np.mean((predictions - prices) ** 2)
print(f"  MSE: {mse_after:,.0f}")

# Predict a house the model has never seen
test_size = 1200
print(f"\nNew house ({test_size} sqft) → ${theta * test_size:,.2f}")
