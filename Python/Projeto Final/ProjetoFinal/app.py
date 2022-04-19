
from flask import Flask,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy


root = Flask(__name__)
root.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_informacoes.db'
db=SQLAlchemy(root)
root.config['DEBUG']=True

class Produtos(db.Model):
    __tablename__ = "produto"
    numero_serie = db.Column(db.Integer,primary_key=True)
    nome_de_produto = db.Column(db.String(100))
    disponibilidade = db.Column(db.Boolean)
    
@root.route('/',methods=['GET'])
def home():
    return render_template('index.html')


root.run()