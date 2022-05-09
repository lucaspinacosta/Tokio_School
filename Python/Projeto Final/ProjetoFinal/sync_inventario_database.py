

from flask import request
import openpyxl, sqlite3

#from app import Produtos

con = sqlite3.connect("database\\dados_informacoes2.db")
cursor = con.cursor()

inventario = openpyxl.load_workbook("database\\inventario_produtos.xlsx")

sheet_usuarios = inventario['Usuarios']
sheet_admin = inventario['Admin']
sheet_fornecedores = inventario['Fornecedores']
sheet_produtos = inventario['Produtos']
print(inventario.sheetnames)

#Envia os dados do excel para a database
def sync_excel_database():
    produtos_list=[]
    for fila in sheet_produtos.rows:
        produtos_list.append((None,fila[1].value,fila[2].value,fila[3].value,fila[4].value,fila[5].value,fila[6].value,fila[7].value,fila[8].value))
    produtos_list.pop(0)

    cursor.execute("SELECT * FROM Produtos")
    verificar = cursor.fetchall()
   #Erro ao adicionar do exel para database, adiciona todos, quando deveria adicionar os que estao em falta 
    for produto in produtos_list:
            if produto[1] in verificar:
                print('\n',produto[1],'adiciona\n')
            elif produto[1] not in verificar: 
                print('\n',produto[1],'nao adiciona\n\n')
            else: cursor.execute("INSERT INTO Produtos VALUES(?,?,?,?,?,?,?,?,?)",produto)

    con.commit()
    


#Calcular lucro/despesa
def despesas():
    cursor.execute("SELECT * FROM Produtos")
    produto_in_stock = cursor.fetchall()
    lista_produtos = []
    total_lucro = 0
    despesa = 0
    lucro=0

    for produto in produto_in_stock:
        detalhes_produtos = {'Nome':produto[1],'valor_venda':produto[5],'preco_fornecedor':produto[4],'total_vendido':produto[3]}
        lista_produtos.append(detalhes_produtos)
        print(detalhes_produtos)
    
    for produto in lista_produtos:
        lucro = produto['valor_venda']*produto['total_vendido']
        despesa = produto['preco_fornecedor']*produto['total_vendido']
        total_lucro += lucro-despesa

        print ( '{} Lucro = {:.2f}'.format(produto['Nome'],total_lucro))
    


def file_galery():
    for produto_select in sheet_produtos.rows:
            return produto_select[2].value


con.commit()
con.close()