from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
import os
from werkzeug.utils import secure_filename
from sqlalchemy import text
from flask import session
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from authlib.integrations.base_client.errors import OAuthError
from requests.exceptions import RequestException

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "outra-chave-segura")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gramatica_online.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

oauth = OAuth(app)
SUAP_BASE_URL = os.environ.get("SUAP_BASE_URL", "https://suap.ifrn.edu.br").rstrip("/")
SUAP_USER_INFO_ENDPOINT = os.environ.get("SUAP_USER_INFO_ENDPOINT", "api/rh/eu/").lstrip("/")
suap_client_kwargs = {}
suap_scope = os.environ.get("SUAP_SCOPE", "").strip()
if suap_scope:
    suap_client_kwargs["scope"] = suap_scope

suap = oauth.register(
    name="suap",
    client_id=os.environ["SUAP_CLIENT_ID"],
    client_secret=os.environ["SUAP_CLIENT_SECRET"],
    authorize_url=f"{SUAP_BASE_URL}/o/authorize/",
    access_token_url=f"{SUAP_BASE_URL}/o/token/",
    api_base_url=f"{SUAP_BASE_URL}/",
    client_kwargs=suap_client_kwargs,
)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db.init_app(app)

from models import Assunto, Atividade, Questao

with app.app_context():
    try: db.session.execute(text("ALTER TABLE atividade ADD COLUMN nome VARCHAR(150);")); db.session.commit()
    except Exception: pass
    try: db.session.execute(text("ALTER TABLE atividade ADD COLUMN dificuldade VARCHAR(50);")); db.session.commit()
    except Exception: pass
    try: db.session.execute(text("ALTER TABLE questao ADD COLUMN alternativa_a TEXT;")); db.session.commit()
    except Exception: pass
    try: db.session.execute(text("ALTER TABLE questao ADD COLUMN alternativa_b TEXT;")); db.session.commit()
    except Exception: pass
    try: db.session.execute(text("ALTER TABLE questao ADD COLUMN alternativa_c TEXT;")); db.session.commit()
    except Exception: pass
    try: db.session.execute(text("ALTER TABLE questao ADD COLUMN alternativa_d TEXT;")); db.session.commit()
    except Exception: pass
    try: db.session.execute(text("ALTER TABLE questao ADD COLUMN alternativa_e TEXT;")); db.session.commit()
    except Exception: pass
    try: db.session.execute(text("ALTER TABLE questao ADD COLUMN resposta_correta VARCHAR(1);")); db.session.commit()
    except Exception: pass

def arquivo_permitido(nome):
    return '.' in nome and nome.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ROTAS PRINCIPAIS
@app.route("/")
def index(): return render_template("index.html")
@app.route("/login")
def login(): return redirect(url_for("auth_suap"))
@app.route("/usuario")
def usuario(): return render_template("usuario.html")
@app.route("/escolha")
def escolha(): return render_template("escolha.html")

@app.route("/gramatica")
def gramatica():
    try:
        assuntos = Assunto.query.all()
        return render_template("gramatica.html", assuntos=assuntos)
    except Exception as e:
        print("ERRO GRAMÁTICA:", str(e))
        flash("Erro ao carregar assuntos.")
        return render_template("gramatica.html", assuntos=[])

@app.route("/atividades")
def atividades():
    try:
        atividades = Atividade.query.all()
        return render_template("atividades.html", atividades=atividades)
    except Exception as e:
        print("ERRO ATIVIDADES:", str(e))
        flash("Erro ao carregar atividades.")
        return render_template("atividades.html", atividades=[])

# ROTA listar_atividades
@app.route('/listar_atividades')
def listar_atividades():
    try:
        atividades = Atividade.query.all()
        assuntos = Assunto.query.all()
        return render_template("listar_atividades.html", atividades=atividades, assuntos=assuntos)
    except Exception as e:
        print("ERRO LISTAR ATIVIDADES:", str(e))
        flash("Erro ao carregar atividades.")
        return redirect(url_for('atividades'))

# GERENCIAR ASSUNTOS
@app.route('/listar_assuntos')
def listar_assuntos():
    try:
        assuntos = Assunto.query.all()
        return render_template("listar_assuntos.html", assuntos=assuntos)
    except Exception as e:
        print("ERRO LISTAR ASSUNTOS:", str(e))
        flash("Erro ao carregar.")
        return redirect(url_for('gramatica'))

