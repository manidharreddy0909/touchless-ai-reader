import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# LOAD DATA
df = pd.read_csv("data/dataset.csv", header=None)

X = df.iloc[:, :-1]   # 9 feature columns
y = df.iloc[:, -1]    # label column

# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# MODEL
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=20,
    random_state=42
)

model.fit(X_train, y_train)

# EVALUATE
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# SAVE MODEL
joblib.dump(model, "gesture_model.pkl")

print("🎯 Model saved as gesture_model.pkl")

 