import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


if not os.path.exists("models"):
    os.makedirs("models")

print("Veri Yükleniyor..")
df = pd.read_csv("data/synthetic_network_traffic.csv")

X= df.drop('label', axis=1)
y=df['label']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

print(f"Eğitim Seti Boyutu: {len(X_train)}")
print(f"Test Seti Boyutu: {len(X_test)}")


print("Model Eğitiliyor")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print("\n" + "="*30)
print("   MODEL PERFORMANS RAPORU")
print("="*30)
print(classification_report(y_test, y_pred))


model_path = 'models/ids_model.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print(f"\nModel başarıyla '{model_path}' konumuna kaydedildi.")