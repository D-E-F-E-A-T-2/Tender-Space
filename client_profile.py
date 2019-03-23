# -*- coding: utf-8 -*-

from tkinter import *
from PIL import ImageTk, Image

def profile():
    root = Toplevel()
    name = "UNIQUE DREAM BUILDERS"

    l1 = Label(root, text=name, fg="blue2", font=("Aerial Font" ,12))
    l1.grid(row=0, column=0)
    #l1.pack(side=LEFT)

    img = ImageTk.PhotoImage(Image.open("appl2.png"))
    l2 = Button(root, image=img)
    l2.image=img
    l2.grid(row=1, column=1, rowspan=2, columnspan=2, pady=8)
    #l2.pack(side=LEFT)

    l3=Label(root, text="Company name", font=("Aerial Bold", '11'))
    l3.grid(row=4, column=0, sticky=W)
    l3=Label(root, text="Unique Dream Builders")
    l3.grid(row=4, column=1, sticky=W)
    

    l3=Label(root, text="Adress", font=("Aerial Bold", '11'))
    l3.grid(row=5, column=0, sticky=W)
    l3=Label(root, text="UDB TOWER, 3rd Floor, SB-59, Opp. Jaipur Nagar Nigam, Rajasthan 302015")
    l3.grid(row=5, column=1, sticky=W)
    

    l3=Label(root, text="Domain", font=("Aerial Bold", '11'))
    l3.grid(row=6, column=0, sticky=W)
    l3=Label(root, text="Real Estate")
    l3.grid(row=6, column=1, sticky=W)

    l3=Label(root, text="Federal Electrorates", font=("Aerial Bold", '11'))
    l3.grid(row=7, column=0, sticky=W)
    l3=Label(root, text="Leichhardt")
    l3.grid(row=7, column=1, sticky=W)

    l3=Label(root, text="Company Type", font=("Aerial Bold", '11'))
    l3.grid(row=8, column=0, sticky=W)
    l3=Label(root, text="Builders")
    l3.grid(row=8, column=1, sticky=W)

    l3=Label(root, text="Tenders Released", font=("Aerial Bold", '11'))
    l3.grid(row=9, column=0, sticky=W)
    l3=Label(root, text="B&B Mayflower Heights, Vasantham Sun City")
    l3.grid(row=9, column=1, sticky=W)

    root.mainloop()    


if __name__ == "__main__":
    profile()
