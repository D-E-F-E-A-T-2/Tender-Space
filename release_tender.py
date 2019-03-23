# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.ttk

def release_open():

    def on_focusout(event):
        text=e1.get()
        f.write(text)
    
    f=open("tenders.txt", "a+")
    f2=open("documents.txt", "a+")
    global count
    count = 3
    global count2
    count2 = 1
    def open_select():
        global count
        global count2
        def create(self):
            global count
            e1 = Entry(root, width=15)
            e1.grid(row=count, column=0, columnspan=2)
            count+=1
            e1.focus_set()
            text = e1.get()
            f.write(text)
            
        def create2(self):

            def close_(self):
                f.close()
                f2.close()
                root.destroy()
            
            try:
                if say:
                    b2.destroy()
                else:
                    pass
            except:
                pass
            global count2
            e1 = Entry(root, width=15)
            e1.grid(row=count2, column=4, columnspan=2)
            count2+=1
            e1.focus_set()
            e1.bind("<FocusOut>", on_focusout)
            #text = e1.get()
            #f2.write(text+'\n')
            print("ok")
            print(text)
            b2 = Button(root, text="RELEASE", relief="groove")
            b2.grid(row=count2, column=4, columnspan=2)
            b2.bind("<Button-1>", close_)
            say = True

        
        options = ["Railway", "Real Estate", "Road", "Custom"]
        var2 = StringVar(root)
        var2.set("Select Domain")
        dd = OptionMenu(root, var2, *options)
        dd.grid(row=1, column=0, columnspan=2)
        
        lh1 = Label(root, text="Add Field", padx=5, pady=5)
        lh1.grid(row=2, column=0)
        #count decided from here
        b1 = Button(root, text="+", bd=1,  relief= "groove", borderwidth= 3)
        b1.bind("<Button-1>", create)
        b1.grid(row=2, column=1)

        lh1 = Label(root, text="Required Documents", padx=5, pady=5)
        lh1.grid(row=0, column=4)
        #count decided from here
        b1 = Button(root, text="+", bd=1,  relief= "groove", borderwidth= 3)
        b1.bind("<Button-1>", create2)
        b1.grid(row=0, column=5)

        root.mainloop()
        

    def radio_calls():
        r_var = var1.get()
        if r_var==1: open_select()
    
    root = Toplevel()
    root.title("RELEASE TENDER")
    tkinter.ttk.Separator(root, orient=VERTICAL).grid(column=3, row=0, rowspan=10, sticky='ns', padx=15, pady=15) #vertical line
    var1 = IntVar()

    r1 = Radiobutton(root, text="OPEN", variable=var1, value=1, command=radio_calls)
    r1.grid(row=0, column=0, padx=10, pady=10)
    r1 = Radiobutton(root, text="SELECTIVE", variable=var1, value=2, command=radio_calls)
    r1.grid(row=0, column=1, padx=10, pady=10)

    



if __name__ == "__main__":
    release_open()
