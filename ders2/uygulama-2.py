#kullanıcıdan 5 tane sayı isteyerek en büyük sayıyı listeye atarak bulunuz
sayi1=input("1.sayıyı alınız")
sayi2=input("2.sayıyı alınız")
sayi3=input("3.sayıyı alınız")
sayi4=input("4.sayıyı alınız")
sayi5=input("5.sayıyı alınız")
sayilar=[]
sayilar.append(sayi1)
sayilar.append(sayi2)
sayilar.append(sayi3)
sayilar.append(sayi4)
sayilar.append(sayi5)
sayilar.sort()

print("alınan sayıların en büyüğü ",sayilar[0])