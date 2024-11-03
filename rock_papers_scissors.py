import random

def tas_kagit_makas():
    print("Taş-Kağıt-Makas Oyununa Hoş Geldiniz!")
    
    # Skorları başlat
    oyuncu_skoru = 0
    sanal_skoru = 0
    
    while True:
        # Oyuncudan seçim al
        oyuncu_secimi = input("Taş, Kağıt veya Makas seçin (çıkmak için 'q' yazın): ").lower()
        
        if oyuncu_secimi == 'q':
            print("Oyundan çıkıyorsunuz. Sonuçlar:")
            print(f"Oyuncu: {oyuncu_skoru} / Sanal: {sanal_skoru}")
            break
        
        if oyuncu_secimi not in ['taş', 'kağıt', 'makas']:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")
            continue
        
        # Bilgisayarın hamlesini rastgele seç
        bilgisayar_secimi = random.choice(['taş', 'kağıt', 'makas'])
        print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
        
        # Sonuçları karşılaştır
        if oyuncu_secimi == bilgisayar_secimi:
            print("Beraberlik!")
        elif (oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
             (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş') or \
             (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt'):
            print("Kazandınız!")
            oyuncu_skoru += 1
        else:
            print("Kaybettiniz!")
            sanal_skoru += 1
        
        # Skorları yazdır
        print(f"Güncel Skor: Oyuncu: {oyuncu_skoru} / Sanal: {sanal_skoru}")
        print()

# Oyunu başlat
tas_kagit_makas()
