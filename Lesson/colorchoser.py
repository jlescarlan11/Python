from tkinter import *
from tkinter import colorchooser #  sub module

def click():
    # color = colorchooser.askcolor()[1]
    # colorHex = color[1]
    # window.config(bg=colorHex)  #   change background color

    # OR
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()

window.geometry('420x420')
button = Button(window, text='click me', command=click)
button.pack()

window.mainloop()