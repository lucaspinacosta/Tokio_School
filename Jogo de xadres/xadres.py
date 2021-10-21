from tkinter import *

master = Tk()
master.geometry("800x800")

w = Canvas(master, width=800, height=800)
w.pack()

canvas_vert= 100
canvas_hori = 100

def casas_brancas_a1():
     w.create_rectangle (1, 1,canvas_vert, canvas_hori, fill = "mint cream")
     w.grid(row=0,column=0)

     w.create_rectangle(200,1,canvas_vert,canvas_hori,fill="black")
     w.grid(row=0,column=1)

     w.create_rectangle(300,1, canvas_vert+100,canvas_hori, fill="mint cream")
     w.grid(row=0,column=2)

     w.create_rectangle(400,1,canvas_hori+200,canvas_vert,fill="black")
     w.grid(row=0,column=3)

     w.create_rectangle(500,1,canvas_hori+300,canvas_vert,fill="mint cream")
     w.grid(row=0,column=4)

     w.create_rectangle(600,1,canvas_hori+400,canvas_vert,fill="black")
     w.grid(row=0,column=5)

     w.create_rectangle(700, 1, canvas_hori+500,canvas_vert,fill="mint cream")
     w.grid(row=0,column=6)

     w.create_rectangle(800,1,canvas_hori+600, canvas_vert,fill="black")
     w.grid(row=1,column=7)

     w.create_rectangle(900, 1, canvas_hori+700,canvas_vert, fill="mint cream")
     w.grid(row=1, column=8)


def casas_pretas_b1():
     w.create_rectangle (1, 200, canvas_vert,canvas_hori, fill= "black")
     w.grid(row=1,column=0)

     w.create_rectangle (200,200, canvas_vert,canvas_hori, fill= "mint cream")
     w.grid(row=1,column=1)

     w.create_rectangle(300,200,canvas_vert+100,canvas_hori,fill="black")
     w.grid(row=1,column=2)

     w.create_rectangle(400,200,canvas_hori+200,canvas_vert,fill="mint cream")
     w.grid(row=1,column=3)

def casas_brancas_c1():
     w.create_rectangle(1,300,canvas_vert,canvas_hori+100,fill="mint cream")
     w.grid(row=2,column=0)
     

     w.create_rectangle(200,300,canvas_vert,canvas_hori+100,fill="black")
     w.grid(row=2,column=1)


     w.create_rectangle(300,300,canvas_vert+100,canvas_hori+100,fill="mint cream")
     w.grid(row=2,column=2)

def casas_pretas_d1():
     w.create_rectangle(1,400,canvas_vert,canvas_hori+200,fill="black")
     w.grid(row=3,column=0)


     w.create_rectangle(200,400,canvas_vert,canvas_hori+200,fill="mint cream")
     w.grid(row=3,column=1)


     w.create_rectangle(300,400,canvas_vert+100,canvas_hori+200,fill="black")
     w.grid(row=3,column=2)


def casas_geral():
     casas_brancas_a1()
     casas_pretas_b1()
     casas_brancas_a1()
     casas_brancas_c1()
     casas_pretas_d1()
     

casas_geral()



          





    


     








mainloop()
