from flask import Flask, render_template, request, redirect, url_for, flash
from database import db

app = Flask(__name__)
app.secret_key = 'chave_secreta_gramatica_online_2026'

# Configurações do banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///gramatica_online.db'
app.config["TEMPLATES_AUTO_RELOAD"] = True

db.init_app(app)

from models import *

with app.app_context():
    db.create_all()

# ==============================================
# SUAS ROTAS ORIGINAIS (TODAS MANTIDAS)
# ==============================================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/usuario")
def usuario():
    return render_template("usuario.html")

@app.route("/escolha")
def escolha():
    return render_template("escolha.html")

@app.route("/gramatica")
def gramatica():
    return render_template("gramatica.html")

@app.route("/atividades")
def atividades():
    return render_template("atividades.html")

@app.route("/sujeito_detalhe")
def sujeito_detalhe():
    return render_template("sujeito_detalhe.html")

@app.route("/revisao_geral_detalhe")
def revisao_geral_detalhe():
    return render_template("revisao_geral_detalhe.html")

@app.route("/predicado_detalhe")
def predicado_detalhe():
    return render_template("predicado_detalhe.html")

@app.route("/complemento_verbal_detalhe")
def complemento_verbal_detalhe():
    return render_template("complemento_verbal_detalhe.html")

@app.route("/complemento_nominal_detalhe")
def complemento_nominal_detalhe():
    return render_template("complemento_nominal_detalhe.html")

@app.route("/aposto_detalhe")
def aposto_detalhe():
    return render_template("aposto_detalhe.html")

@app.route("/agente_da_passiva_detalhe")
def agente_da_passiva_detalhe():
    return render_template("agente_da_passiva_detalhe.html")

@app.route("/adjunto_adverbial_detalhe")
def adjunto_adverbial_detalhe():
    return render_template("adjunto_adverbial_detalhe.html")

@app.route("/adjunto_adnominal_detalhe")
def adjunto_adnominal_detalhe():
    return render_template("adjunto_adnominal_detalhe.html")

@app.route("/atividade1")
def atividade1():
    return render_template("atividade1.html")

@app.route("/atividade2")
def atividade2():
    return render_template("atividade2.html")

@app.route("/atividade3")
def atividade3():
    return render_template("atividade3.html")

@app.route("/atividade4")
def atividade4():
    return render_template("atividade4.html")

@app.route("/atividade5")
def atividade5():
    return render_template("atividade5.html")

@app.route("/atividade6")
def atividade6():
    return render_template("atividade6.html")

@app.route("/atividade7")
def atividade7():
    return render_template("atividade7.html")

@app.route("/atividade8")
def atividade8():
    return render_template("atividade8.html")

@app.route("/atividade9")
def atividade9():
    return render_template("atividade9.html")

@app.route("/pontuacao")
def pontuacao():
    return render_template("pontuacao.html")

@app.route("/periodo_simples")
def periodo_simples():
    return render_template("periodo_simples.html")

@app.route("/periodo_composto")
def periodo_composto():
    return render_template("periodo_composto.html")

@app.route("/classificacao_de_palavras")
def classificacao_de_palavras():
    return render_template("classificacao_de_palavras.html")

@app.route("/att_pontuacao")
def att_pontuacao():
    return render_template("att_pontuacao.html")

@app.route("/att_periodo_simples")
def att_periodo_simples():
    return render_template("att_periodo_simples.html")

@app.route("/att_periodo_composto")
def att_periodo_composto():
    return render_template("att_periodo_composto.html")

@app.route("/att_classificacao_de_palavras")
def att_classificacao_de_palavras():
    return render_template("att_classificacao_de_palavras.html")


# ==============================================
# CRUD ASSUNTO (CORRIGIDO - SEM DUPLICATAS)
# ==============================================
@app.route('/assuntos')
def listar_assuntos():
    assuntos = Assunto.query.all()
    return render_template('listar_assuntos.html', assuntos=assuntos)

