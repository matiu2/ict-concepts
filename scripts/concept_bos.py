"""Concept diagram: BOS (Break of Structure).

Shows a bullish trend making a clean BOS — price breaks past the prior
swing high, confirming the current side is still in charge.
"""

from __future__ import annotations

from chart_utils import (
    GOOD_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("BOS — Break of Structure (continuation)", figsize=(11, 5.5))

    data = [
        (1.0, 1.4, 0.9, 1.3),
        (1.3, 1.8, 1.2, 1.75),
        (1.75, 2.3, 1.7, 2.25),  # swing high forming
        (2.25, 2.35, 2.0, 2.05),
        (2.05, 2.1, 1.7, 1.75),  # pullback low
        (1.75, 1.9, 1.65, 1.85),
        (1.85, 2.2, 1.8, 2.15),
        (2.15, 2.6, 2.1, 2.55),  # BOS candle — breaks prior swing high
        (2.55, 2.95, 2.5, 2.9),
        (2.9, 3.25, 2.85, 3.2),
    ]
    candles(ax, data, start_x=0)

    level(ax, 2.3, -0.5, 9.5, "prior swing high", color=TEXT_COLOR)

    # mark the swing high and the pullback low with dots
    ax.scatter([2], [2.35], marker="v", s=120, color=TEXT_COLOR, zorder=5)
    ax.scatter([4], [1.65], marker="^", s=120, color=TEXT_COLOR, zorder=5)
    ax.annotate("swing high", xy=(2, 2.38), xytext=(2, 2.55), fontsize=9, color=TEXT_COLOR, ha="center")
    ax.annotate("higher low", xy=(4, 1.6), xytext=(4, 1.35), fontsize=9, color=TEXT_COLOR, ha="center")

    annotate(
        ax,
        "BOS — trend continues",
        xy=(7, 2.5),
        xytext=(5, 3.3),
        color=GOOD_COLOR,
    )

    ax.set_ylim(1.1, 3.6)
    ax.set_xlim(-1, 11)
    save(fig, "src/images/concept-bos.png")


if __name__ == "__main__":
    main()
