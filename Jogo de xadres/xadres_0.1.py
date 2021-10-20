from tkinter import *


master = Tk()
w = Canvas(master)
master.geometry("800x800")


casa_size_vert = 100
casa_size_hori = 100



def casas_pretas():
     w.create_rectangle(1, 1,casa_size_vert,casa_size_hori,fill= "black")
     w.grid()

def casas_brancas():
     w.create_rectangle(1, 1, casa_size_vert, casa_size_hori, fill="mint cream")
     w.grid()


def coluna_vert():
     y = 1
     while y < 8:
          casas_pretas
          
          y += 1

          
          return;
     



mainloop()