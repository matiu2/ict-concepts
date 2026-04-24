"""Fair Value Gap: three-candle imbalance.

Middle candle's body leaves a gap between the wicks of candles 1 and 3.
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
    fig, ax = new_axes("Fair Value Gap (bullish) — three-candle imbalance", figsize=(11, 5.5))

    data = [
        (1.4, 1.6, 1.35, 1.55),
        (1.55, 1.7, 1.5, 1.65),
        (1.65, 1.75, 1.55, 1.7),  # candle 1 — high at 1.75
        (1.70, 2.35, 1.68, 2.30), # candle 2 — big bullish
        (2.30, 2.50, 2.25, 2.45), # candle 3 — low at 2.25
        (2.45, 2.60, 2.40, 2.55),
        (2.55, 2.65, 2.35, 2.40), # pullback toward FVG
        (2.40, 2.45, 2.10, 2.15),
        (2.15, 2.20, 1.90, 1.95), # deep pullback into FVG
        (1.95, 2.30, 1.90, 2.25), # bounce from FVG
        (2.25, 2.55, 2.20, 2.50),
        (2.50, 2.80, 2.45, 2.75),
    ]
    candles(ax, data, start_x=0)

    # FVG zone: between candle-1 high (1.75) and candle-3 low (2.25)
    fvg_bottom = 1.75
    fvg_top = 2.25
    ax.add_patch(
        Rectangle(
            (2 + 0.5, fvg_bottom),
            9.5,
            fvg_top - fvg_bottom,
            facecolor=GOOD_COLOR,
            alpha=0.15,
            zorder=0,
        )
    )
    ax.axhline(fvg_bottom, color=GOOD_COLOR, linestyle="--", alpha=0.6, linewidth=1)
    ax.axhline(fvg_top, color=GOOD_COLOR, linestyle="--", alpha=0.6, linewidth=1)

    annotate(ax, "c1 high", xy=(2, 1.76), xytext=(0.5, 1.35), color=TEXT_COLOR)
    annotate(ax, "c3 low", xy=(4, 2.23), xytext=(5.5, 2.9), color=TEXT_COLOR)
    ax.text(7, 2.00, "Fair Value Gap (FVG)", fontsize=10, color=GOOD_COLOR, ha="center", style="italic")
    annotate(ax, "price fills the gap,\nthen continues up", xy=(8, 1.95), xytext=(10, 1.45), color=GOOD_COLOR)

    ax.set_ylim(1.2, 3.0)
    ax.set_xlim(-1, 13)
    save(fig, "src/images/concept-fvg.png")


if __name__ == "__main__":
    main()
