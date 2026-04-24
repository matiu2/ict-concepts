"""Power of 3 — Accumulation, Manipulation, Distribution.

Shows the three-phase daily (or session) pattern: a tight accumulation,
a manipulation move against the intended direction (stop hunt), and
then the main distribution leg.
"""

from __future__ import annotations

from matplotlib.patches import Rectangle

from chart_utils import (
    BAD_COLOR,
    GOOD_COLOR,
    LIQ_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Power of 3 — Accumulation → Manipulation → Distribution", figsize=(13, 6))

    # Phase 1: accumulation (tight range)
    acc = [
        (1.95, 2.05, 1.90, 2.00),
        (2.00, 2.08, 1.95, 2.03),
        (2.03, 2.07, 1.97, 2.00),
        (2.00, 2.05, 1.93, 1.98),
        (1.98, 2.04, 1.92, 2.00),
        (2.00, 2.06, 1.95, 2.02),
    ]
    # Phase 2: manipulation (fake down-move below the range, grabs sell-side liq)
    manip = [
        (2.02, 2.05, 1.85, 1.90),
        (1.90, 1.92, 1.75, 1.80),  # sweep low
    ]
    # Phase 3: distribution (strong reversal up, main leg)
    dist = [
        (1.80, 2.10, 1.78, 2.05),
        (2.05, 2.35, 2.00, 2.30),
        (2.30, 2.60, 2.25, 2.55),
        (2.55, 2.85, 2.50, 2.80),
        (2.80, 3.05, 2.75, 3.00),
    ]
    all_data = acc + manip + dist
    candles(ax, all_data, start_x=0)

    # Phase backgrounds
    ax.add_patch(Rectangle((-0.5, 1.7), 6, 1.5, facecolor=TEXT_COLOR, alpha=0.05, zorder=0))
    ax.add_patch(Rectangle((5.5, 1.7), 2.5, 1.5, facecolor=BAD_COLOR, alpha=0.08, zorder=0))
    ax.add_patch(Rectangle((7.8, 1.7), 6, 1.5, facecolor=GOOD_COLOR, alpha=0.08, zorder=0))

    # Phase labels
    ax.text(2.5, 3.08, "1. ACCUMULATION", fontsize=11, color=TEXT_COLOR, ha="center", fontweight="bold")
    ax.text(6.5, 3.08, "2. MANIPULATION", fontsize=11, color=BAD_COLOR, ha="center", fontweight="bold")
    ax.text(10.5, 3.08, "3. DISTRIBUTION", fontsize=11, color=GOOD_COLOR, ha="center", fontweight="bold")

    # Range line under accumulation
    ax.axhline(1.9, xmin=0.02, xmax=0.42, color=LIQ_COLOR, linestyle="--", alpha=0.7, linewidth=1)
    ax.text(2.5, 1.82, "sell-side liquidity\nbelow range", fontsize=9, color=LIQ_COLOR, ha="center")

    annotate(ax, "fake-out —\nstops swept", xy=(7, 1.80), xytext=(7, 2.4), color=BAD_COLOR)
    annotate(ax, "the real move", xy=(11, 2.6), xytext=(11.5, 1.9), color=GOOD_COLOR)

    ax.set_ylim(1.6, 3.25)
    ax.set_xlim(-1, 14)
    save(fig, "src/images/concept-po3.png")


if __name__ == "__main__":
    main()
