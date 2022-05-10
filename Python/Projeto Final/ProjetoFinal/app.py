# imports
import sqlite3
from colorama import Cursor
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sync_inventario_database import sheet_produtos

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

# DataBase Fornecedor


class Fornecedor(db.Model):
    __tablename__ = 'Fornecedores'
    id_fornecedor = db.Column(db.Integer, primary_key=True)
    email_fornecedor = db.Column(db.String(100))
    nome_forneceder = db.Column(db.String)
    desp_fornecedor = db.Column(db.Float)
    contacto_fornecedor = db.Column(db.Integer)
    db.create_all()
    db.session.commit()

#Produtos em Stock
def lista_produtos():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos")
    produtos = cursor.fetchall()
    return produtos


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
        return render_template('index.html',todos_os_produtos=todos_os_produtos)

    if request.method == 'POST':
        return redirect(url_for('/user-login'))

# Home Page


@root.route('/home', methods=['GET', 'POST'])
def homee():
    if request.method == 'GET':
        return redirect(url_for('home'))

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
        log_in_admin = False
        pass_word_admin = False
        log_in = False
        pass_word = False

        # Input for log in
        verify_loggin = request.form['email_login']
        verify_pswd = request.form['password_login']

        # Base de dados User
        #dados_database = "SELECT * FROM Usuarios"
        verificado_email = db_verificar_email()  # dados_database

        # Base de dados admin
        #dados_database_admin = "SELECT * FROM Admin"
        verificado_email_admin = db_verificar_email_admin()  # dados_database_admin

        try:
            # Verificar admin
            for user in verificado_email_admin:
                if verify_loggin == user[1] and verify_pswd == user[3]:
                    log_in_admin = True
                    pass_word_admin = True
                    return render_template('lista_produtos.html', log_in_admin=log_in_admin, pass_word_admin=pass_word_admin, user=user[1])

            for user in verificado_email:
                if verify_loggin == user[0] and verify_pswd == user[3]:
                    log_in = True
                    pass_word = True
                    return render_template("index.html", log_in=log_in, user=user)
                elif verify_loggin == user[1] and verify_pswd != user[3]:
                    print('Password errada')

                elif verify_loggin != user[0]:
                    print('Email nao encontrado')

                else:
                    print('Faca o seu registo.')

        except:
            # Verificar buyer
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

            # Iniciar como Buyer
            if log_in == True and pass_word == True:
                print('loggin')
                return render_template("index.html", log_in=log_in, user=user[2])

            # Iniciar como admin
            elif log_in_admin == True and pass_word_admin == True:
                print('loggin admin')
                return render_template('index.html', log_in_admin=log_in_admin, pass_word_admin=pass_word_admin, user=user[2])

    if request.method == 'GET':
        return render_template('login.html')

# Pagina do carrinho
@root.route('/user-login/carrinho')
def carrinho():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':
        return redirect(url_for('/user-login/carrinho'))


# Pagina do carrinho
@root.route('/admin')
def gestao_admin():
    if request.method == 'GET':
        return render_template('lista_produtos.html')

    if request.method == 'POST':
        return redirect(url_for('/admin'))
        ##
##Products Section ##
        ##


# Listagem dos produtos
@root.route('/listagem_produto', methods=['GET', 'POST'])
def criar_produtos():
    # informação apresentada ao cliente
    if request.method == 'GET':
        return render_template('lista_produtos.html')

    # Criação de produtos (Acessivel apenas pelo admin)
    if request.method == 'POST':
        return render_template('lista_produtos.html')


# Showcase Template
@root.route('/listagem_produto/armazem', methods=['GET'])
def showProdutos():
    return render_template('produtos.html')


