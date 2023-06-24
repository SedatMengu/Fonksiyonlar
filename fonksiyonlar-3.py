# iç içe fonksiyon kullanımı : 

def dis_fonk():
    print("Dış fonksiyon Çalışıyor")
    def ic_fonk():
        print("iç fonksiyon çalışıyor")
    print("Dış fonksiyon tamamlanıyor...")

dis_fonk()

# / Dış fonksiyon Çalışıyor
# / Dış fonksiyon tamamlanıyor...  ic fonksiyonun çalışmama sebebi biz ona fonksiyonu oluştur dedik. yazdır demedik. 
# / Eğer iç fonksiyonun da çalışmasını istiyorsak dış fonksiyon çalışırken fonksiyon içinde çalıştırmamız gerekir.


def dis_fonk():
    print("Dış fonksiyon Çalışıyor")
    def ic_fonk():
        print("iç fonksiyon çalışıyor")
    ic_fonk()
    print("Dış fonksiyon tamamlanıyor...")

dis_fonk()

# / Dış fonksiyon Çalışıyor      
# / iç fonksiyon çalışıyor       
# / Dış fonksiyon tamamlanıyor...


# parametreli olarak iç içe fonksiyon örneği 

def hesapla(x):                                 # / hesapla adında x parametresi alacak olan bi fonksiyon yazdık
    def karesini_al(a):                         # içerisine karesini alacağımız bir başka fonksiyon yazdık
        return a**2                             # karesini_al fonksiyonu çalşınca ne yapacağını burda tanımadık. a**2 dönecek.
    def karekok_al(a):                          # içerisine karekok_al diye 2.bi fonksiyon tanımladık.
        return a**0.5                           # karekok_al fonksiyonu çalışınca ne yapacağını burda tanımladık. a ** 0.5 dönecek.
    def faktoriyel(a):                          # içerisine faktörüyel hesaplaması için 3.fonksiyonu yazdık.
        carpim=1                                # carpim diye bir değişken olşturduk.
        for i in range(1,a+1):                  # 1 den başlayarak a+1 e kadar olan sayıları i değişkenine atadık.
            carpim*=i                           # döngü neticesinde oluşan her i ile çarpım değişkenini artırdık.
        return carpim                           # faktoriyel fonksiyonu çalışınca ne yapacağını burada tanımladık. oluşan carpim değişkenini return edecek
    kare = karesini_al(x)                       # karesini_al fonksiyonunu kare değişkenine atadık
    karekok = karekok_al(x)                     # karekok_al fonksiyonunu karekok değişkenine atadık
    fak = faktoriyel(x)                         # faktoriyel fonksiyonunu fak değişkenine atadık
    return "karesi : {} , karekoku : {} , faktöriyeli: {}".format(kare,karekok,fak) # bütün fonksiyon neticesinde son hareket olarak sonucu bu şekilde return etmesini istedik ve fonksyion bu şekilde tamamlandı.

print(hesapla(9))           # / karesi : 81 , karekoku : 3.0 , faktöriyeli: 362880  # print yazmamızın sebebi fonksyionun son hareketinde print ifadesi olmadığındandır.


# önemli not: iç içe tanımlanan fonksiyonlarda içeride tanımlı olan fonksiyona erişim mümkün değildir. çünkü içerde


def toplam_carpim(*args):
    def toplama(demet):
        return sum(demet)
    def carpim(demet):
        carpim = 1
        for i in demet:
            carpim *=i
        return carpim
    return "girilen sayıların toplamı: {} , girilen sayıların çarğımı : {}".format(toplama(args),carpim(args))

print(toplam_carpim(2,3,4,5,6,7,8))                     # girilen sayıların toplamı: 35 , girilen sayıların çarğımı : 40320

# önemli not: içerideki fonksiyonlara erişim olmadığından dolayı sonuçlarına da erişim mümkün değildir. o sebepten dolatı toplama(args) , carpim(args) ifadelerini kullandık.




#fonksiyonlardan fonksyion döndürme

def fonk(x):
    return x*x

a = fonk(4)                 # bunu dersek a değişkenine fonk(4) sonucunu atamış oluruz. yani 16

b = fonk                    # bunu dersek v değişkenine fonk fonksiyonunun kendisini atamış oluruz. bu sebepten dolayı herhangi bir sonucu yok.

