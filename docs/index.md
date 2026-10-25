
# Project Performance Monitoring — Static Anomaly Detection

**Author:** Brian Cookson  
**Date:** 2026-10  
**Course:** Continuous Intelligence — Northwest Missouri State University

## Overview

This project applies static anomaly detection techniques to project performance monitoring. The objective is to identify project requests with unusually long response times using Python, Polars, and predefined detection thresholds.

The application builds upon the original pediatric clinic anomaly detection example developed by Dr. Denise Case but applies the same analytical principles to a different business problem.

## Data

The project uses a synthetic dataset containing 20 fictional project requests.

Each observation represents one project request and includes:

- `request_id` — Unique project request identifier.
- `project_phase` — Planning, Design, or Construction.
- `response_days` — Number of days required to receive a response.

The dataset was created specifically for this academic project and does not contain actual employer, client, or confidential information.

[View Project Response Dataset](https://github.com/bcookson85/cintel-02-project-anomalies/blob/main/data/project_responses.csv)

## Techniques Applied

The project demonstrates several analytical and development techniques:

- **Python:** Executes the anomaly detection pipeline.
- **Polars:** Loads, filters, and processes structured CSV data.
- **Rule-Based Anomaly Detection:** Identifies observations exceeding a predefined response-time threshold.
- **Structured Logging:** Records execution details and results.
- **Matplotlib:** Generates a visual representation of response times.
- **Git and GitHub:** Manage source code and document project development.

## Methods and Settings

The application reads the project response dataset from `data/project_responses.csv`.

A response-time threshold of seven days was selected for this instructional analysis.

The detection rule is:

**Flag a request when `response_days > 7`.**

Requests taking seven days or fewer are considered within the selected threshold. Requests taking eight days or longer are flagged for further review.

This threshold is an illustrative analytical assumption rather than an established organizational performance standard.

The custom analysis is implemented in:

- `src/cintel/utils_project.py`
- `src/cintel/project_monitor.py`
- `src/cintel/visualize_project.py`

To execute the detection pipeline:

```powershell
uv run python -m cintel.project_monitor
```

To generate the visualization:

```powershell
uv run python -m cintel.visualize_project
```

## Verification

The custom Python pipeline executed successfully using Python 3.14.8 on Windows 11.

Execution confirmed:

- The input dataset contained 20 project requests.
- The response-time threshold was seven days.
- Four requests exceeded the selected threshold.
- The resulting records were saved to `artifacts/project_anomalies.csv`.
- The visualization was generated successfully.

## Results

The application analyzed **20 project requests** and identified **4 anomalous response times**, representing **20% of the dataset**.

| Request ID | Project Phase | Response Time | Days Above Threshold |
|------------|---------------|--------------:|---------------------:|
| REQ-006 | Construction | 9 | 2 |
| REQ-011 | Design | 12 | 5 |
| REQ-016 | Planning | 15 | 8 |
| REQ-018 | Construction | 8 | 1 |

The remaining 16 requests were within the selected seven-day response threshold.

### Results Visualization

![Bar chart displaying response times for 20 project requests, with four requests highlighted above the seven-day threshold.](images/project_response_chart.png)

*Figure 1. Project request response times compared with the seven-day anomaly detection threshold. Red bars identify requests exceeding the selected limit.*

[View Anomaly Results](https://github.com/bcookson85/cintel-02-project-anomalies/blob/main/artifacts/project_anomalies.csv)

## Observations

The analysis identified four requests exceeding the seven-day threshold.

The longest response time was 15 days for REQ-016 during the Planning phase.

Two flagged requests occurred during Construction, one during Design, and one during Planning.

The other 16 requests did not exceed the selected threshold.

## Interpretation and Insights

The results demonstrate how static anomaly detection can help identify project requests that may warrant further investigation.

Requests with longer response times may indicate potential workflow bottlenecks, delays, or opportunities for process improvement.

REQ-016, with a response time of 15 days, exceeded the threshold by eight days and would be a useful starting point for additional review.

However, exceeding the threshold does not necessarily mean the request was mishandled. Project complexity, approval requirements, and other operational factors could explain longer response times.

This approach provides a straightforward method for screening project performance data and directing attention toward potentially important observations.

## Limitations

Several limitations should be considered:

- The dataset is synthetic and does not represent actual organizational performance.
- The seven-day threshold was selected for demonstration purposes.
- The analysis does not account for differences in project complexity or request priority.
- Response times are evaluated independently of project-specific circumstances.
- The application uses static data rather than continuously updated information.

These limitations prevent the results from being interpreted as evidence of actual organizational performance problems.

## Next Steps

Potential improvements include:

1. Evaluate response-time thresholds using historical project performance data.
2. Introduce different thresholds for different request categories or project phases.
3. Incorporate request priority and complexity into the analysis.
4. Compare static thresholds with statistical detection methods.
5. Explore automated reporting and interactive dashboards.

## Conclusion

This project successfully demonstrates how static anomaly detection can be adapted from a clinical data example to a project performance monitoring application.

Using Python and Polars, the application identified four requests exceeding a seven-day response-time threshold in a synthetic dataset of 20 observations.

The results illustrate how relatively simple analytical techniques can support data screening, operational monitoring, and informed business decision-making.

## Documentation Index

- **Home** — This project report
- [Project Instructions](project-instructions.md)
- [Glossary](glossary.md)
- [API](api.md)

## Project Links

- [GitHub Repository](https://github.com/bcookson85/cintel-02-project-anomalies)
- [Custom Python Pipeline](https://github.com/bcookson85/cintel-02-project-anomalies/blob/main/src/cintel/project_monitor.py)
- [Project Dataset](https://github.com/bcookson85/cintel-02-project-anomalies/blob/main/data/project_responses.csv)
- [Anomaly Results](https://github.com/bcookson85/cintel-02-project-anomalies/blob/main/artifacts/project_anomalies.csv)
- [Original Example Project](https://github.com/denisecase/cintel-02-static-anomalies)

## Project Resources

- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Project Instructions](project-instructions.md)
