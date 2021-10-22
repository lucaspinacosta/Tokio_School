from tkinter import *

master = Tk()
master.geometry("800x800")

w = Canvas(master, width=800, height=800)
w.pack()

canvas_vert= 100
canvas_hori = 100

def Coluna_A():
     casa_a1= { w.create_rectangle (0, 1,canvas_vert, canvas_hori, fill = "mint cream"),
     w.grid(row=0,column=0)}

     casa_a2 = {w.create_rectangle(200,1,canvas_vert,canvas_hori,fill="black"),
     w.grid(row=0,column=1)}

     casa_a3 = {w.create_rectangle(300,1, canvas_vert+100,canvas_hori, fill="mint cream"),
     w.grid(row=0,column=2)}

     casa_a4 = {w.create_rectangle(400,1,canvas_hori+200,canvas_vert,fill="black"),
     w.grid(row=0,column=3)}

     casa_a5 = {w.create_rectangle(500,1,canvas_hori+300,canvas_vert,fill="mint cream"),
     w.grid(row=0,column=4)}

     casa_a6 = {w.create_rectangle(600,1,canvas_hori+400,canvas_vert,fill="black"),
     w.grid(row=0,column=5)}

     casa_a7 = {w.create_rectangle(700, 1, canvas_hori+500,canvas_vert,fill="mint cream"),
     w.grid(row=0,column=6)}

     casa_a8 = {w.create_rectangle(800,1,canvas_hori+600, canvas_vert,fill="black"),
     w.grid(row=0,column=7)}

def Coluna_B():
     casa_b1 = {w.create_rectangle (0, 200, canvas_vert,canvas_hori, fill= "black"),
     w.grid(row=1,column=0)}

     casa_b2 = {w.create_rectangle (200,200, canvas_vert,canvas_hori, fill= "mint cream"),
     w.grid(row=1,column=1)}

     casa_b3 = {w.create_rectangle(300,200,canvas_vert+100,canvas_hori,fill="black"),
     w.grid(row=1,column=2)}

     casa_b4 = {w.create_rectangle(400,200,canvas_hori+200,canvas_vert,fill="mint cream"),
     w.grid(row=1,column=3)}

     casa_b5 = {w.create_rectangle(500,200,canvas_hori+300,canvas_vert,fill="black"),
     w.grid(row=1,column=4)}

     casa_b6 = {w.create_rectangle(600,200,canvas_hori+400,canvas_vert,fill="mint cream"),
     w.grid(row=1,column=5)}

     casa_b7 = {w.create_rectangle(700,200,canvas_hori+500,canvas_vert,fill="black"),
     w.grid(row=1,column=6)}

     casa_b8 = {w.create_rectangle(800,200,canvas_hori+600,canvas_vert,fill="mint cream"),
     w.grid(row=1,column=7)}

def Coluna_C():
     casa_c1 = {w.create_rectangle(0,300,canvas_vert,canvas_hori+100,fill="mint cream"),
          w.grid(row=2,column=0)}
     
     casa_c2 = {w.create_rectangle(200,300,canvas_vert,canvas_hori+100,fill="black"),
          w.grid(row=2,column=1)}

     casa_c3 = {w.create_rectangle(300,300,canvas_vert+100,canvas_hori+100,fill="mint cream"),
     w.grid(row=2,column=2)}

     casa_c4 = {w.create_rectangle(400,300,canvas_hori+200,canvas_vert+100,fill="black"),
     w.grid(row=2,column=3)}

     casa_c5 = {w.create_rectangle(500,300,canvas_vert+300,canvas_vert+100,fill="mint cream"),
     w.grid(row=2,column=4)}

     casa_c6 = {w.create_rectangle(600,300,canvas_hori+400,canvas_vert+100,fill="black"),
     w.grid(row=2,column=5)}

     casa_c7 = {w.create_rectangle(700,300,canvas_hori+500,canvas_vert+100,fill="mint cream"),
     w.grid(row=2,column=6)}

     casa_c7 = {w.create_rectangle(800,300,canvas_hori+600,canvas_vert+100,fill="black"),
     w.grid(row=2,column=7)}

def Coluna_D():
     casa_d1 = {w.create_rectangle(0,400,canvas_vert,canvas_hori+200,fill="black"),
     w.grid(row=3,column=0)}

     casa_d2 = {w.create_rectangle(200,400,canvas_vert,canvas_hori+200,fill="mint cream"),
     w.grid(row=3,column=1)}

     casa_d3 = {w.create_rectangle(300,400,canvas_vert+100,canvas_hori+200,fill="black"),
     w.grid(row=3,column=2)}

     casa_d4 = {w.create_rectangle(400,400,canvas_hori+200,canvas_vert+200,fill="mint cream"),
     w.grid(row=3,column=3)}

     casa_d5 = {w.create_rectangle(500,400,canvas_hori+300,canvas_vert+200,fill="black"),
     w.grid(row=3,column=4)}

     casa_d6 = {w.create_rectangle(600,400,canvas_hori+400,canvas_vert+200,fill="mint cream"),
     w.grid(row=3,column=5)}

     casa_d7 = {w.create_rectangle(700,400,canvas_hori+500,canvas_vert+200,fill="black"),
     w.grid(row=3,column=6)}

     casa_d8 = {w.create_rectangle(800,400,canvas_hori+600,canvas_vert+200,fill="mint cream"),
     w.grid(row=3,column=7)}

