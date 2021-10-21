from tkinter import *


master = Tk()
w = Canvas(master)


colunas = 8
linhas = 8

casa_ver = 50
casa_hor = 50
tabela = []

for i in range(linhas):
     tabela.append(w.create_rectangle(1, 1, casa_ver,casa_hor))

print (tabela)

mainloop()