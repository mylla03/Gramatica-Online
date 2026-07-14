from database import db

class Assunto(db.Model):
    __tablename__ = "assunto"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    conteudo = db.Column(db.Text, nullable=True)
    imagem = db.Column(db.String(255), nullable=True)
    arquivo_pdf = db.Column(db.String(255), nullable=True)

    atividades = db.relationship("Atividade", back_populates="assunto", lazy=True)


class Atividade(db.Model):
    __tablename__ = "atividade"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=True)
    dificuldade = db.Column(db.String(50), nullable=True)
    assunto_id = db.Column(db.Integer, db.ForeignKey("assunto.id"), nullable=True)

    assunto = db.relationship("Assunto", back_populates="atividades")
    questoes = db.relationship("Questao", back_populates="atividade", lazy=True, cascade="all, delete-orphan")


class Questao(db.Model):
    __tablename__ = "questao"
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.Text, nullable=False)
    alternativa_a = db.Column(db.Text, nullable=True)
    alternativa_b = db.Column(db.Text, nullable=True)
    alternativa_c = db.Column(db.Text, nullable=True)
    alternativa_d = db.Column(db.Text, nullable=True)
    alternativa_e = db.Column(db.Text, nullable=True)
    resposta_correta = db.Column(db.String(1), nullable=True)
    atividade_id = db.Column(db.Integer, db.ForeignKey("atividade.id"), nullable=True)

    atividade = db.relationship("Atividade", back_populates="questoes")