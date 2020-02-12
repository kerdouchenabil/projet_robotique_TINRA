from tkinter import *
from Arene import Arene
def mouvement():
    global tourner
    canvas.move(rob1,ar.r1.dx,ar.r1.dy)
    ar.r1.avance()
    if ar.r1.x > 460 and ar.r1.dx == 1:
        ar.r1.tournerDroite()
        print("abouch")
    print(ar.r1.x)
    tk.after(10,mouvement)

ar = Arene(500, 500)
ar.r1.affiche()
tk = Tk()
canvas =Canvas(tk,width = ar.dimx,height = ar.dimy,bg='blue')
canvas.pack(padx = 50, pady = 50)
rob1=canvas.create_rectangle(ar.r1.getX(),ar.r1.getY(),ar.r1.getX()+30,ar.r1.getY()+20,fill="red")
tourner = False
mouvement()

tk.mainloop()

