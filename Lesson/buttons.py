from tkinter import *

# button = you click it, then ti does stuff

count = 0
def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='clipboard.png')

button = Button(window,
                text='click me if I dont have a word!',
                command=click,
                font=("Arial", 20),
                fg="khaki",
                bg='Black',
                activeforeground='khaki',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound='bottom')

button.pack()

window.mainloop()