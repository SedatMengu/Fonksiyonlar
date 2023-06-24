# reduce fonksiyonu : 

# map fonksiyonu bir dizinin tüm elemanlarına işlem uygulanacak ise kullanılır,
# filtre elimizde bulunan liste elemanlarına istediğimiz şartlara göre filtre uyguluyor.
# liste elemanlarının bütün elemanlarının toplanmasını , çarpılmasını gibi işlemler yapıyor. tek 1 değer döndürür.
# parametre olarak bir adet fonksiyon ve 1 adet liste alır. (bu özelliği ile map ve filter a benziyor)
# reduce için yazdığımız fonksyionda 2 adet parametre olması gerekir , aski halde hata alırız.
# sonuç olarak sadece 1 adeat değer döndürür. ( map ve filter dan farkı)
# reduce fonksiyonu functools modülünün içerisindedir.

from functools  import reduce
from math import gcd
liste=[2,3,4,5,6]

def toplam(x,y):
    return x + y
def carpim(x,y):
    return x * y

print(reduce(toplam,liste))                      # / 20
print(reduce(lambda x,y : x + y,liste))          # / 20
print(reduce(carpim,liste))                      # / 720
print(reduce(lambda x,y : x*y,liste))            # / 720


# reduce fonksiyonu ekok almaya da yarayabilir.

# ebob(x,y)*ekok(x,y) = x*y


liste2=[2,3,4,5,6]

def ekok(x,y):
    return int((x * y) / gcd(x,y))              # x*y/ebob(x,y) = ekok(x,y)

print(reduce(ekok,liste))                       # / 60 ( liste2 elemanlarının ekok u 60 imiş)


# listedeki ne büyük sayıyı bulma

liste3=[23,24,10,65,13,88,33,98,101]

def f1(x,y):
    if x>y:
        return x
    return y

print(reduce(f1,liste3))        # / 101 

# reduce fonksiyonu listenin bütün elemanlarının üzerinden döngü yazmadan teker teker döner. 
# fonksiyonumuzda döngü kullanmadık ancak listenin bütün elemanlarını dolaştı. bu reduce fonksiyonu sayesinde oldu.
# yazdığımız fonksiyon iki parametre karşılaştırıp büyük olanı veriyor. 
# 1.adım : x = 23 , y = 24 olarak aldı . 
# 2.adom : y büyük olduğu için fonksiyon sonucu 24 oldu.
# 3.adım : x=24 , y = 10 olarak aldı.
# 4.adım : x büyük olduğu için fonksiyon sonucu 24 oldu.
# 5.adım : x = 24 , y = 65 olarak aldı.
# 6.adım : y büyük olduğu için fonksiyonu sonucu 65 oldu.
# 7.adım : x = 65 , y = 13 olarak aldı,
# 8.adım : y büyük olduğu için fonksiyon sonucu 65 oldu.
# 9.adım : x = 65 , y = 88 olarak aldı,
# 10.adım : y büyük olduğu için fonksiyon sonucu 88 oldu.
# 11.adım : x = 88 , y = 33 olarak aldı.
# 12.adım : x büyük olduğu için fonksyion sonucu 88 oldu.
# 13.adım : x = 88 , y = 98 olarak aldı.
# 14.adım : y büyük olduğu için fonksiyon sonucu 98 oldu.
# 15.adım : x = 98 , y = 101 olarak aldı,
# 16.adım : y büyük olduğu için fonksiyon sonucu 101 oldu ve print edildi.

