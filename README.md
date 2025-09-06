# week1
This repo consist of the work I have done during Edunet Internship's week 1.  
Week 1: Environmental Monitoring & Pollution Control
Understanding the Challenge
Air pollution is a serious issue worldwide, but getting real-time data for specific locations isn’t easy. Most air quality measurements rely on ground monitoring stations, which are expensive to set up and maintain. These stations are often spread thin and sometimes provide incomplete or inconsistent data.

My Project Idea
I’m exploring whether it’s possible to predict air quality—specifically PM2.5 levels—using satellite images, supplemented by ground-based measurements. If successful, this approach could make it easier to monitor pollution across large areas, without depending solely on costly ground stations.

Week 1 Goals
Finalized the Project Topic: Committed to using satellite imagery and ground truth data to predict air pollution levels.

Data Exploration: Researched what kinds of satellite and ground datasets are available, including their formats and coverage.

Started Collecting Data: Began downloading both satellite images and CPCB air quality data to kick off the project.

Data Collection Overview
Satellite Data (INSAT-3D/3DR):

Data Source: MOSDAC.gov.in

Focused on two main spectral bands:

TIR1 (Thermal Infrared): Tracks heat patterns and surface temps.

WV (Water Vapour): Offers insight into atmospheric conditions.

Format: GeoTIFF (.tif) images updated every half hour.

Ground Data (CPCB):

Data Source: Kaggle’s CPCB dataset (hourly PM2.5 values).

Includes several states and stations but is quite raw:

Lots of missing data

Inconsistent timestamps

Mixed data formats

Key Challenges This Week
Huge Satellite Data Volumes: Even for one state, the number of images is overwhelming, which means I need to plan for storage and data processing early on.

Messy Ground Data: The CPCB data requires cleaning—fixing timestamps, handling missing values, and standardizing formats for analysis.

Learning Curve: Getting comfortable with satellite imaging concepts, band selection, data formats, and how to organize downloads from MOSDAC.

What I’ve Done So Far
Defined a clear direction for the project.

Collected the first batch of CPCB data for initial testing.

Downloaded a pilot set of INSAT images for a small time window.

Carried out a basic review of GeoTIFF files and took a first look at CPCB data structure.

Looking Ahead: Week 2 Plans
Finish cleaning and prepping the CPCB data, matching timestamps to station locations.

Write scripts to crop satellite images so they focus on areas around each air quality station.

Start integrating satellite and ground data to build the first air quality prediction model.



# Week 2: Data Preparation & First Model Training
Focus of Week 2

In Week 1, I focused on deciding the project topic and collecting some initial data.
Week 2 was about taking that raw data, cleaning it up, and trying out the first round of models. The aim was just to see if pollution levels (PM2.5) could be predicted at all from satellite image features.

Data Preparation

CPCB Ground Data

Fixed missing values and cleaned timestamps.

Filtered the data to match the time window of satellite images.

Saved as: cpcb_cleaned.csv.

INSAT Satellite Data

Worked with GeoTIFF files from the TIR1 and WV bands.

Pulled out simple features like mean, standard deviation, minimum, and maximum pixel values.

Saved as: insat_features_sample.csv.

Merged Dataset

Matched CPCB readings with the closest INSAT timestamps.

Created a small training dataset:

timestamp | station_id | PM2.5 | band_mean | band_std | band_min | band_max


Saved as: training_dataset.csv.

Model Training

I tested three basic models to get a sense of what works:

Model	R² (approx)	RMSE (µg/m³)	Notes
Linear Regression	~0.15–0.20	High	Too simple, poor fit
Random Forest	~0.45–0.55	Moderate	Better, captured non-linear trends
XGBoost	~0.60–0.68	Lower	Best so far, most reliable
Challenges

CPCB data had gaps and missing values that needed handling.

Timing mismatch between CPCB (hourly) and INSAT (half-hourly) meant I had to use nearest-neighbor matching.

With only very simple features from the satellite images, the models could only go so far.

What I Learned

Even with limited features, it’s possible to explain around 60% of the variance in PM2.5.

XGBoost looks like a strong option for further work.

Cleaning and aligning the data is just as important as the actual model training.

Next Steps (Week 3)

Add more advanced features (rolling stats, percentiles, skewness, etc.).

Crop satellite images around stations to get more location-specific data.

Try out LightGBM and improve evaluation with time-aware validation.
