import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.dummy import DummyClassifier

df = pd.read_csv("tirs.csv")

# Mērķa kolonna
y = df["Machine failure"]

# Pazīmes
X = df.drop([

"Machine failure",

"UDI",

"Product ID",

"TWF",

"HDF",

"PWF",

"OSF",

"RNF"

], axis=1)

# Teksta kolonnas pārvērš skaitļos
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Bāzes līnija
dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_train, y_train)

dummy_pred = dummy.predict(X_test)
dummy_acc = accuracy_score(y_test, dummy_pred)

# Modelis
modelis = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

modelis.fit(X_train, y_train)

y_pred = modelis.predict(X_test)
model_acc = accuracy_score(y_test, y_pred)

print(f"Bāzes līnijas precizitāte: {dummy_acc:.3f}")
print(f"Modeļa precizitāte: {model_acc:.3f}")

if model_acc > dummy_acc:
    print("Modelis pārspēj bāzes līniju.")
else:
    print("Modelis nepārspēj bāzes līniju.")
