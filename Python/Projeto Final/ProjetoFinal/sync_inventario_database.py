
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,request
import openpyxl, sqlite3


root= Flask(__name__)
root.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_informacoes2.db'
db = SQLAlchemy(root)
root.config['DEBUG'] = True

#from app import Produtos

con = sqlite3.connect("database\\dados_informacoes2.db")
cursor = con.cursor()

inventario = openpyxl.load_workbook("database\\inventario_produtos.xlsx")

sheet_usuarios = inventario['Usuarios']
sheet_admin = inventario['Admin']
sheet_fornecedores = inventario['Fornecedores']
sheet_produtos = inventario['Produtos']
print(inventario.sheetnames)





con.commit()
con.close()