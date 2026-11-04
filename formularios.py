from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class AssuntoForm(FlaskForm):
    nome = StringField('Nome do Assunto', validators=[
        DataRequired(message="O nome é obrigatório."),
        Length(min=3, max=100, message="Deve ter entre 3 e 100 caracteres.")
    ])
    conteudo = TextAreaField('Conteúdo')
    submit = SubmitField('Salvar Assunto')


class EditarAssuntoForm(FlaskForm):
    nome = StringField('Nome do Assunto', validators=[
        DataRequired(message="O nome é obrigatório."),
        Length(min=3, max=100, message="Deve ter entre 3 e 100 caracteres.")
    ])
    conteudo = TextAreaField('Conteúdo')
    submit = SubmitField('Atualizar Assunto')


class AtividadeForm(FlaskForm):
    nome = StringField('Nome da Atividade', validators=[
        DataRequired(message="O nome é obrigatório."),
        Length(min=3, message="Mínimo de 3 caracteres.")
    ])
    dificuldade = SelectField('Dificuldade', choices=[
        ('Facil', 'Fácil'),
        ('Medio', 'Médio'),
        ('Dificil', 'Difícil')
    ])
    assunto_id = SelectField('Assunto Relacionado', coerce=int, validators=[
        DataRequired(message="Selecione um assunto.")
    ])
    submit = SubmitField('Salvar Atividade')


class QuestaoForm(FlaskForm):
    enunciado = TextAreaField('Enunciado', validators=[
        DataRequired(message="O enunciado é obrigatório."),
        Length(min=10, message="Mínimo de 10 caracteres.")
    ])
    alternativa_a = StringField('Alternativa A', validators=[DataRequired()])
    alternativa_b = StringField('Alternativa B', validators=[DataRequired()])
    alternativa_c = StringField('Alternativa C', validators=[DataRequired()])
    alternativa_d = StringField('Alternativa D', validators=[DataRequired()])
    alternativa_e = StringField('Alternativa E', validators=[DataRequired()])
    resposta_correta = SelectField('Resposta Correta', choices=[
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')
    ], validators=[DataRequired()])
    atividade_id = SelectField('Atividade Vinculada', coerce=int, validators=[
        DataRequired(message="Selecione uma atividade.")
    ])
    submit = SubmitField('Salvar Questão')
