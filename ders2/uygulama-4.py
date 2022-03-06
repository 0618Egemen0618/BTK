"""
kişinin not ortalaması hesaplamasına göre belge alabilme durumu
"""
ortalama=int(input("ortalama giriniz"))

if ortalama >=85:
    print("takdir geçiyorsunuz")
elif ortalama >=70:
    print((" teşekkür alıyorsunuz"))
else:
    print("hiçbir belge alamadınız")
print("ii tatiller")