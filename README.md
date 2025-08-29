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
