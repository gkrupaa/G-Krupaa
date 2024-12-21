# Incident Prediction and Police Allocation Model

## Introduction
This project analyzes dispatch data to evaluate the efficiency of policing strategies in San Francisco, California. By examining correlations between timeframes, response times, districts, and incident types in calls for service, we aim to construct predictive models that assist in strategic police resource allocation. The goal is to forecast resource demands across different times and locations to improve public safety measures. 

Given San Francisco's dense urban environment, the city faces challenges such as heightened criminal activity and stretched law enforcement resources. Using data from the San Francisco Police Department, this project uncovers patterns in incident locations, call times, and response metrics to enhance the efficiency and accuracy of police response.

## Overview
This project predicts incident counts using a Random Forest model based on factors such as month, district, and neighborhood. Features include:
- **Temporal data**: Encoded month or hour
- **Incident counts**: Normalized counts and K-means clustering-derived cluster information
- **Categorical data**: Police districts and neighborhoods

By analyzing these features, we identify hotspots, trends in response times, and priority areas requiring greater police presence.

## Getting Started
You can find our app running at https://policeallocation.streamlit.app/

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- pandas
- numpy
- scikit-learn
- streamlit
- joblib

Install the necessary libraries using `pip`:
```bash
pip install pandas numpy scikit-learn streamlit
```

### Clone the Repository
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

## Usage
To run the Streamlit application:
```bash
streamlit run app.py
```

Navigate to http://localhost:8501 in your web browser to interact with the app.

## Features
1. **Incident Location Analysis**:
   - Identifies high-frequency incident areas using cluster information and normalized counts.
   - Pinpoints districts requiring additional resources during specific times of the day.

2. **Call Time Analysis**:
   - Evaluates response times based on call frequency and time of day.
   - Highlights patterns like quicker responses during low call volumes (e.g., 2 a.m.–4 a.m.) and longer response times during peak hours (e.g., 9 p.m.–12 a.m.).

3. **Priority Spectrum Allocation**:
   - Predicts priority levels based on historical data to allocate resources efficiently.

## Model Development
- **Primary Model**: Random Forest, used to predict incident counts and analyze trends in resource demand.
- **Features Considered**:
  - Incident category
  - Priority levels
  - Incident locations
  - Call times
- Predictions include visualizations of expected incident distributions and response times.

## Future Work
- Integrate additional models to compare performance and refine predictions.
- Extend the application to include real-time updates for adaptive police allocation.
- Explore deeper insights into response inefficiencies for optimized resource utilization.

---
This project offers a comprehensive approach to improving urban safety by leveraging data analysis and predictive modeling. Through these efforts, we aim to enable better organization, quicker responses, and enhanced security measures for communities.
