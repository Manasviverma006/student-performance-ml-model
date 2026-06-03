import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# 1. Load dataset
data = pd.read_csv("C:\\Users\\manas\\OneDrive\\Desktop\\student\\student-mat.csv", sep=";")

# 2. Target (what we want to predict)
y = data["G3"]

# 3. Features (remove target column)
X = data.drop("G3", axis=1)

# 4. Convert categorical (string) columns into numbers
X = pd.get_dummies(X)

# 5. Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# 6. Create model
model = DecisionTreeRegressor(random_state=1)

# 7. Train model
model.fit(X_train, y_train)

# 8. Predict for ALL test data
y_pred = model.predict(X_test)

# 9. Show predictions
print("Predictions:")
print(y_pred)

# 10. Compare actual vs predicted
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

print("\nComparison:")
print(results)

# 11. Accuracy score
print("\nModel Score (R2):", model.score(X_test, y_test))