"""Utilities for project response-time anomaly detection.

Author: Brian Cookson
Date: 2026-10

Provides reusable functions for loading project response data
and identifying unusually long response times.
"""

from pathlib import Path

import polars as pl


def load_project_data(data_file: Path) -> pl.DataFrame:
    """Load project response records from a CSV file."""
    return pl.read_csv(data_file)


def detect_project_anomalies(
    df: pl.DataFrame,
    max_response_days: int = 7,
) -> pl.DataFrame:
    """Identify requests exceeding the response-time threshold."""
    return df.filter(pl.col("response_days") > max_response_days)
