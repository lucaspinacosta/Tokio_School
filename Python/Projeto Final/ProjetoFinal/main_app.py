# imports
from datetime import date
from glob import glob
import sqlite3
import json
import os
import random
import pathlib
import time
import win32com.client
import pythoncom
from openpyxl import Workbook
from openpyxl.styles import Font
from flask import Flask, redirect, render_template, request, url_for, session
from flask_sqlalchemy import SQLAlchemy


root = Flask(__name__)
root.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/dados_informacoes2.db'
root.secret_key = "aht278945ht2h49sdfgsdfg5t9h"
db = SQLAlchemy(root)
root.config['DEBUG'] = True


# DataBase Produtos
class Produtos(db.Model):
    __tablename__ = "Produtos"
    numero_serie = db.Column(db.Integer, primary_key=True)
    nome_produto = db.Column(db.String(100))
    em_armazem = db.Column(db.Integer)
    vendidos = db.Column(db.Integer)
    preco_fornecedor = db.Column(db.Float)
    valor_venda = db.Column(db.Float)
    prateleira = db.Column(db.String(3))
    fornecedor = db.Column(db.Integer)
    quantidade_encomenda = db.Column(db.Integer)
    id_fornecedor = db.Column(db.Integer)
    especificacoes = db.Column(db.String)
    iva = db.Column(db.Integer)
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
    nome_fornecedor = db.Column(db.String(60))
    desp_fornecedor = db.Column(db.Float)
    lucro_fornecedor = db.Column(db.Float)
    contacto = db.Column(db.Integer)
    numero_IF = db.Column(db.Integer)
    senha_login = db.Column(db.String)
    desconto_fornecedor = db.Column(db.Integer)

    db.create_all()
    db.session.commit()



# Verificar Admin
def db_verificar_email_admin():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Admin")
    emails = cursor.fetchall()
    con.close()
    return emails


# Verificar Usuario
def db_verificar_email():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    emails = cursor.fetchall()
    con.close()
    return emails


# Verificar Fornecedor
def db_verificar_fornecedor():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Fornecedores")
    emails = cursor.fetchall()
    con.close()
    return emails


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


def fatura(lista_compras):
    # futuramente adicionar forma de adicionar cada nova fatura ao prorio excel do usuario
    diretorio = "database/faturas_clientes/"+session['user']+"/"
    path = os.path.join(diretorio)

    try:
        os.mkdir(path)
    except Exception as e:
        print(e)
    wb = Workbook()
    wb['Sheet'].title = 'Fatura'
    print(wb.sheetnames)
    ws = wb.active
    fontStyle = Font(size="9")
    remetente_fatura = session['username'] + \
        '_'+str(random.randint(0, 999999999))
    
    ws['C7'] = 'Nome Produto'
    ws['D7'] = 'Quantidade'
    ws['E7'] = 'Valor Unidade'
    ws['F7'] = 'Valor Total'
    ws['G7'] = 'IVA'
    ws.append(["", "", "", "", "", ""])
    for item in lista_compras:
        print(item)
        ws.append(['','', item['name'], item['quantidade'], "{:.2f}€".format(
            item['preco']), "{:.2f}€".format(item['total']), str(item['iva'])+'%'])
    ws.append(['',"", "", "", "", ""])
    ws.append(['','', 'Total', session['all_total_quantidade'], '', "{:.2f}€".format(
        session['all_total_preco']), ""])
    # incluir datetime na fatura!!
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Get the column name
        for cell in col:
            cell.font = fontStyle
            try:  # Necessary to avoid error on empty cells
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length)*0.80
        ws.column_dimensions[column].width = adjusted_width
    
    ws['A1'] = 'Numero da Fatura'
    ws['A2'] = remetente_fatura
    ws['H1'] = time.strftime('%X')
    date.today()
    ws['H2'] = time.strftime('%x')

    wb.save(diretorio+remetente_fatura+'.xlsx')
    wb.close()

    excel_file = diretorio+remetente_fatura+".xlsx"
    pdf_file = diretorio+remetente_fatura+".pdf"

    excel_path = str(pathlib.Path.cwd() / excel_file)
    pdf_path = str(pathlib.Path.cwd() / pdf_file)
    excel = win32com.client.Dispatch(
        "Excel.Application", pythoncom.CoInitialize())
    excel.Visible = False
    try:
        wb = excel.Workbooks.Open(excel_path)
        ws = wb.Worksheets[0]
        wb.SaveAs(pdf_path, FileFormat=57)
        wb.SaveAs()
        
    except Exception as e:
        print('Fail')
        print(e)
    else:
        print('Sucess')
    finally:
        excel.Quit()

    

# Apresentacao das faturas

def show_faturas(user_email):
    #Cria uma lista com os paths das faturas do cliente X 
    source_faturas = "database/faturas_clientes/"+session['user']+"/"
    faturas = []
    for file in glob(source_faturas+"*"+".pdf"):
        #faturas.append(file)
        tic_c = os.path.getctime(file)
        time_c = time.ctime(tic_c)
        faturas.append({"path":file,"data_c":time_c})

    return faturas


# criacao de Produto


