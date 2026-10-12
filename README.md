# Delivery Time & Customer Complaints Analysis

## Project Overview

This project investigates the relationship between delivery time and customer complaints using Python. It applies exploratory data analysis, Pearson correlation, and linear regression to examine whether longer delivery times are associated with more complaints.

## Objectives

* Explore delivery time and complaint data.
* Measure the strength and direction of the relationship between the two variables.
* Fit a simple linear regression model.
* Visualise the relationship between delivery time and customer complaints.
* Discuss the limitations of the findings.

## Tools and Technologies

* Python
* pandas
* SciPy
* Matplotlib

## Methodology

1. Created a dataset containing 12 illustrative observations.
2. Explored the data using summary statistics.
3. Calculated Pearson's correlation coefficient and p-value.
4. Fitted a simple linear regression model.
5. Predicted the expected complaint count at a delivery time of 82 minutes.
6. Created and saved a scatter plot with a regression line.

## Key Considerations

The dataset is illustrative and does not represent verified real-world delivery records. The results demonstrate statistical techniques rather than establish a real business relationship.

Correlation does not prove causation. Factors such as traffic, weather, order volume, and peak delivery periods could influence both delivery times and complaints.

The dataset is also small, so conclusions should be interpreted cautiously.

## How to Run the Project

1. Install Python.

2. Install the required libraries:

   `py -m pip install pandas scipy matplotlib`

3. Run the analysis:

   `py analysis.py`

The script generates a CSV dataset and saves a visualisation named `correlation_analysis.png`.

## Future Improvements

* Analyse a larger, real-world dataset.
* Investigate additional factors that may influence customer complaints.
* Evaluate regression assumptions and model performance.
* Compare delivery performance across different routes or time periods.
* Develop recommendations supported by stronger evidence.
