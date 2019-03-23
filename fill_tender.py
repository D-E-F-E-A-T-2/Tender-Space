from tkinter import *
import tkinter.ttk

root = Tk()
root.title("FILL TENDER")

back = Button(root, text='<-Back')
back.grid()

tenderid = Label(root, text='Tender ID :')
tenderid.grid(columnspan=2, row=1, column=1, sticky = E, padx=5, pady=5)
idno = Label(root, text='621908B')
idno.grid(columnspan=2, row=1, column=3, padx=5, pady=5)

name = Label(root, text='Name of Bidder :')
name.grid(columnspan=2, row=2, column=1, sticky = E, padx=5, pady=5)
name_entry = Entry(root)
name_entry.grid(columnspan=2, row=2, column=3, padx=5, pady=5)

add = Label(root, text='Address :')
add.grid(columnspan=2, row=3, column=1, sticky = E, padx=5, pady=5)
add_entry = Entry(root)
add_entry.grid(columnspan=2, row=3, column=3, padx=5, pady=5)

tel = Label(root, text='Tel. Number :')
tel.grid(columnspan=2, row=4, column=1, sticky = E, padx=5, pady=5)
tel_entry = Entry(root)
tel_entry.grid(columnspan=2, row=4, column=3, padx=5, pady=5)

fax = Label(root, text='Fax Number :')
fax.grid(columnspan=2, row=5, column=1, sticky = E, padx=5, pady=5)
fax_entry = Entry(root)
fax_entry.grid(columnspan=2, row=5, column=3, padx=5, pady=5)

tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=10, row=1, rowspan=5, sticky='ns', padx = 10)

amount = Label(root, text='Tender Amount :')
amount.grid(columnspan=2, row=2 , column=14, sticky = E, padx=5, pady=5)
amount_entry = Entry(root)
amount_entry.grid(columnspan=2, row=2, column=16, padx=10, pady=5)

docs = Label(root, text='Required Documents :')
docs.grid(columnspan=2, row=3 , column=14, sticky = E, padx=5, pady=5)

doc1 = Label(root, text='doc1: ')
doc1.grid(columnspan=2, row=4 , column=14, sticky = E, padx=5, pady=5)
doc1_button = Button(root, text = 'Add File')
doc1_button.grid(columnspan=1, row=4, column=16, sticky = E, padx=5, pady=5)

submit_button = Button(root, text = 'Submit')
submit_button.grid(columnspan=1, row=9, column=10, sticky = E, pady=10)


root.mainloop()