@app.route('/novo_assunto', methods=['GET', 'POST'])
def novo_assunto():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        if not nome:
            flash("Preencha o nome do assunto!")
            return redirect(url_for('novo_assunto'))
        caminho_pdf = None
        if 'arquivo_pdf' in request.files:
            arq = request.files['arquivo_pdf']
            if arq.filename and arquivo_permitido(arq.filename):
                nome_seg = secure_filename(f"{nome}_{arq.filename}")
                arq.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_seg))
                caminho_pdf = f"uploads/{nome_seg}"
        caminho_img = None
        if 'imagem' in request.files:
            arq = request.files['imagem']
            if arq.filename and arquivo_permitido(arq.filename):
                nome_seg = secure_filename(f"{nome}_{arq.filename}")
                arq.save(os.path.join(app.config['UPLOAD_FOLDER'], nome_seg))
                caminho_img = f"uploads/{nome_seg}"
        novo = Assunto(nome=nome, conteudo=request.form.get('conteudo',''), arquivo_pdf=caminho_pdf, imagem=caminho_img)
        db.session.add(novo)
        db.session.commit()
        flash("Assunto cadastrado com sucesso!")
        return redirect(url_for('listar_assuntos'))
    return render_template("novo_assunto.html")

@app.route('/ver_assunto/<int:id>')
def ver_assunto(id):
    assunto = Assunto.query.get_or_404(id)
    return render_template("ver_assunto.html", assunto=assunto)

@app.route('/editar_assunto/<int:id>', methods=['GET', 'POST'])
def editar_assunto(id):
    assunto = Assunto.query.get_or_404(id)
    if request.method == 'POST':
        assunto.nome = request.form.get('nome', '').strip() or assunto.nome
        assunto.conteudo = request.form.get('conteudo', '').strip()
        db.session.commit()
        flash("Assunto atualizado!")
        return redirect(url_for('listar_assuntos'))
    return render_template("editar_assunto.html", assunto=assunto)

@app.route('/apagar_assunto/<int:id>')
def apagar_assunto(id):
    assunto = Assunto.query.get_or_404(id)
    db.session.delete(assunto)
    db.session.commit()
    flash("Assunto removido!")
    return redirect(url_for('listar_assuntos'))

# CADASTRO E EDIÇÃO DE ATIVIDADES
@app.route('/cadastrar_atividade', methods=['GET', 'POST'])
def cadastrar_atividade():
    assuntos = Assunto.query.all()
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip() or "Atividade sem nome"
        dificuldade = request.form.get('dificuldade', 'Fácil')
        assunto_id = request.form.get('assunto_id')
        if not assunto_id:
            flash("Selecione o assunto da atividade!")
            return redirect(url_for('cadastrar_atividade'))
        nova = Atividade(nome=nome, dificuldade=dificuldade, assunto_id=assunto_id)
        db.session.add(nova)
        db.session.commit()
        flash("Atividade cadastrada!")
        return redirect(url_for('listar_atividades'))
    atividades = Atividade.query.all()
    return render_template("cadastrar_atividade.html", assuntos=assuntos, atividades=atividades)

@app.route('/ver_atividade/<int:id>')
def ver_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    return render_template("ver_atividade.html", atividade=atividade)

@app.route('/responder_atividade/<int:id>', methods=['GET', 'POST'])
def responder_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    if request.method == 'POST':
        acertos = 0
        total = len(atividade.questoes)
        resultado_questoes = []
        for q in atividade.questoes:
            resp_aluno = request.form.get(f"resposta_{q.id}", "").upper().strip()
            resp_correta = q.resposta_correta.upper().strip() if q.resposta_correta else ""
            acertou = (resp_aluno == resp_correta)
            if acertou: acertos += 1
            resultado_questoes.append({
                "questao": q,
                "resposta_aluno": resp_aluno,
                "resposta_correta": resp_correta,
                "acertou": acertou
            })
        nota = round((acertos / total) * 10, 1) if total > 0 else 0
        return render_template("resultado_atividade.html",
            atividade=atividade,
            resultado_questoes=resultado_questoes,
            acertos=acertos,
            total=total,
            nota=nota)
    return render_template("responder_atividade.html", atividade=atividade)

