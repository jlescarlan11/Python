# listbox = a listing of selectable text items within it's own container

from tkinter import *

def submit():
    print('You have ordered: ')
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entryBox.get())    

window = Tk()

listbox = Listbox(window,
                  bg='khaki',
                  font=('Constantia',35),
                  width=12
                  )
listbox.pack()

listbox.insert(0,'pizza')
listbox.insert(1,'pasta')
listbox.insert(2,'garlic bread')
listbox.insert(3,'soup')
listbox.insert(4,'salad')

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window,
                      text='submit',
                      command=submit)
submitButton.pack()

addButton = Button(window,
                   text='add',
                   command=add,
                   )
addButton.pack()

window.mainloop()