def Coluna_E():
     casa_e1 = {w.create_rectangle(0,500,canvas_hori,canvas_vert+300,fill="mint cream"),
     w.grid(row=4,column=0)}

     casa_e2 = {w.create_rectangle(200,500,canvas_hori,canvas_vert+300,fill="black"),
     w.grid(row=4,column=1)}

     casa_e3 = {w.create_rectangle(300,500,canvas_hori+100,canvas_vert+300,fill="mint cream"),
     w.grid(row=4,column=2)}

     casa_e4 = {w.create_rectangle(400,500,canvas_hori+200,canvas_vert+300,fill="black"),
     w.grid(row=4,column=3)}

     casa_e5 = {w.create_rectangle(500,500,canvas_hori+300,canvas_vert+300,fill="mint cream"),
     w.grid(row=4,column=4)}

     casa_e6 = {w.create_rectangle(600,500,canvas_hori+400,canvas_vert+300,fill="black"),
     w.grid(row=4,column=5)}

     casa_e7 = {w.create_rectangle(700,500,canvas_hori+500,canvas_vert+300,fill="mint cream"),
     w.grid(row=4,column=6)}

     casa_e8 = {w.create_rectangle(800,500,canvas_hori+600,canvas_vert+300,fill="black"),
     w.grid(row=4,column=7)}

def Coluna_F():
     casa_f1 = {w.create_rectangle(0,600,canvas_hori,canvas_hori+400,fill="black"),
     w.grid(row=5,column=0)}

     casa_f2 = {w.create_rectangle(200,600,canvas_hori,canvas_vert+400,fill="mint cream"),
     w.grid(row=5,column=1)}

     casa_f3 = {w.create_rectangle(300,600,canvas_hori+100,canvas_vert+400,fill="black"),
     w.grid(row=5,column=2)}

     casa_f4 = {w.create_rectangle(400,600,canvas_hori+200,canvas_vert+400,fill="mint cream"),
     w.grid(row=5,column=3)}

     casa_f5 = {w.create_rectangle(500,600,canvas_hori+300,canvas_vert+400,fill="black"),
     w.grid(row=5,column=4)}

     casa_f6 = {w.create_rectangle(600,600,canvas_hori+400,canvas_vert+400,fill="mint cream"),
     w.grid(row=5,column=5)}

     casa_f7 = {w.create_rectangle(700,600,canvas_hori+500,canvas_vert+400,fill="black"),
     w.grid(row=5,column=6)}

     casa_f8 = {w.create_rectangle(800,600,canvas_hori+600,canvas_vert+400,fill="mint cream"),
     w.grid(row=5,column=7)}

def Coluna_G():
     casa_g1 = {w.create_rectangle(0,700,canvas_hori,canvas_vert+500,fill="mint cream"),
     w.grid(row=6,column=0)}

     casa_g2 = {w.create_rectangle(200,700,canvas_hori,canvas_vert+500,fill="black"),
     w.grid_anchor}

     casa_g3 = {w.create_rectangle(300,700,canvas_hori+100,canvas_vert+500,fill="mint cream"),
     w.grid_anchor}

     casa_g4 = {w.create_rectangle(400,700,canvas_hori+200,canvas_vert+500,fill="black"),
     w.grid_anchor}

     casa_g5 = {w.create_rectangle(500,700,canvas_hori+300,canvas_vert+500,fill="mint cream"),
     w.grid_anchor}

     casa_g6 = {w.create_rectangle(600,700,canvas_hori+400,canvas_vert+500,fill="black"),
     w.grid_anchor}

     casa_g7 = {w.create_rectangle(700,700,canvas_hori+500,canvas_vert+500,fill="mint cream"),
     w.grid_anchor}

     casa_g8 = {w.create_rectangle(800,700,canvas_hori+600,canvas_vert+500,fill="black"),
     w.grid_anchor}

def Coluna_H():
     casa_h1 = {w.create_rectangle(0,800,canvas_hori,canvas_vert+600,fill="black"),
     w.grid_anchor}

     casa_h2 = {w.create_rectangle(200,800,canvas_hori,canvas_vert+600,fill="mint cream"),
     w.grid_anchor}

     casa_h3 = {w.create_rectangle(300,800,canvas_hori+100,canvas_vert+600,fill="black"),
     w.grid_anchor}

     casa_h4 = {w.create_rectangle(400,800,canvas_hori+200,canvas_vert+600,fill="mint cream"),
     w.grid_anchor}

     casa_h5 = {w.create_rectangle(500,800,canvas_hori+300,canvas_vert+600,fill="black"),
     w.grid_anchor}

     casa_h6 = {w.create_rectangle(600,800,canvas_hori+400,canvas_vert+600,fill="mint cream"),
     w.grid_anchor}

     casa_h7 = {w.create_rectangle(700,800,canvas_hori+500,canvas_vert+600,fill="black"),
     w.grid_anchor}

     casa_h8 = {w.create_rectangle(800,800,canvas_hori+600,canvas_vert+600,fill="mint cream"),
     w.grid_anchor}

def casas_geral():
     Coluna_A()
     Coluna_B()
     Coluna_C()
     Coluna_D()
     Coluna_E()
     Coluna_F()
     Coluna_G()
     Coluna_H()
     

def pecas():
     piao_br = Label



casas_geral()



 
mainloop()
