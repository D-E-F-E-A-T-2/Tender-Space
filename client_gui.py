# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk
#from tkinter import Canvas, BOTH
from PIL import ImageTk, Image
import os
import tkinter.messagebox
import client_profile as cp

def nothing():
    tkinter.messagebox.showinfo("Hello", "Hello you!")

def my_prof(self):
    cp.profile()

def client():
    root = Tk()
    root.geometry("535x250")
    root.title("TENDER PORTAL")
    app_name = "TENDER SPACE"
    #l1 = Label(root, text=app_name, font=("Times 32", 16))
    #l1.grid(row=0, column=0, padx=15,pady=25)

    img = ImageTk.PhotoImage(Image.open("appl2.png"))
    l4 = Label(root, image = img)
    l4.image=img
    l4.grid(row=0, column=0, padx=18, pady=8)
    
    tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=1, row=0, rowspan=1, sticky='ns', padx=15, pady=15)
    l2 = Label(root, text="Welcome UDB", font=("Aerial", 14), padx=20, pady=10, fg="gold")
    l2.grid(row=0, column=2)
    tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=3, row=0, rowspan=10, sticky='ns', padx=15, pady=15)
    l3 = Label(root, text="Contractors", font=("Aerial", 14), padx=20, pady=10, fg="SteelBlue1")
    l3.grid(row=0, column=4)
    
    img = ImageTk.PhotoImage(Image.open("logo11.png"))
    #l4 = Label(root, image = img)
    l4 = Button(root, image=img, cursor="mouse")
    l4.bind("<Button-1>", my_prof)
    l4.image=img
    l4.grid(row=1, column=2)

    #ib1 = Button(root, image=img)

    b1 = Button(root, text="RUNNING TENDERS", fg="blue", bg="OliveDrab1", relief="groove", width=15, cursor="star")
    b1.grid(row=3, column = 0)
    b2 = Button(root, text="RELEASE TENDERS", fg="blue", bg="OliveDrab1", relief="groove", width=15, cursor="star")
    b2.grid(row=3, column = 2)

    l5 = Label(root, text="Railway", font=("Aerial Bold", 13), fg="cyan2")
    l5.grid(row=1, column=4)

    #here take data of top 2 railway constructors
    lr1 = Label(root, text="data needed")
    lr1.grid(row=2, column=4)
    lr2 = Label(root, text="data needed")
    lr2.grid(row=3, column=4)

    l5 = Label(root, text="Road", font=("Aerial Bold", 13), fg="cyan2")
    l5.grid(row=4, column=4)

    #here take data of top 2 road constructors
    lr1 = Label(root, text="data needed")
    lr1.grid(row=5, column=4)
    lr2 = Label(root, text="data needed")
    lr2.grid(row=6, column=4)

    root.mainloop()

if __name__ == "__main__":
    client()
    