@root.route('/admin/criar-produto', methods=['GET', 'POST'])
def criar_produto():
    if session['log_in_admin'] == True and request.method == 'POST':

        # É preciso separar as descriçoes do request e depois aplicar a database \\reminder\\
        # Alterar a forma de pedir o fornecedor do produto
        especificacoes = {"especificacoes": {'sistema_operativo': [request.form['sistema_titulo'], request.form['sistema_informacao']],
                                             'memoria_ram': [request.form['titulo_ram'], request.form['informacao_ram']],
                                             'Processador': [request.form['titulo_processador'], request.form['informacao_processador']],
                                             'armazenamento': [request.form['titulo_armazenamento'], request.form['informacao_armazenamento']],
                                             'audio': [request.form['titulo_audio'], request.form['informacao_audio']],
                                             'ecra': [request.form['titulo_ecra'], request.form['informacao_ecra']],
                                             'grafica': [request.form['titulo_grafica'], request.form['informacao_grafica']],
                                             'cor': [request.form['titulo_cor'], request.form['informacao_cor']],
                                             'interface': [request.form['titulo_interface'], request.form['informacao_interface1'],
                                                           request.form['informacao_interface2'], request.form['informacao_interface3'],
                                                           request.form['informacao_interface4']]}}
        diretorio = "static/produtos/"+request.form['nome_produto']

        path = os.path.join(diretorio)
        try:
            os.mkdir(path)
        except Exception as e:
            print(e)

        # Adicionar forma de criar pasta caso ainda nao exista
        with open("static/produtos/"+request.form['nome_produto']+"/espec_produtos.json", "w", encoding='utf-8') as outfile:
            json.dump(especificacoes, outfile)

        descricoes_prod = {"descricao_1": [request.form['arquitetura_titulo'], request.form['arquitetura_descricao']],
                           "descricao_2": [request.form['aceleracao_titulo'], request.form['aceleracao_descricao']],
                           "descricao_3": [request.form['extra_titulo'], request.form['extra_descricao']],
                           "descricao_4": [request.form['extra2_titulo'], request.form['extra2_descricao']],
                           "descricao_5": [request.form['extra3_titulo'], request.form['extra3_descricao']],
                           "descricao_6": [request.form['extra4_titulo'], request.form['extra4_descricao']]}

        def write_json(new_descricao, new_img_path, filename="static/produtos/"+request.form['nome_produto']+"/espec_produtos.json"):
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data['descricoes'] = new_descricao
                file_data['img_path'] = diretorio + "/" + new_img_path
                file.seek(0)
                json.dump(file_data, file, indent=6)
        write_json(descricoes_prod, request.form['myfile'])

        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute("SELECT id_fornecedor FROM Fornecedores WHERE nome_fornecedor = ?", (request.form['nome_fornecedor'],))
        id_fornecedor = cursor.fetchone()
        con.close()


        # apagar  as colunas descricoes, url request e img request da database
        produto = Produtos(nome_produto=request.form['nome_produto'], em_armazem=0, vendidos=0,
                           preco_fornecedor=request.form['preco_fornecedor'], valor_venda=request.form['valor_venda'],
                           prateleira=request.form['Prateleira'], fornecedor=request.form['nome_fornecedor'],
                           especificacoes="static/produtos/" +
                           request.form['nome_produto']+"/espec_produtos.json",
                           quantidade_encomenda=0, id_fornecedor=id_fornecedor[0], iva = request.form['iva'])
        db.session.add(produto)
        db.session.commit()
        return redirect(url_for('.criar_produto'))

    elif session['log_in_admin'] == True and request.method == 'GET':
        fornecedor = lista_fornecedores()
        return render_template('criar_produtos.html',fornecedores = fornecedor)
    else:
        return redirect(url_for('.home'))

# Editar produtos


