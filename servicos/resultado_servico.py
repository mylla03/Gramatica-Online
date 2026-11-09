from database import db
from models import ResultadoAtividade
from flask import session
from sqlalchemy import func


class ResultadoServico:

    @staticmethod
    def salvar_primeira_tentativa(atividade_id, acertos, total):
        """Salva o resultado apenas na PRIMEIRA tentativa"""
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

    @staticmethod
    def listar_ranking():
        """Retorna o ranking ordenado por pontuação total"""
        return db.session.query(
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
