import random
import time


def oyun():
    print("""
    ***********************************

    Sayı Tahmin Oyunu

    ************************************
    """)


    while True:
        print("Zorluk Seviyesini Seçin:")
        print("1. Kolay (1-20 arası)")
        print("2. Orta (1-40 arası)")
        print("3. Zor (1-100 arası)")

        zorluk = input("Seçiminizi yapın (1/2/3): ")

        if zorluk == "1":
            rastgele_sayi = random.randint(1, 20)
            break
        elif zorluk == "2":
            rastgele_sayi = random.randint(1, 40)
            break
        elif zorluk == "3":
            rastgele_sayi = random.randint(1, 100)
            break
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3'ü seçin.")

    tahmin_hakki = 7
    ipucu_sayisi = 0

    while True:
        tahmin = input(f"1 ile {rastgele_sayi} arasında bir sayı tahmin edin: ")


        if not tahmin.isdigit():
            print("Lütfen geçerli bir sayı girin!")
            continue

        tahmin = int(tahmin)

        if tahmin < rastgele_sayi:
            print("Daha yüksek bir sayı söyleyin....")
        elif tahmin > rastgele_sayi:
            print("Daha düşük bir sayı söyleyin....")
        else:
            print(f"Tebrikler! Sayımız {rastgele_sayi}.")
            break

        tahmin_hakki -= 1


        ipucu_sayisi += 1
        if ipucu_sayisi == 3:
            if rastgele_sayi % 2 == 0:
                print("İpucu: Sayımız çift.")
            else:
                print("İpucu: Sayımız tek.")
            ipucu_sayisi = 0

        if tahmin_hakki == 0:
            print(f"Tahmin Hakkınız bitti....")
            print(f"Sayımız: {rastgele_sayi}")
            break


    yeniden_oyna = input("Tekrar oynamak ister misiniz? (Evet/Hayır): ").lower()
    if yeniden_oyna == 'evet':
        oyun()



oyun()