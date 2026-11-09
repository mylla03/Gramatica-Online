from database import db
from models import Atividade, Assunto
from flask import current_app  
from sqlalchemy.exc import IntegrityError


class AtividadeServico:

    @staticmethod
    def listar_paginado(pagina=1):
        """Retorna atividades paginadas"""
        itens_por_pagina = current_app.config['ITENS_POR_PAGINA']
        return Atividade.query.order_by(Atividade.id.desc()).paginate(
            page=pagina,
            per_page=itens_por_pagina,
            error_out=False
        )

    @staticmethod
    def listar_todos():
        return Atividade.query.all()

    @staticmethod
    def listar_com_assuntos():
        atividades = Atividade.query.all()
        assuntos = Assunto.query.all()
        return atividades, assuntos

    @staticmethod
    def buscar_por_id(atividade_id):
        return Atividade.query.get_or_404(atividade_id)

    @staticmethod
    def criar(nome, dificuldade, assunto_id, tipo="USUARIO"):
        nova_atividade = Atividade(
            nome=nome,
            dificuldade=dificuldade,
            assunto_id=assunto_id,
            tipo=tipo
        )
        db.session.add(nova_atividade)
        db.session.commit()
        return nova_atividade

    @staticmethod
    def atualizar(atividade, **dados):
        for chave, valor in dados.items():
            setattr(atividade, chave, valor)
        db.session.commit()
        return atividade

    @staticmethod
    def excluir(atividade):
        try:
            db.session.delete(atividade)
            db.session.commit()
            return True, None
        except IntegrityError:
            db.session.rollback()
            return False, "Existem questões vinculadas a esta atividade. Remova-as primeiro."
