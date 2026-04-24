"""Silver Bullet setup diagram.

Shows the classic Silver Bullet: bullish HTF bias, pullback during the
10-11 AM NY window into a bullish FVG, entry on the gap, target at
prior high liquidity.
"""

from __future__ import annotations

from matplotlib.patches import Rectangle

from chart_utils import (
    GOOD_COLOR,
    LIQ_COLOR,
    TEXT_COLOR,
    BAD_COLOR,
    annotate,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Silver Bullet — FVG entry in the 10-11 AM NY window", figsize=(13, 6))

    data = [
        # Early morning — the impulse up
        (1.8, 2.0, 1.75, 1.95),
        (1.95, 2.2, 1.9, 2.15),
        (2.15, 2.35, 2.1, 2.30),   # leaves a small FVG?
        (2.30, 2.60, 2.25, 2.55),  # candle 1 of FVG
        (2.55, 2.95, 2.50, 2.90),  # candle 2 — big displacement up
        (2.90, 3.05, 2.80, 2.85),  # candle 3 — low is the top of FVG
        (2.85, 2.95, 2.55, 2.60),  # pullback starts
        (2.60, 2.65, 2.35, 2.40),
        # Silver Bullet window begins here (x=8)
        (2.40, 2.50, 2.28, 2.32),  # tags FVG
        (2.32, 2.55, 2.25, 2.50),  # entry candle — bounce off FVG
        (2.50, 2.85, 2.45, 2.80),
        (2.80, 3.10, 2.75, 3.05),
        (3.05, 3.35, 3.00, 3.30),  # target: prior high liquidity
    ]
    candles(ax, data, start_x=0)

    # FVG zone (between c1 high 2.60 and c3 low 2.80 — but adjusting for viz)
    fvg_bottom = 2.25
    fvg_top = 2.50
    ax.add_patch(Rectangle((7.5, fvg_bottom), 6, fvg_top - fvg_bottom,
                           facecolor=GOOD_COLOR, alpha=0.15, zorder=0))

    # Silver bullet window highlight
    ax.add_patch(Rectangle((7.5, 1.7), 3, 1.8,
                           facecolor="#fff59d", alpha=0.3, zorder=0))
    ax.text(9, 3.45, "Silver Bullet window\n(10–11 AM NY)",
            fontsize=10, color=TEXT_COLOR, ha="center", fontweight="bold")

    # Target
    level(ax, 3.35, -0.5, 13.5, "prior high — buy-side liquidity target", color=LIQ_COLOR)

    # Entry and SL
    ax.scatter([9], [2.40], marker="o", s=130, color=GOOD_COLOR, zorder=5, edgecolors="white")
    annotate(ax, "entry", xy=(9, 2.40), xytext=(10.5, 1.85), color=GOOD_COLOR)

    ax.scatter([8], [2.28], marker="_", s=250, color=BAD_COLOR, zorder=5, linewidths=3)
    annotate(ax, "SL below FVG", xy=(8, 2.28), xytext=(5.5, 1.95), color=BAD_COLOR)

    ax.text(10.5, 2.37, "FVG", fontsize=10, color=GOOD_COLOR,
            ha="center", style="italic", fontweight="bold")

    ax.set_ylim(1.65, 3.65)
    ax.set_xlim(-0.7, 14)
    save(fig, "src/images/strategy-silver-bullet.png")


if __name__ == "__main__":
    main()