# Pagina Exibicao do produto detalhado asus geforce 3080
@root.route('/listagem_produto/armazem/asus-geforce-rtx-3080-rog-strix-oc-lhr-12gb6x', methods=['GET'])
def asusgeforce_rtx3080():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 2:
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Asus GeForce® RTX 3080 ROG Strix OC LHR 12GD6X.png'
            descricao_prod ={'arquitetura':["PREPARA-TE PARA VOAR", "De cima abaixo, a ROG Strix GeForce RTX™ 3080 foi radicalmente melhorada para acomodar os novos e impressionantes chips Ampere da NVIDIA e para fornecer a próxima onda de inovação de performance gaming ao mercado. Um novo design e mais metal envolvem um conjunto de ventoinhas Axial-tech.",
            "A disposição uniforme das ventoinhas da última geração foi usurpada por um novo esquema de rotação e funções especializadas para as ventoinhas centrais e auxiliares. Por baixo das pás, um dissipador maior e mais impressionante está pronto para as cargas térmicas mais exigentes.","A PCB tem alguns novos truques na manga, e até a placa traseira recebeu algumas alterações de para melhorarem a performance. Tens estado à espera das últimas e maiores novidades no design do GPU - e são estas!",
            "A PCB tem alguns novos truques na manga, e até a placa traseira recebeu algumas alterações de para melhorarem a performance. Tens estado à espera das últimas e maiores novidades no design do GPU - e são estas!"],
                'aceleracao':["MELHORAMENTOS AXIAL-TECH","O nosso design de ventoinhas Axial-tech foi otimizado com um dissipador novo e maior, com mais aletas e área de superfície do que o da última geração. A contagem de pás foi aumentada nas três ventoinhas, com 13 na ventoinha central e 11 nas ventoinhas auxiliares.",
                "O anel de barreira nas ventoinhas laterais foi encolhido para permitir uma maior entrada de ar lateral e para proporcionar um melhor fluxo de ar através do conjunto de arrefecimento. As pás adicionais da ventoinha central e o anel com altura total proporcionam uma pressão estática mais forte para disparar ar diretamente para o dissipador do GPU."],
                'extra':["DESIGN DE 2.9 RANHURAS"," O dissipador de calor direciona o calor para os heatpipes que o transportam através de um conjunto de aletas que preenche a grande placa de 2.9 ranhuras. Aumentar o tamanho do dissipador comparativamente à última geração proporciona mais amplitude térmica para contabilizar o novo chipset de alta performance."],
                'extra2': ["MAXCONTACT","O encaminhamento do calor para o dissipador, que permite beneficiar do novo design das ventoinhas requer uma atenção especial. Usamos um processo de fabrico que pole a superfície do dissipador de calor para melhorar a suavidade ao nível microscópico. Sendo extra plano permite um melhor contacto com o molde para uma melhor transferência térmica."]}

            especificacoes = {'sistema_operativo':['Processador Gráfico','GeForce RTX 3080'],'Processador':['BUS',"PCI Express 4.0 16x"],
            'memoria_ram':['Memória de Vídeo','12GB GDDR6X'],
            'armazenamento':['Velocidade','OC mode: 1890 MHz (Boost Clock)','Gaming mode: 1860 MHz (Boost Clock)'],
            'audio':['CUDA cores','8960'],
            'ecra':['Velocidade de Memória','19 Gbps'],
            'grafica':['Interface de Memória','384-bit'],
            'cor':['Suporte para multi-monitor','Até 4 monitores'],
            'interface':['Interface','3 x DisplayPort 1.4a','2 x HDMI 2.1']}
            return render_template('produtos.html', nome_produto=nome_produto,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod,especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado asus geforce 3070
@root.route('/listagem_produto/armazem/Gigabyte-GeForce-RTX-3070-Aorus-Master-LHR-8GB-GD6', methods=['GET'])
def geforce_3070():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 3:
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Gigabyte GeForce® RTX 3070 Aorus Master LHR 8GB GD6.png'
            descricao_prod ={'arquitetura':["ARQUITETURA AMPERE DA NVIDIA","MA nova arquitetura Ampere da NVIDIA proporciona a verdadeira jogabilidade, com avançados Ray Tracing Cores da 2.ª geração e Núcleos Tensor de 3.ª geração com maior rendimento."],
                'aceleracao':["ACELERAÇÃO DE INTELIGÊNCIA ARTIFICIAL DLSS","Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                'extra':["DIRECTX 12 ULTIMATE", "Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas."],
                'extra2':["RGB FUSION 2.0","Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo':['Processador Gráfico','NVIDIA® GeForce® RTX 3070'],'Processador':['BUS',"PCI Express 4.0 16x"],
            'memoria_ram':['Memória de Vídeo','8GB GDDR6'],
            'armazenamento':['Velocidade','Base Clock: 1725 MHz','Boost Clock: 1845 MHz'],
            'audio':['CUDA cores','5888'],
            'ecra':['Velocidade de Memória','14 Gbps'],
            'grafica':['Interface de Memória','256 Bits'],
            'cor':['Dimensões','290 x 131 x 60 mm'],
            'interface':['Interface','3 x DisplayPort 1.4a','1 x HDMI 2.1','1 x HDMI 2.0','Suporte HDCP 2.3']}
            return render_template('produtos.html', nome_produto=nome_produto,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                   descricao_prod=descricao_prod,especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado Computador King
@root.route('/listagem_produto/armazem/Computador-King-Mod', methods=['GET'])
def kingModDesktop():
    for produto_select in sheet_produtos.rows:
            if produto_select[0].value == 4:
                nome_produto = produto_select[1].value
                preco_produto = produto_select[5].value
                imagem_produto = '/static/produtos/Computador King Mod.png'
                descricao_prod ={'arquitetura':["KING MOD GAMER MSI i5", "Intel Core i5 11400F | 16GB DDR4 | SSD 500GB | RTX 2060"],
                'aceleracao':["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!","Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                'extra':["DIRECTX 12 ULTIMATE"," Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                'extra2': ["RGB FUSION 2.0","Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

                especificacoes = {'sistema_operativo':['Sistema Operativo','Nao incluido'],'Processador':['Processador',"Intel Core i5 11400F (2.6GHz-4.4GHz) 12MB Socket 1200"],
            'memoria_ram':['Memoria Ram','Kit 16GB (2 x 8GB) DDR4 3200MHz'],
            'armazenamento':['Armazenamento','Disco SSD 500GB M.2 NVMe'],
            'audio':['Fonte de Alimentacao','Fonte 600W 80+ Gold'],
            'ecra':['Motherboard','Motherboard MSI H510 PRO'],
            'grafica':['Grafica','Placa Gráfica MSI GeForce® RTX 2060'],
            'cor':['Cor','Caixa ATX, Preta, Vidro Temperado'],
            'interface':['Interface','1 x USB 3.2 Gen 1 Type-A','1 x USB 3.2 Gen 1 Type-C','2 x USB 2.0 Tipo A','1 x HDMI 1.4','1 x Leitor de auscultadores//micro SD card']}
                return render_template('produtos.html', nome_produto=nome_produto,
                                    preco_produto=preco_produto, imagem_produto=imagem_produto,
                                    descricao_prod=descricao_prod,especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado Asus VivoBook K513EP
@root.route('/listagem_produto/armazem/Asus-VivoBook-K513EP', methods=['GET'])
def vivoBook_K513EP():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 5:
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/Asus VivoBook K513EP.png'
            descricao_prod ={'arquitetura':["ALIMENTE A SUA PRODUTIVIDADE", "Movido pela mais recente geração de processadores Intel® Core™ com memória DDR4 e GPU NVIDIA GeForce, o VivoBook 15 oferece a performance que precisa para lidar com qualquer tarefa."],
                'aceleracao':["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!","Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                'extra':["DIRECTX 12 ULTIMATE"," Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                'extra2': ["RGB FUSION 2.0","Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo':['Sistema Operativo','Windows 10 Home'],'Processador':['Processador',"Intel® Core™ i5-1135G7, 2.4 GHz (8M Cache, até 4.2 GHz, 4 cores)"],
            'memoria_ram':['Memoria Ram',' 8GB de memória RAM on board (4GB DDR4 on board + 4GB DDR4 SO-DIMM)'],
            'armazenamento':['Armazenamento','SSD de 512GB M.2 NVMe™ PCIe® 3.0'],
            'audio':['Audio','Altifalante incorporadoa  Microfone/harman/kardon embutido (Mainstream)'],
            'ecra':['Ecra','15.6" FHD (1920 x 1080) 16:9, LED Backlit, IPS-level Panel, 300nits, 100% sRGB color gamut'],
            'grafica':['Grafica','Placa Gráfica NVIDIA® GeForce® MX330, com 2GB de memória VRAM GDDR5'],
            'cor':['Cor','Prateado'],
            'interface':['Interface','1 x USB 3.2 Gen 1 Type-A','1 x USB 3.2 Gen 1 Type-C','2 x USB 2.0 Tipo A','1 x HDMI 1.4','1 x Leitor de auscultadores//micro SD card']}
            return render_template('produtos.html', nome_produto=nome_produto,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                    descricao_prod=descricao_prod,especificacoes=especificacoes)

# Pagina Exibicao do produto detalhado Asus VivoBook K513EP
@root.route('/listagem_produto/armazem/HP-Pavillon-x360', methods=['GET'])
def hp_pavillon_360():
    for produto_select in sheet_produtos.rows:
        if produto_select[0].value == 6:
            nome_produto = produto_select[1].value
            preco_produto = produto_select[5].value
            imagem_produto = '/static/produtos/HP Pavillon x360.png'
            descricao_prod ={'arquitetura':["ALIMENTE A SUA PRODUTIVIDADE", "Movido pela mais recente geração de processadores Intel® Core™ com memória DDR4 e GPU NVIDIA GeForce, o VivoBook 15 oferece a performance que precisa para lidar com qualquer tarefa."],
                'aceleracao':["O MELHOR AUMENTO DE PERFORMANCE - ATÉ 40%!","Utilizando os Núcleos Tensor de processamento de Inteligência Artificial dedicados da GeForce RTX, NVIDIA DLSS é uma tecnologia inovadora em termos de renderização de Inteligência artificial que aumenta a velocidade de fotogramas com uma qualidade de imagem rigorosa. Isto oferece-lhe a capacidade de desempenho necessária para poder aumentar as definições e resoluções de modo a obteres uma experiência visual incrível. A revolução da Inteligência Artificial chegou ao gaming."],
                'extra':["DIRECTX 12 ULTIMATE"," Os programadores podem agora acrescentar ainda mais efeitos gráficos espetaculares aos jogos para PC executáveis no Microsoft Windows. As placas gráficas GeForce RTX oferecem funcionalidades DX12 avançadas, como o ray tracing e o sombreamento de frequência variável, criando jogos dotados de efeitos visuais ultrarrealistas e velocidades de fotogramas ainda mais rápidas. "],
                'extra2': ["RGB FUSION 2.0","Com 16,7M opções de cor personalizáveis e numerosos efeitos de iluminação, pode escolher efeitos de iluminação ou sincronizar com outros dispositivos AORUS."]}

            especificacoes = {'sistema_operativo':['Sistema Operativo','Windows 10 Home'],'Processador':['Processador',"Intel® Core™ i5-1135G7, 2.4 GHz (8M Cache, até 4.2 GHz, 4 cores)"],
            'memoria_ram':['Memoria Ram',' 8GB de memória RAM on board (4GB DDR4 on board + 4GB DDR4 SO-DIMM)'],
            'armazenamento':['Armazenamento','SSD de 512GB M.2 NVMe™ PCIe® 3.0'],
            'audio':['Audio','Altifalante incorporadoa  Microfone/harman/kardon embutido (Mainstream)'],
            'ecra':['Ecra','15.6" FHD (1920 x 1080) 16:9, LED Backlit, IPS-level Panel, 300nits, 100% sRGB color gamut'],
            'grafica':['Grafica','Placa Gráfica NVIDIA® GeForce® MX330, com 2GB de memória VRAM GDDR5'],
            'cor':['Cor','Prateado'],
            'interface':['Interface','1 x USB 3.2 Gen 1 Type-A','1 x USB 3.2 Gen 1 Type-C','2 x USB 2.0 Tipo A','1 x HDMI 1.4','1 x Leitor de auscultadores//micro SD card']}
            return render_template('produtos.html', nome_produto=nome_produto,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto,
                                    descricao_prod=descricao_prod,especificacoes=especificacoes)


db.create_all()
db.session.commit()
root.run()
