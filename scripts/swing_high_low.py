"""Illustrates what a swing high / swing low is.

Three panels:
- Left: textbook 1-candle swing high (lower candles on each side)
- Middle: 3-candle (fractal) swing high — stricter, 2 lower candles each side
- Right: a "weak" swing high that gets invalidated by later candles
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


def panel_1_candle(ax):
    ax.set_title("1-candle swing high (ICT default)", fontsize=11, color=TEXT_COLOR)
    data = [
        (1.2, 1.6, 1.1, 1.5),
        (1.5, 1.9, 1.4, 1.85),
        (1.85, 2.4, 1.8, 2.35),  # swing high candle
        (2.35, 2.4, 2.05, 2.1),
        (2.1, 2.15, 1.8, 1.85),
    ]
    candles(ax, data, start_x=0)
    ax.scatter([2], [2.45], marker="v", s=140, color=GOOD_COLOR, zorder=5)
    annotate(
        ax,
        "swing high —\n1 lower candle each side",
        xy=(2, 2.4),
        xytext=(3.3, 2.9),
        color=GOOD_COLOR,
    )
    ax.set_ylim(1.0, 3.1)
    ax.set_xlim(-0.7, 6.2)


def panel_fractal(ax):
    ax.set_title("3-candle (fractal) swing high — stricter", fontsize=11, color=TEXT_COLOR)
    data = [
        (1.0, 1.3, 0.9, 1.25),
        (1.25, 1.6, 1.2, 1.55),
        (1.55, 1.9, 1.5, 1.85),
        (1.85, 2.4, 1.8, 2.35),  # swing high candle
        (2.35, 2.4, 2.1, 2.15),
        (2.15, 2.2, 1.85, 1.9),
        (1.9, 1.95, 1.55, 1.6),
    ]
    candles(ax, data, start_x=0)
    ax.scatter([3], [2.45], marker="v", s=140, color=GOOD_COLOR, zorder=5)
    annotate(
        ax,
        "swing high —\n2 lower candles each side",
        xy=(3, 2.4),
        xytext=(5.3, 2.9),
        color=GOOD_COLOR,
    )
    ax.set_ylim(0.8, 3.1)
    ax.set_xlim(-0.7, 7.5)


def panel_weak(ax):
    ax.set_title("Weak swing — invalidated by later candles", fontsize=11, color=TEXT_COLOR)
    data = [
        (1.3, 1.7, 1.2, 1.65),
        (1.65, 2.0, 1.6, 1.95),
        (1.95, 2.3, 1.9, 2.25),  # candidate swing high
        (2.25, 2.35, 2.0, 2.05),
        (2.05, 2.6, 2.0, 2.55),  # higher high — invalidates the earlier "swing"
        (2.55, 2.9, 2.5, 2.85),
    ]
    candles(ax, data, start_x=0)
    ax.scatter([2], [2.35], marker="x", s=160, color=BAD_COLOR, linewidths=3, zorder=5)
    annotate(
        ax,
        "looked like a swing…\nbroken two candles later",
        xy=(2, 2.3),
        xytext=(0.2, 2.95),
        color=BAD_COLOR,
    )
    ax.set_ylim(1.0, 3.1)
    ax.set_xlim(-0.7, 6.2)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    for ax in axes:
        ax.set_facecolor("#fafafa")
        ax.grid(True, alpha=0.15, linestyle="--")
        ax.set_xticks([])
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    panel_1_candle(axes[0])
    panel_fractal(axes[1])
    panel_weak(axes[2])
    fig.suptitle("Swing high: how many candles on each side?", fontsize=14, color=TEXT_COLOR)
    save(fig, "src/images/swing-high-variants.png")


if __name__ == "__main__":
    main()
