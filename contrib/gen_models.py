#!/bin/python3

import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


print("Generating model v1.0.0...")
iris = load_iris()
model1 = RandomForestClassifier(random_state=42)
model1.fit(iris.data, iris.target)
joblib.dump(model1, "iris_model_v1.0.0.joblib")

print("Generating model v1.1.0...")
model2 = LogisticRegression(random_state=42, max_iter=200)
model2.fit(iris.data, iris.target)
joblib.dump(model1, "iris_model_v1.1.0.joblib")
