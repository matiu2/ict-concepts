"""Optimal Trade Entry (OTE) — 62%-79% retracement zone.

Shows an up-leg, a pullback into the OTE zone (between 62% and 79%
retracement), and an entry with SL below the swing low.
"""

from __future__ import annotations

from matplotlib.patches import Rectangle

from chart_utils import (
    BAD_COLOR,
    GOOD_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Optimal Trade Entry — 62%–79% pullback zone", figsize=(11, 5.5))

    low = 1.0
    high = 2.5
    fib_62 = high - (high - low) * 0.62  # 1.57
    fib_79 = high - (high - low) * 0.79  # 1.315

    data = [
        (1.00, 1.20, 0.95, 1.15),   # swing low
        (1.15, 1.50, 1.10, 1.45),
        (1.45, 1.90, 1.40, 1.85),
        (1.85, 2.30, 1.80, 2.25),
        (2.25, 2.55, 2.20, 2.50),   # swing high
        (2.50, 2.55, 2.25, 2.30),
        (2.30, 2.35, 2.05, 2.10),
        (2.10, 2.15, 1.75, 1.80),
        (1.80, 1.85, 1.55, 1.60),   # pullback enters OTE
        (1.60, 1.75, 1.40, 1.45),   # deeper into OTE
        (1.45, 1.80, 1.35, 1.75),   # bounce from OTE
        (1.75, 2.05, 1.70, 2.00),
        (2.00, 2.35, 1.95, 2.30),
        (2.30, 2.65, 2.25, 2.60),
    ]
    candles(ax, data, start_x=0)

    # OTE zone
    ax.add_patch(Rectangle((-0.5, fib_79), 15, fib_62 - fib_79, facecolor=GOOD_COLOR, alpha=0.15, zorder=0))

    level(ax, high, -0.5, 14.5, "swing high (100%)", color=TEXT_COLOR)
    level(ax, fib_62, -0.5, 14.5, "62%", color=GOOD_COLOR)
    level(ax, fib_79, -0.5, 14.5, "79%", color=GOOD_COLOR)
    level(ax, low, -0.5, 14.5, "swing low (0%)", color=TEXT_COLOR)

    ax.text(7, (fib_62 + fib_79) / 2, "OTE zone (62%–79%)", fontsize=10, color=GOOD_COLOR, ha="center", style="italic")

    annotate(ax, "entry", xy=(10, 1.45), xytext=(11.5, 1.1), color=GOOD_COLOR)
    annotate(ax, "SL below swing low", xy=(1, 1.0), xytext=(3.5, 0.8), color=BAD_COLOR)

    ax.set_ylim(0.7, 2.85)
    ax.set_xlim(-1, 15)
    save(fig, "src/images/concept-ote.png")


if __name__ == "__main__":
    main()
