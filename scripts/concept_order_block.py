"""Bullish order block: the last down-close candle before a strong rally.

Shows a down-move, a final red candle, then a strong bullish breakout —
with the red candle's range highlighted as the order block.
"""

from __future__ import annotations

from matplotlib.patches import Rectangle

from chart_utils import (
    GOOD_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Bullish Order Block — last down-close before a rally", figsize=(11, 5.5))

    data = [
        (2.3, 2.35, 2.1, 2.15),
        (2.15, 2.2, 1.95, 2.0),
        (2.0, 2.05, 1.8, 1.85),
        (1.85, 1.9, 1.65, 1.7),  # OB candle — last down-close
        (1.7, 2.15, 1.68, 2.10), # strong rally away
        (2.10, 2.45, 2.05, 2.40),
        (2.40, 2.70, 2.35, 2.65),
        (2.65, 2.80, 2.40, 2.50), # pullback toward OB
        (2.50, 2.55, 2.00, 2.05),
        (2.05, 2.10, 1.75, 1.80), # tag OB zone
        (1.80, 2.20, 1.78, 2.15), # bounce off OB
        (2.15, 2.50, 2.10, 2.45),
        (2.45, 2.80, 2.40, 2.75),
    ]
    candles(ax, data, start_x=0)

    # Highlight OB candle range
    ob_bottom = 1.65
    ob_top = 1.90
    ax.add_patch(
        Rectangle(
            (3 - 0.5, ob_bottom),
            13,
            ob_top - ob_bottom,
            facecolor=GOOD_COLOR,
            alpha=0.15,
            zorder=0,
        )
    )
    ax.axhline(ob_top, xmin=0, xmax=1, color=GOOD_COLOR, linestyle="--", alpha=0.6, linewidth=1)
    ax.axhline(ob_bottom, xmin=0, xmax=1, color=GOOD_COLOR, linestyle="--", alpha=0.6, linewidth=1)

    annotate(ax, "OB candle\n(last red before rally)", xy=(3, 1.68), xytext=(1, 2.5), color=TEXT_COLOR)
    annotate(ax, "price returns —\nOB holds", xy=(9, 1.82), xytext=(11, 1.3), color=GOOD_COLOR)

    ax.text(7, 1.77, "Order Block zone", fontsize=10, color=GOOD_COLOR, ha="center", style="italic")

    ax.set_ylim(1.3, 3.1)
    ax.set_xlim(-1, 14)
    save(fig, "src/images/concept-order-block.png")


if __name__ == "__main__":
    main()