@app.route('/editar_atividade/<int:id>', methods=['GET', 'POST'])
def editar_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    assuntos = Assunto.query.all()
    if request.method == 'POST':
        atividade.nome = request.form.get('nome', '').strip() or atividade.nome
        atividade.dificuldade = request.form.get('dificuldade', atividade.dificuldade)
        atividade.assunto_id = request.form.get('assunto_id', atividade.assunto_id)
        db.session.commit()
        flash("Atividade atualizada!")
        return redirect(url_for('listar_atividades'))
    return render_template("editar_atividade.html", atividade=atividade, assuntos=assuntos)

@app.route('/apagar_atividade/<int:id>')
def apagar_atividade(id):
    atividade = Atividade.query.get_or_404(id)
    db.session.delete(atividade)
    db.session.commit()
    flash("Atividade removida!")
    return redirect(url_for('listar_atividades'))

# ROTA NOVA QUESTÃO
@app.route('/nova_questao', methods=['GET', 'POST'])
def nova_questao():
    if request.method == 'POST':
        atividade_id = request.form.get('atividade_id')
        enunciado = request.form.get('enunciado', '').strip()
        a = request.form.get('alternativa_a', '').strip()
        b = request.form.get('alternativa_b', '').strip()
        c = request.form.get('alternativa_c', '').strip()
        d = request.form.get('alternativa_d', '').strip()
        e = request.form.get('alternativa_e', '').strip()
        correta = request.form.get('resposta_correta', '').upper().strip()
        
        if atividade_id and enunciado and correta in ['A','B','C','D','E']:
            nova = Questao(
                enunciado=enunciado,
                alternativa_a=a, alternativa_b=b, alternativa_c=c,
                alternativa_d=d, alternativa_e=e,
                resposta_correta=correta, atividade_id=atividade_id
            )
            db.session.add(nova)
            db.session.commit()
            flash("Questão cadastrada com sucesso!")
        else:
            flash("Preencha todos os campos corretamente!")
        return redirect(url_for('listar_questoes'))
    
    atividades = Atividade.query.all()
    return render_template("nova_questao.html", atividades=atividades)

# GERENCIAR QUESTÕES
@app.route('/listar_questoes', methods=['GET', 'POST'])
def listar_questoes():
    if request.method == 'POST':
        atividade_id = request.form.get('atividade_id')
        enunciado = request.form.get('enunciado', '').strip()
        a = request.form.get('alternativa_a', '').strip()
        b = request.form.get('alternativa_b', '').strip()
        c = request.form.get('alternativa_c', '').strip()
        d = request.form.get('alternativa_d', '').strip()
        e = request.form.get('alternativa_e', '').strip()
        correta = request.form.get('resposta_correta', '').upper().strip()
        if atividade_id and enunciado and correta in ['A','B','C','D','E']:
            nova = Questao(
                enunciado=enunciado,
                alternativa_a=a, alternativa_b=b, alternativa_c=c,
                alternativa_d=d, alternativa_e=e,
                resposta_correta=correta, atividade_id=atividade_id
            )
            db.session.add(nova)
            db.session.commit()
            flash("Questão cadastrada!")
        else:
            flash("Preencha todos os campos corretamente!")
        return redirect(url_for('listar_questoes'))
    questoes = Questao.query.all()
    atividades = Atividade.query.all()
    return render_template("listar_questoes.html", questoes=questoes, atividades=atividades)

@app.route('/editar_questao/<int:id>', methods=['GET', 'POST'])
def editar_questao(id):
    questao = Questao.query.get_or_404(id)
    atividades = Atividade.query.all()
    if request.method == 'POST':
        questao.atividade_id = request.form.get('atividade_id')
        questao.enunciado = request.form.get('enunciado', '').strip()
        questao.alternativa_a = request.form.get('alternativa_a', '').strip()
        questao.alternativa_b = request.form.get('alternativa_b', '').strip()
        questao.alternativa_c = request.form.get('alternativa_c', '').strip()
        questao.alternativa_d = request.form.get('alternativa_d', '').strip()
        questao.alternativa_e = request.form.get('alternativa_e', '').strip()
        questao.resposta_correta = request.form.get('resposta_correta', '').upper().strip()
        db.session.commit()
        flash("Questão atualizada com sucesso!")
        return redirect(url_for('listar_questoes'))
    return render_template("editar_questao.html", questao=questao, atividades=atividades)

@app.route('/apagar_questao/<int:id>')
def apagar_questao(id):
    q = Questao.query.get_or_404(id)
    db.session.delete(q)
    db.session.commit()
    flash("Questão removida!")
    return redirect(url_for('listar_questoes'))

