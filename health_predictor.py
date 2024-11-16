import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Veri kümesi: Farklı hastalıklar ve semptomlar
data = {
    'Ateş': [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    'Öksürük': [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
    'Baş Ağrısı': [0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    'Boğaz Ağrısı': [1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    'Hastalık': ['Grip', 'COVID-19', 'Migren', 'Boğaz Enfeksiyonu', 'Sinüzit', 'Grip', 'COVID-19', 
                 'Migren', 'Boğaz Enfeksiyonu', 'Sinüzit', 'Grip', 'COVID-19', 'Migren', 
                 'Boğaz Enfeksiyonu', 'Sinüzit', 'Grip', 'COVID-19', 'Migren', 'Boğaz Enfeksiyonu', 'Sinüzit',
                 'Grip', 'COVID-19', 'Migren', 'Boğaz Enfeksiyonu', 'Sinüzit']
}

# DataFrame oluşturuluyor
df = pd.DataFrame(data)

# Semptomlar (X) ve hastalıklar (y) olarak veriyi ayıralım
X = df[['Ateş', 'Öksürük', 'Baş Ağrısı', 'Boğaz Ağrısı']]
y = df['Hastalık']

# Veriyi eğitim ve test setlerine ayıralım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# RandomForestClassifier modelini oluşturalım
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Modeli eğitelim
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapalım
y_pred = model.predict(X_test)

# Modelin başarı oranını görelim
print("Model Başarı Oranı:", accuracy_score(y_test, y_pred))

# Confusion Matrix ile modelin performansını inceleyelim
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
disp.plot(cmap='Blues')
plt.show()

# Kullanıcıdan semptomları alalım ve tahmin yapalım
def predict_disease(symptoms):
    symptoms_df = pd.DataFrame([symptoms], columns=['Ateş', 'Öksürük', 'Baş Ağrısı', 'Boğaz Ağrısı'])
    prediction = model.predict(symptoms_df)
    return prediction[0]

# Kullanıcıdan semptomları alalım (örnek: Ateş=1, Öksürük=1, Baş Ağrısı=0, Boğaz Ağrısı=1)
user_input = [1, 1, 0, 1]  # Bu, 'Grip' hastalığına yakın bir semptom kümesidir
predicted_disease = predict_disease(user_input)
print("Tahmin Edilen Hastalık:", predicted_disease)
