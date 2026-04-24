"""Gotcha: swing highs/lows are liquidity pools.

Shows a swing high with resting buy-stop liquidity above it, a sweep that
grabs those stops, then a reversal — the opposite of what a naive
continuation reader expects.
"""

from __future__ import annotations

from chart_utils import (
    BAD_COLOR,
    LIQ_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Gotcha: ignoring liquidity above the swing high", figsize=(11, 5.5))

    data = [
        (1.0, 1.4, 0.9, 1.3),
        (1.3, 1.8, 1.2, 1.7),
        (1.7, 2.3, 1.6, 2.25),  # swing high
        (2.25, 2.3, 2.0, 2.05),
        (2.05, 2.15, 1.85, 1.9),  # pullback
        (1.9, 2.1, 1.85, 2.05),
        (2.05, 2.3, 2.0, 2.25),
        (2.25, 2.55, 2.2, 2.5),  # SWEEP — grabs stops above
        (2.5, 2.55, 1.9, 1.95),  # strong rejection
        (1.95, 2.0, 1.6, 1.65),
        (1.65, 1.7, 1.3, 1.35),
    ]
    candles(ax, data, start_x=0)

    level(ax, 2.3, -0.5, 10.5, "swing high", color=TEXT_COLOR)
    level(ax, 2.55, -0.5, 10.5, "buy-side liquidity (stops)", color=LIQ_COLOR)

    annotate(
        ax,
        "sweep → stops taken",
        xy=(7, 2.52),
        xytext=(4, 3.0),
        color=LIQ_COLOR,
    )
    annotate(
        ax,
        "reversal — not continuation",
        xy=(8.2, 2.0),
        xytext=(9.5, 2.8),
        color=BAD_COLOR,
    )

    ax.set_ylim(0.9, 3.3)
    ax.set_xlim(-1, 12)
    save(fig, "src/images/gotcha-liquidity-sweep.png")


if __name__ == "__main__":
    main()
