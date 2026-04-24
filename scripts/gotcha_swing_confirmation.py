"""Gotcha: a swing high/low needs candles on BOTH sides to be valid.

Left panel: "phantom swing" — called too early, invalidated by the next candles.
Right panel: confirmed swing — candles on both sides make lower highs/lower lows.
"""

from __future__ import annotations

import matplotlib.pyplot as plt

from chart_utils import (
    BAD_COLOR,
    GOOD_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    save,
)


def left_panel(ax):
    ax.set_title("Phantom swing — called too early", fontsize=12, color=TEXT_COLOR)
    data = [
        (1.0, 1.3, 0.9, 1.25),
        (1.25, 1.8, 1.2, 1.75),
        (1.75, 2.1, 1.7, 2.05),  # "swing high?"
        (2.05, 2.4, 2.0, 2.35),  # next candle goes HIGHER → not a swing
        (2.35, 2.7, 2.3, 2.65),
        (2.65, 3.0, 2.6, 2.95),
    ]
    candles(ax, data, start_x=0)
    ax.scatter([2], [2.15], marker="x", s=180, color=BAD_COLOR, linewidths=3, zorder=5)
    annotate(
        ax,
        "not a swing —\nright-side higher",
        xy=(2, 2.1),
        xytext=(0.5, 2.9),
        color=BAD_COLOR,
    )
    ax.set_ylim(0.8, 3.3)
    ax.set_xlim(-1, 7)


def right_panel(ax):
    ax.set_title("Confirmed swing — lower candles on both sides", fontsize=12, color=TEXT_COLOR)
    data = [
        (1.0, 1.3, 0.9, 1.25),
        (1.25, 1.8, 1.2, 1.75),
        (1.75, 2.5, 1.7, 2.4),  # swing high candle
        (2.4, 2.45, 2.0, 2.1),  # lower high - right side confirms
        (2.1, 2.15, 1.7, 1.75),
        (1.75, 1.8, 1.3, 1.35),
    ]
    candles(ax, data, start_x=0)
    ax.scatter([2], [2.55], marker="v", s=160, color=GOOD_COLOR, zorder=5)
    annotate(
        ax,
        "valid swing high",
        xy=(2, 2.5),
        xytext=(3.5, 3.0),
        color=GOOD_COLOR,
    )
    ax.set_ylim(0.8, 3.3)
    ax.set_xlim(-1, 7)


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
    fig.suptitle("Gotcha: swings need confirmation on both sides", fontsize=14, color=TEXT_COLOR)
    save(fig, "src/images/gotcha-swing-confirmation.png")


if __name__ == "__main__":
    main()
