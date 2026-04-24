"""Gotcha: BOS is continuation, CHoCH is reversal hint.

Two panels:
- Left: bullish trend making a BOS (continuation)
- Right: bullish trend making a CHoCH (break of prior swing low)
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from chart_utils import (
    BAD_COLOR,
    GOOD_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    level,
    save,
)


def left_panel(ax):
    ax.set_title("BOS — continuation (NOT a reversal)", fontsize=12, color=TEXT_COLOR)
    # up-leg, pullback, up-leg breaking prior high
    data = [
        (1.0, 1.4, 0.9, 1.3),
        (1.3, 1.9, 1.2, 1.8),
        (1.8, 2.3, 1.7, 2.2),  # swing high forming
        (2.2, 2.35, 2.0, 2.05),  # pullback
        (2.05, 2.1, 1.6, 1.7),
        (1.7, 1.9, 1.55, 1.85),  # swing low
        (1.85, 2.2, 1.8, 2.15),
        (2.15, 2.6, 2.1, 2.55),  # breaks prior high -> BOS
        (2.55, 3.0, 2.5, 2.95),
        (2.95, 3.3, 2.85, 3.2),
    ]
    candles(ax, data, start_x=0)
    level(ax, 2.3, -0.5, 9.5, "prior swing high", color=TEXT_COLOR)
    annotate(ax, "BOS ✓ continuation", xy=(7, 2.5), xytext=(4.5, 3.4), color=GOOD_COLOR)
    ax.set_ylim(1.3, 3.8)
    ax.set_xlim(-1, 11)


def right_panel(ax):
    ax.set_title("CHoCH — first hint of reversal", fontsize=12, color=TEXT_COLOR)
    # bullish structure that then breaks a prior swing low
    data = [
        (1.0, 1.4, 0.9, 1.3),
        (1.3, 1.9, 1.2, 1.8),
        (1.8, 2.3, 1.7, 2.2),  # swing high
        (2.2, 2.25, 1.95, 2.0),
        (2.0, 2.1, 1.7, 1.75),  # swing low to watch
        (1.75, 2.0, 1.65, 1.95),
        (1.95, 2.15, 1.85, 2.1),
        (2.1, 2.2, 1.8, 1.85),  # lower high
        (1.85, 1.9, 1.5, 1.55),  # breaks the swing low -> CHoCH
        (1.55, 1.6, 1.2, 1.25),
    ]
    candles(ax, data, start_x=0)
    level(ax, 1.7, -0.5, 9.5, "prior swing low", color=TEXT_COLOR)
    annotate(ax, "CHoCH ⚠ reversal hint\n(not confirmation)", xy=(8, 1.5), xytext=(5, 2.8), color=BAD_COLOR)
    ax.set_ylim(1.0, 3.3)
    ax.set_xlim(-1, 11)


def main():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    for ax in (ax1, ax2):
        ax.set_facecolor("#fafafa")
        ax.grid(True, alpha=0.15, linestyle="--")
        ax.set_xticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    left_panel(ax1)
    right_panel(ax2)
    fig.suptitle("Gotcha: don't confuse BOS with CHoCH", fontsize=14, color=TEXT_COLOR)
    save(fig, "src/images/gotcha-bos-vs-choch.png")


if __name__ == "__main__":
    main()
