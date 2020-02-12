from tkinter import *
import cmath,math
from Arene import Arene
def mouvement():

    canvas.move(rob1,ar.r1.dx,ar.r1.dy)
    ar.r1.avance()
    if ar.r1.x > 470 and ar.r1.dx > 0:
        ar.r1.setDir(-ar.r1.dx,ar.r1.dy)
    if ar.r1.x < 0 and ar.r1.dx < 0 :
        ar.r1.setDir(-ar.r1.dx,ar.r1.dy)
    if ar.r1.y > 480 and ar.r1.dy > 0:
        ar.r1.setDir(ar.r1.dx,-ar.r1.dy)
    if ar.r1.y < 0 and ar.r1.dy < 0:
        ar.r1.setDir(ar.r1.dx,-ar.r1.dy)


    print("x=",ar.r1.x)
    print("y=",ar.r1.x)
    tk.after(20,mouvement)


ar = Arene(500, 500)
ar.r1.affiche()
tk = Tk()
canvas =Canvas(tk,width = ar.dimx,height = ar.dimy,bg='blue')
canvas.pack(padx = 50, pady = 50)
rob1 = canvas.create_rectangle(ar.r1.getX(), ar.r1.getY(), ar.r1.getX() + 30, ar.r1.getY() + 20, fill="red")

mouvement()
tk.mainloop()


