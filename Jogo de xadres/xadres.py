from tkinter import *






master = Tk()
master.geometry("800x800")

w = Canvas(master, width=800, height=800)
w.pack()






def casas_brancas():
     casa_branca = int (canvas_vert/2)
     w.create_rectangle (1, 100,canvas_vert, canvas_hori+100, fill = "mint cream")
     w.create_rectangle (100, 1, canvas_vert+100, canvas_hori+100,fill ="black")
     w.grid()



def coluna_vert():
     for x in range(8):
          canvas_vert= 100
          canvas_hori = 100

          x_vert = int (1)
          y_hori = int (1)

          while y_hori < 800:
               y_hori += 200

               w.create_rectangle(x_vert,y_hori, canvas_vert, canvas_hori, fill = "mint cream")
               w.create_rectangle(1, 200, canvas_vert, canvas_hori, fill = "black")
               w.grid()
               return;

coluna_vert()


          





    


     








mainloop()
