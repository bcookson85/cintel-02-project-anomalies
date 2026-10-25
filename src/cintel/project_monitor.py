"""Project Performance Monitoring - Static Anomaly Detection.

Author: Brian Cookson
Date: 2026-10

Analyze synthetic project request response times and flag
requests that exceed a predefined response-time threshold.
"""

import logging
from pathlib import Path

from datafun_toolkit.logger import get_logger, log_header, log_path

from cintel.utils_project import detect_project_anomalies, load_project_data

LOG: logging.Logger = get_logger("P2", level="DEBUG")

ROOT_DIR = Path.cwd()
DATA_FILE = ROOT_DIR / "data" / "project_responses.csv"
OUTPUT_FILE = ROOT_DIR / "artifacts" / "project_anomalies.csv"

MAX_RESPONSE_DAYS = 7


def main() -> None:
    """Run the project response-time anomaly detection pipeline."""
    log_header(LOG, "PROJECT PERFORMANCE MONITORING")

    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Load project request data.
    df = load_project_data(DATA_FILE)
    LOG.info(f"Loaded {df.height} project requests")

    # Apply the response-time anomaly rule.
    LOG.info(f"Response-time threshold: {MAX_RESPONSE_DAYS} days")

    anomalies_df = detect_project_anomalies(
        df,
        max_response_days=MAX_RESPONSE_DAYS,
    )

    LOG.info(f"Count of anomalies found: {anomalies_df.height}")

    # Save detected anomalies.
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    anomalies_df.write_csv(OUTPUT_FILE)

    LOG.info("Project anomaly results saved successfully.")
    LOG.info("Pipeline executed successfully!")


if __name__ == "__main__":
    main()
