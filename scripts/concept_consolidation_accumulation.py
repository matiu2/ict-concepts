"""How accumulation works inside consolidation.

Shows a range bounded by a high and low. Inside the range:
- Buy arrows at the lows (institutions accumulating)
- Sell arrows at the highs (institutions selling some back to push price down)
- Labels for stops building above/below the range
- A final breakout showing where the built position gets released
"""

from __future__ import annotations

from chart_utils import (
    BULL_COLOR,
    BEAR_COLOR,
    GOOD_COLOR,
    LIQ_COLOR,
    TEXT_COLOR,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Consolidation — accumulation inside a range", figsize=(12, 6))

    # A range roughly between 1.70 and 2.20, lasting ~14 candles, then breakout up
    data = [
        (1.2, 1.5, 1.15, 1.45),
        (1.45, 1.85, 1.4, 1.8),   # approach into range
        (1.8, 2.15, 1.75, 2.10),  # touches range high
        (2.10, 2.20, 1.95, 2.0),  # push to top
        (2.0, 2.05, 1.75, 1.80),  # sell-off inside range
        (1.80, 1.90, 1.70, 1.75), # touches range low
        (1.75, 2.00, 1.72, 1.95), # bounce up
        (1.95, 2.18, 1.90, 2.15), # touches range high again
        (2.15, 2.20, 1.95, 2.00), # sell
        (2.00, 2.05, 1.72, 1.78), # down to low
        (1.78, 1.85, 1.70, 1.80), # low tap
        (1.80, 2.05, 1.78, 2.00), # bounce
        (2.00, 2.20, 1.95, 2.18), # up to high
        (2.18, 2.55, 2.15, 2.50), # breakout!
        (2.50, 2.80, 2.45, 2.75),
        (2.75, 3.00, 2.70, 2.95),
    ]
    candles(ax, data, start_x=0)

    # Range boundaries
    level(ax, 2.20, -0.5, 12.5, "range high", color=TEXT_COLOR)
    level(ax, 1.70, -0.5, 12.5, "range low", color=TEXT_COLOR)

    # Liquidity pools (stops) above and below
    level(ax, 2.32, -0.5, 12.5, "buy-side liquidity (retail short stops)", color=LIQ_COLOR)
    level(ax, 1.58, -0.5, 12.5, "sell-side liquidity (retail long stops)", color=LIQ_COLOR)

    # Buy arrows at the lows — institutions accumulating
    buy_xs = [5, 10]
    for x in buy_xs:
        ax.annotate(
            "BUY",
            xy=(x, 1.72),
            xytext=(x, 1.35),
            fontsize=10,
            color=BULL_COLOR,
            ha="center",
            fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=BULL_COLOR, lw=1.5),
        )

    # Sell arrows at the highs — pushing price back down
    sell_xs = [3, 8]
    for x in sell_xs:
        ax.annotate(
            "SELL",
            xy=(x, 2.18),
            xytext=(x, 2.55),
            fontsize=10,
            color=BEAR_COLOR,
            ha="center",
            fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=BEAR_COLOR, lw=1.5),
        )

    # Breakout annotation
    ax.annotate(
        "position built →\nreleased",
        xy=(14, 2.7),
        xytext=(15, 2.1),
        fontsize=10,
        color=GOOD_COLOR,
        ha="center",
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=GOOD_COLOR, lw=1.5),
    )

    # Centre label explaining net accumulation
    ax.text(
        6.5, 1.95,
        "Net: accumulating long\n(buying more than selling)",
        fontsize=9,
        color=TEXT_COLOR,
        ha="center",
        style="italic",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor=TEXT_COLOR, alpha=0.85),
    )

    ax.set_ylim(1.2, 3.1)
    ax.set_xlim(-1, 17)
    save(fig, "src/images/concept-consolidation-accumulation.png")


if __name__ == "__main__":
    main()