print(b(5))                 # b ifadesini fonksiyona kısa isim vermiş gibi düşünebilriz.




def islem_sec(islem):                     # islem_sec adında bir fonksiyon oluşturduk. parametre olarak "islem" adında bir şey alacak. isme takılma
    def toplama(*args):                   # içerisine toplama adında dışardan kullanıma ve sonucuna ulaşımın kapalı olduğu bir fonksyion daha yazdık. parametre olarak birden fazla şey alabilir.
        return sum(args)                  # toplama fonksiyonu çağırılnca ne yapacğaını belirttik.
    def carpim(*args):                    # içerisine çarpma adında dışardan kullanıma ve sonucuna ulaşımın kapalı olduğu bir fonksyion daha yazdık. parametre olarak birden fazla şey alabilir.
        carpim=1
        for i in args:
            carpim *=i
        return carpim                     # carpim fonksiyonu çağırılnca ne yapacğaını belirttik.
    def ortalama(*args):                  # içerisine çarpma adında dışardan kullanıma ve sonucuna ulaşımın kapalı olduğu bir fonksyion daha yazdık. parametre olarak birden fazla şey alabilir.
        return sum(args) / len(args)      # ortalama fonksiyonu çağırılnca ne yapacğaını belirttik.
    
    if islem == "toplama":                # eğer dışardan parametre olarak girilen ifade "toplama" ise 
        return toplama                    # islem_sec fonksiyonunun içinden toplama fonksiyonu değişkene atansın.
    elif islem == "carpim":               # eğer dışardan parametre olarak girilen ifade "carpim" ise 
        return carpim                     #islem_sec fonksiyonunun içinden carpma fonksiyonu değişkene atansın.
    elif islem=="ortalama":               # eğer dışardan parametre olarak girilen ifade "ortalama" ise 
        return ortalama                   # islem_sec fonksiyonunun içinden ortalama fonksiyonu değişkene atansın.
    
top_fonk = islem_sec("toplama")           # islem_sec fonksyionunu top_fonk diye uydurduğumuz bir değişkene atadık. ve "islem" parametresi yerine "toplama" girdik
print(top_fonk(3,4,5,6,7,10))             # 3,4,5,6,7,10 sayılarının toplamı : 35

carp_fonk = islem_sec("carpim")           # islem_sec fonksyionunu carp_fonk diye uydurduğumuz bir değişkene atadık. ve "islem" parametresi yerine "carpim" girdik
print(carp_fonk(2,3,4,5,6,7,8))           # 2,3,4,5,6,7,8 sayılarının çarpımı : 40320

ort_fonk = islem_sec("ortalama")          # islem_sec fonksyionunu ort_fonk diye uydurduğumuz bir değişkene atadık. ve "islem" parametresi yerine "ortalama" girdik
print(ort_fonk(100,34,35,765))            # 100,34,35,765 sayılarının ortalaması : 233.5
 


def kisi_sec(kisi):                         # kisi_sec adında "kisi" adında bir adet parametre alan bir fonksiyon oluşturduk
    def takim_sec(takim):                   # fonksiyon içerisine takim_sec adında bir adet "takim" adında parametre alan vbir fonksiyon daha oluşturduk
        return "{} {} takımını tutuyor.".format(kisi,takim) # içerideki fonksiyon çalışırsa ne yapacağını belirttik.
    return takim_sec                        # dışarıdaki fonksiyon çalışırsa ne yapacağını belirttik. takim_sec fonksiyonunun kendisini geri dönecek

a = kisi_sec("Ali")                         # a diye herhangi bir değişken tanımladık ve kisi_sec fonksiyonunu atadık. kisi_sec fonksiyonu "kisi" parametresi istediği için string olarak bir kisi girmemiz gerekir. kisi_sec fonksiyonunun sonucu olarak takim_sec fonksiyonu atanmış oldu. 
b = kisi_sec("Hamza")                       # b diye herhangi bir değişken tanımladık ve kisi_sec fonksiyonunu atadık. kisi_sec fonksiyonu "kisi" parametresi istediği için string olarak bir kisi girmemiz gerekir. kisi_sec fonksiyonunun sonucu olarak takim_sec fonksiyonu atanmış oldu.

print(a("Fenerbahçe"))                      # Ali Fenerbahçe takımını tutuyor.
print(b("istanbulspor"))                    # Hamza istanbulspor takımını tutuyor.


