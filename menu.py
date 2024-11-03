# Menü ve fiyatlar
menu = {
    'Tavuk Şeritleri': 3.50,
    'Patates Kızartması': 2.50,
    'Hamburger': 4.00,
    'Sosisli Sandviç': 3.50,
    'Büyük İçecek': 1.75,
    'Orta Boy İçecek': 1.50,
    'Sütlü İçecek': 2.25,
    'Salata': 3.75,
    'Küçük İçecek': 1.25
}

def siparis_hesapla(siparis):
    toplam = 0
    siparis_sayisi = {urun: 0 for urun in menu}

    # Siparişleri ayır ve hesapla
    siparis_listesi = siparis.split(',')
    print('sipariş listesi',siparis_listesi)

    for urun in siparis_listesi:
        urun = urun.strip().strip("'").strip('"')  # Boşluk ve tırnakları temizle
        print('ürün',urun)
        if urun in menu:
            siparis_sayisi[urun] += 1
            toplam += menu[urun]

    return toplam, siparis_sayisi

def main():
    while True:
        # Menü yazdır
        print("Menü:")
        for i, (urun, fiyat) in enumerate(menu.items()):
            print(f"{i}: {urun} - ${fiyat:.2f}")

        # Kullanıcıdan sipariş al
        siparis = input("Siparişinizi girin (örneğin, 'hamburger, küçük içecek') veya 'çık' yazın: ")
        
        if siparis.lower() == 'çık':
            print("Programdan çıkılıyor...")
            break
        
        # Eğer kullanıcı "menü" yazarsa, menüyü tekrar göster
        if 'menü' in siparis.lower():
            continue
        
        # Kullanıcı sipariş giriyorsa
        toplam, siparis_sayisi = siparis_hesapla(siparis)
        print("\nSipariş Özeti:")
        for urun, adet in siparis_sayisi.items():
            if adet > 0:
                print(f"{urun}: {adet} adet")
        print(f"Toplam Maliyet: ${toplam:.2f}\n")

if __name__ == "__main__":
    main()
