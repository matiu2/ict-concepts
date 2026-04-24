"""Shared helpers for drawing schematic candlestick diagrams.

All gotcha diagrams use these primitives to keep a consistent visual language:
- Green bullish candles, red bearish candles
- Dashed horizontal lines for structural levels
- Annotations with arrows for callouts
"""

from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

BULL_COLOR = "#26a69a"
BEAR_COLOR = "#ef5350"
LEVEL_COLOR = "#455a64"
GOOD_COLOR = "#2e7d32"
BAD_COLOR = "#c62828"
LIQ_COLOR = "#f9a825"
TEXT_COLOR = "#263238"


def new_axes(title: str, figsize=(10, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title, fontsize=14, color=TEXT_COLOR, pad=12)
    ax.set_facecolor("#fafafa")
    fig.patch.set_facecolor("white")
    ax.grid(True, alpha=0.15, linestyle="--")
    ax.set_xticks([])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    return fig, ax


def candle(ax, x: float, o: float, h: float, l: float, c: float, width: float = 0.6):
    """Draw a single candle at x with OHLC."""
    color = BULL_COLOR if c >= o else BEAR_COLOR
    ax.plot([x, x], [l, h], color=color, linewidth=1.2, zorder=2)
    body_bottom = min(o, c)
    body_height = max(abs(c - o), 0.02)
    ax.add_patch(
        Rectangle(
            (x - width / 2, body_bottom),
            width,
            body_height,
            facecolor=color,
            edgecolor=color,
            zorder=3,
        )
    )


def candles(ax, ohlc_list, start_x: float = 0.0, spacing: float = 1.0):
    """Draw a series of candles. ohlc_list = [(o, h, l, c), ...]"""
    for i, (o, h, l, c) in enumerate(ohlc_list):
        candle(ax, start_x + i * spacing, o, h, l, c)


def level(ax, y: float, x0: float, x1: float, label: str = "", color: str = LEVEL_COLOR):
    ax.plot([x0, x1], [y, y], linestyle="--", color=color, linewidth=1.3, alpha=0.8, zorder=1)
    if label:
        ax.text(x1 + 0.3, y, label, color=color, fontsize=9, va="center")


def annotate(ax, text: str, xy, xytext, color: str = TEXT_COLOR):
    ax.annotate(
        text,
        xy=xy,
        xytext=xytext,
        fontsize=10,
        color=color,
        arrowprops=dict(arrowstyle="->", color=color, lw=1.2),
        ha="center",
    )


def save(fig, path: str):
    fig.tight_layout()
    fig.savefig(path, dpi=140, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {path}")