@root.route('/admin/editar/<code_edit>', methods=['GET', 'POST'])
def editar_prod(code_edit):

    if session['log_in_admin'] == True and request.method == 'POST':
        modificar_produro = False
        query = "UPDATE Produtos SET nome_produto =?, valor_venda=?,preco_fornecedor=? WHERE numero_serie =?"
        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM Produtos WHERE numero_serie=?", (code_edit,))
        produto_em_edicao = cursor.fetchone()
        get_especificacoes = open(produto_em_edicao[10], encoding="utf8")
        especificacoes = json.load(get_especificacoes)

        #Guardamos as informacoes antigas caso nao sejam alteradas poderemos reutiliza-las
        old_nome = produto_em_edicao[1]
        old_preco = produto_em_edicao[5]
        old_preco_fornecedor = produto_em_edicao[4]
        old_img_path = especificacoes['img_path']
        # Terminar a edicao dos produtos
        novo_nome = request.form['novo_nome']
        novo_preco = request.form['novo_preco']
        novo_preco_fornecedor = request.form['novo_preco_fornecedor']
        nova_img_path = request.form['nova_img_path']
        
        #Verifica se cada parametro foi alterado e guarda as novas alteracoes
        if novo_nome != '' and novo_preco != '' and novo_preco_fornecedor != '':
            parametros = (novo_nome, novo_preco,
                          novo_preco_fornecedor, code_edit)
            os.rename(os.path.join("static/produtos/",old_nome),
                      os.path.join("static/produtos/",novo_nome))
            update_path = "UPDATE Produtos SET especificacoes=? where numero_serie=?"
            cursor.execute(update_path,(code_edit,))
            db.session.commit()
               
            modificar_produro = True
            print('novo nome, preco e preco do fornecedor')
        elif novo_nome != '' and novo_preco != '' and novo_preco_fornecedor == '':
            parametros = (novo_nome, novo_preco,
                          old_preco_fornecedor, code_edit)
            os.rename(os.path.join("static/produtos/",old_nome),
                      os.path.join("static/produtos/",novo_nome))
            update_path = "UPDATE Produtos SET especificacoes=? where numero_serie=?"
            cursor.execute(update_path,(code_edit,))
            db.session.commit()
            modificar_produro = True
            print('novo nome e preco')
        elif novo_nome != '' and novo_preco == '' and novo_preco_fornecedor != '':
            parametros = (novo_nome, old_preco,
                          novo_preco_fornecedor, code_edit)
            os.rename(os.path.join("static/produtos/",old_nome),
                      os.path.join("static/produtos/",novo_nome))
            update_path = "UPDATE Produtos SET especificacoes=? where numero_serie=?"
            cursor.execute(update_path,(code_edit,))
            db.session.commit()
            modificar_produro = True
            print('novo nome e preco fornecedor')
        elif novo_nome == '' and novo_preco != '' and old_preco_fornecedor != '':
            parametros = (old_nome, novo_preco,
                          novo_preco_fornecedor, code_edit)
            modificar_produro = True
            print('Novo preco e preco fornecedor')
        elif novo_nome != '' and novo_preco == '' and old_preco_fornecedor == '':
            parametros = (novo_nome, old_preco,
                          old_preco_fornecedor, code_edit)
            os.rename(os.path.join("static/produtos/",old_nome),
                      os.path.join("static/produtos/",novo_nome))
            update_path = "UPDATE Produtos SET especificacoes=? where numero_serie=?"
            cursor.execute(update_path,(code_edit,))
            db.session.commit()
            modificar_produro = True
            print('Novo nome')
        elif novo_nome == '' and novo_preco == '' and old_preco_fornecedor != '':
            parametros = (old_nome, old_preco,
                          novo_preco_fornecedor, code_edit)
            modificar_produro = True
            print('Novo preco fornecedor')
        elif novo_nome == '' and novo_preco != '' and old_preco_fornecedor == '':
            parametros = (old_nome, novo_preco,
                          old_preco_fornecedor, code_edit)
            modificar_produro = True
            print('Novo preco')
        else:
            print('Nenhuma alteracao')
            modificar_produro = False
        
        #Armazenamos as especificacoes atuais
        old_descr_1 = especificacoes['descricoes']['descricao_1']
        old_descr_2 = especificacoes['descricoes']['descricao_2']
        old_descr_3 = especificacoes['descricoes']['descricao_3']
        old_descr_4 = especificacoes['descricoes']['descricao_4']
        old_descr_5 = especificacoes['descricoes']['descricao_5']
        old_descr_6 = especificacoes['descricoes']['descricao_6']
        #Armazenamos as novas especificacoes
        descricao_1 = [request.form['editar_tit_descr_1'],request.form['editar_descr_1']]
        descricao_2 = [request.form['editar_tit_descr_2'],request.form['editar_descr_2']]
        descricao_3 = [request.form['editar_tit_descr_3'],request.form['editar_descr_3']]
        descricao_4 = [request.form['editar_tit_descr_4'],request.form['editar_descr_4']]
        descricao_5 = [request.form['editar_tit_descr_5'],request.form['editar_descr_5']]
        descricao_6 = [request.form['editar_tit_descr_6'],request.form['editar_descr_6']]

        #Atualiza as Especificacoes do Produto
        def write_espec_json(new_descricao_1,new_descricao_2,new_descricao_3,new_descricao_4,new_descricao_5,new_descricao_6, filename=produto_em_edicao[10]):
            print(produto_em_edicao[10])
            with open(filename,'r+',encoding='utf8') as file:
                file_data = json.load(file)
                if new_descricao_1[0] != "" and new_descricao_1[1] !="":        #Atualiza a seccao 1 das especificacoes
                    file_data['descricoes']['descricao_1'] = new_descricao_1
                    file.seek(0)
                elif new_descricao_1[0] == "" and new_descricao_1[1] != "":     #Atualiza apenas o texto da especificacao 1
                    file_data['descricoes']['descricao_1'] = [old_descr_1[0],new_descricao_1[1]]
                    file.seek(0)
                elif new_descricao_1[0] != "" and new_descricao_1[1] == "":     #Atualiza apenas o titulo da Especificacao 1
                    file_data['descricoes']['descricao_1'] = [new_descricao_1[0],old_descr_1[1]]
                    file.seek(0)
                elif new_descricao_1[0] == "" and new_descricao_1[1] == "":     #Mantem os dados antigos da Especificacao 1
                    file_data['descricoes']['descricao_1'] = old_descr_1
                    file.seek(0)
                if new_descricao_2[0] != "" and new_descricao_2[1] !="":        #Atualiza a seccao 2 das especificacoes
                    file_data['descricoes']['descricao_2'] = new_descricao_2
                    file.seek(0)
                elif new_descricao_2[0] == "" and new_descricao_2[1] != "":     #Atualiza apenas o texto da especificacao 2
                    file_data['descricoes']['descricao_2'] = [old_descr_2[0],new_descricao_2[1]]
                    file.seek(0)
                elif new_descricao_2[0] != "" and new_descricao_2[1] == "":     #Atualiza apenas o titulo da Especificacao 2
                    file_data['descricoes']['descricao_2'] = [new_descricao_2[0],old_descr_2[1]]
                    file.seek(0)
                elif new_descricao_2[0] == "" and new_descricao_2[1] == "":     #Mantem os dados antigos da Especificacao 2
                    file_data['descricoes']['descricao_2'] = old_descr_2
                    file.seek(0)
                if new_descricao_3[0] != "" and new_descricao_3[1] !="":            #ETC...
                    file_data['descricoes']['descricao_3'] = new_descricao_3                    
                    file.seek(0)
                elif new_descricao_3[0] == "" and new_descricao_3[1] != "":
                    file_data['descricoes']['descricao_3'] = [old_descr_3[0],new_descricao_3[1]]
                    file.seek(0)
                elif new_descricao_3[0] != "" and new_descricao_3[1] == "":
                    file_data['descricoes']['descricao_3'] = [new_descricao_3[0],old_descr_3[1]]
                    file.seek(0)
                elif new_descricao_3[0] == "" and new_descricao_3[1] == "":
                    file_data['descricoes']['descricao_3'] = old_descr_3
                    file.seek(0)
                if new_descricao_4[0] != ""and new_descricao_4[1] !="":
                    file_data['descricoes']['descricao_4'] = new_descricao_4
                    file.seek(0)
                elif new_descricao_4[0] == "" and new_descricao_4[1] != "":
                    file_data['descricoes']['descricao_4'] = [old_descr_4[0],new_descricao_4[1]]
                    file.seek(0)
                elif new_descricao_4[0] != "" and new_descricao_4[1] == "":
                    file_data['descricoes']['descricao_4'] = [new_descricao_4[1],old_descr_4[0]]
                    file.seek(0)
                elif new_descricao_4[0] == "" and new_descricao_4[1] == "":
                    file_data['descricoes']['descricao_4'] = old_descr_4
                    file.seek(0)
                if new_descricao_5[0] != "" and new_descricao_5[1] !="":
                    file_data['descricoes']['descricao_5'] = new_descricao_5
                    file.seek(0)
                elif new_descricao_5[0] == "" and new_descricao_5[1] != "":
                    file_data['descricoes']['descricao_5'] = [old_descr_5[0],new_descricao_5[1]]
                    file.seek(0)
                elif new_descricao_5[0] != "" and new_descricao_5[1] == "":
                    file_data['descricoes']['descricao_5'] = [new_descricao_5[1],old_descr_5[0]]
                    file.seek(0)
                elif new_descricao_5[0] == "" and new_descricao_5[1] == "":
                    file_data['descricoes']['descricao_5'] = old_descr_5
                    file.seek(0)
                if new_descricao_6[0] != "" and new_descricao_6[1] != "":
                    file_data['descricoes']['descricao_6'] = new_descricao_6
                    file.seek(0)
                elif new_descricao_6[0] == "" and new_descricao_6[1] != "":
                    file_data['descricoes']['descricao_6'] = [old_descr_6[0],new_descricao_6[1]]
                    file.seek(0)
                elif new_descricao_6[0] != "" and new_descricao_6[1] == "":
                    file_data['descricoes']['descricao_6'] = [new_descricao_6[0],old_descr_6[1]]
                    file.seek(0)
                elif new_descricao_6[0] == "" and new_descricao_6[1] == "":
                    file_data['descricoes']['descricao_6'] = old_descr_6
                    file.seek(0)
                json.dump(file_data,file,indent=6)                          #Fim das atualizacoes das especificacoes
        write_espec_json(descricao_1,descricao_2,descricao_3,descricao_4,descricao_5,descricao_6)

        #Atualiza a Imagem do produto
        if nova_img_path != '':
            get_especificacoes = open(produto_em_edicao[10], encoding="utf8")
            especificacoes = json.load(get_especificacoes)

            def write_json(new_img_path, filename="static/produtos/"+old_nome+"/espec_produtos.json"):
                with open(filename, 'r+') as file:
                    file_data = json.load(file)
                    file_data['img_path'] = "static/produtos/" + \
                        old_nome + '/' + new_img_path
                    file.seek(0)
                    json.dump(file_data, file, indent=6)
            write_json(nova_img_path)
        else:
            pass
        
        #Guarda Alteracoes
        if modificar_produro == True:
            print('alterado')
            cursor.execute(query, parametros)
            db.session.commit()
            db.session.close()
        else:
            pass

        return redirect(url_for('.show_room', code_prod=code_edit))

    elif session['log_in_admin'] == True and request.method == 'GET':
        con = sqlite3.connect('database/dados_informacoes2.db')
        cursor = con.cursor()
        cursor.execute(
            "SELECT * FROM Produtos WHERE numero_serie=?", (code_edit,))
        produto_em_edicao = cursor.fetchone()
        get_especificacoes = open(produto_em_edicao[10], encoding="utf8")
        especificacoes = json.load(get_especificacoes)
        old_nome = produto_em_edicao[1]
        old_preco = produto_em_edicao[5]
        old_preco_fornecedor = produto_em_edicao[4]
        old_img_path = especificacoes['img_path']
        return render_template('editar_produtos.html', especificacoes=especificacoes, old_nome=old_nome, old_preco=old_preco,
                               old_img_path=old_img_path, old_preco_fornecedor=old_preco_fornecedor, id_do_produto=produto_em_edicao[0])


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

