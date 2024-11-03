print("Yapay Zeka Kullanım Alanı: ", seçilen_kullanım_alanı)
print("Potansiyel Etik Sorunlar: ", seçilen_etik_sorun)
print("Önerilen Çözümler: ", seçilen_çözüm)

# İnsan kontrolü için seçimi yap
insan_kontrolü_seçimi = input("Yapay zeka seçimi ile aynı mı? (Evet/Hayır): ")

if insan_kontrolü_seçimi.lower() == "evet":
    print("İnsan kontrolü seçimi: Yapay zeka ile aynı.")
else:
    insan_kullanım_alanı = input("Hangi kullanım alanını seçtiniz? (1-6): ")
    insan_index = int(insan_kullanım_alanı) - 1
    print("Yapay Zeka Seçimi: ", seçilen_kullanım_alanı)
    print("İnsan Kontrolü Seçimi: ", kullanım_alanları[insan_index])
    print("Yapay Zeka Sorunlar: ", seçilen_etik_sorun)
    print("İnsan Kontrolü Sorunlar: ", potansiyel_etik_sorunlar[insan_index])
    print("Yapay Zeka Çözüm: ", seçilen_çözüm)
    print("İnsan Kontrolü Çözüm: ", önerilen_çözümler[insan_index])

devam = input("Devam etmek istiyor musunuz? (Evet/Hayır): ")
if devam.lower() != "evet":
    break