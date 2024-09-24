
# Climate Data Analysis for Zankalon, Egypt

This repository contains scripts and notebooks for downloading climate data, performing machine learning model training, and analyzing trends in evapotranspiration (AETI) across multiple crops and climate scenarios for the Zankalon region.

## Table of Contents
1. [Overview](#overview)
2. [Setup](#setup)
3. [Running the Scripts](#running-the-scripts)
4. [Analysis](#analysis)
5. [License](#license)

## Overview
This project involves the following key tasks:
- Downloading climate data (AgERA5 and CMIP6) and WaPOR AETI and LCC data.
- Calculating zonal statistics to analyze crop-specific water consumption.
- Correlation matrix and PCA analysis for dimensionality reduction.
- Machine learning model development (Support Vector Regression - SVR).
- Climate scenario analysis (SSP2-4.5 and SSP5-8.5) for predicting AETI trends.
- Seasonal and yearly AETI analysis for major crops: Orchards, Wheat, Rice, Clover, Grapes, Potatoes.

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/sadow999/IHE-Thesis
   cd IHE-Thesis
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Scripts

1. **Download Climate Data**:
   ```bash
   python scripts/download_climate_data.py
   ```

2. **Download AETI and LCC Data from WaPOR**:
   ```bash
   python scripts/download_wapor_data.py
   ```

3. **Zonal Statistics**:
   ```bash
   python scripts/zonal_statistics_crop_AETI.py
   ```

4. **Correlation Matrix Analysis**:
   ```bash
   python scripts/correlation_matrix_analysis.py
   ```

5. **PCA Analysis**:
   ```bash
   python scripts/pca_analysis.py
   ```

6. **SVR Model Training**:
   ```bash
   python scripts/train_svr_model.py
   ```

7. **Z-Score Analysis**:
   ```bash
   python scripts/z_score_analysis.py
   ```

8. **Climate Scenarios Analysis**:
   ```bash
   python scripts/climate_scenarios_analysis.py
   ```

9. **Mann-Kendall Test**:
   ```bash
   python scripts/mann_kendall_test.py
   ```

## Analysis
You can find detailed analysis and results in the notebooks provided in the `/notebooks/` folder. This includes data download processes, model training, and visualizations for trends under different climate scenarios.

## License
This repository is licensed under the MIT License.