# Criacao de fornecedor
@root.route('/admin/criar-fornecedor', methods=['GET', 'POST'])
def criar_fornecedor():
    fornecedor = lista_fornecedores()
    if request.method == 'GET':
        return render_template('criar_fornecedor.html',fornecedores = fornecedor)
    # adicionar forncedor
    # experimentar aplicar na pagina de criacao de produto e criar uma propria pagina
    # so para adicionar um fonecedor
    if request.method =='POST':
        fornecedor = Fornecedor(email_fornecedor = request.form['email_fornecedor'],nome_fornecedor = request.form['nome_fornecedor_reg'],
                    contacto=request.form['contacto_fornecedor'], numero_IF = request.form['numero_If'], senha_login = request.form['password_fornecedor'],desp_fornecedor = 0,
                    lucro_fornecedor = 0, desconto_fornecedor = 0)
        db.session.add(fornecedor)
        db.session.commit()
        return redirect(url_for('.todos_produtos'))

# Home Page


@root.route('/', methods=['GET', 'POST'])
def home():
    todos_os_produtos = lista_produtos()
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    apresentacao = []
    for produto in todos_os_produtos:
        prod_img_desj = produto[0]
        cursor.execute(
            "SELECT * FROM Produtos WHERE numero_serie = ? ", (prod_img_desj,))
        produto_select = cursor.fetchone()
        get_especificacoes = open(produto_select[10], encoding="utf8")
        detalhes = json.load(get_especificacoes)
        novos_detalhes = produto+(detalhes['img_path'],)
        apresentacao.append(novos_detalhes)
        print(novos_detalhes)
    if request.method == 'GET':
        try:
            if session['log_in'] == True:
                return render_template('index.html', todos_os_produtos=apresentacao, log_in=session['log_in'], user=session['username'])
            elif session['log_in_admin'] == True:
                return render_template('index.html', todos_os_produtos=apresentacao, log_in=session['log_in_admin'], user=session['username'])
        except:
            return render_template('index.html', todos_os_produtos=apresentacao, log_in=False, user=None)
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


