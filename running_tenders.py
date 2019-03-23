# -*- coding: utf-8 -*-

from tkinter import *

def showcase():
     root = Toplevel()
     root.title("RUNNING TENDERS")
     l1 = Label(root, text="633521D", fg="green", font=("Aerial Bold", 16))
     l1.grid(row=0, column=0, padx=15, pady=15)

     l1 = Label(root, text="831522E", fg="green", font=("Aerial Bold", 16))
     l1.grid(row=1, column=0, padx=15, pady=15)

     l1 = Label(root, text="573521A", fg="green", font=("Aerial Bold", 16))
     l1.grid(row=2, column=0, padx=15, pady=15)

     l1 = Label(root, text="235132A", fg="green", font=("Aerial Bold", 16))
     l1.grid(row=3, column=0, padx=15, pady=15)

     root.mainloop()


if __name__ == "__main__":
    showcase()
