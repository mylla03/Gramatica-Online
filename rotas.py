from flask import render_template, request, redirect, url_for, flash, session
from database import db
from models import Assunto, Atividade, Questao, ResultadoAtividade
from sqlalchemy import func
from werkzeug.utils import secure_filename
import os
from sqlalchemy.exc import IntegrityError 
from formularios import AssuntoForm, EditarAssuntoForm, AtividadeForm, QuestaoForm


# IMPORTA DO APP
from app import (
    arquivo_permitido,
    suap,
    SUAP_BASE_URL,
    SUAP_USER_INFO_ENDPOINT,
    OAuthError,
    RequestException
)

# FUNÇÕES DE VERIFICAÇÃO DE ACESSO
def verificar_login():
    if "usuario_suap" not in session:
        flash("Faça login com o SUAP para acessar o sistema.")
        return redirect(url_for("index"))
    return None

def verificar_professor():
    # REMOVER a linha 'return None' abaixo quando terminar os testes
    return None
    # -------------------------------------------------
    redir = verificar_login()
    if redir:
        return redir
    tipo = session["usuario_suap"].get("tipo_vinculo", "")
    if "professor" not in tipo.lower():
        flash("Acesso restrito aos professores.")
        return redirect(url_for("usuario"))
    return None

# FUNÇÃO AUXILIAR
def salvar_primeira_tentativa(atividade_id, acertos, total):
    if "usuario_suap" not in session:
        return False

    usuario = session["usuario_suap"]
    matricula = usuario["matricula"]
    nome = usuario["nome"]

    ja_existe = ResultadoAtividade.query.filter_by(
        usuario_matricula=matricula,
        atividade_numero=atividade_id
    ).first()

    if ja_existe:
        return False

    nota = round((acertos / total) * 10, 1) if total > 0 else 0
    novo = ResultadoAtividade(
        usuario_nome=nome,
        usuario_matricula=matricula,
        atividade_numero=atividade_id,
        nota=nota,
        acertos=acertos,
        total_questoes=total
    )
    db.session.add(novo)
    db.session.commit()
    return True

