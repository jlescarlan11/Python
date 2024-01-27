from tkinter import *

def display():
    if(x.get()):
        print('You agree!')
    else:
        print("You don't agree :(")

window = Tk()

x = BooleanVar()

photo = PhotoImage(file='clipboard.png')

check_button = Checkbutton(window,
                           text='I agree to something',
                           variable=x,
                           onvalue=TRUE,
                           offvalue=FALSE,
                           command=display,
                           font=('Garamond',20),
                           fg='khaki',
                           bg='black',
                           activeforeground='khaki',
                           activebackground='black',
                           padx=25,
                           pady=25,
                           image=photo,
                           compound=LEFT)

        

check_button.pack()




window.mainloop()