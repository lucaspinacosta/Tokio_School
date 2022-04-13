
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tarefas.db'
db = SQLAlchemy(app)

class Tarefa(db.Model):
    __tablename__="tarefas"
    id = db.Column(db.Integer,primary_key=True) #Identificador unico de cada terefa (nao pode haver duas tarefas com o mesmo id, por isso e primary key)
    conteudo = db.Column(db.String(200)) #Conteudo da tarefa, um texto de maximo 200 caracteres
    feita = db.Column(db.Boolean) #Booleano que indica se uma tarefa foi feita ou nao

db.create_all()#cria as tabelas
db.session.commit()#Execucao das tarefas pendesntes da base de dados


@app.route('/',methods=['GET'])
def home():
    todas_as_tarefas = Tarefa.query.all() #Consulta e armazena todas as tarefas da base de dados
    return render_template("index.html",lista_de_tarefas=todas_as_tarefas)

@app.route('/eliminar-tarefa/<id>')
def eliminar(id):
    tarefa = Tarefa.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))
@app.route('/tarefa-feita/<id>')
def feita(id):
    tarefa = Tarefa.query.filter_by(id=int(id)).first()
    tarefa.feita = not(tarefa.feita)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/criar-tarefa', methods=['POST'])
def criar():
    tarefa = Tarefa(conteudo=request.form['conteudo_tarefa'],feita=False)

    db.session.add(tarefa)
    db.session.commit()
    return redirect(url_for('home'))



app.run()