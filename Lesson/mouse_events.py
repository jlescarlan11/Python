from tkinter import *

def doSomething(event):
    # print('Mouse coordinates: '+ str(event.x)+","+str(event.y))
    label.config(text=f"{event.x},{event.y}")
    

window =Tk()

window.bind('<Button-1>',doSomething) # left mouse click
window.bind('<Button-2>',doSomething) # middle scroll wheel click
window.bind('<Button-3>',doSomething) # right mouse click
window.bind('<ButtonRelease>',doSomething) # right mouse click

label = Label(window, font=('Helvetica', 100))
label.pack()

window.mainloop()