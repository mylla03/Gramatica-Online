from database import db
from models import Assunto
from flask import current_app
from sqlalchemy.exc import IntegrityError


class AssuntoServico:

    @staticmethod
    def listar_paginado(pagina=1):
        """Retorna assuntos paginados"""
        itens_por_pagina = current_app.config['ITENS_POR_PAGINA']
        return Assunto.query.order_by(Assunto.id.desc()).paginate(
            page=pagina,
            per_page=itens_por_pagina,
            error_out=False
        )

    @staticmethod
    def listar_todos():
        return Assunto.query.all()

    @staticmethod
    def buscar_por_id(assunto_id):
        return Assunto.query.get_or_404(assunto_id)

    @staticmethod
    def criar(nome, conteudo, arquivo_pdf=None, imagem=None, tipo="USUARIO"):
        novo_assunto = Assunto(
            nome=nome,
            conteudo=conteudo,
            arquivo_pdf=arquivo_pdf,
            imagem=imagem,
            tipo=tipo
        )
        db.session.add(novo_assunto)
        db.session.commit()
        return novo_assunto

    @staticmethod
    def atualizar(assunto, nome, conteudo):
        assunto.nome = nome
        assunto.conteudo = conteudo
        db.session.commit()
        return assunto

    @staticmethod
    def excluir(assunto):
        try:
            db.session.delete(assunto)
            db.session.commit()
            return True, None
        except IntegrityError:
            db.session.rollback()
            return False, "Existem atividades vinculadas a este assunto. Remova-as primeiro."
