cinsiyet=input("Bir harf giriniz E/K: ")

if cinsiyet=="E" or cinsiyet== " e":
    print("Erkek")
elif cinsiyet=="K" or cinsiyet== "k": #2. veya daha fazla şart olursa elif kullanılır
    print("Kadın")
else:
    print("lütfen E veya k giriniz")
print("Hoşçakalın...")
