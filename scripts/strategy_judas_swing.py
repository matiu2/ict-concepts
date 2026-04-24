"""Judas Swing Reversal diagram.

Asian range highlighted. London sweeps below the low (judas), then
NY reverses up for the main move.
"""

from __future__ import annotations

from matplotlib.patches import Rectangle

from chart_utils import (
    GOOD_COLOR,
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
    fig, ax = new_axes("Judas Swing — London sweep, NY reversal", figsize=(14, 6))

    # Asian range: candles 0-6 (narrow chop between ~1.95 and 2.15)
    asia = [
        (2.00, 2.10, 1.95, 2.05),
        (2.05, 2.12, 1.98, 2.00),
        (2.00, 2.15, 1.97, 2.10),
        (2.10, 2.13, 1.98, 2.02),
        (2.02, 2.10, 1.97, 2.05),
        (2.05, 2.13, 1.95, 1.98),
        (1.98, 2.08, 1.95, 2.02),
    ]
    # London judas — sweeps below Asian low
    london = [
        (2.02, 2.05, 1.85, 1.88),
        (1.88, 1.90, 1.72, 1.75),   # breakdown — looks bearish
        (1.75, 1.85, 1.70, 1.80),   # stops taken at range low
    ]
    # NY reversal — the real move up
    ny = [
        (1.80, 2.10, 1.78, 2.05),
        (2.05, 2.35, 2.00, 2.30),
        (2.30, 2.60, 2.25, 2.55),
        (2.55, 2.80, 2.50, 2.75),
        (2.75, 3.00, 2.70, 2.95),
    ]
    all_data = asia + london + ny
    candles(ax, all_data, start_x=0)

    # Asian range box
    ax.add_patch(Rectangle((-0.5, 1.95), 7.5, 0.2,
                           facecolor=TEXT_COLOR, alpha=0.05, zorder=0))
    # London phase
    ax.add_patch(Rectangle((7, 1.65), 3, 1.45,
                           facecolor=BAD_COLOR, alpha=0.08, zorder=0))
    # NY phase
    ax.add_patch(Rectangle((10, 1.65), 5.5, 1.45,
                           facecolor=GOOD_COLOR, alpha=0.08, zorder=0))

    # Phase labels
    ax.text(3, 2.35, "ASIA — range", fontsize=11, color=TEXT_COLOR,
            ha="center", fontweight="bold")
    ax.text(8.5, 3.05, "LONDON\n(judas swing)", fontsize=11,
            color=BAD_COLOR, ha="center", fontweight="bold")
    ax.text(12.5, 3.05, "NEW YORK\n(real move)", fontsize=11,
            color=GOOD_COLOR, ha="center", fontweight="bold")

    # Asian range high/low
    level(ax, 2.15, -0.5, 15.5, "Asian high", color=TEXT_COLOR)
    level(ax, 1.95, -0.5, 15.5, "Asian low", color=TEXT_COLOR)
    # Sell-side liquidity target
    level(ax, 1.83, -0.5, 15.5, "sell-side liquidity (swept)", color=LIQ_COLOR)

    annotate(ax, "fake breakdown\nsweeps stops", xy=(9, 1.75),
             xytext=(6, 1.75), color=BAD_COLOR)
    ax.scatter([10], [1.82], marker="o", s=130,
               color=GOOD_COLOR, zorder=5, edgecolors="white")
    annotate(ax, "entry\nafter sweep", xy=(10, 1.82),
             xytext=(11.5, 2.4), color=GOOD_COLOR)
    annotate(ax, "NY delivers the move", xy=(14, 2.9),
             xytext=(12, 3.35), color=GOOD_COLOR)

    ax.set_ylim(1.60, 3.5)
    ax.set_xlim(-1, 16)
    save(fig, "src/images/strategy-judas-swing.png")


if __name__ == "__main__":
    main()
