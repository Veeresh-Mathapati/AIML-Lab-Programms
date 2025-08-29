import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

# Step 1: Load dataset
df = pd.read_csv("salary.csv")

# Step 2: Split into features (X) and target (y)
x = df[["EDU", "WC"]]   # features
y = df["SAL"]           # target

# Step 3: Train Random Forest Regressor
regressor = RandomForestRegressor(n_estimators=100, random_state=0)
regressor.fit(x, y)

# Step 4: Predict an example (EDU=16, WC=1) using DataFrame
test_point = pd.DataFrame({"EDU": [16], "WC": [1]})
y_pred = regressor.predict(test_point)
print("Predicted Salary:", y_pred)

# Step 5: Visualization (like PDF)
# Create grid of EDU values
X_grid = np.arange(min(x["EDU"]), max(x["EDU"]), 0.1)

# Make DataFrame for predictions with WC fixed at 1
X_full = pd.DataFrame({"EDU": X_grid, "WC": 1})
y_grid_pred = regressor.predict(X_full)

# Scatter plot of real data
plt.scatter(x["EDU"], y, color="blue")

# Prediction line
plt.plot(X_grid, y_grid_pred, color="green")

plt.title("Random Forest Regression (Salary vs EDU)")
plt.xlabel("Education (years)")
plt.ylabel("Salary")
plt.show()

