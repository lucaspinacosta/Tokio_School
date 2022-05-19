# imports
import sqlite3
from flask import Flask, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy
from sync_inventario_database import sheet_produtos


root = Flask(__name__)
root.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_informacoes2.db'
root.secret_key = "aht278945ht2h49sdfgsdfg5t9h"
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
    url_prod = db.Column(db.String)
    img_dir = db.Column(db.String)
    id_fornecedor = db.Column(db.Integer)
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

# Carrinho


# DataBase Fornecedor
class Fornecedor(db.Model):
    __tablename__ = 'Fornecedores'
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    email_fornecedor = db.Column(db.String(100))
    nome_forneceder = db.Column(db.String)
    desp_fornecedor = db.Column(db.Float)
    contacto_fornecedor = db.Column(db.Integer)
    encomenda_for = db.Column(db.String)
    db.create_all()
    db.session.commit()


# Verificar Usuario
def db_verificar_email_admin():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Admin")
    emails = cursor.fetchall()
    con.close()
    return emails

# Verificar Admin


def db_verificar_email():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    emails = cursor.fetchall()
    con.close()
    return emails

# Home Page


@root.route('/', methods=['GET', 'POST'])
def home():
    todos_os_produtos = lista_produtos()
    if request.method == 'GET':
        try:
            if session['log_in'] == True:
                return render_template('index.html', todos_os_produtos=todos_os_produtos, log_in=session['log_in'], user=session['username'])
            elif session['log_in_admin'] == True:
                return render_template('index.html', todos_os_produtos=todos_os_produtos, log_in=session['log_in_admin'], user=session['username'])
        except:
            return render_template('index.html', todos_os_produtos=todos_os_produtos, log_in=False, user=None)
    if request.method == 'POST':
        return redirect(url_for('/user-login'))


# Pagina de Registro de utilizador
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
        # Permissoes de login

        # Input for log in
        user_loggin = request.form['email_login']
        user_pswd = request.form['password_login']

        # Base de dados User
        #dados_database = "SELECT * FROM Usuarios"
        verificado_email = db_verificar_email()  # dados_database

        # Base de dados admin
        #dados_database_admin = "SELECT * FROM Admin"
        verificado_email_admin = db_verificar_email_admin()  # dados_database_admin
        todos_os_produto = lista_produtos()
        # Verificar admin

        for user in verificado_email_admin:
            if user_loggin == user[1] and user_pswd == user[3]:
                session['log_in_admin'] = True
                session['pass_word_admin'] = True
                session["user"] = user_loggin
                session["password"] = user_pswd
                session['username'] = user[2]
                print(session['username'])
                return redirect(url_for('todos_produtos',  log_in_admin=session['user'], user=session['username']))

        for user in verificado_email:
            if user_loggin == user[0] and user_pswd == user[3]:
                session['log_in'] = True
                session['pass_word'] = True
                session["user"] = user_loggin
                session["password"] = user_pswd
                session['username'] = user[2]
                print(session['username'])

            elif user_loggin == user[1] and user_pswd != user[3]:
                print('Password errada')
            elif user_loggin != user[0]:
                print('Email nao encontrado')
            else:
                print('Faca o seu registo')

        # Iniciar como Buyer

        try:
            todos_os_fornecedores = lista_fornecedores()
            todos_os_produto = lista_produtos()
            if session['log_in'] == True and session['pass_word'] == True:
                print('loggin')
                session["user"] = user_loggin
                session["password"] = user_pswd
                # session['carrinho']
                return render_template("index.html", log_in=session['log_in'], user=session['username'], todos_os_produtos=todos_os_produto, lista_fornecedores=None)
        # Iniciar como admin
        except:
            if session['log_in_admin'] == True and session['pass_word_admin'] == True:
                print('loggin admin')
                session["user"] = user_loggin
                session["password"] = user_pswd
                session['username'] = user[2]
                # session['carrinho']
                return redirect(url_for('todos_produtos', todos_os_produtos=todos_os_produto, log_in_admin=session['log_in_admin'], user=session['username'],
                                        lista_fornecedores=todos_os_fornecedores,))
            else:
                return render_template('login.html')

    if request.method == 'GET':
        return render_template('login.html')