# Pagina de LOGIN
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

        # Base de dados fornecedor
        #dados_database_fornecedor = "SELECT * FROM Fornecedores"
        verificar_email_fornecedor = db_verificar_fornecedor()  # dados_database_fornecedor

        todos_os_produto = lista_produtos()

        # Verificar se user e admin
        for user in verificado_email_admin:
            if user_loggin == user[1] and user_pswd == user[3]:
                session['log_in_admin'] = True
                session['pass_word_admin'] = True
                session['user'] = user_loggin
                session["password"] = user_pswd
                session['username'] = user[2]
                print(session['username'])
                return redirect(url_for('.todos_produtos',  log_in_admin=session['log_in_admin'], user=session['username']))

        # Verificar fornecedor
        for user in verificar_email_fornecedor:
            if user_loggin == user[1] and user_pswd == user[7]:
                session['log_in_fornecedor'] = True
                session['pass_word_fornecedor'] = True
                session['user'] = user_loggin
                session['password'] = user_pswd
                session['username'] = user[2]
                session['id'] = user[0]
                return redirect(url_for('.todos_produtos',  log_in_fornecedor=session['log_in_fornecedor'], user=session['username']))

        # Verificar se user e cliente
        for user in verificado_email:
            if user_loggin == user[0] and user_pswd == user[3]:
                session['log_in'] = True
                session['pass_word'] = True
                session['user'] = user_loggin
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
                return redirect(url_for(".home", log_in=session['log_in'], user=session['username'], todos_os_produtos=todos_os_produto, lista_fornecedores=None))
        # Iniciar como admin
        except:
            if 'log_in_admin' in session:
                if session['log_in_admin'] == True and session['pass_word_admin'] == True:
                    print('loggin admin')
                    session["user"] = user_loggin
                    session["password"] = user_pswd
                # session['carrinho']
                    return redirect(url_for('todos_produtos', todos_os_produtos=todos_os_produto, log_in_admin=session['log_in_admin'], user=session['username'],
                                            lista_fornecedores=todos_os_fornecedores,))

            elif 'log_in_fornecedor' in session:
                if session['log_in_fornecedor'] == True and session['pass_word_fornecedor'] == True:
                    print('loggin fornecedor')
                    session["user"] = user_loggin
                    session["password"] = user_pswd

                # session['carrinho']
                    return redirect(url_for('todos_produtos', todos_os_produtos=todos_os_produto, log_in_forneccedor=session['log_in_fornecedor'], user=session['username'],
                                            lista_fornecedores=todos_os_fornecedores))

            else:
                return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('login.html')

# Log Out


@root.route("/logout")
def logout():

    if 'log_in' in session:
        if session['log_in'] == True:
            session.pop('log_in')
            session.pop('pass_word')
            session.pop('user')
            session.pop('username')
            session.clear()

    if 'log_in_admin' in session:
        if session['log_in_admin'] == True:
            session.pop('log_in_admin')
            session.pop('pass_word_admin')
            session.pop('user')
            session.pop('username')
            session.clear()

    elif 'log_in_fornecedor' in session:
        if session['log_in_fornecedor'] == True:
            session.pop('log_in_fornecedor')
            session.pop('pass_word_fornecedor')
            session.pop('user')
            session.pop('username')
            session.pop('id')
            session.clear()

    return redirect(url_for('home'))


