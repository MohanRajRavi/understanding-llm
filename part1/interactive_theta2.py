import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

sizes  = np.array([500, 1000, 1500, 2000, 2500, 3000, 3500], dtype=float)
prices = np.array([100000, 150000, 200000, 250000, 300000, 350000, 400000], dtype=float)

x_line = np.linspace(0, 4000, 300)

INITIAL_T1 = 150.0
INITIAL_T2 = 0.0

def mse(t1, t2):
    return np.mean((t1 * sizes + t2 - prices) ** 2)

def mse_color(m):
    if m < 1e6:    return "#2E9B5A"
    if m < 5e8:    return "#E07B20"
    return "#D94F4F"

# ── layout ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6.5))
fig.patch.set_facecolor("#FFFDF5")
ax.set_facecolor("#FFFDF5")
plt.subplots_adjust(bottom=0.36)

ax.scatter(sizes, prices, color="#2855A0", s=100, zorder=5,
           label="Actual prices", edgecolors="white", linewidths=0.8)
pred_line, = ax.plot(x_line, INITIAL_T1 * x_line + INITIAL_T2,
                     color="#D94F4F", linewidth=2.5, label="Your prediction")

# mark where the line crosses the Y-axis — helps visualise theta2
intercept_dot, = ax.plot(0, INITIAL_T2, marker='o', markersize=9,
                          color="#E07B20", zorder=6, label="θ₂ (base price)")

ax.set_xlim(0, 4000)
ax.set_ylim(-60000, 500000)
ax.set_xlabel("House Size (sq ft)", fontsize=11)
ax.set_ylabel("Price ($)", fontsize=11)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v/1000:.0f}K"))
ax.grid(True, alpha=0.2, linestyle="--")
ax.legend(fontsize=10, loc="upper left")

formula_text = ax.text(
    0.60, 0.18, "", transform=ax.transAxes,
    fontsize=11, va="top",
    bbox=dict(boxstyle="round,pad=0.45", facecolor="white", edgecolor="#cccccc", alpha=0.9)
)

hint_text = ax.text(
    0.60, 0.04, "🎯  θ₁ ≈ 100  |  θ₂ ≈ 50,000", transform=ax.transAxes,
    fontsize=8.5, va="top", color="#aaaaaa"
)

def update_text(t1, t2):
    m = mse(t1, t2)
    color = mse_color(m)
    formula_text.set_text(f"price = {t1:.0f}×size + {t2:,.0f}\nMSE = {m:,.0f}")
    formula_text.get_bbox_patch().set_edgecolor(color)
    formula_text.set_color(color)

update_text(INITIAL_T1, INITIAL_T2)

# ── sliders ───────────────────────────────────────────────────────────────────
ax_s1 = plt.axes([0.15, 0.22, 0.70, 0.04], facecolor="#f0ede4")
ax_s2 = plt.axes([0.15, 0.13, 0.70, 0.04], facecolor="#f0ede4")

slider1 = Slider(ax_s1, "θ₁  (slope)",     10.0,   250.0,
                 valinit=INITIAL_T1, valstep=1.0,     color="#2855A0")
slider2 = Slider(ax_s2, "θ₂  (base price)", -50000, 150000,
                 valinit=INITIAL_T2, valstep=500.0,   color="#E07B20")

for s in (slider1, slider2):
    s.label.set_fontsize(11)
    s.valtext.set_fontsize(10)

def on_change(_):
    t1, t2 = slider1.val, slider2.val
    y = t1 * x_line + t2
    pred_line.set_ydata(y)
    pred_line.set_color(mse_color(mse(t1, t2)))
    intercept_dot.set_ydata([t2])
    update_text(t1, t2)
    fig.canvas.draw_idle()

slider1.on_changed(on_change)
slider2.on_changed(on_change)

# ── reset button ──────────────────────────────────────────────────────────────
ax_btn = plt.axes([0.80, 0.04, 0.10, 0.05])
btn = Button(ax_btn, "Reset", color="#f0ede4", hovercolor="#ddd8cc")
btn.label.set_fontsize(10)

def on_reset(_):
    slider1.reset()
    slider2.reset()

btn.on_clicked(on_reset)

# ── instructions ──────────────────────────────────────────────────────────────
fig.text(0.5, 0.05,
         "Use both sliders to make the line pass through all the dots  —  watch the orange dot mark θ₂ on the Y-axis",
         ha="center", fontsize=9, color="#555555")

ax.set_title("Interactive: Find the Right θ₁ and θ₂", fontsize=13, fontweight="bold", pad=12)

plt.show()