@root.route("/logout")
def logout():
    try:
        if session['log_in'] == True:
            session.pop('log_in')
            session.pop('pass_word')
            session.pop('user')
            session.pop('username')

            session.clear()

    except:
        if session['log_in_admin'] == True:
            session.pop('log_in_admin')
            session.pop('pass_word_admin')
            session.pop('user')
            session.pop('username')

            session.clear()
    return redirect(url_for('home'))

# pagina carrinho


@root.route('/user-login/carrinho', methods=['GET', 'POST'])
def carrinho():
    if request.method == 'GET':
        return render_template('carrinho.html')

    if request.method == 'POST':
        try:
            print(session['carrinho'])
            return render_template('carrinho.html', log_in=session['log_in'], user=session['username'], carrinho=session['carrinho'])
        except:
            return render_template('carrinho.html', log_in=None, user=None)

        ##
##Products Section ##
        ##

        # Produtos em Stock

# Lista Produtos


def lista_produtos():
    try:
        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Produtos")
        produtos = cursor.fetchall()
        return produtos
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()


# Listagem de fornecedores
def lista_fornecedores():
    try:
        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Fornecedores")
        fornecedores = cursor.fetchall()
        return fornecedores
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

# Lista de Produtos


@root.route('/listagem_produto', methods=['GET', 'POST'])
def todos_produtos():
    # informação apresentada ao cliente
    todos_os_produtos = lista_produtos()
    print(lista_fornecedores())
    lista_de_fornecedores = lista_fornecedores()
    if request.method == 'GET':
        try:
            if session['log_in'] == True:
                return render_template('lista_produtos.html', todos_os_produtos=todos_os_produtos, log_in=session['log_in'], user=session['username'], lista_de_fornecedores=lista_de_fornecedores)
        except:
            if session['log_in_admin'] == True:
                return render_template('lista_produtos.html', todos_os_produtos=todos_os_produtos, log_in_admin=session['log_in_admin'], user=session['username'], lista_de_fornecedores=lista_de_fornecedores)
        else:
            return render_template('lista_produtos.html', todos_os_produtos=todos_os_produtos, log_in_admin=False, log_in=False, user=None)


# Pagina Exibicao do produto detalhado asus geforce 3080
@root.route('/listagem_produto/armazem/asus-geforce-rtx-3080-rog-strix-oc-lhr-12gb6x', methods=['GET'])
def asusgeforce_rtx3080():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 2:
            numero_serie = int(produto_select[0].value)
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Asus GeForce® RTX 3080 ROG Strix OC LHR 12GD6X.png'
            descricao_prod = {'arquitetura': ["PREPARA-TE PARA VOAR", "De cima abaixo, a ROG Strix GeForce RTX™ 3080 foi radicalmente melhorada para acomodar os novos e impressionantes chips Ampere da NVIDIA e para fornecer a próxima onda de inovação de performance gaming ao mercado. Um novo design e mais metal envolvem um conjunto de ventoinhas Axial-tech.",
                                              "A disposição uniforme das ventoinhas da última geração foi usurpada por um novo esquema de rotação e funções especializadas para as ventoinhas centrais e auxiliares. Por baixo das pás, um dissipador maior e mais impressionante está pronto para as cargas térmicas mais exigentes.", "A PCB tem alguns novos truques na manga, e até a placa traseira recebeu algumas alterações de para melhorarem a performance. Tens estado à espera das últimas e maiores novidades no design do GPU - e são estas!",
                                              "A PCB tem alguns novos truques na manga, e até a placa traseira recebeu algumas alterações de para melhorarem a performance. Tens estado à espera das últimas e maiores novidades no design do GPU - e são estas!"],
                              'aceleracao': ["MELHORAMENTOS AXIAL-TECH", "O nosso design de ventoinhas Axial-tech foi otimizado com um dissipador novo e maior, com mais aletas e área de superfície do que o da última geração. A contagem de pás foi aumentada nas três ventoinhas, com 13 na ventoinha central e 11 nas ventoinhas auxiliares.",
                                             "O anel de barreira nas ventoinhas laterais foi encolhido para permitir uma maior entrada de ar lateral e para proporcionar um melhor fluxo de ar através do conjunto de arrefecimento. As pás adicionais da ventoinha central e o anel com altura total proporcionam uma pressão estática mais forte para disparar ar diretamente para o dissipador do GPU."],
                              'extra': ["DESIGN DE 2.9 RANHURAS", " O dissipador de calor direciona o calor para os heatpipes que o transportam através de um conjunto de aletas que preenche a grande placa de 2.9 ranhuras. Aumentar o tamanho do dissipador comparativamente à última geração proporciona mais amplitude térmica para contabilizar o novo chipset de alta performance."],
                              'extra2': ["MAXCONTACT", "O encaminhamento do calor para o dissipador, que permite beneficiar do novo design das ventoinhas requer uma atenção especial. Usamos um processo de fabrico que pole a superfície do dissipador de calor para melhorar a suavidade ao nível microscópico. Sendo extra plano permite um melhor contacto com o molde para uma melhor transferência térmica."]}

            especificacoes = {'sistema_operativo': ['Processador Gráfico', 'GeForce RTX 3080'], 'Processador': ['BUS', "PCI Express 4.0 16x"],
                              'memoria_ram': ['Memória de Vídeo', '12GB GDDR6X'],
                              'armazenamento': ['Velocidade', 'OC mode: 1890 MHz (Boost Clock)', 'Gaming mode: 1860 MHz (Boost Clock)'],
                              'audio': ['CUDA cores', '8960'],
                              'ecra': ['Velocidade de Memória', '19 Gbps'],
                              'grafica': ['Interface de Memória', '384-bit'],
                              'cor': ['Suporte para multi-monitor', 'Até 4 monitores'],
                              'interface': ['Interface', '3 x DisplayPort 1.4a', '2 x HDMI 2.1']}
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto,
                               descricao_prod=descricao_prod, especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado asus geforce 3070


