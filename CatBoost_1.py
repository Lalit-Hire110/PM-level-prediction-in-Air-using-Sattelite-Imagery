# === 1. Imports ===
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import shap
import matplotlib.pyplot as plt

# === 2. Load dataset ===
df = pd.read_csv("final_dataset/cleaned_final_dataset.csv")

# === 3. Define target and features
target = 'PM2.5'
features = [col for col in df.columns if col != target]

# 🔍 Identify categorical columns
cat_features = ['station_id']  # Update if more categorical cols added later

# === 4. Split data
X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# === 5. Train CatBoost
cat_model = CatBoostRegressor(
    iterations=500,
    learning_rate=0.05,
    depth=6,
    loss_function='RMSE',
    verbose=False
)

cat_model.fit(X_train, y_train, cat_features=cat_features)

# === 6. Predict & Evaluate
y_pred = cat_model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # ✅ avoid squared=False
r2 = r2_score(y_test, y_pred)

print("📊 CatBoost Results:")
print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²: {r2:.4f}")

# === 7. SHAP
explainer = shap.TreeExplainer(cat_model)
shap_values = explainer.shap_values(X_test)

plt.figure(figsize=(12, 8))
shap.summary_plot(shap_values, X_test, show=True)
plt.savefig("catboost_shap.png")