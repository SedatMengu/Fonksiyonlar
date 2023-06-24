# zip fonksiyonu

# birden fazla listenin elemanlarını fermuar mantığı ile birleştirmeye yarar. 
# birden fazla liste elemanları için çalıştırıldığı takdirde ilk biten liste ile birlikte tamamlanır.


liste1=[1,2,3,4]
liste2=["a","b","c","d"]

print(list(zip(liste1,liste2)))                 # / [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')] list yazdığımız için liste olarak dönderdi
print(set(zip(liste1,liste2)))                  # / {(3, 'c'), (2, 'b'), (4, 'd'), (1, 'a')} set yazdığımız için dict veri tipinde dönderdi. her çalıştığında farklı dizilimle gelir.
print(tuple(zip(liste1,liste2)))                # / ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')) tuple yazdığımız için tuple veri tipinde dönerdir.


liste3=list("python")
liste4=[1,2,3,4]
liste5=["a","b"]

print(list(zip(liste3,liste4,liste5)))          # / [('p', 1, 'a'), ('y', 2, 'b')] 2 elemanlı oldu çünkü liste5 2 elemana sahip


# isim , puan ve harf notu ile ilgili örnek

kisi=["ali","oya","ece","nuh"]
puan=[90,80,70,95]
harf=["AA","BB","BA","AA"]

for k,p,h in zip(kisi , puan , harf):
    print("{} isimli öğrenci , {} puan alarak , {} harf notu ile geçti.".format(k,p,h))