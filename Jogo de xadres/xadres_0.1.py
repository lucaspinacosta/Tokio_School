from tkinter import *


master = Tk()
w = Canvas(master, width=800, height=800)
w.pack()





def tabuleiro():
     i = 0
     coluna_vertical = 1
     coluna_horizontal = 1
     medida_lateral = 100
     medida_base = 100
     numero_qudrados = 64
     
     for i in range (8):
          w.create_rectangle(coluna_horizontal,coluna_vertical,medida_base,medida_lateral, fill="black")
          w.grid()
          coluna_horizontal+=200
          i+=1
          return

     
tabuleiro()
         

mainloop()