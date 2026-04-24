"""Concept diagram: trendline liquidity.

Three swing lows forming an ascending trendline. Retail places stops
just below — the giants see the line too, and sweep it.
"""

from __future__ import annotations

from chart_utils import (
    LIQ_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Trendline liquidity — stops ride the line", figsize=(11, 5.5))

    # three ascending swing lows, then a sweep below the line
    data = [
        (1.0, 1.2, 0.95, 1.15),
        (1.15, 1.6, 1.0, 1.55),   # first swing low ~1.0
        (1.55, 1.9, 1.5, 1.85),
        (1.85, 1.95, 1.6, 1.65),
        (1.65, 1.8, 1.55, 1.75),  # higher low ~1.55
        (1.75, 2.1, 1.7, 2.05),
        (2.05, 2.3, 2.0, 2.25),
        (2.25, 2.35, 2.1, 2.15),
        (2.15, 2.2, 2.05, 2.1),   # higher low ~2.05
        (2.1, 2.35, 2.05, 2.3),
        (2.3, 2.4, 2.15, 2.2),
        (2.2, 2.25, 1.95, 2.0),   # sweep below trendline
        (2.0, 2.05, 1.7, 1.75),   # breakdown
    ]
    candles(ax, data, start_x=0)

    # ascending trendline drawn through the three lows
    line_xs = [1, 4, 8, 11.5]
    line_ys = [1.0, 1.55, 2.05, 2.35]
    ax.plot(line_xs, line_ys, color=LIQ_COLOR, linewidth=1.4, linestyle="--", alpha=0.9, zorder=1)

    for x, y in zip([1, 4, 8], [1.0, 1.55, 2.05]):
        ax.scatter([x], [y - 0.05], marker="^", s=100, color=TEXT_COLOR, zorder=5)

    annotate(
        ax,
        "stops stacked below\nthe trendline",
        xy=(9, 1.98),
        xytext=(5, 1.25),
        color=LIQ_COLOR,
    )
    annotate(
        ax,
        "sweep → breakdown",
        xy=(12, 1.9),
        xytext=(11, 2.7),
        color=LIQ_COLOR,
    )

    ax.set_ylim(0.7, 3.0)
    ax.set_xlim(-1, 14)
    save(fig, "src/images/concept-trendline-liquidity.png")


if __name__ == "__main__":
    main()
