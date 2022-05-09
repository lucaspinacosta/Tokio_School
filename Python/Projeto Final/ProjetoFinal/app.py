# imports
import sqlite3
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import  sync_inventario_database

root = Flask(__name__)
root.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_informacoes2.db'
db = SQLAlchemy(root)
root.config['DEBUG'] = True

# DataBase Produtos


class Produtos(db.Model):
    __tablename__ = "Produtos"
    numero_serie = db.Column(db.Integer, primary_key=True)
    nome_de_produto = db.Column(db.String(100))
    em_armazem = db.Column(db.Integer)
    vendidos = db.Column(db.Integer)
    preco_fornecedor = db.Column(db.Float)
    valor_venda = db.Column(db.Float)
    prateleira = db.Column(db.String(3))
    descricao = db.Column(db.String)
    fornecedor = db.Column(db.Integer)
    db.create_all()
    db.session.commit()


# DataBase Clientes
class Clientes(db.Model):
    __tablename__ = 'Usuarios'
    email = db.Column(db.String(128))
    numero_ID = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(60))
    password_user = db.Column(db.String(12))
    morada_user = db.Column(db.String(100))
    codigo_postal = db.Column(db.Integer)
    cidade_destino = db.Column(db.String(30))
    db.create_all()
    db.session.commit()

#DataBase Fornecedor
class Fornecedor(db.Model):
    __tablename__ = 'Fornecedores'
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    email_fornecedor = db.Column(db.String(100))
    nome_forneceder = db.Column(db.String)
    desp_fornecedor = db.Column(db.Float)
    contacto_fornecedor = db.Column(db.Integer)
    db.create_all()
    db.session.commit()


#Verificar Usuario
def db_verificar_email_admin():
        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Admin")
        emails = cursor.fetchall()
        con.close()
        return emails

#Verificar Admin
def db_verificar_email():
        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        emails = cursor.fetchall()
        con.close()
        return emails



#Home Page
@root.route('/', methods=['GET','POST'])
def home():
    log_in = False
    pass_word = False
    log_in_admin = False
    pass_word_admin=False

    if request.method == 'GET':
        return render_template('index.html',log_in=log_in, pass_word=pass_word, log_in_admin=log_in_admin, pass_word_admin=pass_word_admin)

    if request.method =='POST':
        return redirect(url_for('index.html',log_in=log_in))

#Pagina de Registro de utilizador
@root.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')

    if request.method == 'POST':
        email = Clientes(email=request.form['email_signup'], password_user=request.form['password_signup'],
                         nome_usuario=request.form['nome_usuario_signup'], morada_user=request.form['morada_usuario_signup'],
                         codigo_postal=request.form[
                             'codigoPostal_usuario_signup'], cidade_destino=request.form['cidade_usuario_signup'],
                        )
        db.session.add(email)
        db.session.commit()
        return redirect(url_for('login'))

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
        #dados_database = "SELECT * FROM Usuarios"
        verificado_email = db_verificar_email()#dados_database

        #Base de dados admin
        #dados_database_admin = "SELECT * FROM Admin"
        verificado_email_admin = db_verificar_email_admin()#dados_database_admin
        
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
                    return render_template("index.html",log_in=log_in,user=user)
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
                    return render_template("index.html",log_in=log_in,user=user[2])

                #Iniciar como admin
                elif log_in_admin == True and pass_word_admin == True:
                    print('loggin admin')
                    return render_template('index.html',log_in_admin=log_in_admin,pass_word_admin=pass_word_admin,user=user[2])
         
    if request.method == 'GET':
        return render_template('login.html')

#Pagina do carrinho
@root.route('/user-login/carrinho')
def carrinho():
    if request.method =='GET':
        return render_template('index.html')

    if request.method == 'POST':
        return redirect(url_for('/user-login/carrinho'))

#Listagem dos produtos
@root.route('/listagem-produtos', methods=['GET', 'POST'])
def criar_produtos():
    # informação apresentada ao cliente
    if request.method == 'GET':
        return render_template('lista_produtos.html')

    # Criação de produtos (Acessivel apenas pelo admin)
    if request.method == 'POST':
        return render_template('lista_produtos.html')


#Pagina Exibicao do produto detalhado
@root.route('/listagem_produto/asus-geforce-rtx-3080-rog-strix-oc-lhr-12gb6x',methods=['GET'])
def asusgeforce_rtx3080():
    #request_nome = request.form['nome_produto']
    #request_valor = request.form['valor']
    #request_quantida = request.form['em_armazem']
    #request_descricao = request.form['descricao']

    for produto_select in sync_inventario_database.sheet_produtos.rows:
            if produto_select[0].value == 2:
                asusgeforce_rtx3080 = produto_select[1].value
                asusgeforce_rtx3080_price =produto_select[5].value

                return render_template('produtos.html',aasusgeforce_rtx3080 = asusgeforce_rtx3080, 
                asusgeforce_rtx3080_price=asusgeforce_rtx3080_price)


db.create_all()
db.session.commit()
root.run()

