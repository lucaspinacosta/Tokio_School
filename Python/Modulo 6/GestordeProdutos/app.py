
from tkinter import ttk
from  tkinter import *
import sqlite3

from sqlalchemy import column

class Produto:
    db = 'database/produtos.db'
    def __init__(self,root):
        self.janela = root
        self.janela.title("App Gestor de Produtos")
        self.janela.resizable(1,1)
        self.janela.wm_iconbitmap('recursos/M6_P2_icon.ico')
        
        
        frame = LabelFrame(self.janela,text="Registar um novo produto")
        frame.grid(row=0,column=0,columnspan=3,pady=30,padx=10,ipadx=5,ipady=5)
        #frame.pack(expand=True)

        #Label Nome
        self.etiqueta_nome = Label(frame, text="Nome: ")
        self.etiqueta_nome.grid(row=1,column=0) #Posicao no grid


        #Entry Nome label(input label)
        self.nome = Entry(frame)
        self.nome.focus() #Para que o foco do rato va a este Entry no inicio
        self.nome.grid(row=1,column=1,padx=5,pady=5)

        #Label Preco
        self.etiqueta_preco = Label(frame, text="Preco: ")
        self.etiqueta_preco.grid(row=2,column=0)#Posicionamento
        
        #Entry precoLabel
        self.preco = Entry(frame)
        self.preco.grid(row=2,column=1,padx=5,pady=5)

        #Button Add Produto
        self.button_adicionar = ttk.Button(frame,text="Guardar Produto",command=self.add_produto)
        self.button_adicionar.grid(row=3,columnspan=2,sticky= W+E)
        #self.button_remover = ttk.Button(frame,text="Eliminar produto",command=self.eleiminar_produto)

        #Mensagem informativa para o utilizador
        self.mensagem = Label(text='',fg='#000000',bg='#283c86',font=('Calibri',15,'bold'))
        self.mensagem.grid(row=3,column=0,columnspan=2,sticky=W+E)

        #Tabela Database
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthinckness=0,bd=10, font=('Calibri',11)) #Modifica a fonte e a tabela
        style.configure("mystyle.Treeview.Heading",font=('Calibri',11,'bold')) #Modifica a fonte das cabeceiras
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea',{'sticky':'nswe'})]) #Elimina as bordas

        self.tabela = ttk.Treeview(height=20,columns=2,style="mystyle.Treeview")
        self.tabela.grid(row=4,column=0,columnspan=2,padx=10,pady=5,ipadx=5,ipady=5)
        self.tabela.heading('#0',text='Nome',anchor=CENTER)
        self.tabela.heading('#1',text='Preco',anchor=CENTER)

        #Botao Eliminar
        botao_eliminar = ttk.Button(text='ELIMINAR',command=self.del_produto)
        botao_eliminar.grid(row=5,column=0,sticky=W+E)
        #Botao Editar
        botao_editar = ttk.Button(text='EDITAR',command=self.editar_produtos)
        botao_editar.grid(row=5,column=1,sticky=W+E)
        self.get_produtos()
        
    def db_consulta(self,consulta,parametros =()):
        with sqlite3.connect(self.db) as con:  #Inciciamos uma conexao com base de dados (alias on)
            cursor = con.cursor()
            resultado = cursor.execute(consulta,parametros)
            con.commit()
            return resultado
    
    def get_produtos(self):
        #limpar a tabela de dados residuais ou antigos
        registos_tabela = self.tabela.get_children()  #obtem todos os dados da tabela
        for linha in registos_tabela:
            self.tabela.delete(linha)

        #Consulta SQL
        query = 'SELECT * FROM produto ORDER BY nome DESC'
        registos_db = self.db_consulta(query) # Chama o metodo db_consultas

        #Escrever os dados no ecra
        for linha in registos_db:
            print(linha)
            self.tabela.insert('',0,text=linha[1],values=linha[2])
            
    def validacao_nome(self):
        nome_introduzido_por_utilizador = self.nome.get()
        return len(nome_introduzido_por_utilizador) !=0

    def validacao_preco(self):
        preco_introduzido_por_utilizador = self.preco.get()
        return len(preco_introduzido_por_utilizador) !=0

    #Adicionar produtos na base de dados
    def add_produto(self):
        if self.validacao_nome() and self.validacao_preco():
            query='INSERT INTO produto VALUES(NULL,?,?)'
            parametros = (self.nome.get(), self.preco.get())

            self.db_consulta(query,parametros)
            print ("Dados Guardados")
            self.mensagem['text'] = f'Produto {self.nome.get()} adicionado com exito'
            self.nome.delete(0,END)
            self.preco.delete(0,END)           

        elif self.validacao_nome() and self.validacao_preco() == False:
            self.mensagem['text'] = 'O preco e obrigatorio'
        elif  self.validacao_nome() == False and self.validacao_preco():
            self.mensagem['text']="O nome e obrigatorio"
        else:
            self.mensagem['text']="O nome e o preco sao obrigatorios"
        
        self.get_produtos()

    def del_produto(self):
        self.mensagem['text']=''
        try:
            self.tabela.item(self.tabela.selection())['text'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Por favor, selecione um produto'
            return
        self.mensagem['text'] =''
        nome = self.tabela.item(self.tabela.selection())['text']
        query = 'DELETE FROM produto WHERE nome = ?'
        self.db_consulta(query,(nome,))
        self.mensagem['text'] = f'Produto {nome} eliminado com exito'
        self.get_produtos()

    def editar_produtos(self):
        self.mensagem['text']=''
        try:
            self.tabela.item(self.tabela.selection())['text'][0]
        except IndexError as e:
            self.mensagem['text'] = 'Por favor, selecione um produto'
            return
        nome = self.tabela.item(self.tabela.selection())['text']
        old_preco = self.tabela.item(self.tabela.selection())['values'][0]

        self.janela_edit = Toplevel()
        self.janela_edit.title='Editar Produto'
        self.janela_edit.resizable(1,1)
        self.janela_edit.wm_iconbitmap('recursos/M6_P2_icon.ico')
        self.janela_edit.configure(background="#283c86")
        
        titulo = Label(self.janela_edit,text='Edicao de Produtos',font=('Calibri',50,'bold'),bg="#283c86")
        titulo.grid(column=0,row=0)

        frame_ep = LabelFrame(self.janela_edit,text='Editar o seguinte produto')
        frame_ep.grid(row=1,column=0,columnspan=20,pady=20)

        self.etiqueta_nome_antigo =Label(frame_ep, text="Nome antigo: ")
        self.etiqueta_nome_antigo.grid(row=2,column=0)
        self.input_nome_antigo = Entry(frame_ep,textvariable=StringVar(self.janela_edit,value=nome),state='readonly')
        self.input_nome_antigo.grid(row=2,column=1)

        #Label nome novo
        self.etiqueta_nome_novo = Label(frame_ep,text="Nome novo: ")
        self.etiqueta_nome_novo.grid(row=3,column=0)
        self.input_nome_novo = Entry(frame_ep)
        self.input_nome_novo.grid(row=3,column=1)
        self.input_nome_novo.focus()

        #Label Preco Antigo
        self.etiqueta_preco_antigo = Label(frame_ep, text="Preco antigo: ")
        self.etiqueta_preco_antigo.grid(row=4,column=0)
        self.input_preco_antigo = Entry(frame_ep,textvariable=StringVar(self.janela_edit,value=old_preco),state='readonly')
        self.input_preco_antigo.grid(row=4,column=1)

        #Label Preco Novo
        self.etiqueta_preco_novo = Label(frame_ep,text='Preco novo: ')
        self.etiqueta_preco_novo.grid(row=5,column=0)
        self.input_preco_novo = Entry(frame_ep)
        self.input_preco_novo.grid(row=5,column=1)

        #Botao atualizar
        self.botao_atualizar = ttk.Button(frame_ep,text='Atualizar Produto',command=lambda:
        self.atualizar_produto(self.input_nome_novo.get(),self.input_nome_antigo.get(),self.input_preco_novo.get(),self.input_preco_antigo.get()))
        self.botao_atualizar.grid(row=6,columnspan=2,sticky=W+E)
    
    def atualizar_produto(self,novo_nome,antigo_nome,novo_preco,antigo_preco):
        produto_modificador = False
        query = 'UPDATE  produto SET nome = ?, preco= ? WHERE nome = ? AND preco= ?'
        if novo_nome!= '' and novo_preco != '':
            parametros= (novo_nome, novo_preco,antigo_nome,antigo_preco)
            produto_modificador = True
        elif  novo_nome!='' and novo_preco == '':
            parametros = (novo_nome,antigo_preco,antigo_nome,antigo_preco)
            produto_modificador = True
        elif novo_nome == '' and novo_preco != '':
            parametros = (antigo_nome,novo_preco,antigo_nome,antigo_preco)
            produto_modificador=True
        
        if (produto_modificador):
            self.db_consulta(query,parametros)
            self.janela_edit.destroy()
            self.mensagem['text'] = f'O Produto {antigo_nome} foi atualizado com exito.'
            self.get_produtos()
        else: 
            self.janela_edit.destroy()
            self.mensagem['text'] = f'O Produto {antigo_nome} NAO foi altualizado.'
            self.get_produtos()
            

if __name__ == '__main__':
    root = Tk()
    root.geometry("430x700")
    root.configure(background="#283c86")
    app = Produto(root)
    root.mainloop()
