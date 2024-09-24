
# IHE Thesis: Machine Learning and Climate Data Analysis for Zankalon, Egypt

This repository contains the necessary scripts and notebooks used for the analysis of Actual Evapotranspiration and Interception (AETI) in the Zankalon region, Egypt. The analysis utilizes climate data from AgERA5, WaPOR, and CMIP6 models. This repository provides workflows for downloading data, performing zonal statistics, training machine learning models, and conducting trend analyses.

## Table of Contents
1. [Overview](#overview)
2. [Setup Instructions](#setup-instructions)
3. [Directory Structure](#directory-structure)
4. [Scripts Usage](#scripts-usage)
5. [Notebooks Overview](#notebooks-overview)
6. [License](#license)

## Overview

This repository supports a wide range of analysis tasks:
- **Climate Data Downloads**: Fetching climate data from AgERA5, WaPOR v2, and CMIP6 models.
- **Zonal Statistics**: Performing spatial analysis on AETI data to track water consumption trends for crops.
- **Machine Learning**: Training Support Vector Regression (SVR) models on climate data to predict AETI under different scenarios.
- **Trend and Correlation Analysis**: Evaluating trends using Mann-Kendall tests, correlation matrices, and PCA (Principal Component Analysis).

The analysis focuses on major crops in Zankalon, Egypt, including **Orchards, Wheat, Rice, Clover, Grapes, and Potatoes**. Seasonal and yearly variations in AETI are examined under future climate scenarios (SSP2-4.5 and SSP5-8.5).

## Setup Instructions

### 1. Clone the Repository
   ```bash
   git clone https://github.com/sadow999/IHE-Thesis.git
   cd IHE-Thesis
   ```
   
### 2. Install Dependencies
Ensure you have Python 3.x installed. Use the provided `requirements.txt` to install the necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Set Up the CDS API Key (for downloading AgERA5 and CMIP6 data)
To download climate data from Copernicus, set up your CDS API key by following these [instructions](https://cds.climate.copernicus.eu/api-how-to).

### 4. Data Access for WaPOR
For WaPOR data, ensure you have access to the WaPOR platform.

## Directory Structure
```plaintext
├── scripts/             # Python scripts for various tasks
│   ├── 01A_downloading_from_wapor.py
│   ├── BoxPlot_Subplot.py
│   ├── Climate_Variables_AgERA5_vs_CMIP6.py
│   ├── Download_AgERA5_CMIP6.py
│   ├── IHE-NILE_DELTA_CONSUMPTION.py
│   ├── ML_Model_Training.py
│   ├── PCA_and_Correlation_Matrix.py
│   ├── Zonal_Statistics_AETI.py
│   └── correlation_matrix_analysis.py
├── notebooks/           # Jupyter Notebooks for detailed analysis
│   ├── 01A_downloading_from_wapor.ipynb
│   ├── BoxPlot_Subplot.ipynb
│   ├── Climate_Variables_AgERA5_vs_CMIP6.ipynb
│   ├── Download_AgERA5_CMIP6.ipynb
│   ├── IHE-NILE_DELTA_CONSUMPTION.ipynb
│   ├── ML_Model_Training.ipynb
│   ├── PCA_and_Correlation_Matrix.ipynb
│   └── Zonal_Statistics_AETI.ipynb
├── README.md            # This README file
```

## Scripts Usage

### 1. Downloading Data

- **AgERA5 and CMIP6 data**: Run `Download_AgERA5_CMIP6.py` to download climate data (temperature, humidity, precipitation, etc.) for the Zankalon region:
   ```bash
   python scripts/Download_AgERA5_CMIP6.py
   ```

- **WaPOR data**: Run `01A_downloading_from_wapor.py` to fetch AETI and LCC data from the WaPOR v2 platform:
   ```bash
   python scripts/01A_downloading_from_wapor.py
   ```

### 2. Zonal Statistics
Use `Zonal_Statistics_AETI.py` to compute the percentage of area covered by each crop type and calculate AETI values:
   ```bash
   python scripts/Zonal_Statistics_AETI.py
   ```

### 3. Correlation and PCA Analysis

- **Correlation Matrix**: Run `correlation_matrix_analysis.py` to generate a correlation matrix for climate variables:
   ```bash
   python scripts/correlation_matrix_analysis.py
   ```

- **PCA Analysis**: Run `PCA_and_Correlation_Matrix.py` to perform PCA for dimensionality reduction:
   ```bash
   python scripts/PCA_and_Correlation_Matrix.py
   ```

### 4. Machine Learning Model Training
Train and test the Support Vector Regression (SVR) model using the `ML_Model_Training.py` script. This model is trained on AgERA5-WaPOR data and tested on CMIP6 data:
   ```bash
   python scripts/ML_Model_Training.py
   ```

### 5. Climate Scenarios and Trend Analysis

- **Climate Variables Comparison**: Compare AgERA5 and CMIP6 data using `Climate_Variables_AgERA5_vs_CMIP6.py`:
   ```bash
   python scripts/Climate_Variables_AgERA5_vs_CMIP6.py
   ```

- **Mann-Kendall Test for Trends**: Perform trend analysis using `IHE-NILE_DELTA_CONSUMPTION.py`:
   ```bash
   python scripts/IHE-NILE_DELTA_CONSUMPTION.py
   ```

### 6. Box Plot Visualizations
Generate box plots to visualize climate data trends using `BoxPlot_Subplot.py`:
   ```bash
   python scripts/BoxPlot_Subplot.py
   ```

## Notebooks Overview

- **Download_AgERA5_CMIP6.ipynb**: Contains code to download climate data from AgERA5 and CMIP6 models.
- **Zonal_Statistics_AETI.ipynb**: Demonstrates the process of calculating zonal statistics to analyze water consumption per crop.
- **ML_Model_Training.ipynb**: Details the machine learning process for training SVR models using climate data.
- **PCA_and_Correlation_Matrix.ipynb**: Walkthrough of correlation matrix generation and PCA for feature reduction.
- **BoxPlot_Subplot.ipynb**: Creates visualizations like box plots to compare data distributions.

## License
This repository is licensed under the MIT License. See the `LICENSE` file for more details.
