def metin_analizi(metin):
    # Cümle sayısını hesapla ('.' ile ayrılmış)
    cumleler = metin.split('.')
    cumleler = [c for c in cumleler if c.strip() != '']  # Boş cümleleri çıkar
    cumle_sayisi = len(cumleler)

    # Kelime sayısını hesapla
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)

    # Karakter sayısını hesapla (boşluklar dahil)
    karakter_sayisi = len(metin)

    # Karakter sayısını boşluklar hariç hesapla
    karakter_sayisi_boşluksuz = len(metin.replace(" ", ""))

    return kelime_sayisi, karakter_sayisi, cumle_sayisi, karakter_sayisi_boşluksuz

# Kullanıcıdan metin al
metin = input("Lütfen bir metin girin: ")

# Analiz et
kelime_sayisi, karakter_sayisi, cumle_sayisi, karakter_sayisi_boşluksuz = metin_analizi(metin)

# Sonuçları yazdır
print(f"Girilen metindeki kelime sayısı: {kelime_sayisi}")
print(f"Girilen metindeki karakter sayısı (boşluklar dahil): {karakter_sayisi}")
print(f"Girilen metindeki cümle sayısı: {cumle_sayisi}")
print(f"Girilen metindeki karakter sayısı (boşluklar hariç): {karakter_sayisi_boşluksuz}")
