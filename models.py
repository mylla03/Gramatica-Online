from database import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime


class Aluno(db.Model):
    __tablename__ = "aluno"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)

    atividades: so.Mapped[list["AlunoAtividade"]] = so.relationship(
        back_populates="aluno",
        cascade="all, delete-orphan"
    )


class Assunto(db.Model):
    __tablename__ = "assunto"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False, unique=True)

    atividades: so.Mapped[list["Atividade"]] = so.relationship(
        back_populates="assunto",
        cascade="all, delete-orphan"
    )


class Atividade(db.Model):
    __tablename__ = "atividade"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    dificuldade: so.Mapped[str] = so.mapped_column(sa.String(50), nullable=False)

    assunto_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey("assunto.id"),
        nullable=False
    )

    assunto: so.Mapped["Assunto"] = so.relationship(back_populates="atividades")

    questoes: so.Mapped[list["Questao"]] = so.relationship(
        back_populates="atividade",
        cascade="all, delete-orphan"
    )

    alunos: so.Mapped[list["AlunoAtividade"]] = so.relationship(
        back_populates="atividade",
        cascade="all, delete-orphan"
    )


class Questao(db.Model):
    __tablename__ = "questao"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    enunciado: so.Mapped[str] = so.mapped_column(sa.String(255), nullable=False)

    atividade_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey("atividade.id"),
        nullable=False
    )

    atividade: so.Mapped["Atividade"] = so.relationship(back_populates="questoes")


class AlunoAtividade(db.Model):
    __tablename__ = "aluno_atividade"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    aluno_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey("aluno.id"),
        nullable=False
    )

    atividade_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey("atividade.id"),
        nullable=False
    )

    progresso: so.Mapped[int] = so.mapped_column(sa.Integer, default=0)

    data_inicio: so.Mapped[datetime] = so.mapped_column(
        default=datetime.utcnow
    )

    data_fim: so.Mapped[datetime] = so.mapped_column(
        nullable=True
    )

    aluno: so.Mapped["Aluno"] = so.relationship(back_populates="atividades")
    atividade: so.Mapped["Atividade"] = so.relationship(back_populates="alunos")