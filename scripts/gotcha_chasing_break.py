"""Gotcha: chasing the break buys the top.

Left panel: entry at break = top-tick, price immediately retraces.
Right panel: wait for retrace into discount → better fill.
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


def make_data():
    # shared price action: up-leg, BOS, retrace, continuation
    return [
        (1.0, 1.4, 0.9, 1.3),
        (1.3, 1.8, 1.25, 1.7),
        (1.7, 2.0, 1.6, 1.95),  # prior swing high at 2.0
        (1.95, 2.0, 1.75, 1.8),
        (1.8, 1.9, 1.6, 1.65),  # swing low
        (1.65, 1.85, 1.6, 1.8),
        (1.8, 2.4, 1.75, 2.35),  # break — top candle
        (2.35, 2.45, 2.05, 2.1),  # retrace
        (2.1, 2.2, 1.95, 2.05),  # discount
        (2.05, 2.3, 2.0, 2.25),
        (2.25, 2.7, 2.2, 2.65),
        (2.65, 3.0, 2.6, 2.95),
    ]


def left_panel(ax):
    ax.set_title("Chasing the break — buys the top", fontsize=12, color=TEXT_COLOR)
    data = make_data()
    candles(ax, data, start_x=0)
    level(ax, 2.0, -0.5, 11.5, "prior swing high", color=TEXT_COLOR)
    # entry at the break candle close
    ax.scatter([6], [2.35], marker="o", s=140, color=BAD_COLOR, zorder=5, edgecolors="white")
    annotate(ax, "entry @ break\n= top-tick", xy=(6, 2.35), xytext=(3, 3.0), color=BAD_COLOR)
    ax.set_ylim(0.8, 3.3)
    ax.set_xlim(-1, 13)


def right_panel(ax):
    ax.set_title("Waiting for retrace — better fill", fontsize=12, color=TEXT_COLOR)
    data = make_data()
    candles(ax, data, start_x=0)
    level(ax, 2.0, -0.5, 11.5, "prior swing high", color=TEXT_COLOR)
    ax.scatter([8], [2.05], marker="o", s=140, color=GOOD_COLOR, zorder=5, edgecolors="white")
    annotate(ax, "entry on retrace\n(discount zone)", xy=(8, 2.05), xytext=(10, 1.4), color=GOOD_COLOR)
    ax.set_ylim(0.8, 3.3)
    ax.set_xlim(-1, 13)


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
    fig.suptitle("Gotcha: don't chase the break — wait for the retrace", fontsize=14, color=TEXT_COLOR)
    save(fig, "src/images/gotcha-chasing-break.png")


if __name__ == "__main__":
    main()
