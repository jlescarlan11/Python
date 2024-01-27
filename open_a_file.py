from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir=r'D:\UP Files\Python\Lesson',
                                          title='open file okay',
                                          filetypes=(('text files','*.txt'),
                                          ('all files','*.*')))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window,text='open',command=openFile)
button.pack()

window.mainloop()