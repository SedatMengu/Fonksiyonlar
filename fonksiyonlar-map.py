# map fonksiyonu:

# yazdığımız kodun daha kısa ve kullanışlı olmasını sağlar.
# parametre olarak bir fonksiyon ve bir liste alır. liste elemanlarını teker teker fonksiyonda yerine koyar ve sonucu yeni bir liste olarak döndürür.

# map fonksiyonu kullanmadan:

liste= [1,2,3,4,5]              # bir liste tanımladık
def f1 (x):                     # içerisine 1 adet parametre alan (x) bir fonksiyon tanımladık
    return x*x                  # fonksiyon çalışmasını bitirince bize x*x şeklinde bir değer return edecek. 

liste2=[]                       # işlem sonucunda kullanacağımı boş bir liste oluşturduk.
for i in liste:                 # yukarda tanımlanan liste elemanlarının tammamına teker teker uğra dedik.
    liste2.append(f1(i))        # uğradığı elemanı(i) liste2 isimli listeye append etti.
print(liste2)                   # / oluşan listeyi bastık . [1, 4, 9, 16, 25]


# map fonksyionu kullanarak yaparsak:

liste3= map(f1,liste)           # liste3 adında bir değişken oluşturduk ve yukarıdaki işlemin aynısını map fonksiyonu ile yapmak istedik.
print(liste3)                   # / <map object at 0x000001F51CF1C250>

liste3= list(map(f1,liste))     # mao fonksiyonuna özel bu şekilde kullanılmak ister. istersek list , istersek tuple  istersek set olarak döndürebiliriz.
print(liste3)                   # / [1, 4, 9, 16, 25]

# lambda ile iç içe kullanım : 

liste4 = [9,8,7,6,5]
liste5=list(map(lambda x : x*x ,liste4))        # lambda x : x*x ifadesi bir fonksiyonu yerine yazıldı.
print(liste5)                   # / [81, 64, 49, 36, 25]

liste6=[6,6,6,6,6]
liste7=list(map(lambda x : x*x , liste6))
print(liste7)                   # / [36, 36, 36, 36, 36]


#listedeki bütün elemanlara aynı işlemi uygulamak istersek (listedeki bütün elemanların karesini al , kokunu al , vb) map fonksiyonu çok kullanışlı olabilir.

# örnek : birbirinden bağımsız iki listedeki elemanları index numaralarına göre birleştirip tek liste yapalım.
liste8 = [1,3,4,5,6]                        # liste8 adında bir liste oluşturduk.
liste9 = [9,6,5,4,5]                        # liste9 adında bir liste oluşturduk. ana amacmız bu 2 listeyi indexlerine göre toplamak

def toplam(x,y):                            # asıl işi yapacak bir fonksiyonu yazdık
    return x+y                              # yazılan fonksiyon bize iki sayının toplamını döndürecek.

liste10= list(map(toplam , liste8,liste9))  # map fonksiyonu iskelet yapısında fonksiyon ve parametre olduğundan bu şekilde yazdık.

print(liste10)                              # / [10, 9, 9, 9, 11]

# örnek - 2

liste11 = [1,3,4,5,6]                       # liste11 adında 5 elemanlı bir liste oluşturduk.
liste12 = [9,6,5,4,5]                       # liste12 adında 5 elemanlı bir liste oluşturduk. 
liste13 = [7,6,5]                           # liste13 adında 3 elemanlı bir liste olşturduk. ana amacmız bu 3 listeyi indexlerine göre toplamak

def toplam(x,y,z):                            # asıl işi yapacak bir fonksiyonu yazdık
    return x+y+z                              # yazılan fonksiyon bize iki sayının toplamını döndürecek.

liste14= list(map(toplam , liste11,liste12,liste13))  # map fonksiyonu iskelet yapısında fonksiyon ve parametre olduğundan bu şekilde yazdık.

print(liste14)                              # / [17, 15, 14] en düşük eleman sayısı olan liste elemanı kadar eleman döndürür.

liste15 = list(map(lambda x,y,z : x+y+z,liste11,liste12,liste13))
print(liste15)
