from tkinter import*
import random
class ss:
    def __init__(self,sayfa):
        self.sayfa=sayfa
        sayfa.title("Gui Örneği")

        self.baslık=Label(sayfa,text="Hoşgeldiniz,bilgileri görmek için\n Kişi/Buluş butonuna basınız...",font=("Arial",20),fg=("black"),bg=("light blue"))
        self.baslık.pack(side="top")

        self.buton=Button(sayfa,text="Kişi/Buluş",font=("Arial",14),fg=("black"),background=("light blue"),command=self.bilimİnsanı)
        self.buton.pack(side="left")

        self.buton2 = Button(sayfa, text="kapat", font=("Arial", 14), fg=("black"), background=("light blue"),command=sayfa.quit)
        self.buton2.pack(side="right")

    def bilimİnsanı(self):
        kisiveBulus = ("Cai Lun-Kağıt", "Galileo-Teleskop", "Cullen-Buzdolabı", "Kirkpatrick MacMillan-Bisiklet", "Johannes Guthenberg-Matbaa", "Rowland Hill-Pul", "Salvino D’Armate-Gözlük")
        secilen = random.choice(kisiveBulus)
        self.kisiveBulus = Label(self.sayfa, text=secilen)
        self.kisiveBulus.pack()

root = Tk()
secilen = ss(root)
root.mainloop()
