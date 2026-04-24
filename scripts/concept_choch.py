"""Concept diagram: CHoCH (Change of Character).

Shows a bullish trend making a bearish CHoCH — price breaks a prior
swing low, hinting that the side in charge may have changed.
"""

from __future__ import annotations

from chart_utils import (
    BAD_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("CHoCH — Change of Character (first hint of a shift)", figsize=(11, 5.5))

    # bullish structure that rolls over and breaks the last swing low
    data = [
        (1.0, 1.4, 0.9, 1.3),
        (1.3, 1.9, 1.2, 1.85),
        (1.85, 2.4, 1.8, 2.35),  # swing high
        (2.35, 2.4, 2.05, 2.1),
        (2.1, 2.2, 1.8, 1.85),   # swing low to watch
        (1.85, 2.1, 1.75, 2.05),
        (2.05, 2.25, 2.0, 2.2),  # lower high starting
        (2.2, 2.25, 1.9, 1.95),
        (1.95, 2.0, 1.55, 1.6),  # CHoCH candle — breaks the swing low
        (1.6, 1.65, 1.25, 1.3),
    ]
    candles(ax, data, start_x=0)

    level(ax, 1.8, -0.5, 9.5, "prior swing low", color=TEXT_COLOR)

    ax.scatter([2], [2.45], marker="v", s=120, color=TEXT_COLOR, zorder=5)
    ax.scatter([4], [1.78], marker="^", s=120, color=TEXT_COLOR, zorder=5)
    ax.annotate("swing high", xy=(2, 2.48), xytext=(2, 2.65), fontsize=9, color=TEXT_COLOR, ha="center")
    ax.annotate("swing low", xy=(4, 1.75), xytext=(4, 1.45), fontsize=9, color=TEXT_COLOR, ha="center")

    annotate(
        ax,
        "CHoCH — someone new\njust showed up",
        xy=(8, 1.7),
        xytext=(5.5, 2.75),
        color=BAD_COLOR,
    )

    ax.set_ylim(1.0, 3.0)
    ax.set_xlim(-1, 11)
    save(fig, "src/images/concept-choch.png")


if __name__ == "__main__":
    main()
