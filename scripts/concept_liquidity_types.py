"""Concept diagram: buy-side vs sell-side liquidity.

Two panels showing where resting orders sit relative to swings.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from chart_utils import (
    LIQ_COLOR,
    TEXT_COLOR,
    candles,
    level,
    save,
)


def buyside(ax):
    ax.set_title("Buy-side liquidity — stops above swing highs", fontsize=11, color=TEXT_COLOR)
    data = [
        (1.0, 1.4, 0.9, 1.3),
        (1.3, 1.85, 1.2, 1.8),
        (1.8, 2.3, 1.75, 2.25),  # swing high
        (2.25, 2.3, 1.95, 2.0),
        (2.0, 2.1, 1.75, 1.8),
        (1.8, 2.0, 1.75, 1.95),
        (1.95, 2.2, 1.9, 2.15),
    ]
    candles(ax, data, start_x=0)
    level(ax, 2.3, -0.5, 7.5, "swing high", color=TEXT_COLOR)
    level(ax, 2.45, -0.5, 7.5, "buy-side liquidity", color=LIQ_COLOR)
    ax.text(3.5, 2.55, "(buy stops from shorts,\nbreakout buy orders)", fontsize=9, color=LIQ_COLOR, ha="center")
    ax.set_ylim(1.0, 3.0)
    ax.set_xlim(-0.7, 8)


def sellside(ax):
    ax.set_title("Sell-side liquidity — stops below swing lows", fontsize=11, color=TEXT_COLOR)
    data = [
        (2.2, 2.25, 1.9, 1.95),
        (1.95, 2.0, 1.55, 1.6),
        (1.6, 1.7, 1.3, 1.35),  # swing low
        (1.35, 1.5, 1.25, 1.45),
        (1.45, 1.7, 1.4, 1.65),
        (1.65, 1.8, 1.55, 1.75),
        (1.75, 1.9, 1.6, 1.65),
    ]
    candles(ax, data, start_x=0)
    level(ax, 1.3, -0.5, 7.5, "swing low", color=TEXT_COLOR)
    level(ax, 1.15, -0.5, 7.5, "sell-side liquidity", color=LIQ_COLOR)
    ax.text(3.5, 1.02, "(sell stops from longs,\nbreakout sell orders)", fontsize=9, color=LIQ_COLOR, ha="center")
    ax.set_ylim(0.85, 2.6)
    ax.set_xlim(-0.7, 8)


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    for ax in (ax1, ax2):
        ax.set_facecolor("#fafafa")
        ax.grid(True, alpha=0.15, linestyle="--")
        ax.set_xticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    buyside(ax1)
    sellside(ax2)
    fig.suptitle("Two sides of the same coin: where the liquidity sits", fontsize=14, color=TEXT_COLOR)
    save(fig, "src/images/concept-liquidity-types.png")


if __name__ == "__main__":
    main()
