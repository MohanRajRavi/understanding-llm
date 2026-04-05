# Understanding LLM — Part 1: What is a Model?

> Companion code for the Medium blog series **"Understanding LLM"**
>
> 📖 **Part 1:** [What is a Model?](https://medium.com/@YOUR_USERNAME) — you are here

---

## What is this?

This repo contains four Python scripts for Part 1 of the series — two that run in the terminal, and two interactive ones with sliders you can drag to explore the concepts yourself.

No libraries. No frameworks. Just Python, NumPy, and Matplotlib.

**The big idea:** A model is just a formula with unknown numbers (called *parameters* or *thetas*). The computer learns the right values for those numbers by looking at data — guessing, checking the error, and adjusting, over and over again.

GPT-4 does the exact same thing. It just has 1.7 trillion parameters instead of 1 or 2.

---

## Part 1 — Files

### Core scripts (terminal output)

| File | What it does |
|---|---|
| `theta1.py` | One-parameter model. Learns `price = θ × size`. Simplest possible example. |
| `theta2.py` | Two-parameter model. Learns `price = θ₁ × size + θ₂`. Discovers a hidden base cost. |

### Interactive scripts (drag sliders, see live results)

| File | What it does |
|---|---|
| `interactive_theta1.py` | Drag a single slider to find the right θ. Line and MSE update live. |
| `interactive_theta2.py` | Two sliders — one for slope (θ₁), one for base price (θ₂). An orange dot on the Y-axis tracks θ₂ as you move it. |

---

## Requirements

```bash
pip install numpy matplotlib
```

---

## How to Run

**Clone the repo:**
```bash
git clone https://github.com/YOUR_USERNAME/understanding-llm.git
cd understanding-llm
```

**Terminal examples:**
```bash
python theta1.py
python theta2.py
```

**Interactive examples (opens a window with sliders):**
```bash
python interactive_theta1.py
python interactive_theta2.py
```

---

## What to Expect

### theta1.py output

```
DATASET
  500 sq ft  →  $50,000
 1000 sq ft  →  $100,000
  ...

BEFORE TRAINING  (theta = 150 — our bad starting guess)
  500 sq ft → predicted $75,000  actual $50,000  error +$25,000  ✗
  ...

TRAINING  (watching theta improve...)
  Iteration    theta           MSE
       1,000  109.09   1,523,491,736
       5,000  100.90      26,003,469
      10,000  100.00               5

AFTER TRAINING  (theta = 100.00)
  500 sq ft → predicted $50,000  actual $50,000  error $0  ✓
  ...
```

### theta2.py output

```
DATASET
  500 sq ft  →  $100,000
  ...
  Notice: even the smallest house (500 sq ft) costs $100,000.

ATTEMPT WITH ONE THETA  (best single theta = 114.3)
  500 sq ft → predicted $57,143  actual $100,000  error -$42,857  ✗
  ...
  The small houses are consistently wrong.

TRAINING  (both thetas improving together...)
  Iteration    theta1    theta2             MSE
      1,000    118.12    4705.0   410,409,311
     20,000    102.71   43215.6     9,207,363
    100,000    100.00   49997.7               1

AFTER TRAINING
  theta1 = 100.00  (should be ~100)
  theta2 = 49997.7  (should be ~50,000)

  500 sq ft → predicted $99,998  actual $100,000  ✓
  ...
```

---

## The Key Concept

| | theta1.py | theta2.py |
|---|---|---|
| **Parameters** | 1 (theta) | 2 (theta1, theta2) |
| **Formula** | `price = θ × size` | `price = θ₁ × size + θ₂` |
| **What it learns** | price per sq ft | price per sq ft + base price |
| **Limitation** | Can't model a base cost | — |
| **Comparison** | A model with 1 neuron | A model with 2 neurons |

And for perspective:

| Model | Parameters |
|---|---|
| theta1.py | 1 |
| theta2.py | 2 |
| GPT-2 (2019) | 117,000,000 |
| GPT-3 (2020) | 175,000,000,000 |
| GPT-4 (2023) | ~1,700,000,000,000 |

Same core idea. Different scale.

---

## Things to Try

**interactive_theta1.py** — drag the slider and find where MSE hits 0. Try starting from θ = 10 vs θ = 240 — does it feel different?

**interactive_theta2.py** — try fixing θ₁ = 100 first, then adjusting only θ₂. Then do it the other way. Notice how the two parameters are independent of each other.

**theta1.py** — change `learning_rate` to `1e-5` (10× bigger). What happens to theta? Does it overshoot?

**theta2.py** — change the starting guesses to `theta1 = 50.0, theta2 = 100000.0` and rerun. Does it still find the right answer?

---

## Blog Series

| Part | Topic | Code | Post |
|---|---|---|---|
| Part 1 | What is a Model? | `theta1.py`, `theta2.py`, `interactive_theta1.py`, `interactive_theta2.py` | ✅ [Read on Medium](https://medium.com/@YOUR_USERNAME) |
| Part 2 | How Does a Model Read Words? | coming soon | 🔜 Coming soon |
| Part 3 | What is Training Data? | coming soon | 🔜 Coming soon |
| Part 4 | What Makes GPT Different? | coming soon | 🔜 Coming soon |

---

## Author

**Sujay** — writing ML concepts for complete beginners.

Follow on Medium: [@YOUR_USERNAME](https://medium.com/@YOUR_USERNAME)

---

*If this helped you understand ML a little better — leave a ⭐ on the repo!*
