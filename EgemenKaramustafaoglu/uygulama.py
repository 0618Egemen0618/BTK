#kendisine gönderilen kullanıcı adını şifreyi kontrol ederek
#sonucunda True ve False gönderilen fonksiyonu phyton kodu
#kullanıcıadı: admin şifre:123456 olmalı
def kontrol(kullanici,şifre):
    if kullanici=="admin" and şifre=="123456":
        return True
    else:
        return False


kullanici=input("kullanıcı adı:")
şifre=input("şifreniz:")
sonuc=kontrol(kullanici,şifre)
if sonuc==True:
    print("doğru giriş")
else:
    print("kullanıcı adı veya şifre hatalı")
print(sonuc)