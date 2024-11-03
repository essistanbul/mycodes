def metin_analizi(metin): # Cümle sayısını hesapla ('.' ile ayrılmış) cumleler = metin.split('.') cumleler = [c for c in cumleler if c.strip() != ''] # Boş cümleleri çıkar cumle_sayisi = len(cumleler)
Plain Text
# Kelime sayısını hesapla
kelimeler = metin.split()
kelime_sayisi = len(kelimeler)
# Karakter sayısını hesapla (boşluklar dahil)
karakter_sayisi = len(metin)
# Karakter sayısını boşluklar hariç hesapla
karakter_sayisi_boşluksuz = len(metin.replace(" ", ""))
return kelime_sayisi, karakter_sayisi, cumle_sayisi, karakter_sayisi_boşluksuz
