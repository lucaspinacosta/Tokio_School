
import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


root = Flask(__name__)
root.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_informacoes.db'
db = SQLAlchemy(root)
root.config['DEBUG'] = True


class Produtos(db.Model):
    __tablename__ = "produto"
    numero_serie = db.Column(db.Integer, primary_key=True)
    nome_de_produto = db.Column(db.String(100))
    disponibilidade = db.Column(db.Boolean)
    quantidade = db.Column(db.Integer)
    genero_do_produto = db.Column(db.String(30))
    db.create_all()
    db.session.commit()


@root.route('/criar-produtos', methods=['GET', 'POST'])
def criar_produtos():
    if request.method == 'GET':
        return redirect(url_for('home'))
    if request.method == 'POST':
        produto = Produtos(nome_de_produto=request.form['nome_de_produto'])
        db.session.add(produto)
        db.session.commit()
        pass
    return redirect(url_for('criar_produtos'))


class Clientes(db.Model):
    __tablename__ = 'usuarios'
    email = db.Column(db.String(128))
    numero_ID = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(60))
    password_usuario = db.Column(db.String(12))
    morada_usuario = db.Column(db.String(100))
    codigoPostal_usuario = db.Column(db.Integer)
    cidade_usuario = db.Column(db.String(30))
    direitos_admin = db.Column(db.Boolean)
    db.create_all()
    db.session.commit()


def db_consulta(self, consulta, parametros=()):
    with sqlite3.connect(self.db) as con:
        cursor = con.cursor()
        resultados = cursor.execute(consulta, parametros)
        con.commit()
        return resultados


@root.route('/', methods=['GET'])
def home():

    return render_template('index2.html')

##Pagina de LOGIN##


@root.route('/user-login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'POST':
            log_in = False
            pass_word = False
            verify_loggin = request.form['email_login']
            verify_password = request.form['password_login']
            dados_database = "SELECT email FROM usuarios"
            pass_database = "SELECT password FROM usuarios"
            verificado_email = db_consulta(dados_database)
            verificado_pass = db_consulta(pass_database)
            for user in verificado_email:
                if user == verify_loggin:
                    log_in = True
                else:
                    print('Email nao encontrado')
                
            for pswd in verificado_pass:
                if pswd == verify_password:
                    pass_word = True
                else:
                    print('pass errada')
            if log_in == True and pass_word == True:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    except TypeError as e:
        if e == TypeError:
            print('favor introduzir dados')
            return redirect(url_for('sign-up'))

    if request.method == 'GET':
        return render_template('login.html')
    return render_template('login.html')


@root.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')

    if request.method == 'POST':
        email = Clientes(email=request.form['email_signup'], password_usuario=request.form['password_signup'],
                         nome_usuario=request.form['nome_usuario_signup'], morada_usuario=request.form['morada_usuario_signup'],
                         codigoPostal_usuario=request.form[
                             'codigoPostal_usuario_signup'], cidade_usuario=request.form['cidade_usuario_signup'],
                         direitos_admin=False)
        db.session.add(email)
        db.session.commit()
        print(email)
        return redirect(url_for('login'))

    return render_template('sign_up.html')


db.create_all()
db.session.commit()
root.run()