# REGISTRO DAS ROTAS
def registrar_rotas(app):

    # ROTAS PRINCIPAIS
    @app.route("/")
    def index():
        if "usuario_suap" in session:
            return redirect(url_for("usuario"))
        else:
            return render_template("index.html")

    @app.route("/login")
    def login():
        return redirect(url_for("auth_suap"))

    @app.route("/usuario")
    def usuario():
        redir = verificar_login()
        if redir: return redir
        return render_template("usuario.html")

    @app.route("/escolha")
    def escolha():
        redir = verificar_login()
        if redir: return redir
        return render_template("escolha.html")

    @app.route("/gramatica")
    def gramatica():
        redir = verificar_login()
        if redir: return redir
        try:
            assuntos = Assunto.query.all()
            return render_template("gramatica.html", assuntos=assuntos)
        except Exception as e:
            print("ERRO GRAMATICA:", str(e))
            flash("Erro ao carregar assuntos.")
            return render_template("gramatica.html", assuntos=[])

    @app.route("/atividades")
    def atividades():
        redir = verificar_login()
        if redir: return redir
        try:
            atividades = Atividade.query.all()
            return render_template("atividades.html", atividades=atividades)
        except Exception as e:
            print("ERRO ATIVIDADES:", str(e))
            flash("Erro ao carregar atividades.")
            return render_template("atividades.html", atividades=[])

    @app.route('/listar_atividades')
    def listar_atividades():
        redir = verificar_professor()
        if redir: return redir
        try:
            atividades = Atividade.query.all()
            assuntos = Assunto.query.all()
            return render_template("listar_atividades.html", atividades=atividades, assuntos=assuntos)
        except Exception as e:
            print("ERRO LISTAR ATIVIDADES:", str(e))
            flash("Erro ao carregar atividades.")
            return redirect(url_for('atividades'))

    @app.route('/listar_assuntos')
    def listar_assuntos():
        redir = verificar_professor()
        if redir: return redir
        try:
            assuntos = Assunto.query.all()
            return render_template("listar_assuntos.html", assuntos=assuntos)
        except Exception as e:
            print("ERRO LISTAR ASSUNTOS:", str(e))
            flash("Erro ao carregar.")
            return redirect(url_for('gramatica'))

    @app.route('/novo_assunto', methods=['GET', 'POST'])
    def novo_assunto():
        redir = verificar_professor()
        if redir: return redir
        
        form = AssuntoForm()
        
        if form.validate_on_submit():
            nome = form.nome.data.strip()
            
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

            novo = Assunto(
                nome=nome,
                conteudo=form.conteudo.data.strip(),
                arquivo_pdf=caminho_pdf,
                imagem=caminho_img
            )
            db.session.add(novo)
            db.session.commit()
            flash("Assunto cadastrado com sucesso!")
            return redirect(url_for('listar_assuntos'))
        
        return render_template("novo_assunto.html", form=form)

    @app.route('/assunto/<int:id>')
    def assunto_dinamico(id):
        redir = verificar_login()
        if redir: return redir
        assunto = Assunto.query.get_or_404(id)
        return render_template("assunto_dinamico.html", assunto=assunto)

    @app.route('/ver_assunto/<int:id>')
    def ver_assunto(id):
        redir = verificar_login()
        if redir: return redir
        assunto = Assunto.query.get_or_404(id)
        return render_template("ver_assunto.html", assunto=assunto)

    @app.route('/editar_assunto/<int:id>', methods=['GET', 'POST'])
    def editar_assunto(id):
        redir = verificar_professor()
        if redir: return redir
        assunto = Assunto.query.get_or_404(id)
        
        form = EditarAssuntoForm(obj=assunto)
        
        if form.validate_on_submit():
            assunto.nome = form.nome.data.strip()
            assunto.conteudo = form.conteudo.data.strip()
            db.session.commit()
            flash("Assunto atualizado!")
            return redirect(url_for('listar_assuntos'))
        
        return render_template("editar_assunto.html", assunto=assunto, form=form)


    @app.route('/apagar_assunto/<int:id>')
    def apagar_assunto(id):
        redir = verificar_professor()
        if redir: return redir
        
        assunto = Assunto.query.get_or_404(id)
        try:
            db.session.delete(assunto)
            db.session.commit()
            flash("Assunto removido com sucesso!")
        except IntegrityError:
            db.session.rollback()  # Desfaz a tentativa
            flash("Não é possível excluir este assunto! "
                  "Existem atividades vinculadas a ele. "
                  "Remova as atividades primeiro.")
        return redirect(url_for('listar_assuntos'))

    @app.route('/cadastrar_atividade', methods=['GET', 'POST'])
    def cadastrar_atividade():
        redir = verificar_professor()
        if redir: return redir
        
        form = AtividadeForm()
        form.assunto_id.choices = [(a.id, a.nome) for a in Assunto.query.all()]
        
        if form.validate_on_submit():
            nova = Atividade(
                nome=form.nome.data.strip(),
                dificuldade=form.dificuldade.data,
                assunto_id=form.assunto_id.data,
                tipo="USUARIO"
            )
            db.session.add(nova)
            db.session.commit()
            flash("Atividade cadastrada!")
            return redirect(url_for('listar_atividades'))

        return render_template("cadastrar_atividade.html", form=form)


    @app.route('/ver_atividade/<int:id>')
    def ver_atividade(id):
        redir = verificar_login()
        if redir: return redir
        atividade = Atividade.query.get_or_404(id)
        return render_template("ver_atividade.html", atividade=atividade)

    @app.route('/responder_atividade/<int:id>', methods=['GET', 'POST'])
    def responder_atividade(id):
        redir = verificar_login()
        if redir: return redir
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
        redir = verificar_professor()
        if redir: return redir
        atividade = Atividade.query.get_or_404(id)
        
        form = AtividadeForm(obj=atividade)
        form.assunto_id.choices = [(a.id, a.nome) for a in Assunto.query.all()]
        
        if form.validate_on_submit():
            form.populate_obj(atividade)
            db.session.commit()
            flash("Atividade atualizada!")
            return redirect(url_for('listar_atividades'))
        
        return render_template("editar_atividade.html", atividade=atividade, form=form)


    @app.route('/apagar_atividade/<int:id>')
    def apagar_atividade(id):
        redir = verificar_professor()
        if redir: return redir
        
        atividade = Atividade.query.get_or_404(id)
        try:
            db.session.delete(atividade)
            db.session.commit()
            flash("Atividade removida com sucesso!")
        except IntegrityError:
            db.session.rollback()
            flash("Não é possível excluir esta atividade! "
                  "Existem questões vinculadas a ela. "
                  "Remova as questões primeiro.")
        return redirect(url_for('listar_atividades'))


    @app.route('/nova_questao', methods=['GET', 'POST'])
    def nova_questao():
        redir = verificar_professor()
        if redir: return redir
        
        form = QuestaoForm()
        form.atividade_id.choices = [(a.id, a.nome) for a in Atividade.query.all()]
        
        if form.validate_on_submit():
            nova = Questao(
                enunciado=form.enunciado.data.strip(),
                alternativa_a=form.alternativa_a.data.strip(),
                alternativa_b=form.alternativa_b.data.strip(),
                alternativa_c=form.alternativa_c.data.strip(),
                alternativa_d=form.alternativa_d.data.strip(),
                alternativa_e=form.alternativa_e.data.strip(),
                resposta_correta=form.resposta_correta.data,
                atividade_id=form.atividade_id.data
            )
            db.session.add(nova)
            db.session.commit()
            flash("Questão cadastrada com sucesso!")
            return redirect(url_for('listar_questoes'))

        return render_template("nova_questao.html", form=form)


    @app.route('/listar_questoes', methods=['GET', 'POST'])
    def listar_questoes():
        redir = verificar_professor()
        if redir: return redir
        
        form = QuestaoForm()
        form.atividade_id.choices = [(a.id, a.nome) for a in Atividade.query.all()]
        
        if form.validate_on_submit():
            nova = Questao(
                enunciado=form.enunciado.data.strip(),
                alternativa_a=form.alternativa_a.data.strip(),
                alternativa_b=form.alternativa_b.data.strip(),
                alternativa_c=form.alternativa_c.data.strip(),
                alternativa_d=form.alternativa_d.data.strip(),
                alternativa_e=form.alternativa_e.data.strip(),
                resposta_correta=form.resposta_correta.data,
                atividade_id=form.atividade_id.data
            )
            db.session.add(nova)
            db.session.commit()
            flash("Questão cadastrada!")
            return redirect(url_for('listar_questoes'))
        
        questoes = Questao.query.all()
        return render_template("listar_questoes.html", questoes=questoes, form=form)

    @app.route('/editar_questao/<int:id>', methods=['GET', 'POST'])
    def editar_questao(id):
        redir = verificar_professor()
        if redir: return redir
        questao = Questao.query.get_or_404(id)
        
        form = QuestaoForm(obj=questao)
        form.atividade_id.choices = [(a.id, a.nome) for a in Atividade.query.all()]
        
        if form.validate_on_submit():
            form.populate_obj(questao)
            db.session.commit()
            flash("Questão atualizada com sucesso!")
            return redirect(url_for('listar_questoes'))
        
        return render_template("editar_questao.html", questao=questao, form=form)


    @app.route('/apagar_questao/<int:id>')
    def apagar_questao(id):
        redir = verificar_professor()
        if redir: return redir
        q = Questao.query.get_or_404(id)
        try:
            db.session.delete(q)
            db.session.commit()
            flash("Questão removida com sucesso!")
        except IntegrityError:
            db.session.rollback()
            flash("Não foi possível remover a questão!")
        return redirect(url_for('listar_questoes'))


    # ROTAS DE CONTEÚDO — ARQUIVOS INDIVIDUAIS
    @app.route("/pontuacao")
    def pontuacao(): return render_template("pontuacao.html")
    @app.route("/periodo_simples_e_composto")
    def periodo_simples_e_composto(): return render_template("periodo_simples_e_composto.html")
    @app.route("/classificacao_de_palavras")
    def classificacao_de_palavras(): return render_template("classificacao_de_palavras.html")
    @app.route("/att_pontuacao")
    def att_pontuacao(): return render_template("att_pontuacao.html")
    @app.route("/att_periodo_simples")
    def att_periodo_simples(): return render_template("att_periodo_simples.html")
    @app.route("/att_periodo_composto")
    def att_periodo_composto(): return render_template("att_periodo_composto.html")
    @app.route("/att_classificacao_de_palavras")
    def att_classificacao_de_palavras(): return render_template("att_classificacao_de_palavras.html")

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

    @app.route("/atividade/<int:atividade_id>", methods=["GET", "POST"])
    def atividade_dinamica(atividade_id):
        redir = verificar_login()
        if redir: return redir
        atividade = Atividade.query.get_or_404(atividade_id)
        
        if request.method == "POST":
            acertos = 0
            total = len(atividade.questoes)
            resultados = {}
            
            for idx, q in enumerate(atividade.questoes, 1):
                resp_aluno = request.form.get(f"q{idx}", "").upper().strip()
                resp_correta = q.resposta_correta.upper().strip() if q.resposta_correta else ""
                acertou = (resp_aluno == resp_correta)
                resultados[idx] = acertou
                if acertou:
                    acertos += 1
            
            nota = round((acertos / total) * 10, 1) if total > 0 else 0
            salvar_primeira_tentativa(atividade_id, acertos, total)
            
            return render_template("atividade_dinamica.html", 
                atividade=atividade, 
                enviado=True, 
                respostas_corretas=resultados,
                nota=nota,
                acertos=acertos,
                total=total)
        
        return render_template("atividade_dinamica.html", atividade=atividade, enviado=False)

    @app.route("/sistema/<int:indice>", methods=["GET", "POST"])
    def atividade_sistema(indice):
        redir = verificar_login()
        if redir: return redir
        atividades_sistema = Atividade.query.join(Assunto).filter(
            Assunto.tipo == "SISTEMA"
        ).order_by(Atividade.id).all()
        
        idx = indice - 1
        if idx < 0 or idx >= len(atividades_sistema):
            flash("Atividade não encontrada!")
            return redirect(url_for('atividades'))
        
        atividade = atividades_sistema[idx]
        
        if request.method == "POST":
            acertos = 0
            total = len(atividade.questoes)
            resultados = {}
            
            for i, q in enumerate(atividade.questoes, 1):
                resp_aluno = request.form.get(f"q{i}", "").upper().strip()
                resp_correta = q.resposta_correta.upper().strip() if q.resposta_correta else ""
                acertou = (resp_aluno == resp_correta)
                resultados[i] = acertou
                if acertou:
                    acertos += 1
            
            nota = round((acertos / total) * 10, 1) if total > 0 else 0
            salvar_primeira_tentativa(atividade.id, acertos, total)
            
            return render_template("atividade_dinamica.html",
                atividade=atividade,
                enviado=True,
                respostas_corretas=resultados,
                nota=nota,
                acertos=acertos,
                total=total)
        
        return render_template("atividade_dinamica.html", atividade=atividade, enviado=False)

    @app.route("/ranking")
    def ranking():
        redir = verificar_login()
        if redir: return redir
        resultados = db.session.query(
            ResultadoAtividade.usuario_nome,
            ResultadoAtividade.usuario_matricula,
            func.sum(ResultadoAtividade.nota).label("pontuacao_total"),
            func.count(ResultadoAtividade.id).label("atividades_concluidas")
        ).group_by(
            ResultadoAtividade.usuario_matricula,
            ResultadoAtividade.usuario_nome
        ).order_by(
            db.desc("pontuacao_total")
        ).all()
        
        return render_template("ranking.html", ranking=resultados)

    @app.route("/auth/suap")
    def auth_suap():
        redirect_uri = url_for("auth_suap_callback", _external=True)
        return suap.authorize_redirect(redirect_uri)

    @app.route("/auth/suap/callback")
    def auth_suap_callback():
        if request.args.get("error"):
            flash("Falha no login SUAP: " + request.args.get("error"))
            return redirect(url_for("index"))
        
        try:
            token = suap.authorize_access_token()
        except OAuthError as e:
            flash("Falha no login SUAP: " + e.error)
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
            foto = SUAP_BASE_URL + foto
        
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
