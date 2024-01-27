# radio button = similar to checkbox but you can select one from a froup

from tkinter import *

food = ['pizza','hamburger','hotdog']

def order():
    if (x.get()==0):
        print('You ordered pizza')
    elif (x.get()==1):
        print('You ordered a hamburger')
    elif (x.get()==2):
        print('You ordered hotdog')
    else:
        print('huh?')

window = Tk()

pizzaImage = PhotoImage(file='pizza.png')
hotdogImage = PhotoImage(file='hotdog.png')
hamburgerImage = PhotoImage(file='hamburger.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage]

x = IntVar()


for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index], # adds text to radio buttons
                              variable=x, # groups radio buttons together if they share the same variable
                              value=index, # assigns each radio button a different value
                              padx=25,  #   This adds padding on x-axis
                              font=("Garamond",50),
                              bg='white',
                              activebackground='white',
                              image=foodImages[index],   #   This adds image to radiobutton
                              compound = LEFT,  #adds images & text (left-side)
                              indicatoron=False, #   Eliminates circle indicators
                              width = 500,   #   This sets width of radio buttoms
                              command=order #   set command of radiobutton to function
                            )
    radiobutton.config()
    radiobutton.pack(anchor=W)
    
window.mainloop()