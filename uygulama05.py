__author__="selin ÇİFCİ
import random
ülkeler=random.choice(["türkiye","rusya","amerika","almanya","fransa","çin","japonya"])
harfhavuzu=[]
deneme=5
karaktercizgisi='_'
yazi=list(karaktercizgisi)*len(ülkeler)
dongu=1

while dongu:
    print(' '.join(yazi),end='\n\n')
    harf=input("harf giriniz:")
    try:
        int(harf)
        print("harf giriniz")
    except:
        if len(harf)>1:
            print("bir harf girebilirsiniz")
        else:
            if harf in harfhavuzu:
                print("başka bir harf giriniz")
            else:
                bulduk=None
                for i in range(len(ülkeler)):
                    if harf==ülkeler[i]:
                        bulduk=True

                        yazi[i]=harf
                        harfhavuzu.append(harf)
                        if karaktercizgisi not in yazi:
                            print(' '.join(harf))
                            print("kazandınız")
                            dongu=0
    else:
        if bulduk !=True:
           deneme -=1
        print("yanlış harf seçimi kalan hak:{}".format(deneme))
        harfhavuzu.append(harf)
    if deneme==0:
        print("yenildiniz.kelime '{}'".format(ülkeler))
        break
