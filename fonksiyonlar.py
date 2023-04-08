# fonkisyonlara neden ihtiyaç duyarız: 

# birden fazla kere kullanacağımız bir kod parçasını fonksiyon olarak tanımlarsak eğer daha efektif olabilir.
# örneğin çıktı metnini değiştirmemiz gerektiğinde teker teker ifadelerin tamamını değiştirmek yerine fonksiyonu güncellemek yeterli olur.
# örnek : bir web sitesi akışı içerisinde birden fazla kere işlem başarılı sonucu döndürülebilir. 
            # bunu fonksiyon olmadan yaparsak aşağıdaki gibi bir manzara oluşurdu.
            # işlem başarılı yerine işlem başarılı bir şekilde gerçekleşti olarak değiştirmek istersek tek tek yapmamız gerekir.


print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")
print("işlem başarılı")

# eğer yukardaki işlemi fonksiyon yardımı ile yapacak olursak:

def bildirim():
    print("İşlem Başarılı")

bildirim()
bildirim()
bildirim()
bildirim()
bildirim()
bildirim()
bildirim()

# çıktı ekranı aynı olacak ancak metini değiştirmek istersek sadece fonksiyonu değiştirmemiz yeterlidir.
# bu seepten dolayı fonksiyonlara ihtiyaç duyarız.


# 2 farklı fonksiyon vardır. parametre alan ve parametre almayan.

# parametre almayan fonksiyon iskelet yapısı:

# def fonksiyon ():
# // kodlar

# fonksiyonu çağırmak için 

# fonksiyon()

# örnek:

def selamla():
    print("merhaba")

selamla()                        #/ merhaba


# parametre alan foknksiyon iskelet yapısı:

# def parametreli_fonksiyon (parametre1 , parametre2)
    #// kodlar

# örnek : 

def selamla(isim):
    print("merhaba {}".format(isim))

selamla("Kemal")                # / merhaba kemal
selamla("İhsan")                # / merhaba İhsan
selamla("tayfun")               # / merhaba tayfun

# 2 parametreli fonksiyon örnek

def topla(x,y):
    print("{} ve {} toplamı {} dır".format(x,y,x+y))

topla(4,5)                      # / 4 ve 5 toplamı 9 dır


def birlestir(str1,str2):
    print(str1 + str2)

birlestir("a","b")                      # / ab
birlestir("Merhaba","- dünya")          # / Merhaba- dünya
birlestir("Pythom","- Ögreniyorum")     # / Python- Ögreniyorum


def ortalama_hesapla(liste):
    toplam=sum(liste)
    adet=len(liste)
    ortalama= toplam/adet
    print("listenin ortalaması : {}".format(ortalama))

ortalama_hesapla([2,3,4,5,6,7,8,9,10])  # liste girmek gerektiği için [] kullandık  # / listenin ortalaması : 6.0


def buyuk_harfe_cevir(metin):
    metin=metin.upper()
    print(metin)

buyuk_harfe_cevir("Ahmet ABASIyanık")           # / AHMET ABASIYANIK

def kucuk_harfe_cevir(metin):
    metin=metin.lower()
    print(metin)

kucuk_harfe_cevir("EN BÜYÜK CİMBOM")            # / en büyük cimbom

# tanımlanan fonksiyonda ne kadar parametre isteniyorsa o kadar girmek gerekir. aksi hale hata alırız.
# bazı parametrelere default değerler atayarak boş geçilmesi durumunda oluşacak hatayı önleyebilriz.

def selamla(mesaj,isim="anonim"):
    print("{} {} ".format(mesaj,isim))

selamla("merhaba")                              # / merhaba anonim


def indirim_yap(fiyat , yuzde=20):              # eğer indirim girmediysek bu indirimi 20 kabul et dedik
    indirim_miktari = fiyat * (yuzde/100)
    indirimli_fiyat = fiyat-indirim_miktari
    print("indirimli fiyat {}".format(indirimli_fiyat))

indirim_yap(100,40)                         # / indirimli fiyat 60.0
indirim_yap(50,10)                          # / indirimli fiyat 45.0


# return kavramı

# kullanacağımız fonksiyonun sonucunu her zaman fonksiyon bitince ekrana bastırmasını istemeyebilriz.
# bu gibi durumlarda return anahtar kelimesi devreye girer. 
# iç içe fonksiyonların kullanılmasında da işe yarar.

# örnek : 

def ortalama_hesapla(x,y):
    return (x + y) /2

ortalama_hesapla(3,7)           # / ortalama_hesapla fonksiyonu print içermediği için hesaplamayı yaptı ancak ekrana bir şey bastırmadı


sonuc = ortalama_hesapla(3,7)
print(sonuc)                    # hesaplanan ortalamayı sonuc değişkeninin içine attık ve print ile sonuc ifadesini ekrana yazarak geçici hafızada tutulan return u kullandık.
