# Week 1: Environmental Monitoring & Pollution Control
Understanding the Challenge

Air pollution is a serious issue worldwide, but getting real-time data for specific locations isn’t easy. Most air quality measurements rely on ground monitoring stations, which are expensive to set up and maintain. These stations are often spread thin and sometimes provide incomplete or inconsistent data.

My Project Idea

I’m exploring whether it’s possible to predict air quality—specifically PM2.5 levels—using satellite images, supplemented by ground-based measurements. If successful, this approach could make it easier to monitor pollution across large areas, without depending solely on costly ground stations.

Week 1 Goals

Finalized the Project Topic: Committed to using satellite imagery and ground truth data to predict air pollution levels.

Data Exploration: Researched what kinds of satellite and ground datasets are available, including their formats and coverage.

Started Collecting Data: Began downloading both satellite images and CPCB air quality data to kick off the project.

Data Collection Overview

Satellite Data (INSAT-3D/3DR)

Source: MOSDAC.gov.in

Focused on two main bands:

TIR1 (Thermal Infrared) → tracks heat patterns and surface temps

WV (Water Vapour) → gives insight into atmospheric conditions

Format: GeoTIFF (.tif), updated every half hour

Ground Data (CPCB)

Source: Kaggle CPCB dataset (hourly PM2.5 values)

Covers multiple stations but raw data had issues:

Missing values

Inconsistent timestamps

Mixed file formats

Key Challenges This Week

Huge Satellite Data Volumes → even for one state, the number of images was overwhelming.

Messy Ground Data → CPCB data needed timestamp fixes, missing-value handling, and standardization.

Learning Curve → working with GeoTIFFs, spectral bands, and MOSDAC downloads.

What I’ve Done So Far

Defined a clear direction for the project.

Collected the first batch of CPCB data.

Downloaded a pilot set of INSAT images.

Took a first look at both GeoTIFFs and CPCB CSVs.

Looking Ahead: Week 2 Plans

Clean CPCB data and align timestamps.

Write scripts to crop satellite images around stations.

Begin integrating satellite + ground data for the first prediction model.

Week 2: Data Preparation & First Model Training
Focus of Week 2

In Week 1, I focused on project direction and data collection.
Week 2 was about cleaning up the raw data and running the first round of models. The goal was just to check if PM2.5 could be predicted at all from satellite features.

Data Preparation

CPCB Ground Data

Cleaned missing values and standardized timestamps.

Filtered to match INSAT data time windows.

Output: cpcb_cleaned.csv.

INSAT Satellite Data

Worked with TIR1 & WV GeoTIFF bands.

Extracted simple stats: mean, std, min, max pixel values.

Output: insat_features_sample.csv.

Merged Dataset

Matched CPCB readings with closest INSAT timestamps.

Created training_dataset.csv with aligned values.

Model Training – Baselines
Model	R² (approx)	RMSE (µg/m³)	Notes
Linear Regression	~0.15–0.20	High	Too simple, poor fit
Random Forest	~0.45–0.55	Moderate	Captured non-linear trends
XGBoost	~0.60–0.68	Lower	Best among baselines, reliable
Extended Models (Deeper Tests)

I also tested a few stronger models with more data/features:

LightGBM_1

MAE: 39.90

RMSE: 63.85

R²: 0.6065

Good performance, very close to XGBoost. Time-aware evaluation worked well.

CatBoost_1

MAE: 21.84

RMSE: 34.01

R²: -0.0161 (underfitting, poor generalization)

XGB6 (Lite Version)

MAE: 36.86

RMSE: 60.76

R²: 0.371 (weaker than full XGBoost, but still usable)

Challenges

CPCB data gaps meant I had to drop or interpolate missing values.

INSAT and CPCB timestamps didn’t always match → solved with nearest-neighbor alignment.

Simple features limited model performance; more advanced features are needed.

What I Learned

Even basic satellite features can explain ~60% of PM2.5 variance.

XGBoost and LightGBM are the most promising models so far.

Data cleaning & alignment take as much time (if not more) than the actual training.

Next Steps (Week 3)

Add richer image features (rolling stats, percentiles, skewness).

Crop satellite images to station bounding boxes.

Run stronger models with time-aware validation.

Compare LightGBM, CatBoost, and XGBoost on a larger dataset.
