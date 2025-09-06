import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import shap
import matplotlib.pyplot as plt
import joblib
import numpy as np

# === Load Dataset ===
df = pd.read_csv("final_dataset/cleaned_final_dataset.csv")

# === Feature Engineering: Create missing SHAP features ===
df['inv_dry_combo'] = df['min_TIR1'] * df['min_WV']  # Adjust if needed

# === Top 5 SHAP Features ===
top_features = ['inv_dry_combo', 'max_WV', 'img_mean', 'range_TIR1', 'min_TIR1']

# === Check for missing features (debugging aid) ===
missing = [f for f in top_features if f not in df.columns]
if missing:
    raise ValueError(f"❌ These required features are missing: {missing}")

# === Feature Matrix & Target ===
X = df[top_features]
y = df['PM2.5']

# === Train-Test Split ===
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# === XGBoost Regressor (Lite) ===
xgb_lite = xgb.XGBRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1
)

# === Train Model ===
xgb_lite.fit(X_train, y_train)

# === Predict & Evaluate ===
y_pred = xgb_lite.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\n📊 XGBoost Lite Model Results:")
print("MAE: ", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R²:  ", round(r2, 4))

# === SHAP Analysis ===
print("\n🔍 Running SHAP analysis...")
explainer = shap.Explainer(xgb_lite, X_train)
shap_values = explainer(X_test)

# === SHAP Summary Plot (Bar + Beeswarm) ===
plt.figure()
shap.summary_plot(shap_values, X_test, plot_type='bar', show=False)
plt.savefig("shap_lite_bar.png", bbox_inches='tight')
plt.close()

plt.figure()
shap.summary_plot(shap_values, X_test, show=False)
plt.savefig("shap_lite_beeswarm.png", bbox_inches='tight')
plt.close()

# # === Save Model ===
# joblib.dump(xgb_lite, "xgb_lite_model.pkl")
# print("\n✅ Model saved as xgb_lite_model.pkl")
print("✅ SHAP plots saved as shap_lite_bar.png and shap_lite_beeswarm.png")

# === Optional: Compare with Full Model ===
try:
    full_model = joblib.load("xgb_full_model.pkl")
    full_pred = full_model.predict(X_test)

    print("\n📊 Comparison with Full Model:")
    print("Full MAE: ", round(mean_absolute_error(y_test, full_pred), 2))
    print("Lite MAE: ", round(mae, 2))
    print("Full RMSE:", round(mean_squared_error(y_test, full_pred, squared=True) ** 0.5, 2))
    print("Lite RMSE:", round(rmse, 2))
    print("Full R²:  ", round(r2_score(y_test, full_pred), 4))
    print("Lite R²:  ", round(r2, 4))
except FileNotFoundError:
    print("ℹ️ Skipping full model comparison (xgb_full_model.pkl not found)")
