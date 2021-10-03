from tkinter import *

var = Tk()
canvas = Canvas(var, width=500, height=500)

def leftclick(event):
    print("left")
    getcoord(event)
    create_red_circle(event)

def middleclick(event):
    print("middle")
    deletekey("all")

def rightclick(event):
    print("right")
    deletekey("current")

def deletekey(key):
    print("Deleting: " + key)
    canvas.delete(key)

def create_circle(event):
    x, y = event.x, event.y
    r = 50
    x0, y0 = x-r, y-r
    x1, y1 = x+r, y+r
    return canvas.create_oval(x0, y0, x1, y1, fill='white')

def create_red_circle(event):
    x, y = event.x, event.y
    r = 15
    x0, y0 = x-r, y-r
    x1, y1 = x+r, y+r
    return canvas.create_oval(x0, y0, x1, y1, fill='red', width=2)


def getcoord(event):
    x, y = event.x, event.y
    print("Location: "+'{}, {}'.format(x, y))

def removeall(event):
    print("a")
    deletekey("all")

def cursor(event):
    deletekey("current")
    create_red_circle(event)

var.bind('a', removeall)


canvas.bind("<Button-1>", leftclick)
canvas.bind("<Button-2>", middleclick)
canvas.bind("<Button-3>", rightclick)

canvas.bind("<Motion>", cursor)

# canvas.bind("<B1-Motion>", leftclick)
# canvas.bind("<B2-Motion>", middleclick)
# canvas.bind("<B3-Motion>", rightclick)
# canvas.bind('<Motion>', motion)
# canvas.bind('<Motion>', create_circle, add="+")

canvas.pack()
var.mainloop()