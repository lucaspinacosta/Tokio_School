# imports
import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


root = Flask(__name__)
root.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_informacoes.db'
db = SQLAlchemy(root)
root.config['DEBUG'] = True

# DataBase Produtos


class Produtos(db.Model):
    __tablename__ = "produto"
    numero_serie = db.Column(db.Integer, primary_key=True)
    nome_de_produto = db.Column(db.String(100))
    disponibilidade = db.Column(db.Boolean)
    quantidade = db.Column(db.Integer)
    genero_do_produto = db.Column(db.String(30))
    db.create_all()
    db.session.commit()


# DataBase Clientes
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


#Verificar Usuario
def db_verificar_email_admin(self):
        con = sqlite3.connect('database/dados_informacoes.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM admin")
        emails = cursor.fetchall()
        con.close()
        return emails

#Verificar Admin
def db_verificar_email(self):
        con = sqlite3.connect('database/dados_informacoes.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios")
        emails = cursor.fetchall()
        con.close()
        return emails


# listagem dos produtos
@root.route('/listagem-produtos', methods=['GET', 'POST'])
def criar_produtos():
    # informação apresentada ao cliente
    if request.method == 'GET':
        return render_template('lista_produtos.html')

    # Criação de produtos (Acessivel apenas pelo admin)
    if request.method == 'POST':
            produto = Produtos(nome_de_produto=request.form['nome_de_produto'])
            db.session.add(produto)
            db.session.commit()
            return render_template('lista_produtos.html')

#Home Page
@root.route('/', methods=['GET','POST'])
def home():
    log_in = False
    pass_word = False
    log_in_admin = False
    pass_word_admin=False

    if request.method == 'GET':
        return render_template('index2.html',log_in=log_in, pass_word=pass_word, log_in_admin=log_in_admin, pass_word_admin=pass_word_admin)

    if request.method =='POST':
        return redirect(url_for('index2.html',log_in=log_in))


##Pagina de LOGIN##
@root.route('/user-login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Permissoes de login
        log_in_admin = False
        pass_word_admin = False
        log_in = False
        pass_word = False
        
        #Input for log in
        verify_loggin = request.form['email_login']
        verify_pswd = request.form['password_login']

        #Base de dados User
        dados_database = "SELECT * FROM usuarios"
        verificado_email = db_verificar_email(dados_database)

        #Base de dados admin
        dados_database_admin = "SELECT * FROM admin"
        verificado_email_admin = db_verificar_email_admin(dados_database_admin)
        
        try:
            #Verificar admin
            for user in verificado_email_admin:
                if verify_loggin == user[1] and verify_pswd == user[3]:
                    log_in_admin=True  
                    pass_word_admin = True
                    return render_template('lista_produtos.html',log_in_admin=log_in_admin,pass_word_admin=pass_word_admin,user=user[1])
                    
            for user in verificado_email:
                if verify_loggin == user[0] and verify_pswd == user[3]:
                    log_in = True
                    pass_word = True
                    return render_template("index2.html",log_in=log_in,user=user)
                elif verify_loggin == user[1] and verify_pswd != user[3]:
                    print('Password errada')
                    
                elif verify_loggin != user[0]:
                    print('Email nao encontrado')

                else:
                    print('Faca o seu registo.')
            

        except:
            #Verificar buyer
            for user in verificado_email:
                if verify_loggin == user[0] and verify_pswd == user[3]:
                    log_in = True
                    pass_word = True
                    
                elif verify_loggin == user[0] and verify_pswd != user[3]:
                    print('Password errada')
                elif verify_loggin != user[0]:
                    print('Email nao encontrado')
                else:
                    print('Faca o seu registo.')
                
        finally:
                
            #Iniciar como Buyer
                if log_in == True and pass_word == True:
                    print('loggin')
                    return render_template("index2.html",log_in=log_in,user=user[2])

                #Iniciar como admin
                elif log_in_admin == True and pass_word_admin == True:
                    print('loggin admin')
                    return render_template('index2.html',log_in_admin=log_in_admin,pass_word_admin=pass_word_admin,user=user[2])
         
    if request.method == 'GET':
        return render_template('login.html')

#Pagina do carrinho
@root.route('/user-login/carrinho')
def carrinho():
    if request.method =='GET':
        return render_template('carrinho.html')

    if request.method == 'POST':
        return redirect(url_for('/user-login/carrinho'))



#Pagina Exibicao do produto detalhado
@root.route('/asus-geforce-rtx-3080-rog-strix-oc-lhr-12gb6x',methods=['GET'])
def asusgeforce_rtx3080():
    return render_template('produtos.html')


#Pagina de Registro de utilizador
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
        return redirect(url_for('login'))

db.create_all()
db.session.commit()
root.run()
