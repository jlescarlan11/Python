# canvas = widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0,0,500,500,fill='blue',width=5)
# canvas.create_line(0,500,500,0,fill='red',width=5)
# canvas.create_rectangle(50,50,250,250,fill='fuchsia')
# points = [250,0,0,500,500,500]
# canvas.create_polygon(points, fill='khaki',outline='black', width=5)
# canvas.create_arc(0,0,500,500,fill='brown',style=PIESLICE,start=270, extent=180)

canvas.create_arc(0, 0, 500, 500, fill='Red',extent=180, width=0.5)
canvas.create_arc(0, 0, 500, 500, fill='white', start=180, extent=180, width=0.5)
canvas.create_line(0,250,500,250,fill='black', width=7.5)
canvas.create_oval(190,190,310,310, fill='White', width=7.5)

canvas.pack()

window.mainloop()
