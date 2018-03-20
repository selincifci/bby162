"__author__selin çifci"
#uygulama 2: saniyeyi dakika,saat,gün,ay,yıl şekline dönüştürme.

saniye=36256989896545

dakika=int(saniye/60)
print("dakika="+str(dakika))

saat=int(dakika/60)
print("saat="+str(saat))
gün=int(saat/24)
print("gün="+str(gün))
ay=int(gün/30)
print("ay="+str(ay))
yıl=int(ay%12)
print("yıl="+str(yıl))

