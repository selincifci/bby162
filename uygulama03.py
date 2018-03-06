#__author__"selin çifci"
# liste/sözlük oluşturma ve fonksiyonları kullanma
a=["ocak","şubat","mart","nisan","mayıs","haziran","temmuz","ağustos","eylül","ekim","kasım"]
print(a)
a+=("aralık")#sabit ekleme
print(a)
a.append("aylar")
print(a)
a[2:5]=["ilk bahar"]
print(a)
print("ocak" in a)
print("kış" in a)

b={"kış":"aralık-ocak-şubat","ilk bahar":"mart-nisan-mayıs","yaz":"haziran-temmuz-ağustos","son bahar":"eylül-ekim-kasım"}
print(b)
b["mevsim"]="ay içeriği"
print(b)
print(b["kış"])
print(b.keys())
print(b.values())
