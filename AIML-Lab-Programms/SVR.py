import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

# Step 1: Load dataset
df = pd.read_csv("salary.csv")

# Step 2: Split into features (X) and target (y)
X = df[["EDU", "WC"]].values
y = df["SAL"].values.reshape(-1, 1)

# Step 3: Feature scaling
sc_X = StandardScaler()
sc_y = StandardScaler()
X_scaled = sc_X.fit_transform(X)
y_scaled = sc_y.fit_transform(y).ravel()  # flatten for SVR

# Step 4: Train SVR with RBF kernel
regressor = SVR(kernel="rbf")
regressor.fit(X_scaled, y_scaled)

# Step 5: Predict (EDU=16, WC=1)
test_point = sc_X.transform([[16, 1]])   # scale input
y_pred_scaled = regressor.predict(test_point)
y_pred = sc_y.inverse_transform([[y_pred_scaled]])  # inverse scaling
print("Predicted Salary (SVR):", y_pred[0][0])

# Step 6: Visualization (Salary vs EDU, WC=1)
edu_range = np.arange(df["EDU"].min(), df["EDU"].max(), 0.1)
X_grid = sc_X.transform(np.column_stack([edu_range, np.ones(len(edu_range))]))
y_grid_pred = sc_y.inverse_transform(regressor.predict(X_grid).reshape(-1, 1))

plt.scatter(df["EDU"], df["SAL"], color="red")
plt.plot(edu_range, y_grid_pred, color="blue")
plt.title("Support Vector Regression (Salary vs EDU, WC=1)")
plt.xlabel("Education (years)")
plt.ylabel("Salary")
plt.show()
