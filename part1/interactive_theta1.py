import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

sizes  = np.array([500, 1000, 1500, 2000, 2500], dtype=float)
prices = np.array([50000, 100000, 150000, 200000, 250000], dtype=float)

x_line = np.linspace(0, 3000, 300)

INITIAL_THETA = 50.0  # start far from the answer so there's room to explore

def mse(theta):
    return np.mean((theta * sizes - prices) ** 2)

def mse_color(m):
    if m < 1e6:    return "#2E9B5A"   # green — very close
    if m < 5e8:    return "#E07B20"   # orange — getting there
    return "#D94F4F"                  # red — far off

# ── layout ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor("#FFFDF5")
ax.set_facecolor("#FFFDF5")
plt.subplots_adjust(bottom=0.28)

ax.scatter(sizes, prices, color="#2855A0", s=100, zorder=5,
           label="Actual prices", edgecolors="white", linewidths=0.8)
pred_line, = ax.plot(x_line, INITIAL_THETA * x_line,
                     color="#D94F4F", linewidth=2.5, label="Your prediction")

ax.set_xlim(0, 3000)
ax.set_ylim(-20000, 380000)
ax.set_xlabel("House Size (sq ft)", fontsize=11)
ax.set_ylabel("Price ($)", fontsize=11)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v/1000:.0f}K"))
ax.grid(True, alpha=0.2, linestyle="--")
ax.legend(fontsize=10)

# formula + MSE text (updates live)
formula_text = ax.text(
    0.03, 0.93, "", transform=ax.transAxes,
    fontsize=12, va="top",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="#cccccc", alpha=0.9)
)

hint_text = ax.text(
    0.03, 0.76, "🎯  Target: MSE = 0", transform=ax.transAxes,
    fontsize=9, va="top", color="#888888"
)

def update_text(theta):
    m = mse(theta)
    color = mse_color(m)
    formula_text.set_text(f"price = {theta:.1f} × size\nMSE = {m:,.0f}")
    formula_text.get_bbox_patch().set_edgecolor(color)
    formula_text.set_color(color)

update_text(INITIAL_THETA)

# ── slider ────────────────────────────────────────────────────────────────────
ax_slider = plt.axes([0.15, 0.13, 0.70, 0.04], facecolor="#f0ede4")
slider = Slider(ax_slider, "θ (theta)", 10.0, 250.0,
                valinit=INITIAL_THETA, valstep=0.5, color="#2855A0")
slider.label.set_fontsize(11)
slider.valtext.set_fontsize(11)

def on_slider(val):
    theta = slider.val
    pred_line.set_ydata(theta * x_line)
    pred_line.set_color(mse_color(mse(theta)))
    update_text(theta)
    fig.canvas.draw_idle()

slider.on_changed(on_slider)

# ── reset button ──────────────────────────────────────────────────────────────
ax_btn = plt.axes([0.80, 0.04, 0.10, 0.05])
btn = Button(ax_btn, "Reset", color="#f0ede4", hovercolor="#ddd8cc")
btn.label.set_fontsize(10)

def on_reset(_):
    slider.reset()

btn.on_clicked(on_reset)

# ── instructions ──────────────────────────────────────────────────────────────
fig.text(0.5, 0.05,
         "Drag the slider to find the θ that makes the line pass through all the blue dots  (MSE → 0)",
         ha="center", fontsize=9, color="#555555")

ax.set_title("Interactive: Find the Right θ", fontsize=13, fontweight="bold", pad=12)

plt.show()
