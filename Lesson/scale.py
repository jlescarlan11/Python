from tkinter import *

def submit():
    print(f"The temperature is {scale.get()} decrees C")

window = Tk()


hotImage = PhotoImage(file='fire.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()


scale = Scale(window,
              from_=0,
              to=100,
              length=300,
              orient=VERTICAL,    #   orientation of scale
              font=('garamond',10),
              tickinterval=25,  #   adds numeric indicators for value
              showvalue=0, #    show the current value
              resolution=5, #   increment of slider
              troughcolor='grey',
              fg='khaki',
              bg='black'
              )

scale.set(((scale['to']-scale['from'])/2)+scale['from'])
scale.pack()


coldImage = PhotoImage(file='cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,
                text='submit',
                command=submit,
                )
button.pack()

window.mainloop()