# pagina carrinho
@root.route('/user-login/carrinho', methods=['GET', 'POST'])
def carrinho():
    if request.method == 'GET':
        faturas = show_faturas(session['user'])
        print(faturas)

        return render_template('carrinho.html', faturas=faturas, faturas_len = len(faturas))

    if request.method == 'POST':
        faturas = show_faturas(session['user'])
        path = request.form['path']
        print(path)
        os.startfile(path)
        try:
            print(session['carrinho'])
            return render_template('carrinho.html', log_in=session['log_in'], user=session['username'], carrinho=session['carrinho'], faturas=faturas, faturas_len = len(faturas))
        except:
            return render_template('carrinho.html', log_in=None, user=None, faturas=faturas, faturas_len = len(faturas))


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

        if _quantity <= row[2]:
            itemArray = {'id': row[0], 'name': row[1], 'preco': row[5], 'iva': row[11],
                         'quantidade': _quantity, 'total': _quantity*row[5]}
            all_total_preco = 0
            all_total_quantidade = 0
            session.modified = True
            if'carrinho' in session:
                try:
                    for item in session['carrinho']:
                        if itemArray['id'] == item['id']:
                            # soma produto que ja se encontra na lista

                            print(itemArray, item['id'])
                            old_quantity = item['quantidade']
                            total_quantidade = old_quantity + \
                                itemArray['quantidade']
                            item['quantidade'] = total_quantidade
                            iva = item['iva'] / 100
                            preco_com_iva = itemArray['preco'] * iva
                            preco_total = (itemArray['preco'] * itemArray['quantidade']) + item['preco']
                            item['total'] = preco_total

                            print('\n{}\n'.format(itemArray))
                            print('soma produto que ja se encontra na lista')
                            break
                        elif itemArray['id'] != item['id']:
                            # This is not a bug, its a feature
                            print('adiciona produto que nao se encontra na lista')

                        else:
                            print('Erro ao somar produto')
                    else:
                        try:
                            session['carrinho'].append(itemArray)
                            print("feature")

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
                iva = item['iva'] / 100
                preco_com_iva = item['preco'] * iva
                preco_total = (preco_com_iva +
                               item['preco']) * quantidade_individual
                all_total_quantidade += quantidade_individual
                all_total_preco += preco_total

            session['all_total_quantidade'] = all_total_quantidade
            session['all_total_preco'] = all_total_preco
            print(session['carrinho'])

            cursor.close()
            con.close()

            return redirect(url_for('.carrinho'))
        else:
            print('Quantidade de produto nao disponivel')
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
        return redirect(url_for('.carrinho'))

    except Exception as e:
        print(e)
    finally:
        return redirect(url_for('.carrinho'))


# Remover item do carrinho
@root.route('/delete/<string:code>')
def delete_product(code):
    all_total_preco = session['all_total_preco']
    all_total_quantidade = session['all_total_quantidade']
    session.modified = True
    print(session['carrinho'])
    for item in session['carrinho']:
        print(type(code))
        item_id = item['id']
        iva = item['iva'] / 100
        preco_iva = item['preco'] * iva

        if int(item_id) == int(code):
            retirar_daconta = item['quantidade'] * (item['preco'] + preco_iva)
            session['all_total_preco'] = all_total_preco - retirar_daconta
            session['all_total_quantidade'] = all_total_quantidade - \
                item['quantidade']
            session['carrinho'].remove(item)
            return redirect(url_for('.carrinho'))

        else:
            print('carrinho:', session['carrinho'])
            pass
    if session['all_total_quantidade'] <= 0:
        session['carrinho'] = []
        all_total_preco = 0
        session['all_total_preco'] = 0
    # return redirect('/')
    return redirect(url_for('.carrinho'))


# Finalizar Compras
@root.route('/pagamento')
def finalizar_compra():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    for item in session['carrinho']:
        print(item['name'])
        # seleciona o produto na base de dados, atravez do id do produto dentro de session['carrinho']
        cursor.execute(
            "SELECT * FROM Produtos WHERE numero_serie={}".format(item['id']))
        row = cursor.fetchone()
        fornecedor_id = row[9]
        # seleciona o fornecedor na base de dados, atraves dos dados obtidos pelo produto
        cursor.execute(
            "SELECT * FROM Fornecedores WHERE id_fornecedor={}".format(fornecedor_id))
        fornecedor_dados = cursor.fetchone()
        # despesa obtida pelo admin com a venda de produtos do fornecedor 'X'
        des_fornecedores = float(
            fornecedor_dados[3]) + item['quantidade']*row[4]
        # lucro obtido pelo admin com vendas de produtos do fornecedor 'X'
        lucro_fornecedor = float(
            fornecedor_dados[4])+(item['quantidade']*row[5]) - (item['quantidade']*row[4])

        # Atualiza as despesas de fornecedor ao somar, quantidade de produto vendido ao valor que cada um custou ao fornecedor
        cursor.execute("UPDATE Fornecedores SET desp_fornecedor={:.2f}, lucro_fornecedor={:.2f} WHERE id_fornecedor={} ".format(
            des_fornecedores, lucro_fornecedor, fornecedor_id))
        con.commit()
        db.session.commit()

    for item in session['carrinho']:
        print('item id:', item['id'])
        cursor.execute(
            "SELECT * FROM Produtos WHERE numero_serie={}".format(item['id']))
        row = cursor.fetchone()
        produto_quantidade_vendida = row[3] + item['quantidade']
        produto_quantidade_armazem = row[2] - item['quantidade']
        cursor.execute("UPDATE Produtos SET em_armazem={}, vendidos={} WHERE numero_serie={}".format(
            produto_quantidade_armazem, produto_quantidade_vendida, item['id']))
        con.commit()
        db.session.commit()
    fatura(session['carrinho'])
    empty_cart()
    return redirect(url_for('.carrinho'))


