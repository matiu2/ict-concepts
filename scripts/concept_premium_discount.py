"""Premium and Discount zones within a dealing range.

Range high = top of premium. Range low = bottom of discount.
50% line = equilibrium.
Premium is the upper half (good for shorts).
Discount is the lower half (good for longs).
"""

from __future__ import annotations

from matplotlib.patches import Rectangle

from chart_utils import (
    BAD_COLOR,
    GOOD_COLOR,
    TEXT_COLOR,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Premium & Discount — the dealing range", figsize=(11, 5.5))

    data = [
        (1.3, 1.6, 1.25, 1.55),  # run-up from low
        (1.55, 1.9, 1.5, 1.85),
        (1.85, 2.25, 1.8, 2.20),
        (2.20, 2.55, 2.15, 2.50),
        (2.50, 2.80, 2.45, 2.75),  # range high at 2.80
        (2.75, 2.80, 2.55, 2.60),
        (2.60, 2.65, 2.40, 2.45),
        (2.45, 2.50, 2.20, 2.25),
        (2.25, 2.30, 2.00, 2.05),
        (2.05, 2.15, 1.85, 1.90),
        (1.90, 1.95, 1.65, 1.70),
        (1.70, 1.90, 1.60, 1.85),  # bounce from discount
        (1.85, 2.20, 1.82, 2.15),
        (2.15, 2.50, 2.10, 2.45),
    ]
    candles(ax, data, start_x=0)

    range_high = 2.80
    range_low = 1.25
    eq = (range_high + range_low) / 2

    # Premium zone (upper half)
    ax.add_patch(Rectangle((-0.5, eq), 15, range_high - eq, facecolor=BAD_COLOR, alpha=0.08, zorder=0))
    # Discount zone (lower half)
    ax.add_patch(Rectangle((-0.5, range_low), 15, eq - range_low, facecolor=GOOD_COLOR, alpha=0.08, zorder=0))

    level(ax, range_high, -0.5, 14.5, "range high (premium top)", color=TEXT_COLOR)
    level(ax, eq, -0.5, 14.5, "equilibrium (50%)", color=TEXT_COLOR)
    level(ax, range_low, -0.5, 14.5, "range low (discount bottom)", color=TEXT_COLOR)

    ax.text(7, 2.55, "PREMIUM — look for shorts", fontsize=11, color=BAD_COLOR, ha="center", fontweight="bold")
    ax.text(7, 1.50, "DISCOUNT — look for longs", fontsize=11, color=GOOD_COLOR, ha="center", fontweight="bold")

    ax.set_ylim(1.15, 3.0)
    ax.set_xlim(-1, 15)
    save(fig, "src/images/concept-premium-discount.png")


if __name__ == "__main__":
    main()
