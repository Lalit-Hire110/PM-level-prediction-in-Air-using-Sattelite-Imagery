AirCast — Final Project README

Short version: I built a proof-of-concept pipeline that combines INSAT satellite imagery with CPCB ground measurements to predict PM₂.₅. After cleaning and merging the data, doing careful time & station validation, and iterating on features and models, the final XGBoost model gives strong temporal and spatial performance (RMSE ≈ 28–29 μg/m³, R² ≈ 0.68–0.79).

This README sums up what I did in Weeks 1–4, what the final model looks like, how it was validated, and what’s next.

Project summary

Goal: Predict PM₂.₅ (hourly) using INSAT (TIR1 & WV) satellite imagery + CPCB station data.

Why: Ground stations are sparse and expensive. If satellite-derived features + historical pollution can predict PM₂.₅ reliably, this enables broader spatial coverage for air-quality monitoring.

Scope: 20 CPCB stations, 2021–2022, ~102,720 hourly samples.

Week-by-week (short)

Week 1: Picked the topic, researched datasets, started downloading INSAT GeoTIFFs and CPCB CSVs. Learned the limits (data volume, messy ground data).

Week 2: Cleaned CPCB timestamps/values, parsed GeoTIFFs, pulled simple image stats (mean/std/min/max), made a merged training file, ran baseline models (Linear, RF, XGBoost).

Week 3: Scaled merging across stations & time, engineered more features (lags, rolling stats), ran stronger models including LightGBM/CatBoost/XGBoost variants.

Week 4: Final feature selection, locked leakage-safe features, trained the final XGBoost model, and ran robust validation (time splits, leave-one-station-out, nested CV).

What I improvised (short)

I didn’t just run default pipelines — I tried multiple learners (LightGBM, CatBoost, XGBoost variants), switched to time-aware evaluation instead of random splits, tightened timestamp alignment logic, and enforced a leakage-safe feature selection (correlation + VIF checks). Those small changes turned a quick proof-of-concept into a reproducible, validated model.

Final model — quick facts

Algorithm: XGBoost Regressor (1000 trees)

Target: log1p(PM2.5) during training — inverse expm1() for final metrics.

Features used: 72 leakage-safe features (fixed after correlation & VIF screening)

Training samples: 102,720 hourly observations

Stations: 20 CPCB monitoring stations

Date range: 2021–2022

Final performance (detailed)
TimeSeriesSplit (temporal robustness)

Mean RMSE: 27.98 ± 5.34 μg/m³

Mean R²: 0.676 ± 0.154

(Mean MAE not explicitly reported globally — see per-fold below; typical MAE ≈ 0.7×RMSE)
