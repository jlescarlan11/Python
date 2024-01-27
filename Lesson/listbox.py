# listbox = a listing of selectable text items within it's own container

from tkinter import *

def submit():

    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print('You have ordered: ')
    for index in food:
        print(index)
    # print(listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size()) 

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
        listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg='khaki',
                  font=('Constantia',35),
                  width=12,
                  selectmode=MULTIPLE
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

deleteButton = Button(window,
                      text='delete',
                      command=delete)
deleteButton.pack()

window.mainloop()