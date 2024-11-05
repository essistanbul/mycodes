class KiyafetDegisimEtkinligi:
    def __init__(self):
        self.katilimcilar = {}
        self.kiyafetler = [
            "sarı şapka",
            "mor elbise",
            "kırmızı eldiven",
            "mavi tshirt",
            "yeşil pantolon",
            "siyah ceket",
            "beyaz spor ayakkabı"
        ]

    def katilimci_ekle(self, isim, kiyafetler):
        self.katilimcilar[isim] = kiyafetler
        print(f"{isim} etkinliğe eklendi.")

    def katilimcilarin_listesi(self):
        print("\nKayıtlı Katılımcılar:")
        for isim, kiyafetler in self.katilimcilar.items():
            print(f"{isim}: {', '.join(kiyafetler)}")

    def kiyafet_takasi(self, katilimci1, katilimci2, kiyafet1, kiyafet2):
        if katilimci1 in self.katilimcilar and katilimci2 in self.katilimcilar:
            if kiyafet1 in self.katilimcilar[katilimci1] and kiyafet2 in self.katilimcilar[katilimci2]:
                self.katilimcilar[katilimci1].remove(kiyafet1)
                self.katilimcilar[katilimci2].remove(kiyafet2)
                self.katilimcilar[katilimci1].append(kiyafet2)
                self.katilimcilar[katilimci2].append(kiyafet1)
                print(f"{katilimci1} ve {katilimci2} kıyafetlerini takas etti: {kiyafet1} <-> {kiyafet2}.")
            else:
                print("Takas edilecek kıyafetler bulunamadı.")
        else:
            print("Katılımcılardan biri kayıtlı değil.")

    def kiyafet_listesi_goster(self):
        print("\nKullanılabilir Kıyafetler:")
        for kiyafet in self.kiyafetler:
            print(f"- {kiyafet}")

    def ana_menu(self):
        while True:
            print("\nKıyafet Değişim Etkinliği")
            print("1. Katılımcı Ekle")
            print("2. Katılımcıları Listele")
            print("3. Kıyafet Takası Yap")
            print("4. Çıkış")
            
            secim = input("Seçiminizi yapın (1-4): ")
            
            if secim == "1":
                isim = input("Katılımcının ismini girin: ")
                kiyafetler = input("Getirilen kıyafetleri virgülle ayırarak girin (örneğin: sarı şapka, mor elbise): ").split(',')
                kiyafetler = [kiyafet.strip() for kiyafet in kiyafetler]  # Boşlukları temizle
                self.katilimci_ekle(isim, kiyafetler)
            
            elif secim == "2":
                self.katilimcilarin_listesi()
            
            elif secim == "3":
                self.kiyafet_listesi_goster()  # Kıyafet listesini göster
                katilimci1 = input("Takas yapmak isteyen 1. katılımcının ismini girin: ")
                kiyafet1 = input(f"{katilimci1} tarafından takas edilecek kıyafeti girin: ")
                katilimci2 = input("Takas yapmak isteyen 2. katılımcının ismini girin: ")
                kiyafet2 = input(f"{katilimci2} tarafından takas edilecek kıyafeti girin: ")
                self.kiyafet_takasi(katilimci1, katilimci2, kiyafet1, kiyafet2)

            elif secim == "4":
                print("Çıkılıyor...")
                break
            
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")

# Programı başlat
etkinlik = KiyafetDegisimEtkinligi()
etkinlik.ana_menu()
