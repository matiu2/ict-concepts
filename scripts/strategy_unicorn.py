"""Unicorn Model diagram.

Breaker block + overlapping FVG at a discount level.
Structure: bullish trend -> pullback that forms a breaker (failed bearish OB)
-> displacement up leaving an FVG inside the breaker -> entry at the overlap.
"""

from __future__ import annotations

from matplotlib.patches import Rectangle

from chart_utils import (
    GOOD_COLOR,
    BAD_COLOR,
    annotate,
    candles,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Unicorn — Breaker + FVG overlap", figsize=(13, 6))

    data = [
        (1.2, 1.4, 1.15, 1.35),
        (1.35, 1.65, 1.3, 1.60),
        (1.60, 1.90, 1.55, 1.85),   # up-leg
        (1.85, 2.10, 1.80, 2.05),
        (2.05, 2.20, 1.90, 1.95),   # bearish OB (up candle then reversal)
        (1.95, 2.00, 1.75, 1.80),   # drops
        (1.80, 1.85, 1.60, 1.65),   # new low — reversal seemed valid
        (1.65, 1.85, 1.60, 1.80),   # starts recovering
        (1.80, 2.10, 1.78, 2.05),   # breaks back above — OB is now a BREAKER
        (2.05, 2.35, 2.00, 2.30),   # candle 1 of FVG
        (2.30, 2.70, 2.28, 2.65),   # candle 2 — displacement
        (2.65, 2.80, 2.55, 2.60),   # candle 3 — FVG formed
        (2.60, 2.70, 2.35, 2.40),   # pullback to zone
        (2.40, 2.50, 2.08, 2.12),   # tags the overlap
        (2.12, 2.40, 2.08, 2.35),   # bounces
        (2.35, 2.70, 2.30, 2.65),
        (2.65, 2.95, 2.60, 2.90),
    ]
    candles(ax, data, start_x=0)

    # Breaker block zone (the failed bearish OB — the up candle at index 4)
    breaker_bottom = 2.00
    breaker_top = 2.20
    ax.add_patch(Rectangle((4 - 0.5, breaker_bottom), 13,
                           breaker_top - breaker_bottom,
                           facecolor=BAD_COLOR, alpha=0.12, zorder=0))

    # FVG zone (between c1 high 2.35 and c3 low 2.55)
    fvg_bottom = 2.10
    fvg_top = 2.28
    ax.add_patch(Rectangle((9 - 0.5, fvg_bottom), 8,
                           fvg_top - fvg_bottom,
                           facecolor=GOOD_COLOR, alpha=0.18, zorder=0))

    # Overlap zone (where breaker and FVG intersect)
    overlap_bottom = 2.10
    overlap_top = 2.20
    ax.add_patch(Rectangle((9 - 0.5, overlap_bottom), 8,
                           overlap_top - overlap_bottom,
                           facecolor=GOOD_COLOR, alpha=0.4, zorder=1,
                           edgecolor=GOOD_COLOR, linewidth=1.5))

    ax.text(6, 2.26, "Breaker block", fontsize=10,
            color=BAD_COLOR, style="italic")
    ax.text(14, 2.32, "FVG", fontsize=10, color=GOOD_COLOR, style="italic")
    ax.text(13, 2.15, "Unicorn (overlap)", fontsize=11,
            color=GOOD_COLOR, fontweight="bold", ha="center")

    ax.scatter([13], [2.12], marker="o", s=130,
               color=GOOD_COLOR, zorder=5, edgecolors="white")
    annotate(ax, "entry at overlap", xy=(13, 2.12),
             xytext=(10, 1.65), color=GOOD_COLOR)

    ax.set_ylim(1.3, 3.1)
    ax.set_xlim(-1, 18)
    save(fig, "src/images/strategy-unicorn.png")


if __name__ == "__main__":
    main()
