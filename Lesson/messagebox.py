from tkinter import *
from tkinter import messagebox  #   import messagebox library 

def click():
    # messagebox.showinfo(title='This is an info messagebox', message='You are a person')
    # while(True):
    #     messagebox.showwarning(title='WARNING!', message='You have a VIRUS')
    # messagebox.showerror(title='ERROR!', message='Something went wrong :(')

    # if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'):
    #     print('You did a thing!')
    # else:
    #     print('What now?')

    # if messagebox.askretrycancel(title='ask retry cancel', message='Do you want to retry the thing?'):
    #     print('You retry a thing!')
    # else:
    #     print('What now?')

    # if messagebox.askyesno(title='ask yes or no', message='Do you like me?'):
    #     print('I like you too')
    # else:
    #     print("That's good, you are ugly")

    # answer = messagebox.askquestion(title='ask question', message='do you like me?')
    # if (answer == 'yes'):
    #     print('I like you too')
    # else:
    #     print("That's good, you are ugly")

    answer = messagebox.askyesnocancel(title='yes no cancel', message='Do you like to code?', icon='info')
    if (answer==True):
        print('You like to code')
    elif (answer==False):
        print('idiot')
    else:
        print('Cancelled')

    



window = Tk()

button = Button(window,
                command=click,
                text='click me')

button.pack()

window.mainloop()