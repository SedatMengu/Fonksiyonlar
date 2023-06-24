# lambda ifadeleri ismi olmayan fonksyionlar oluşturmaya yararlar.


def kare_al(x):
    return x*x

a = kare_al(3)
print(a)

# yukardaki fonksiyonu lambda ifadesi ile oluşturalım

kare_al2 = lambda x : x * x     # : ifaesinden önceki kısım ( bu fonksiyonda "x" oluyor) fonksiyonun alacağı parametreyi gösteriyor. sonraki kısım ise fonksyionun ne yapacağını gösteriyr.

b = kare_al2(8)
print(b)


# hem def yöntemi ile hem de lamvda yöntemi ile aynı fonksiyonu yazalım

def kup_al(x):
    return x*x*x

print(kup_al(2))            # / 8

# aynı fonksiyonu lambda ifadesi ile kullanalım

kup_al2 = lambda x : x*x*x

print(kup_al2(3))           # / 27

# birden fazla değişken alması durumunda:

def topla(a,b):
    return a+b

print(topla(2,3))           # / 5

topla2 = lambda a,b : a+b

print(topla2(3,4))          # / 7

# belirsiz sayıda parametre alsaydı

def topla3(*args):
    return sum(args)

print(topla3(2,3,4,5))      # / 14

topla4 = lambda *args : sum(args)

print(topla4(2,3,4,5,6))    # / 20

# herhangi bir değere atamadan da lambda çalışabilir ki ana mantığı bu zaten.


print((lambda a,b,c : a+b+c)(3,4,5))    # / 12
# yukarda topla4 = lambda ..... diye devam eden fonksiyında topla4 olayını tamamen kaldırıp direkt olarak print içerisine lambda ifadesini yazabiliriz.

# listelerde sıralama yapmak gibi ara işlemleri yaparken tekrar def ile fonksiyon tanımlamak yerine lambda ile istediğimiz sonuvcu elde edebiliriz.

liste = [("ali",20),("veli",34),("cenk",32),("ece",16),("oya",25),("duru",21)]

liste.sort(key=lambda x : x[1]) 
print(liste)                                # / [('ece', 16), ('ali', 20), ('duru', 21), ('oya', 25), ('cenk', 32), ('veli', 34)]

# yukarıdaki örnekte elimizdeki listede adları ve yaşları bulunan liste elemanlarını yaşlarına göre sıralamak istediğimizi varsaydık.
# sort listelere özgü sıralama yapmaya yarar. key ile belirli kritere göre sıralama yapar. kriter olarak da lambda ifadesinin return undan faydalandık.

liste2= [{"ad":"osman","soyad":"kaçar","yas":23},{"ad":"idris","soyad":"konar","yas":34},{"ad":"eda","soyad":"zorlu","yas":19}]

liste2.sort(key=lambda x : x["ad"])
print(liste2)                           # / [{'ad': 'eda', 'soyad': 'zorlu', 'yas': 19}, {'ad': 'idris', 'soyad': 'konar', 'yas': 34}, {'ad': 'osman', 'soyad': 'kaçar', 'yas': 23}]

# yukarıdaki örnekte elimizde ad,soyad,yasları olan sözlük tipinde bir liste olduğunu ve bu sözlük elemanlarını istediğimiz kriterlere göre sıralamak istediğimizi varsyalım.
# sort sözlük veri tipinde de sıralama yapmaya yarar. key ile sıralamak istediğimiz kriteri belirledik. 

