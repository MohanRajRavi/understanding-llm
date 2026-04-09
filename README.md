# Understanding LLM

Interactive code for the series: [Medium – Understanding LLM](https://medium.com/@mohansujay22054044/58b20eddf2f4)

## Table of contents

- [What's in here](#whats-in-here)
- [Setup](#setup)
- [Run](#run)
- [Series](#series)

---

## What's in here

| File | Description |
|---|---|
| `part1/theta1.py` | One parameter. Learns `price = θ × size` from scratch. |
| `part1/theta2.py` | Two parameters. Learns `price = θ₁ × size + θ₂`. Discovers a hidden base cost. |
| `part1/interactive_theta1.py` | Drag a slider to find the right θ yourself. |
| `part1/interactive_theta2.py` | Two sliders — find both θ₁ and θ₂ by hand. |

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
# from repo root — follow along with the blog
python part1/theta1.py
python part1/theta2.py

# play with it yourself (opens a window)
python part1/interactive_theta1.py
python part1/interactive_theta2.py
```

---

## Series

| Part | Topic | Status |
|---|---|---|
| Part 1 | What is a Model? | [Medium – Understanding LLM](https://medium.com/@mohansujay22054044/58b20eddf2f4) |
| Part 2 | How Does a Model Read Words? | Coming soon |
| Part 3 | What is Training Data? | Coming soon |
| Part 4 | What Makes GPT Different? | Coming soon |

---

<p align="center">
  <img src="sujay_logo.png" width="80" alt="Sujay"><br>
  Made by Mohan/Sujay ⭐
</p>
