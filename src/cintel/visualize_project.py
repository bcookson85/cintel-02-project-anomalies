"""Visualize project response-time anomalies.

Author: Brian Cookson
Date: 2026-10
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import polars as pl

ROOT_DIR = Path.cwd()
DATA_FILE = ROOT_DIR / "data" / "project_responses.csv"
OUTPUT_FILE = ROOT_DIR / "docs" / "images" / "project_response_chart.png"

THRESHOLD = 7


def main() -> None:
    """Create a chart showing response times and the anomaly threshold."""
    df = pl.read_csv(DATA_FILE)

    request_ids = df["request_id"].to_list()
    response_days = df["response_days"].to_list()

    colors = [
        "firebrick" if days > THRESHOLD else "steelblue" for days in response_days
    ]

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.bar(request_ids, response_days, color=colors)

    ax.axhline(
        y=THRESHOLD,
        color="black",
        linestyle="--",
        linewidth=1.5,
        label="7-day response threshold",
    )

    ax.set_title("Project Request Response Times")
    ax.set_xlabel("Request ID")
    ax.set_ylabel("Response Time (Days)")
    ax.tick_params(axis="x", rotation=60)
    ax.legend()

    fig.tight_layout()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_FILE, dpi=150)
    plt.close(fig)

    print(f"Chart saved successfully: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
