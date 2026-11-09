from database import db
from models import Questao, Atividade
from flask import current_app  
from sqlalchemy.exc import IntegrityError


class QuestaoServico:

    @staticmethod
    def listar_paginado(pagina=1):
        """Retorna questões paginadas"""
        itens_por_pagina = current_app.config['ITENS_POR_PAGINA']
        return Questao.query.order_by(Questao.id.desc()).paginate(
            page=pagina,
            per_page=itens_por_pagina,
            error_out=False
        )

    @staticmethod
    def listar_todas():
        return Questao.query.all()

    @staticmethod
    def listar_atividades():
        return Atividade.query.all()

    @staticmethod
    def buscar_por_id(questao_id):
        return Questao.query.get_or_404(questao_id)

    @staticmethod
    def criar(enunciado, alternativa_a, alternativa_b, alternativa_c,
              alternativa_d, alternativa_e, resposta_correta, atividade_id):
        nova_questao = Questao(
            enunciado=enunciado,
            alternativa_a=alternativa_a,
            alternativa_b=alternativa_b,
            alternativa_c=alternativa_c,
            alternativa_d=alternativa_d,
            alternativa_e=alternativa_e,
            resposta_correta=resposta_correta,
            atividade_id=atividade_id
        )
        db.session.add(nova_questao)
        db.session.commit()
        return nova_questao

    @staticmethod
    def atualizar(questao, **dados):
        for chave, valor in dados.items():
            setattr(questao, chave, valor)
        db.session.commit()
        return questao

    @staticmethod
    def excluir(questao):
        try:
            db.session.delete(questao)
            db.session.commit()
            return True, None
        except IntegrityError:
            db.session.rollback()
            return False, "Não foi possível remover a questão."
