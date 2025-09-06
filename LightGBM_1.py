import pandas as pd
import lightgbm as lgb
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Load & Basic Cleanup
# -------------------------------
df = pd.read_csv("final_dataset/final_dataset.csv")

# Drop unneeded columns
drop_cols = ['state', 'station_location', 'station_id', 'has_TIR1', 'has_WV']
df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors='ignore')

# Convert timestamp
df['timestamp_utc'] = pd.to_datetime(df['timestamp_utc'])
df = df.sort_values('timestamp_utc')  # ensure temporal order

# -------------------------------
# Add Time Features
# -------------------------------
df['hour'] = df['timestamp_utc'].dt.hour
df['month'] = df['timestamp_utc'].dt.month
df['dayofweek'] = df['timestamp_utc'].dt.dayofweek

# -------------------------------
# Lag & Rolling Features
# -------------------------------
LAG_HOURS = [1, 2, 3, 6]
ROLL_WINDOWS = [3, 6, 12]

for lag in LAG_HOURS:
    df[f'PM2.5_lag_{lag}'] = df['PM2.5'].shift(lag)

for window in ROLL_WINDOWS:
    df[f'PM2.5_roll_mean_{window}'] = df['PM2.5'].shift(1).rolling(window=window).mean()

# Drop rows with missing lag/roll data
df = df.dropna()

# -------------------------------
# Time-Based Split
# -------------------------------
# Train = Sept–Oct, Test = November
train_df = df[df['timestamp_utc'].dt.month.isin([9, 10])]
test_df = df[df['timestamp_utc'].dt.month == 11]

# Define features and target
target = 'PM2.5'
features = [col for col in df.columns if col not in ['timestamp_utc', 'PM2.5']]

X_train, y_train = train_df[features], train_df[target]
X_test, y_test = test_df[features], test_df[target]

# -------------------------------
# Train LightGBM
# -------------------------------
model = lgb.LGBMRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Fixed line
r2 = r2_score(y_test, y_pred)

print("📊 Time-Aware Evaluation Metrics:")
print(f"✅ MAE:  {mae:.2f}")
print(f"✅ RMSE: {rmse:.2f}")
print(f"✅ R²:   {r2:.4f}")

# -------------------------------
# Feature Importance Plot
# -------------------------------
importances = model.feature_importances_
feat_imp = pd.DataFrame({'Feature': features, 'Importance': importances})
feat_imp = feat_imp.sort_values(by='Importance', ascending=False)

plt.figure(figsize=(12, 6))
plt.barh(feat_imp['Feature'], feat_imp['Importance'])
plt.gca().invert_yaxis()
plt.title("📈 LightGBM Feature Importances (Time-Aware + Lag)")
plt.tight_layout()
plt.show()