# Lista de Produtos
@root.route('/listagem_produto', methods=['GET', 'POST'])
def todos_produtos():
    # informação apresentada ao cliente
    todos_os_produtos = lista_produtos()
    lista_de_fornecedores = lista_fornecedores()
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    apresentacao = []
    for produto in todos_os_produtos:
        prod_img_desj = produto[0]
        cursor.execute(
            "SELECT * FROM Produtos WHERE numero_serie = ? ", (prod_img_desj,))
        produto_select = cursor.fetchone()
        get_especificacoes = open(produto_select[10], encoding="utf8")
        detalhes = json.load(get_especificacoes)
        novos_detalhes = produto+(detalhes['img_path'],)
        apresentacao.append(novos_detalhes)
        print(novos_detalhes)

    if request.method == 'GET':
        if 'log_in' in session:
            if session['log_in'] == True:
                return render_template('lista_produtos.html', todos_os_produtos=apresentacao, img_prod=detalhes['img_path'], log_in=session['log_in'],
                                       user=session['username'], lista_de_fornecedores=lista_de_fornecedores)

        if 'log_in_admin' in session:
            if session['log_in_admin'] == True:
                return render_template('lista_produtos.html', todos_os_produtos=apresentacao, img_prod=detalhes['img_path'], log_in_admin=session['log_in_admin'],
                                       user=session['username'], lista_de_fornecedores=lista_de_fornecedores)
        if 'log_in_fornecedor' in session:
            return render_template('lista_produtos.html', todos_os_produtos=apresentacao, img_prod=detalhes['img_path'], log_in_forn=session['log_in_fornecedor'],
                                   user=session['username'], lista_de_fornecedores=lista_de_fornecedores)

        else:
            return render_template('lista_produtos.html', todos_os_produtos=apresentacao, img_prod=detalhes['img_path'], log_in_admin=False, log_in=False,
                                   log_in_fornecedor=False, user=None)


# Encomenda de produtos ao Fornecedor
@root.route('/encomendas', methods=['POST'])
def fornecer_produto():
    id_encomenda = request.form['id_produto']
    _quantidade_encomenda = int(request.form['quantidade'])
    if id_encomenda and _quantidade_encomenda and request.method == "POST":
        try:
            if 'log_in_admin' in session:
                # Realiza a encomenda ao fornecedor
                con = sqlite3.connect('database/dados_informacoes2.db')
                cursor = con.cursor()
                cursor.execute(
                    "SELECT * FROM Produtos WHERE numero_serie=?", (id_encomenda,))
                info_prod = cursor.fetchone()
                old_encomendas = info_prod[8]
                print(info_prod)
                total = old_encomendas + _quantidade_encomenda

                cursor.execute("UPDATE Produtos SET quantidade_encomenda={} WHERE numero_serie={} ".format(
                    total, id_encomenda))

                con.commit()
                cursor.close()
                return redirect(url_for('.todos_produtos'))

            if 'log_in_fornecedor' in session:
                # Realiza a entrega das encomendas ao armazem da loja
                con = sqlite3.connect('database/dados_informacoes2.db')
                cursor = con.cursor()
                cursor.execute(
                    "SELECT * FROM Produtos WHERE numero_serie=?", (id_encomenda,))
                info_prod = cursor.fetchone()
                old_stock = info_prod[2]

                total = old_stock + _quantidade_encomenda
                cursor.execute("UPDATE Produtos SET em_armazem={} WHERE numero_serie={} ".format(
                    total, id_encomenda))

                entrega = info_prod[8]
                if entrega > 0:
                    entrega = info_prod[8] - _quantidade_encomenda
                    cursor.execute("UPDATE Produtos SET quantidade_encomenda={} WHERE numero_serie={} ".format(
                        entrega, id_encomenda))
                elif entrega < 0:
                    pass
                con.commit()
                cursor.close()
                return redirect(url_for('.todos_produtos'))
        except Exception as e:
            print(e)
            return redirect(url_for('.todos_produtos'))
    else:
        try:
            print(id_encomenda, _quantidade_encomenda)
        except Exception as e:
            print(e)


# Produtos disponiveis para destaque
# Pagina Exibicao do produto detalhado asus geforce 3080


@root.route('/listagem_produto/armazem/asus-geforce-rtx-3080-rog-strix-oc-lhr-12gb6x', methods=['GET'])
def asusgeforce_rtx3080():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE numero_serie=2")
    produto_select = cursor.fetchone()
    get_especificacoes = open(produto_select[10], encoding="utf8")
    especificacoes = json.load(get_especificacoes)

    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = especificacoes['img_path']
    descricao_prod = produto_select[8]
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                   2],
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


