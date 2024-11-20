import pandas as pd
from sklearn.model_selection import train_test_split #veri ön işleme, model seçimi, model değerlendirmesi ve daha fazlası için araçlar sağlar.
from sklearn.ensemble import RandomForestClassifier # rastgele oluşturulmuş birden çok karar ağacının çıktısını birleştiren algoritma
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay #tahmin hatasını değerlendirmek ve doğru tahminlerin oranını veya sayısını hesaplar ve sınıflandırıcı algoritma sonuçları için bir görselleşirme oluşturur
import matplotlib.pyplot as plt #  veri görselleştirme kütüphanesidir, çeşitli grafikler oluşturmayı sağlar.

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

# DataFrame oluşturuluyor # satırları ve sütunları olan iki boyutlu etiketli veri yapısıdır. 
df = pd.DataFrame(data)

# Semptomlar (X) ve hastalıklar (y) olarak veriyi ayıralım
X = df[['Ateş', 'Öksürük', 'Baş Ağrısı', 'Boğaz Ağrısı']]
y = df['Hastalık']

# Veriyi eğitim ve test setlerine ayıralım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #X_train ve y_train: Modelin eğitileceği eğitim verisi.#X_test ve y_test: Modelin doğruluğunu test etmek için kullanılacak test verisi.#test_size=0.2: Veri kümesinin %20'si test için ayrılır, geri kalan %80'i eğitim için kullanılır

# RandomForestClassifier modelini oluşturalım
model = RandomForestClassifier(n_estimators=100, random_state=42) #n_estimators=100: Modelin 100 karar ağacı kullanmasını sağlar.
#random_state=42: Sonuçların tekrarlanabilir olmasını sağlamak için rastgelelikğin kontrol edilmesini sağlar.

# Modeli eğitelim
model.fit(X_train, y_train)

#y_pred: Test verisi üzerinde modelin tahmin ettiği hastalıklar.
# accuracy_score: Modelin doğruluğunu hesaplar. Bu, doğru tahminlerin oranıdır.
y_pred = model.predict(X_test)

# Modelin başarı oranını görelim
print("Model Başarı Oranı:", accuracy_score(y_test, y_pred))

# confusion_matrix: Modelin doğruluğunu ve hatalarını görsel olarak incelemek için kullanılan karışıklık matrisini oluşturur.
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_) #görsel olarak görüntüleme
disp.plot(cmap='Blues') # renk haritası olarak kullanma
plt.show() #Görselleştirmenin ekranda görünmesini sağlar.

# Bu fonksiyon, kullanıcı tarafından sağlanan semptomları alır
def predict_disease(symptoms):
    symptoms_df = pd.DataFrame([symptoms], columns=['Ateş', 'Öksürük', 'Baş Ağrısı', 'Boğaz Ağrısı'])
    prediction = model.predict(symptoms_df)
    return prediction[0] #Modelin tahmini sonucu.

# Kullanıcıdan semptomları alalım (örnek: Ateş=1, Öksürük=1, Baş Ağrısı=0, Boğaz Ağrısı=1)
user_input = [1, 1, 0, 1]  # Bu, 'Grip' hastalığına yakın bir semptom kümesidir
predicted_disease = predict_disease(user_input)
print("Tahmin Edilen Hastalık:", predicted_disease)
