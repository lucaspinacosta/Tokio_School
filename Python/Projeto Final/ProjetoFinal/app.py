
from flask import Flask, redirect,render_template,request,url_for
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
    genero_do_produto = db.Column(db.String(30))
    db.create_all()
    db.session.commit()

@root.route('/criar_produtos',methods=['POST'])
def criar_produtos():
    produto=Produtos(conteudo=request.form[''])


class Clientes(db.Model):
    __tablename__ = 'usuarios'
    email = db.Column(db.String(128))
    numero_ID = db.Column(db.Integer,primary_key=True)
    nome_usuario = db.Column(db.String(60))
    password_usuario = db.Column(db.String(12))
    morada_usuario = db.Column(db.String(100))
    codigoPostal_usuario = db.Column(db.Integer)
    cidade_usuario = db.Column(db.String(30))
    direitos_admin = db.Column(db.Boolean)
    db.create_all()
    db.session.commit()
    
    
@root.route('/',methods=['GET'])
def home():

    return render_template('index2.html')

@root.route('/user-login',methods=['GET'])
def login():
    
    return render_template('login.html')

@root.route('/sign-up',methods=['GET','POST'])
def sign_up():
    if request.method =='GET':
        pass
    if request.method == 'POST':
        email = Clientes(email=request.form['email'])
        senha = Clientes(password_usuario=request.form['password_usuario'])
        nome = Clientes(nome_usuario=request.form['nome_usuario'])
        morada = Clientes(morada_usuario=request.form['morada_usuario'])
        codigoPostal = Clientes(codigoPostal_usuario=request.form['codigoPostal_usuario'])
        cidade = Clientes(cidade_usuario=request.form['cidade_usuario'])
        db.session.add(email,senha)
        db.session.add(nome,morada)
        db.session.add(codigoPostal)
        db.session.add(cidade)
        db.session.commit()
    return render_template('sign_up.html')

db.create_all()
db.session.commit()
root.run()