@root.route('/listagem_produto/armazem/Gigabyte-GeForce-RTX-3070-Aorus-Master-LHR-8GB-GD6', methods=['GET'])
def geforce_3070():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 3:
            numero_serie = produto_select[0].value
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Gigabyte GeForce® RTX 3070 Aorus Master LHR 8GB GD6.png'
            descricao_prod = {'arquitetura': ["ARQUITETURA AMPERE DA NVIDIA", "MA nova arquitetura Ampere da NVIDIA proporciona a verdadeira jogabilidade, com avançados Ray Tracing Cores da 2.ª geração e Núcleos Tensor de 3.ª geração com maior rendimento."],
                              'aceleracao': ["ACELERAÇÃO DE INTELIGÊNCIA ARTIFICIAL DLSS", "Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                              'extra': ["DIRECTX 12 ULTIMATE", "Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas."],
                              'extra2': ["RGB FUSION 2.0", "Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo': ['Processador Gráfico', 'NVIDIA® GeForce® RTX 3070'], 'Processador': ['BUS', "PCI Express 4.0 16x"],
                              'memoria_ram': ['Memória de Vídeo', '8GB GDDR6'],
                              'armazenamento': ['Velocidade', 'Base Clock: 1725 MHz', 'Boost Clock: 1845 MHz'],
                              'audio': ['CUDA cores', '5888'],
                              'ecra': ['Velocidade de Memória', '14 Gbps'],
                              'grafica': ['Interface de Memória', '256 Bits'],
                              'cor': ['Dimensões', '290 x 131 x 60 mm'],
                              'interface': ['Interface', '3 x DisplayPort 1.4a', '1 x HDMI 2.1', '1 x HDMI 2.0', 'Suporte HDCP 2.3']}
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto,
                               descricao_prod=descricao_prod, especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado Computador King


@root.route('/listagem_produto/armazem/Computador-King-Mod', methods=['GET'])
def kingModDesktop():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 4:
            numero_serie = produto_select[0].value
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Computador King Mod.png'
            descricao_prod = {'arquitetura': ["KING MOD GAMER MSI i5", "Intel Core i5 11400F | 16GB DDR4 | SSD 500GB | RTX 2060"],
                              'aceleracao': ["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!", "Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                              'extra': ["DIRECTX 12 ULTIMATE", " Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                              'extra2': ["RGB FUSION 2.0", "Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo': ['Sistema Operativo', 'Nao incluido'], 'Processador': ['Processador', "Intel Core i5 11400F (2.6GHz-4.4GHz) 12MB Socket 1200"],
                              'memoria_ram': ['Memoria Ram', 'Kit 16GB (2 x 8GB) DDR4 3200MHz'],
                              'armazenamento': ['Armazenamento', 'Disco SSD 500GB M.2 NVMe'],
                              'audio': ['Fonte de Alimentacao', 'Fonte 600W 80+ Gold'],
                              'ecra': ['Motherboard', 'Motherboard MSI H510 PRO'],
                              'grafica': ['Grafica', 'Placa Gráfica MSI GeForce® RTX 2060'],
                              'cor': ['Cor', 'Caixa ATX, Preta, Vidro Temperado'],
                              'interface': ['Interface', '1 x USB 3.2 Gen 1 Type-A', '1 x USB 3.2 Gen 1 Type-C', '2 x USB 2.0 Tipo A', '1 x HDMI 1.4', '1 x Leitor de auscultadores//micro SD card']}
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto,
                               descricao_prod=descricao_prod, especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado Asus VivoBook K513EP


@root.route('/listagem_produto/armazem/Asus-VivoBook-K513EP', methods=['GET'])
def vivoBook_K513EP():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 5:
            numero_serie = produto_select[0].value
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Asus VivoBook K513EP.png'
            descricao_prod = {'arquitetura': ["ALIMENTE A SUA PRODUTIVIDADE", "Movido pela mais recente geração de processadores Intel® Core™ com memória DDR4 e GPU NVIDIA GeForce, o VivoBook 15 oferece a performance que precisa para lidar com qualquer tarefa."],
                              'aceleracao': ["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!", "Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                              'extra': ["DIRECTX 12 ULTIMATE", " Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                              'extra2': ["RGB FUSION 2.0", "Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo': ['Sistema Operativo', 'Windows 10 Home'], 'Processador': ['Processador', "Intel® Core™ i5-1135G7, 2.4 GHz (8M Cache, até 4.2 GHz, 4 cores)"],
                              'memoria_ram': ['Memoria Ram', ' 8GB de memória RAM on board (4GB DDR4 on board + 4GB DDR4 SO-DIMM)'],
                              'armazenamento': ['Armazenamento', 'SSD de 512GB M.2 NVMe™ PCIe® 3.0'],
                              'audio': ['Audio', 'Altifalante incorporadoa  Microfone/harman/kardon embutido (Mainstream)'],
                              'ecra': ['Ecra', '15.6" FHD (1920 x 1080) 16:9, LED Backlit, IPS-level Panel, 300nits, 100% sRGB color gamut'],
                              'grafica': ['Grafica', 'Placa Gráfica NVIDIA® GeForce® MX330, com 2GB de memória VRAM GDDR5'],
                              'cor': ['Cor', 'Prateado'],
                              'interface': ['Interface', '1 x USB 3.2 Gen 1 Type-A', '1 x USB 3.2 Gen 1 Type-C', '2 x USB 2.0 Tipo A', '1 x HDMI 1.4', '1 x Leitor de auscultadores//micro SD card']}
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto,
                               descricao_prod=descricao_prod, especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado Asus VivoBook K513EP


@root.route('/listagem_produto/armazem/HP-Pavillon-x360', methods=['GET'])
def hp_pavillon_360():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 6:
            numero_serie = produto_select[0].value
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/HP Pavillon x360.png'
            descricao_prod = {'arquitetura': ["ALIMENTE A SUA PRODUTIVIDADE", "Movido pela mais recente geração de processadores Intel® Core™ com memória DDR4 e GPU NVIDIA GeForce, o VivoBook 15 oferece a performance que precisa para lidar com qualquer tarefa."],
                              'aceleracao': ["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!", "Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                              'extra': ["DIRECTX 12 ULTIMATE", " Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                              'extra2': ["RGB FUSION 2.0", "Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo': ['Sistema Operativo', 'Windows 10 Home'], 'Processador': ['Processador', "Intel® Core™ i5-1135G7, 2.4 GHz (8M Cache, até 4.2 GHz, 4 cores)"],
                              'memoria_ram': ['Memoria Ram', ' 8GB de memória RAM on board (4GB DDR4 on board + 4GB DDR4 SO-DIMM)'],
                              'armazenamento': ['Armazenamento', 'SSD de 512GB M.2 NVMe™ PCIe® 3.0'],
                              'audio': ['Audio', 'Altifalante incorporadoa  Microfone/harman/kardon embutido (Mainstream)'],
                              'ecra': ['Ecra', '15.6" FHD (1920 x 1080) 16:9, LED Backlit, IPS-level Panel, 300nits, 100% sRGB color gamut'],
                              'grafica': ['Grafica', 'Placa Gráfica NVIDIA® GeForce® MX330, com 2GB de memória VRAM GDDR5'],
                              'cor': ['Cor', 'Prateado'],
                              'interface': ['Interface', '1 x USB 3.2 Gen 1 Type-A', '1 x USB 3.2 Gen 1 Type-C', '2 x USB 2.0 Tipo A', '1 x HDMI 1.4', '1 x Leitor de auscultadores//micro SD card']}
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto,
                               descricao_prod=descricao_prod, especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado SSD Kingston NV1


@root.route('/listagem_produto/armazem/SSD-Kingston-NV1', methods=['GET'])
def ssd_kingston_nv1():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 7:
            numero_serie = produto_select[0].value
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/SSD Kingston NV1.png'
            descricao_prod = {'arquitetura': ["ALIMENTE A SUA PRODUTIVIDADE", "Movido pela mais recente geração de processadores Intel® Core™ com memória DDR4 e GPU NVIDIA GeForce, o VivoBook 15 oferece a performance que precisa para lidar com qualquer tarefa."],
                              'aceleracao': ["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!", "Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                              'extra': ["DIRECTX 12 ULTIMATE", " Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                              'extra2': ["RGB FUSION 2.0", "Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo': ['Sistema Operativo', 'Windows 10 Home'], 'Processador': ['Processador', "Intel® Core™ i5-1135G7, 2.4 GHz (8M Cache, até 4.2 GHz, 4 cores)"],
                              'memoria_ram': ['Memoria Ram', ' 8GB de memória RAM on board (4GB DDR4 on board + 4GB DDR4 SO-DIMM)'],
                              'armazenamento': ['Armazenamento', 'SSD de 512GB M.2 NVMe™ PCIe® 3.0'],
                              'audio': ['Audio', 'Altifalante incorporadoa  Microfone/harman/kardon embutido (Mainstream)'],
                              'ecra': ['Ecra', '15.6" FHD (1920 x 1080) 16:9, LED Backlit, IPS-level Panel, 300nits, 100% sRGB color gamut'],
                              'grafica': ['Grafica', 'Placa Gráfica NVIDIA® GeForce® MX330, com 2GB de memória VRAM GDDR5'],
                              'cor': ['Cor', 'Prateado'],
                              'interface': ['Interface', '1 x USB 3.2 Gen 1 Type-A', '1 x USB 3.2 Gen 1 Type-C', '2 x USB 2.0 Tipo A', '1 x HDMI 1.4', '1 x Leitor de auscultadores//micro SD card']}

    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto,
                               descricao_prod=descricao_prod, especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado Monitor Dell 27 S2721HGF Curvo FHD


@root.route('/listagem_produto/armazem/Monitor-Dell-27-S2721HGF-Curvo-FHD', methods=['GET'])
def monitor_dell_s2721hgf():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 8:
            numero_serie = produto_select[0].value
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Monitor Dell 27 S2721HGF.png'
            descricao_prod = {'arquitetura': ["ALIMENTE A SUA PRODUTIVIDADE", "Movido pela mais recente geração de processadores Intel® Core™ com memória DDR4 e GPU NVIDIA GeForce, o VivoBook 15 oferece a performance que precisa para lidar com qualquer tarefa."],
                              'aceleracao': ["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!", "Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                              'extra': ["DIRECTX 12 ULTIMATE", " Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                              'extra2': ["RGB FUSION 2.0", "Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo': ['Sistema Operativo', 'Windows 10 Home'], 'Processador': ['Processador', "Intel® Core™ i5-1135G7, 2.4 GHz (8M Cache, até 4.2 GHz, 4 cores)"],
                              'memoria_ram': ['Memoria Ram', ' 8GB de memória RAM on board (4GB DDR4 on board + 4GB DDR4 SO-DIMM)'],
                              'armazenamento': ['Armazenamento', 'SSD de 512GB M.2 NVMe™ PCIe® 3.0'],
                              'audio': ['Audio', 'Altifalante incorporadoa  Microfone/harman/kardon embutido (Mainstream)'],
                              'ecra': ['Ecra', '15.6" FHD (1920 x 1080) 16:9, LED Backlit, IPS-level Panel, 300nits, 100% sRGB color gamut'],
                              'grafica': ['Grafica', 'Placa Gráfica NVIDIA® GeForce® MX330, com 2GB de memória VRAM GDDR5'],
                              'cor': ['Cor', 'Prateado'],
                              'interface': ['Interface', '1 x USB 3.2 Gen 1 Type-A', '1 x USB 3.2 Gen 1 Type-C', '2 x USB 2.0 Tipo A', '1 x HDMI 1.4', '1 x Leitor de auscultadores//micro SD card']}
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto,
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


# Adicionar ao carrinho
@root.route('/add', methods=['POST'])
def add_product_to_cart():

    _quantity = int(request.form['quantidade'])
    _code = request.form['code']

    # validar valores recebidos
    if _quantity and _code and request.method == 'POST':
        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM Produtos WHERE numero_serie={}".format(_code))
        row = cursor.fetchone()
        itemArray = {'id': row[0], 'name': row[1], 'preco': row[5],  
                     'quantidade': _quantity, 'total': _quantity*row[5]}
        all_total_preco = 0
        all_total_quantidade = 0
        session.modified = True
        if'carrinho' in session:
            try:
                for item in session['carrinho']:
                    if itemArray['id'] == item['id']:
                        # soma produto que ja se encontra na lista
                        print('soma produto que ja se encontra na lista')
                        print(itemArray, item['id'])
                        old_quantity = item['quantidade']
                        total_quantidade = old_quantity + \
                            itemArray['quantidade']
                        item['quantidade'] = total_quantidade
                        item['total'] = total_quantidade * item['preco']

                        print('\n\n{}'.format(itemArray))
                        break
                    elif itemArray['id'] != item['id']:
                        # adiciona produto que nao se encontra na lista
                        print('adiciona produto que nao se encontra na lista')
                        print(session['carrinho'], '\n', (itemArray))

                    else:
                        print('Erro ao somar produto')
                else:
                    try:
                        session['carrinho'].append(itemArray)
                        print("Erro qualquer estupido")

                    except Exception as e:
                        session['carrinho'] = list(session['carrinho'])
                        print(e)
            finally:
                try:
                    if itemArray in session['carrinho']:
                        print("ja em lista")
                except Exception as e:
                    print(e)
                    session['carrinho'].append(itemArray)

        else:
            session['carrinho'] = []
            session['carrinho'].append(itemArray)

        for item in session['carrinho']:
            quantidade_individual = item['quantidade']
            preco_total = item['total']
            all_total_quantidade += quantidade_individual
            all_total_preco += preco_total


        session['all_total_quantidade'] = all_total_quantidade
        session['all_total_preco'] = all_total_preco
        print(session['carrinho'])

        cursor.close()
        con.close()

        return redirect(url_for('.carrinho'))
    else:
        return 'erro ao adicionar'

# Limpar Carrinho


@root.route('/empty')
def empty_cart():
    try:
        del(session['carrinho'])
        del(session['all_total_preco'])
        del(session['all_total_quantidade'])
        print(session['carrinho'])
        print(session)
        return redirect(url_for('.carrinho'))

    except Exception as e:
        print(e)
    finally:
        return redirect(url_for('.carrinho'))
# Remover item do carrinho


@root.route('/delete/<string:code>')
def delete_product(code):
    all_total_preco = 0
    all_total_quantidade = 0
    session.modified = True
    for item in session['carrinho']:
        if item['id'] == code:
            session['carrinho'].pop(item[0], None)
            if 'carrinho' in session:
                for key in session['carrinho']:
                    individual_quantidade = int(key['quantidade'])
                    individual_preco = float(key['total'])
                    all_total_quantidade = all_total_quantidade - individual_quantidade
                    all_total_preco = all_total_preco - \
                        (individual_preco*individual_quantidade)
    if all_total_quantidade == 0:
        session['carrinho'] = []
    else:
        session['all_total_quantidade'] = all_total_quantidade
        session['all_total_preco'] = all_total_preco
    # return redirect('/')
    return redirect(url_for('.carrinho'))

#Finalizar Compras
@root.route('/pagamento')
def finalizar_compra():
   carrinho = session['carrinho']
   con = sqlite3.connect('database/dados_informacoes2.db')
   cursor = con.cursor()
   for item in session['carrinho']:
       print(item)
       cursor.execute("SELECT * FROM Produtos WHERE numero_serie={}".format(item['id']))
       row = cursor.fetchone() 
       print(row)





if __name__ == "__main__":
    root.run()
    db.create_all()
    db.session.commit()
