# kendisine gönderilen dikdörtgenin alanını ve çevresini hesaplayan 2 ayrı fonksiyon
#kullanıcıdan alınan değere göre alanı bulunuz
#çevre ve alanı ekrana yazdrınızız

def çevre(a, b):
    return a + b
uzunKenar = int(input("uzunluk"))
kısaKenar = int(input("kısaUzunluk"))
sonuç=çevre(uzunKenar,kısaKenar)*2
print("çevresi",sonuç)

def alan(a, b):
    return a * b
sonuç=alan(uzunKenar,kısaKenar)
print("alanı",sonuç)