# ROTAS DA PÁGINA GRAMÁTICA
@app.route("/pontuacao")
def pontuacao(): return render_template("pontuacao.html")

@app.route("/periodo_simples_e_composto")
def periodo_simples_e_composto(): return render_template("periodo_simples_e_composto.html")

@app.route("/classificacao_de_palavras")
def classificacao_de_palavras(): return render_template("classificacao_de_palavras.html")

# ROTAS DA PÁGINA ATIVIDADES
@app.route("/att_pontuacao")
def att_pontuacao(): return render_template("att_pontuacao.html")

@app.route("/att_periodo_simples")
def att_periodo_simples(): return render_template("att_periodo_simples.html")

@app.route("/att_periodo_composto")
def att_periodo_composto(): return render_template("att_periodo_composto.html")

@app.route("/att_classificacao_de_palavras")
def att_classificacao_de_palavras(): return render_template("att_classificacao_de_palavras.html")


# ROTAS DAS ATIVIDADES DE SINTAXE
@app.route("/atividade1")
def atividade1(): return render_template("atividade1.html")
@app.route("/atividade2")
def atividade2(): return render_template("atividade2.html")
@app.route("/atividade3")
def atividade3(): return render_template("atividade3.html")
@app.route("/atividade4")
def atividade4(): return render_template("atividade4.html")
@app.route("/atividade5")
def atividade5(): return render_template("atividade5.html")
@app.route("/atividade6")
def atividade6(): return render_template("atividade6.html")
@app.route("/atividade7")
def atividade7(): return render_template("atividade7.html")
@app.route("/atividade8")
def atividade8(): return render_template("atividade8.html")
@app.route("/atividade9")
def atividade9(): return render_template("atividade9.html")

# ROTAS DOS CONTEUDOS DE SINTAXE
@app.route("/sujeito_detalhe")
def sujeito_detalhe(): return render_template("sujeito_detalhe.html")
@app.route("/predicado_detalhe")
def predicado_detalhe(): return render_template("predicado_detalhe.html")
@app.route("/aposto_detalhe")
def aposto_detalhe(): return render_template("aposto_detalhe.html")
@app.route("/complemento_verbal_detalhe")
def complemento_verbal_detalhe(): return render_template("complemento_verbal_detalhe.html")
@app.route("/complemento_nominal_detalhe")
def complemento_nominal_detalhe(): return render_template("complemento_nominal_detalhe.html")
@app.route("/agente_da_passiva_detalhe")
def agente_da_passiva_detalhe(): return render_template("agente_da_passiva_detalhe.html")
@app.route("/adjunto_adnominal_detalhe")
def adjunto_adnominal_detalhe(): return render_template("adjunto_adnominal_detalhe.html")
@app.route("/adjunto_adverbial_detalhe")
def adjunto_adverbial_detalhe(): return render_template("adjunto_adverbial_detalhe.html")
@app.route("/revisao_geral_detalhe")
def revisao_geral_detalhe(): return render_template("revisao_geral_detalhe.html")

# ROTAS DE LOGIN SUAP
@app.route("/auth/suap")
def auth_suap():
    redirect_uri = url_for("auth_suap_callback", _external=True)
    return suap.authorize_redirect(redirect_uri)

@app.route("/auth/suap/callback")
def auth_suap_callback():
    if request.args.get("error"):
        flash(f"Falha no login SUAP: {request.args.get('error')}")
        return redirect(url_for("index"))
    try:
        token = suap.authorize_access_token()
    except OAuthError as e:
        flash(f"Falha no login SUAP: {e.error}")
        return redirect(url_for("index"))
    try:
        resp = suap.get(SUAP_USER_INFO_ENDPOINT, token=token)
        resp.raise_for_status()
        dados = resp.json()
    except RequestException:
        flash("Falha ao buscar os dados do usuário no SUAP.")
        return redirect(url_for("index"))
    foto = dados.get("foto")
    if foto and foto.startswith("/"):
        foto = f"{SUAP_BASE_URL}{foto}"
    session["usuario_suap"] = {
        "nome": dados.get("nome_usual") or dados.get("nome"),
        "email": dados.get("email"),
        "matricula": dados.get("matricula") or dados.get("identificacao"),
        "tipo_vinculo": dados.get("tipo_vinculo") or dados.get("tipo_usuario"),
        "foto": foto,
    }
    return redirect(url_for("usuario"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# EXECUÇÃO
if __name__ == "__main__":
    app.run(debug=True)