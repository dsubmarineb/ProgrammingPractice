from tkinter import *

var = Tk()
frame = Frame(var, width=300, height=250)
canvas = Canvas(var, width=300, height=250)

def leftclick(event):
    print("left")
    motion(event)
    pointerx = var.winfo_pointerx()
    pointery = var.winfo_pointery()
    rootx = var.winfo_rootx()
    rooty = var.winfo_rooty()
    x = pointerx-rootx
    y = pointery-rooty
    print("Pointer x is", pointerx)
    print("Root x is", rootx)
    create_circle(x, y, canvas)


def middleclick(event):
    print("middle")
    motion(event)

def rightclick(event):
    print("right")
    motion(event)

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

def create_circle(x, y, canvas, r=50):

    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r

    return canvas.create_oval(x0, y0, x1, y1)




frame.bind("<Button-1>", leftclick, motion)
frame.bind("<Button-2>", middleclick)
frame.bind("<Button-3>", rightclick)
#frame.bind('<Motion>', motion)

canvas.bind("<Button-1>", leftclick, motion)

frame.pack()
canvas.pack()
var.mainloop()