# understanding-llm

Companion code for the Medium series **"Understanding LLM"** — written for complete beginners.

📖 **Part 1:** [What is a Model?](https://medium.com/@YOUR_USERNAME)

---

## What's in here

**Part 1 — What is a Model?**

| File | Description |
|---|---|
| `theta1.py` | One parameter. Learns `price = θ × size` from scratch. |
| `theta2.py` | Two parameters. Learns `price = θ₁ × size + θ₂`. Discovers a hidden base cost. |
| `interactive_theta1.py` | Drag a slider to find the right θ yourself. |
| `interactive_theta2.py` | Two sliders — find both θ₁ and θ₂ by hand. |

![interactive_theta1](interactive_theta1.gif)
![interactive_theta2](interactive_theta2.gif)

---

## Setup

```bash
pip install numpy matplotlib
```

---

## Run

```bash
# follow along with the blog
python theta1.py
python theta2.py

# play with it yourself (opens a window)
python interactive_theta1.py
python interactive_theta2.py
```

---

## Series

| | Part | Status |
|---|---|---|
| Part 1 | What is a Model? | ✅ [Read on Medium](https://medium.com/@YOUR_USERNAME) |
| Part 2 | How Does a Model Read Words? | 🔜 Coming soon |
| Part 3 | What is Training Data? | 🔜 Coming soon |
| Part 4 | What Makes GPT Different? | 🔜 Coming soon |

---

Made by [Sujay](https://medium.com/@YOUR_USERNAME) — if this helped, leave a ⭐
