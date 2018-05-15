import tkinter
from random import choice
class Simon() :
    def __init__(self, anaSayfa) 
        self.anaSayfa = anaSayfa
        self.anaSayfa.minsize(640, 480)
        self.anaSayfa.title("Simon oyunu")
        self.anaSayfa.update()

        self.tablo = tkinter.Canvas(self.anaSayfa, width = self.anaSayfa.winfo_width(), height = self.anaSayfa.winfo_height(), highlightthickness = 0)
        self.tablo.pack()


        self.renkler = ("red", "blue", "green", "yellow")
        self.tonlar = ("#ff4d4d", "#4d4dff", "#4dff4d", "#ffff4d")
        self.olan_renk = [color for color in self.renkler]

        self.renk_list = []
        self.secim = [choice(self.renkler)]
        self.baslangic = 0

        self.cizim()
        self.gor()
        self.anaSayfa.mainloop()


    def gor(self):
        self.bak(self.secim[self.baslangic])
        if(self.baslangic< len(self.secim) - 1) :
            self.baslangic+= 1
            self.anaSayfa.after(1250, self.gor())
        else :
            self.baslangic= 0

    def bak(self, renk) :
        index = self.renkler.index(renk)
        if self.olan_renk[index] == self.renkler[index]:              #renk eşlemesi için konuma bakılıyor
            self.olan_renk[index] = self.tonlar[index]
            self.anaSayfa.after(500, self.bak,renk)
        else :
            self.olan_renk[index] = self.renkler[index]
        self.cizim()

    def kontrol(self) :
        renk = self.renkler[self.renk_list.index(self.tablo.find_withtag("current")[0])]
        if(renk == self.secim[self.baslangic]) :
            if(self.baslangic < len(self.secim) - 1) :
                self.baslangic += 1
            else :
                self.anaSayfa.title("Simon oyunu - puan: {}".format(len(self.secim)))
                self.secim.append(choice(self.renkler))
                self.sequence_position = 0
                self.gor()
        else :
            self.anaSayfa.title("Simon oyunu- Oyun Bitti! | Puanınız: {}".format(len(self.secim)))
            self.secim[:] = []
            self.secim.append(choice(self.renkler))
            self.sequence_position = 0
            self.gor()

    def cizim(self) :
        self.renk_list[:] = []
        self.tablo.delete("tümü")
        for index, renk in enumerate(self.olan_renk) :
            if index <= 1 :
                self.renk_list.append(self.tablo.create_rectangle(index * self.anaSayfa.winfo_width(), 0, self.anaSayfa.winfo_width() / 2, self.anaSayfa.winfo_height() / 2, fill = renk, outline = renk))
            else :
                self.renk_list.append(self.tablo.create_rectangle((index - 2) * self.anaSayfa.winfo_width(), self.anaSayfa.winfo_height(), self.anaSayfa.winfo_width() / 2, self.anaSayfa.winfo_height() / 2, fill = renk, outline = renk))
        for id in self.renk_list :
            self.tablo.tag_bind(id, '<ButtonPress-1>', lambda e : self.kontrol())



root = tkinter.Tk()
gui = Simon(root)
root.mainloop()
