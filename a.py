from tkinter import *
import tkinter.ttk

root = Tk()

back = Button(root, text='<-Back')
back.grid()

tenderid = Label(root, text='Tender ID :')
tenderid.grid(columnspan=2, row=1, column=1, sticky = E)
idno = Label(root, text='123')
idno.grid(columnspan=2, row=1, column=3)

name = Label(root, text='Name of Bidder :')
name.grid(columnspan=2, row=2, column=1, sticky = E)
name_entry = Entry(root)
name_entry.grid(columnspan=2, row=2, column=3)

add = Label(root, text='Address :')
add.grid(columnspan=2, row=3, column=1, sticky = E)
add_entry = Entry(root)
add_entry.grid(columnspan=2, row=3, column=3)

tel = Label(root, text='Tel. Number :')
tel.grid(columnspan=2, row=4, column=1, sticky = E)
tel_entry = Entry(root)
tel_entry.grid(columnspan=2, row=4, column=3)

fax = Label(root, text='Fax Number :')
fax.grid(columnspan=2, row=5, column=1, sticky = E)
fax_entry = Entry(root)
fax_entry.grid(columnspan=2, row=5, column=3)

tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=10, row=1, rowspan=5, sticky='ns', padx = 10)

amount = Label(root, text='Tender Amount :')
amount.grid(columnspan=2, row=2 , column=14, sticky = E)
amount_entry = Entry(root)
amount_entry.grid(columnspan=2, row=2, column=16)

docs = Label(root, text='Required Documents :')
docs.grid(columnspan=2, row=3 , column=14, sticky = E)

doc1 = Label(root, text='doc1: ')
doc1.grid(columnspan=2, row=4 , column=14, sticky = E)
doc1_button = Button(root, text = 'Add File')
doc1_button.grid(columnspan=1, row=4, column=16, sticky = E)

submit_button = Button(root, text = 'Submit')
submit_button.grid(columnspan=1, row=9, column=10, sticky = E)


root.mainloop()
