from flask import render_template, request, redirect, url_for, flash, session
from database import db
from models import Assunto, Atividade, Questao, ResultadoAtividade
from sqlalchemy import func
from werkzeug.utils import secure_filename
import os
from sqlalchemy.exc import IntegrityError
from formularios import AssuntoForm, EditarAssuntoForm, AtividadeForm, QuestaoForm

# IMPORTAÇÃO DOS SERVIÇOS
from servicos import (
    AssuntoServico,
    AtividadeServico,
    QuestaoServico,
    ResultadoServico
)

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
    # REMOVA a linha 'return None' abaixo quando terminar os testes
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
            assuntos = AssuntoServico.listar_todos()
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
            atividades = AtividadeServico.listar_todos()
            return render_template("atividades.html", atividades=atividades)
        except Exception as e:
            print("ERRO ATIVIDADES:", str(e))
            flash("Erro ao carregar atividades.")
            return render_template("atividades.html", atividades=[])

    @app.route('/listar_atividades')
    def listar_atividades():
            redir = verificar_professor()
            if redir: return redir
            
            pagina = request.args.get('pagina', 1, type=int)
            try:
                atividades_paginado = AtividadeServico.listar_paginado(pagina)
                assuntos = AssuntoServico.listar_todos()
                return render_template("listar_atividades.html", atividades=atividades_paginado.items, assuntos=assuntos, paginacao=atividades_paginado)
            except Exception as e:
                print("ERRO LISTAR ATIVIDADES:", str(e))
                flash("Erro ao carregar atividades.")
                return redirect(url_for('atividades'))

    @app.route('/listar_assuntos')
    def listar_assuntos():
        redir = verificar_professor()
        if redir: return redir
        
        pagina = request.args.get('pagina', 1, type=int)
        try:
            assuntos_paginado = AssuntoServico.listar_paginado(pagina)
            return render_template("listar_assuntos.html", assuntos=assuntos_paginado.items, paginacao=assuntos_paginado)
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

            AssuntoServico.criar(
                nome=nome,
                conteudo=form.conteudo.data.strip(),
                arquivo_pdf=caminho_pdf,
                imagem=caminho_img
            )
            flash("Assunto cadastrado com sucesso!")
            return redirect(url_for('listar_assuntos'))
        
        return render_template("novo_assunto.html", form=form)

    @app.route('/assunto/<int:id>')
    def assunto_dinamico(id):
        redir = verificar_login()
        if redir: return redir
        assunto = AssuntoServico.buscar_por_id(id)
        return render_template("assunto_dinamico.html", assunto=assunto)

    @app.route('/ver_assunto/<int:id>')
    def ver_assunto(id):
        redir = verificar_login()
        if redir: return redir
        assunto = AssuntoServico.buscar_por_id(id)
        return render_template("ver_assunto.html", assunto=assunto)

    @app.route('/editar_assunto/<int:id>', methods=['GET', 'POST'])
    def editar_assunto(id):
        redir = verificar_professor()
        if redir: return redir
        assunto = AssuntoServico.buscar_por_id(id)
        
        form = EditarAssuntoForm(obj=assunto)
        
        if form.validate_on_submit():
            AssuntoServico.atualizar(
                assunto,
                nome=form.nome.data.strip(),
                conteudo=form.conteudo.data.strip()
            )
            flash("Assunto atualizado!")
            return redirect(url_for('listar_assuntos'))
        
        return render_template("editar_assunto.html", assunto=assunto, form=form)

    @app.route('/apagar_assunto/<int:id>')
    def apagar_assunto(id):
        redir = verificar_professor()
        if redir: return redir
        
        assunto = AssuntoServico.buscar_por_id(id)
        sucesso, erro = AssuntoServico.excluir(assunto)
        if sucesso:
            flash("Assunto removido com sucesso!")
        else:
            flash(f"Não é possível excluir este assunto! {erro}")
        return redirect(url_for('listar_assuntos'))

    @app.route('/cadastrar_atividade', methods=['GET', 'POST'])
    def cadastrar_atividade():
        redir = verificar_professor()
        if redir: return redir
        
        form = AtividadeForm()
        form.assunto_id.choices = [(a.id, a.nome) for a in AssuntoServico.listar_todos()]
        
        if form.validate_on_submit():
            AtividadeServico.criar(
                nome=form.nome.data.strip(),
                dificuldade=form.dificuldade.data,
                assunto_id=form.assunto_id.data
            )
            flash("Atividade cadastrada!")
            return redirect(url_for('listar_atividades'))

        return render_template("cadastrar_atividade.html", form=form)

    @app.route('/ver_atividade/<int:id>')
    def ver_atividade(id):
        redir = verificar_login()
        if redir: return redir
        atividade = AtividadeServico.buscar_por_id(id)
        return render_template("ver_atividade.html", atividade=atividade)

    @app.route('/responder_atividade/<int:id>', methods=['GET', 'POST'])
    def responder_atividade(id):
        redir = verificar_login()
        if redir: return redir
        atividade = AtividadeServico.buscar_por_id(id)
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
        atividade = AtividadeServico.buscar_por_id(id)
        
        form = AtividadeForm(obj=atividade)
        form.assunto_id.choices = [(a.id, a.nome) for a in AssuntoServico.listar_todos()]
        
        if form.validate_on_submit():
            AtividadeServico.atualizar(atividade,
                nome=form.nome.data.strip(),
                dificuldade=form.dificuldade.data,
                assunto_id=form.assunto_id.data
            )
            flash("Atividade atualizada!")
            return redirect(url_for('listar_atividades'))
        
        return render_template("editar_atividade.html", atividade=atividade, form=form)

    @app.route('/apagar_atividade/<int:id>')
    def apagar_atividade(id):
        redir = verificar_professor()
        if redir: return redir
        
        atividade = AtividadeServico.buscar_por_id(id)
        sucesso, erro = AtividadeServico.excluir(atividade)
        if sucesso:
            flash("Atividade removida com sucesso!")
        else:
            flash(f"Não é possível excluir esta atividade! {erro}")
        return redirect(url_for('listar_atividades'))

    @app.route('/nova_questao', methods=['GET', 'POST'])
    def nova_questao():
        redir = verificar_professor()
        if redir: return redir
        
        form = QuestaoForm()
        form.atividade_id.choices = [(a.id, a.nome) for a in QuestaoServico.listar_atividades()]
        
        if form.validate_on_submit():
            QuestaoServico.criar(
                enunciado=form.enunciado.data.strip(),
                alternativa_a=form.alternativa_a.data.strip(),
                alternativa_b=form.alternativa_b.data.strip(),
                alternativa_c=form.alternativa_c.data.strip(),
                alternativa_d=form.alternativa_d.data.strip(),
                alternativa_e=form.alternativa_e.data.strip(),
                resposta_correta=form.resposta_correta.data,
                atividade_id=form.atividade_id.data
            )
            flash("Questão cadastrada com sucesso!")
            return redirect(url_for('listar_questoes'))

        return render_template("nova_questao.html", form=form)

    @app.route('/listar_questoes', methods=['GET', 'POST'])
    def listar_questoes():
        redir = verificar_professor()
        if redir: return redir
        
        form = QuestaoForm()
        form.atividade_id.choices = [(a.id, a.nome) for a in QuestaoServico.listar_atividades()]
        
        if form.validate_on_submit():
            QuestaoServico.criar(
                enunciado=form.enunciado.data.strip(),
                alternativa_a=form.alternativa_a.data.strip(),
                alternativa_b=form.alternativa_b.data.strip(),
                alternativa_c=form.alternativa_c.data.strip(),
                alternativa_d=form.alternativa_d.data.strip(),
                alternativa_e=form.alternativa_e.data.strip(),
                resposta_correta=form.resposta_correta.data,
                atividade_id=form.atividade_id.data
            )
            flash("Questão cadastrada!")
            return redirect(url_for('listar_questoes'))
        
        pagina = request.args.get('pagina', 1, type=int)
        questoes_paginado = QuestaoServico.listar_paginado(pagina)
        return render_template("listar_questoes.html", questoes=questoes_paginado.items, form=form, paginacao=questoes_paginado)

    @app.route('/editar_questao/<int:id>', methods=['GET', 'POST'])
    def editar_questao(id):
        redir = verificar_professor()
        if redir: return redir
        questao = QuestaoServico.buscar_por_id(id)
        
        form = QuestaoForm(obj=questao)
        form.atividade_id.choices = [(a.id, a.nome) for a in QuestaoServico.listar_atividades()]
        
        if form.validate_on_submit():
            QuestaoServico.atualizar(questao,
                enunciado=form.enunciado.data.strip(),
                alternativa_a=form.alternativa_a.data.strip(),
                alternativa_b=form.alternativa_b.data.strip(),
                alternativa_c=form.alternativa_c.data.strip(),
                alternativa_d=form.alternativa_d.data.strip(),
                alternativa_e=form.alternativa_e.data.strip(),
                resposta_correta=form.resposta_correta.data,
                atividade_id=form.atividade_id.data
            )
            flash("Questão atualizada com sucesso!")
            return redirect(url_for('listar_questoes'))
        
        return render_template("editar_questao.html", questao=questao, form=form)

    @app.route('/apagar_questao/<int:id>')
    def apagar_questao(id):
        redir = verificar_professor()
        if redir: return redir
        questao = QuestaoServico.buscar_por_id(id)
        sucesso, erro = QuestaoServico.excluir(questao)
        if sucesso:
            flash("Questão removida com sucesso!")
        else:
            flash(f"Não foi possível remover a questão! {erro}")
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
        atividade = AtividadeServico.buscar_por_id(atividade_id)
        
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
            ResultadoServico.salvar_primeira_tentativa(atividade_id, acertos, total)
            
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
        from models import Assunto
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
            ResultadoServico.salvar_primeira_tentativa(atividade.id, acertos, total)
            
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
        resultados = ResultadoServico.listar_ranking()
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

