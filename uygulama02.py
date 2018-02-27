"__author__selin çifci"
#uygulama 2: saniyeyi dakika,saat,gün,ay,yıl şekline dönüştürme.


number=439849987698764864388758
result=int(number/60)
remainder=(number%60)
print("saat="+str(result))
print(("dakika="+str(remainder)))

number=7330833128312747851776
result=int(number/30)
remainder=(number%30)
print("ay="+str(result))
print(("gün="+str(remainder)))

number=244361104277091581952
result=int(number/365)
print("yıl="+str(result))
