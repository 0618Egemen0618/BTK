#kullanıcıadı  ve şifre alınız "admin " kullanıcı adı
#123456 "sisteme başarıyla girdiniz "
#yanlış girdikçe tekrar denesin "kullanıcı adı veya şifre hatalı"

while True:
    isim=input("isminiz")
    if isim=="admin":
       break
    else:
        print("tekrar deneyeiniz")
while True:
     şifre=input("şifreniz")
     if şifre == "123456" :
         break
     else:
         print("tekrar deneyeiniz")
print("sisteme hoşgeldiniz")