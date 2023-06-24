# positional arguments: 

# tanımlanan fonksiyonların içerisine alıdığı parametrelere denir.


def kuvvet_al(x,y):             
    return x**y 

print(kuvvet_al(3,4))           # / 81
# print(kuvvet_al(5))           # / TypeError: kuvvet_al() missing 1 required positional argument: 'y'
# print(kuvvet_al(3,4,5))         # / TypeError: kuvvet_al() takes 2 positional arguments but 3 were given

#keyword arguments :

# tanımlanan fonksiyonlarda varsayılan olarak gelen argumanlar olabilir. bunlar keyword arguemts olarak isimlendirilir.

def bilgi_ver(isim,soyisim,yas="Girilmedi"):
    return "Ad:{} , soyad: {} , yas: {}".format(isim,soyisim,yas) 

print(bilgi_ver("Ahmet","Kuzu"))            # / Ad:Ahmet , soyad: Kuzu , yas: Girilmedi
# print(bilgi_ver("orhan"))                   # TypeError: bilgi_ver() missing 1 required positional argument: 'soyisim'

def bilgi_ver2(isim,soyisim = "Girilmedi",yas="Girilmedi"):
    return "Ad:{} , soyad: {} , yas: {}".format(isim,soyisim,yas)

print(bilgi_ver2("Halim"))              # / Ad:Halim , soyad: Girilmedi , yas: Girilmedi

# kendime not: fonksiyon tanımlarken boş bırakılmasını uygun gördüğümüz yerlerde default olarak bi ifade tanıtabiliriz. aksi hale hata alırız ve program biter. 


def bilgi_ver3(isim,soyisim="girilmedi",yas="Girilmedi"):
    return "Ad:{} , soyad: {} , yas: {}".format(isim,soyisim,yas)

print(bilgi_ver3("uğur",34))             # / Ad:uğur , soyad: 34 , yas: Girilmedi / pythonda veri sıralaması önemlidir. fonksyionda belirtildiği şekliyle veri girmek gerekir. eğer bilinmiyorsa şu şekilde yapılabilir.
print(bilgi_ver3("oğuz",yas=34))         # / Ad:oğuz , soyad: girilmedi , yas: 34



# *args argument

# parametrede kaç tane parametre olduğunu bilmediğimiz zamanlarda kullanılır.

def topla2 (x,y):                       # / 2 den az veya çok değer verirsek hata alırız
    return x + y

def topla3 (x,y,z):                     # / 3 den az veya çok değer verirsek hata alırız
    return x+y+z
 
def topla4 (*args):                     # isteğimiz kadar değer girebiliriz.
    return args 

print(topla2(5,6))                                    # / 11
print(topla3(2,3,4))                                  # / 9
print(topla4(1,2,3,4,5,6,7,8,9,True,"Python"))        # / (1, 2, 3, 4, 5, 6, 7, 8, 9, True, 'Python')


def carpim(*args):          # / *args dediğimiz için istediğimiz kadar değer girebiliriz.
    carpim = 1      
    for i in args:
        carpim*=i
    return(carpim)


print(carpim(3,4,5))                # / 60
print(carpim(3,4,5,6,7,8,9))        # / 181440 


def selamla(mesaj,*args):
    print(mesaj)
    print("****************")
    for i in args:
        print(i)
    return "fonksyionun çalışması tamamlandı"

print(selamla("selamlar","nasılsınız","iyi günler","hoşçakalın"))

# / selamlar
# / ****************
# / nasılsınız
# / iyi günler
# / hoşçakalın
# / fonksyionun çalışması tamamlandı


# / ilk arguman mesaj değişkeni içerisine girdi ve ekrana basıldı. diğer bütün argumanlar args ı oluşturdu ve for döngüsü ile teker teker ekrana basıldı.



# / **kwargs arguments : verileri sözlük olarak saklar.

def fonk(**kwargs):
    print(kwargs)


fonk(ad="Ali",soyad="Veli",yas=3)               # / {'ad': 'Ali', 'soyad': 'Veli', 'yas': 3}


def fonk2(zorunlu,*args,**kwargs):
    print(zorunlu)
    print("********************")
    for i in args:
        print(i)
    print("********************")
    for j in kwargs:
        print(j)

fonk2(1,2,3,4,5,6,ad="ahmet",soyad="varlı",yas=7)

# 1
# ********************
# 2
# 3
# 4
# 5
# 6
# ********************
# ad
# soyad
# yas
