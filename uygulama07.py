from tkinter import *
from PIL import Image, ImageTk
album = Tk()
album.title("Doğa Manzaraları")
album.configure(background="purple")


resim1 = ImageTk.PhotoImage(Image.open("manzara1.jpg"))
resim2 = ImageTk.PhotoImage(Image.open("manzara2.jpg"))
resim3= ImageTk.PhotoImage(Image.open("manzara3.jpg"))
resim4=ImageTk.PhotoImage(Image.open("manzara4.jpg"))
etiket = Label(album, text="Doğa Manzaraları", bg="grey", font="arial 15 bold")
etiket.pack()

def ileri():
    if display == resim1:
        panel1.configure(image=resim2)
    else:
        panel1.configure(image=resim1)

ileributon = Button(album, text="İleri", command=ileri , bg="red", font="arial 15 bold")
ileributon.pack(side="right")

def geri():
    if display2 == resim2:
        panel1.configure(image = resim1)
    else:
        panel1.configure(image = resim2)

geributon = Button(album, text="Geri", command=geri, bg="red", font="arial 15 bold")
geributon.pack(side="left")

panel1 = Label(album, image=resim1)
display = resim1
panel1.pack(side="top")

panel2 = Label(album, image=resim2)
display2 = resim2


album.mainloop()
