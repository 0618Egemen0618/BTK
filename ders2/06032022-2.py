liste=[] # boş bir liste tanımlanır
liste=[" Elma , Armut ",20] # artık listenin elemeanları değişti

sayilar=[15,19,2,3,8,25,6]
isimler=["Ali","Aşye","veli","ahmet","hatice"]
gunler=[" Pazaartesi" , "Salı" , "Çarşamba"]
print(gunler)
print("0. indeksdei eleman ", gunler[0])
print(gunler[1])
print(gunler[2])
gunler.append("cuma") # yeni eleman ekler0
print(gunler)
print("Eleman sayısı",len(gunler)) # listenin eleman sayısı
gunler.pop() # hiçbirşey olmadğı zmn en son eleman silinir
print(gunler)
gunler.pop(0) # yazdığın index silinir
print(gunler)
print(sayilar)
sayilar.sort() # barsayılan sayıları büyükten küçüğe sıralar
print(sayilar)
sayilar.sort(reverse=True)# barsayılan sayıları büyükten küçüğe sıralar
print(sayilar)
isimler.sort(reverse=True)
print(isimler)
