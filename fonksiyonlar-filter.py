# filter fonksiyonu

# tanımı: bir listeyi belirli koşulara göre listelememize yardımcı olur.
# parametre olarak 1 tane fonksyion ve 1 tane liste alır.
# önemli nokta parametre olarak aldığı fonksiyonun true ya da false olarak döndüren bir fonksiyon olması gerekiyor.


liste = [1,2,3,4,5,6,7,8,9,11,13,15,17,101,123,54,23,67]

# filter fonksiyonundan yararlanarak 

# 1 - çift olan sayıları listeleyelim

def cift_mi(x):
    if x %2==0:
        return True
    return False

print(list(filter(cift_mi,liste)))               # / [2, 4, 6, 8, 54]
print(list(filter(lambda x : x%2==0,liste)))    # / [2, 4, 6, 8, 54]

# 2 - tek olan sayıları listeleyelim

def tek_mi(x):
    if x%2!=0:
        return True
    return False

print(list(filter(tek_mi,liste)))               # / [1, 3, 5, 7, 9, 11, 13, 15, 17, 101, 123, 23, 67]
print(list(filter(lambda x : x%2!=0,liste)))    # / [1, 3, 5, 7, 9, 11, 13, 15, 17, 101, 123, 23, 67]

# 3 - 5e tam bölünenler

def bolunen(x):
    if x %5==0:
        return True
    return False

print(list(filter(bolunen,liste)))                        # / [5, 15]
print(list(filter(lambda x : x%5==0,liste)))              # / [5, 15]

# 4 - hem 3 hem 5e bölünenler

def ikili_bolunen(x):
    if x %3==0 and x%5==0:
        return True
    return False

print(list(filter(ikili_bolunen,liste)))                  # / [15]
print(list(filter(lambda x: x%3==0 and x%5==0,liste)))      # / [15]
# 5 - 2 ye bölünüp 5e bölünmeyenler

def ikilibolunen2(x):
    if x%2==0 and x%5!=0:
        return True
    return False
print(list(filter(ikilibolunen2,liste)))                   # / [2, 4, 6, 8, 54]
print(list(filter(lambda x: x%2==0 and x%5!=0,liste)))       # / [2, 4, 6, 8, 54]

# 6 - iki basamaklı olanları listele

def iki_basamakli(x):
    if x >=10 and x <= 99:
        return True
    return False

print(list(filter(iki_basamakli,liste)))                    # / [11, 13, 15, 17, 54, 23, 67]
print(list(filter(lambda x : x>=10 and x<=99,liste)))       # / [11, 13, 15, 17, 54, 23, 67]


kelimeler = ["ahmet","ayna","ana","kalem","defter","son","beyaz","kitap","lale","ufuk"]

print(list(filter(lambda x : x[0]=="a",kelimeler)))                         # listede ilk harfi "a" olanları filtrele / ['ahmet', 'ayna', 'ana']
print(list(filter(lambda x : x[-1]=="a",kelimeler)))                        # listedeki son harfi "a" olanları filtrele / ['ayna', 'ana']
print(list(filter(lambda x : x[0]=="a" or x[0]=="k",kelimeler)))            # listedeki ilk harfi "a" veya "k" olanları filtrele / ['ahmet', 'ayna', 'ana', 'kalem', 'kitap']
print(list(filter(lambda x : x[0]!="l",kelimeler)))                         # listede ilk harfi "k" olmayanları filtrele / ['ahmet', 'ayna', 'ana', 'kalem', 'defter', 'son', 'beyaz', 'kitap', 'ufuk']
print(list(filter(lambda x : x.startswith("b"),kelimeler)))                 # listede "b" harfi ile başlayanları filtrele / ['beyaz']
print(list(filter(lambda x : "a" in x,kelimeler)))                          # listede "a" harfini içerenleri filtrele  / ['ahmet', 'ayna', 'ana', 'kalem', 'beyaz', 'kitap', 'lale']
print(list(filter(lambda x : x == x[::-1],kelimeler)))                      # listede tersten ve düzden aynı olanları filtrele / ['ana']



liste2 = [1,2,(1,2,3),True,"Örnek","string",{1,2,3}]

print(list(filter(lambda x : isinstance(x,str),liste2)))                    # listede string olanları filtrele / ['Örnek', 'string']
print(list(filter(lambda x : isinstance(x,bool),liste2)))                   # listede bool olanları filtrele / [True]
print(list(filter(lambda x : isinstance(x,set),liste2)))                    # listede set olanları filtrele / [{1, 2, 3}]


liste3 = [{"ad":"ozan","yas":23},{"ad":"can","yas":21},{"ad":"adnan","yas":17},{"ad":"ali","yas":34}]

print(list(filter(lambda x : x ["ad"].startswith("a"),liste3)))             # sözlükte adı "a" ile başlayanları filtrele  / [{'ad': 'adnan', 'yas': 17}, {'ad': 'ali', 'yas': 34}]
print(list(filter(lambda x : x["yas"] >23 , liste3)))                       # sözlğkte yası 23 den büyük olanları filtrele / [{'ad': 'ali', 'yas': 34}]
