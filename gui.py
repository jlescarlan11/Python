from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets 

window = Tk() # instatantiate an intance of a window
window.geometry("420x420")
window.title("Blacky")

icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)
window.config(background="sky blue")

window.mainloop() # place window on computer screen, listen for events