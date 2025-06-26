import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 1: Load & clean data
df = pd.read_csv('bracket_data.csv')
df.columns = df.columns.str.strip()
df = df.rename(columns={'mass (g)': 'mass'})  # Renaming for consistency

# Step 2: Set up features and outputs
X = df[['hole_dia', 'rib_thickness', 'fillet_r']]
y = df[['max_stress', 'safety_factor', 'mass']]

# Step 3: Train the multi-output model
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# Step 4: Predict on known data (for validation)
y_pred = model.predict(X)

# Step 5: Evaluate model with RMSE
outputs = ['max_stress', 'safety_factor', 'mass']
for i, label in enumerate(outputs):
    rmse = mean_squared_error(y.iloc[:, i], y_pred[:, i]) ** 0.5
    print(f"RMSE for {label}: {rmse:.2f}")

# Step 6: Predict for a new design
new_design = [[20, 20, 5]]  # hole_dia, rib_thickness, fillet_r
predicted = model.predict(new_design)

print("\n📈 Prediction for [hole_dia=20, rib_thickness=20, fillet_r=5]:")
print(f"  Max Stress:     {predicted[0][0]:.2f} MPa")
print(f"  Safety Factor:  {predicted[0][1]:.2f}")
print(f"  Mass:           {predicted[0][2]:.2f} g")

# Step 7: Plot actual vs predicted stress
plt.scatter(y['max_stress'], y_pred[:, 0], color='blue')
plt.plot([y['max_stress'].min(), y['max_stress'].max()],
         [y['max_stress'].min(), y['max_stress'].max()], 'k--')
plt.xlabel("Actual Max Stress")
plt.ylabel("Predicted Max Stress")
plt.title("Actual vs Predicted Max Stress")
plt.grid(True)
plt.tight_layout()
plt.show()