@app.route('/assuntos/novo', methods=['GET', 'POST'])
def novo_assunto():
    if request.method == 'POST':
        nome = request.form['nome']
        novo = Assunto(nome=nome)
        db.session.add(novo)
        db.session.commit()
        flash('Assunto cadastrado com sucesso!')
        return redirect(url_for('listar_assuntos'))
    return render_template('novo_assunto.html')

@app.route('/assuntos/editar/<int:id>', methods=['GET', 'POST'])
def editar_assunto(id):
    assunto = Assunto.query.get_or_404(id)
    if request.method == 'POST':
        assunto.nome = request.form['nome']
        db.session.commit()
        flash('Assunto atualizado!')
        return redirect(url_for('listar_assuntos'))
    return render_template('editar_assunto.html', assunto=assunto)

@app.route('/assuntos/apagar/<int:id>')
def apagar_assunto(id):
    assunto = Assunto.query.get_or_404(id)
    db.session.delete(assunto)
    db.session.commit()
    flash('Assunto removido!')
    return redirect(url_for('listar_assuntos'))


# ==============================================
# CRUD ATIVIDADE (CORRIGIDO)
# ==============================================
@app.route('/atividades/crud')
def listar_atividades():
    atividades = Atividade.query.all()
    return render_template('listar_atividades.html', atividades=atividades)

@app.route('/atividades/novo', methods=['GET', 'POST'])
def nova_atividade():
    assuntos = Assunto.query.all()
    if request.method == 'POST':
        dificuldade = request.form['dificuldade']
        assunto_id = request.form['assunto_id']
        nova = Atividade(dificuldade=dificuldade, assunto_id=assunto_id)
        db.session.add(nova)
        db.session.commit()
        flash('Atividade cadastrada!')
        return redirect(url_for('listar_atividades'))
    return render_template('nova_atividade.html', assuntos=assuntos)

@app.route('/atividades/editar/<int:id>', methods=['GET', 'POST'])
def editar_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    assuntos = Assunto.query.all()
    if request.method == 'POST':
        atividade.dificuldade = request.form['dificuldade']
        atividade.assunto_id = request.form['assunto_id']
        db.session.commit()
        flash('Atividade atualizada!')
        return redirect(url_for('listar_atividades'))
    return render_template('editar_atividade.html', atividade=atividade, assuntos=assuntos)

@app.route('/atividades/apagar/<int:id>')
def apagar_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    db.session.delete(atividade)
    db.session.commit()
    flash('Atividade removida!')
    return redirect(url_for('listar_atividades'))


# ==============================================
# CRUD QUESTÃO (CORRIGIDO)
# ==============================================
@app.route('/questoes')
def listar_questoes():
    questoes = Questao.query.all()
    return render_template('listar_questoes.html', questoes=questoes)

@app.route('/questoes/novo', methods=['GET', 'POST'])
def nova_questao():
    atividades = Atividade.query.all()
    if request.method == 'POST':
        enunciado = request.form['enunciado']
        atividade_id = request.form['atividade_id']
        nova = Questao(enunciado=enunciado, atividade_id=atividade_id)
        db.session.add(nova)
        db.session.commit()
        flash('Questão cadastrada!')
        return redirect(url_for('listar_questoes'))
    return render_template('nova_questao.html', atividades=atividades)

@app.route('/questoes/editar/<int:id>', methods=['GET', 'POST'])
def editar_questao(id):
    questao = Questao.query.get_or_404(id)
    atividades = Atividade.query.all()
    if request.method == 'POST':
        questao.enunciado = request.form['enunciado']
        questao.atividade_id = request.form['atividade_id']
        db.session.commit()
        flash('Questão atualizada!')
        return redirect(url_for('listar_questoes'))
    return render_template('editar_questao.html', questao=questao, atividades=atividades)

@app.route('/questoes/apagar/<int:id>')
def apagar_questao(id):
    questao = Questao.query.get_or_404(id)
    db.session.delete(questao)
    db.session.commit()
    flash('Questão removida!')
    return redirect(url_for('listar_questoes'))


if __name__ == "__main__":
    app.run(debug=True)