__author__"Selin ÇİFCİ"
kadin=input("isim giriniz:")
erkek=input("isim giriniz")
misra=input("mısra sayısı giriniz:")
sec=int(misra)
bosluk=" "

i=["ilk görüşte","vapurdayken","okula giderken","arkadaşlarıyla gezerken","ağlarken","mesajlaştığında","sinirlendiğinde","ders çalışıyorken","saçmalarken"]
k=["yanına gitti","konuştu","mesajına cevap vermedi","görüldü attı","eğlendi","depresyona girdi","dizi izleyip ağladı","çikolata yiyip kilo aldı","canı sıkıldı"]

import random
def ilk():
    secim=random.choice(i)
    i.remove(secim)
    return secim
def ikinci():
    secim=random.choice(k)
    k.remove(secim)
    return secim

a=(kadin+bosluk+ilk()+bosluk+erkek+bosluk+ikinci()+"\n")
b=(erkek+bosluk+ilk()+bosluk+kadin+bosluk+ikinci()+"\n")
c=(kadin+bosluk+ilk()+bosluk+erkek+bosluk+ikinci()+"\n")
d=(erkek+bosluk+ilk()+bosluk+kadin+bosluk+ikinci()+"\n")
e=(kadin+bosluk+ilk()+bosluk+erkek+bosluk+ikinci()+"\n")
f=(erkek+bosluk+ilk()+bosluk+kadin+bosluk+ikinci()+"\n")

if sec==1 :
    print(a or b or c or d or e or f)

elif sec==2:
    print(a,b)

elif sec==3:
    print(a,b,c)

elif sec==4:
    print(a,b,c,d)

elif sec==5:
    print(a,b,c,d,e)

elif sec==6:
    print(a,b,c,d,e,f)

else:
    print("en fazla 6 mısra girebilirsiniz")
