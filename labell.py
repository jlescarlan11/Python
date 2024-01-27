from tkinter import *

window = Tk()

photo = PhotoImage(file='logo.png')

label = Label(
    window, 
    text="what the fuck the fuck?",
    font=('Arial',12,'bold'),
    fg='red',
    bg='black',
    relief=SUNKEN,
    bd=10,
    padx=20,
    pady=20,
    image=photo,
    compound='right'
    )

label.pack()
# label.place(x=100,y=100)

window.mainloop()