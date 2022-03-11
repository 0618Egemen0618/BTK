print("""

HESAP MAKİNESİ

TOPLAMA İŞLEMİ İÇİN 1'e
ÇIKARTMA İŞLEMİ İÇİN 2'e
ÇARPMA İŞLEMİ İÇİN 3'e
BÖLME İŞLEMİ İÇİN 4'e
ÜSLÜ İFADE İŞLEMİ İÇİN 5'e
TAM BÖLÜMÜ İŞLEMİ İÇİN 6'e

""")

islem=str(input("İşlem seçiniz: "))

if islem == "1":
    sayi1 = int(input("sayı1 1 giriniz :"))
    sayi2 = int(input("sayı1 2 giriniz :"))
    print("Sonuç : ", sayi1 + sayi2 )


elif islem == "2":
    sayi1 = int(input("sayı1 1 giriniz :"))
    sayi2 = int(input("sayı1 2 giriniz :"))
    print("Sonuç : ", sayi1 - sayi2 )

elif islem == "3":
    sayi1 = int(input("sayı1 1 giriniz :"))
    sayi2 = int(input("sayı1 2 giriniz :"))
    print("Sonuç : ", sayi1 * sayi2 )

elif islem == "4":
    sayi1 = int(input("sayı1 1 giriniz :"))
    sayi2 = int(input("sayı1 2 giriniz :"))
    print("Sonuç : ", sayi1 / sayi2 )

elif islem == "5":
    sayi1 = int(input("sayı1 1 giriniz :"))
    sayi2 = int(input("sayı1 2 giriniz :"))
    print("Sonuç : ", sayi1 ** sayi2 )    

elif islem == "6":
    sayi1 = int(input("sayı1 1 giriniz :"))
    sayi2 = int(input("sayı1 2 giriniz :"))
    print("Sonuç : ", sayi1 // sayi2 )

else:
    print("geçersiz işlem girdiniz")