# Pagina Exibicao do produto detalhado asus geforce 3070
@root.route('/listagem_produto/armazem/Gigabyte-GeForce-RTX-3070-Aorus-Master-LHR-8GB-GD6', methods=['GET'])
def geforce_3070():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE numero_serie=3")
    produto_select = cursor.fetchone()
    get_especificacoes = open(produto_select[10], encoding="utf8")
    especificacoes = json.load(get_especificacoes)

    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = especificacoes['img_path']
    descricao_prod = produto_select[8]
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                   2],
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


# Pagina Exibicao do produto detalhado Computador King
@root.route('/listagem_produto/armazem/Computador-King-Mod', methods=['GET'])
def kingModDesktop():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE numero_serie=4")
    produto_select = cursor.fetchone()
    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = produto_select[10]
    descricao_prod = produto_select[8]
    get_especificacoes = open(produto_select[10], encoding="utf8")

    especificacoes = json.load(get_especificacoes)
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                   2],
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


# Pagina Exibicao do produto detalhado Asus VivoBook K513EP
@root.route('/listagem_produto/armazem/Asus-VivoBook-K513EP', methods=['GET'])
def vivoBook_K513EP():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE numero_serie=5")
    produto_select = cursor.fetchone()
    get_especificacoes = open(produto_select[10], encoding="utf8")
    especificacoes = json.load(get_especificacoes)

    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = especificacoes['img_path']
    descricao_prod = produto_select[8]
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                   2],
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


# Pagina Exibicao do produto detalhado Asus VivoBook K513EP
@root.route('/listagem_produto/armazem/HP-Pavillon-x360', methods=['GET'])
def hp_pavillon_360():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE numero_serie=6")
    produto_select = cursor.fetchone()
    get_especificacoes = open(produto_select[10], encoding="utf8")
    especificacoes = json.load(get_especificacoes)

    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = especificacoes['img_path']
    descricao_prod = produto_select[8]

    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                   2],
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


# Pagina Exibicao do produto detalhado SSD Kingston NV1
@root.route('/listagem_produto/armazem/SSD-Kingston-NV1', methods=['GET'])
def ssd_kingston_nv1():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE numero_serie=7")
    produto_select = cursor.fetchone()
    get_especificacoes = open(produto_select[10], encoding="utf8")
    especificacoes = json.load(get_especificacoes)

    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = especificacoes['img_path']
    descricao_prod = produto_select[8]

    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                   2],
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


# Pagina Exibicao do produto detalhado Monitor Dell 27 S2721HGF Curvo FHD
@root.route('/listagem_produto/armazem/Monitor-Dell-27-S2721HGF-Curvo-FHD', methods=['GET'])
def monitor_dell_s2721hgf():
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Produtos WHERE numero_serie=8")
    produto_select = cursor.fetchone()
    get_especificacoes = open(produto_select[10], encoding="utf8")
    especificacoes = json.load(get_especificacoes)

    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = especificacoes['img_path']
    descricao_prod = produto_select[8]
    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                       2],
                                   descricao_prod=descricao_prod, especificacoes=especificacoes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=produto_select[
                                   2],
                               descricao_prod=descricao_prod, especificacoes=especificacoes)


@root.route('/<code_prod>', methods=['GET'])
def show_room(code_prod):
    con = sqlite3.connect('database/dados_informacoes2.db')
    cursor = con.cursor()
    cursor.execute(
        "SELECT * FROM Produtos WHERE numero_serie = ?", (code_prod,))
    produto_select = cursor.fetchone()
    print(produto_select)
    get_especificacoes = open(produto_select[10], encoding="utf8")
    detalhes = json.load(get_especificacoes)

    numero_serie = produto_select[0]
    nome_produto = produto_select[1]
    preco_produto = produto_select[5]
    imagem_produto = detalhes['img_path']
    descricao_prod = produto_select[8]
    quantidade_armazem = produto_select[2]

    try:
        if session['log_in'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=quantidade_armazem,
                                   descricao_prod=descricao_prod, especificacoes=detalhes,
                                   log_in=session['log_in'], pass_word=session['pass_word'],
                                   user=session['username'])
        elif session['log_in_admin'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=quantidade_armazem,
                                   descricao_prod=descricao_prod, especificacoes=detalhes,
                                   log_in_admin=session['log_in_admin'], pass_word_admin=session['pass_word_admin'],
                                   user=session['username'])
        elif session['log_in_fornecedor'] == True:
            return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                                   preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=quantidade_armazem,
                                   descricao_prod=descricao_prod, especificacoes=detalhes,
                                   log_in_fornecedor=session['log_in_fornecedor'], pass_word_fornecedor=session['pass_word_fornecedor'],
                                   user=session['username'])
    except:
        return render_template('produtos.html', nome_produto=nome_produto, id_do_produto=numero_serie,
                               preco_produto=preco_produto, imagem_produto=imagem_produto, quanti_armazem=quantidade_armazem,
                               descricao_prod=descricao_prod, especificacoes=detalhes)


if __name__ == "__main__":
    root.run()
    db.create_all()
    db.session.commit()