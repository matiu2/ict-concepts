"""Concept diagram: equal highs as a liquidity pool.

Two swing highs at roughly the same level — every retail trader watching
will have stops clustered just above. The giants see a magnet.
"""

from __future__ import annotations

from chart_utils import (
    LIQ_COLOR,
    TEXT_COLOR,
    annotate,
    candles,
    level,
    new_axes,
    save,
)


def main():
    fig, ax = new_axes("Equal highs — a pool of resting orders", figsize=(11, 5.5))

    data = [
        (1.0, 1.4, 0.9, 1.35),
        (1.35, 1.9, 1.3, 1.85),
        (1.85, 2.30, 1.8, 2.25),  # first swing high ~2.30
        (2.25, 2.35, 1.95, 2.0),
        (2.0, 2.1, 1.75, 1.8),
        (1.8, 2.0, 1.75, 1.95),
        (1.95, 2.20, 1.9, 2.15),
        (2.15, 2.32, 1.95, 2.0),  # second swing high ~2.32 (equal)
        (2.0, 2.1, 1.7, 1.75),
        (1.75, 1.9, 1.65, 1.85),
        (1.85, 2.15, 1.8, 2.1),
        (2.1, 2.45, 2.05, 2.4),   # sweep — third touch grabs the liquidity
    ]
    candles(ax, data, start_x=0)

    level(ax, 2.33, -0.5, 11.5, "equal highs = liquidity", color=LIQ_COLOR)

    ax.scatter([2, 7], [2.35, 2.37], marker="v", s=110, color=TEXT_COLOR, zorder=5)
    annotate(
        ax,
        "stops pile up\njust above",
        xy=(7, 2.4),
        xytext=(4, 2.85),
        color=LIQ_COLOR,
    )
    annotate(
        ax,
        "sweep",
        xy=(11, 2.42),
        xytext=(10.5, 2.8),
        color=LIQ_COLOR,
    )

    ax.set_ylim(1.0, 3.1)
    ax.set_xlim(-1, 13)
    save(fig, "src/images/concept-equal-highs.png")


if __name__ == "__main__":
    main()
