from app import app 
from moldes import Atividade, Questao
from database import db

def inserir_atividades_sistema():
    with app.app_context():
        if Atividade.query.filter_by(tipo="SISTEMA").first():
            print("Atividades do sistema já existem no banco de dados.")
            return

            print("Inserindo atividades do sistema no banco de dados...")

#atividade1#
        atividade1 = Atividade(nome="Atividade 1 - Sujeito",dificuldade="Facil", tipo="SISTEMA")
        db.session.add(atividade1)
        db.session.flush()

        q1 = Questao(
            enunciado="1. Identifique o tipo de sujeito na frase: “Maria foi à padaria pela manhã.”",
            alternativa_a="Sujeito simples",
            alternativa_b="Sujeito composto",
            alternativa_c="Sujeito indeterminado",
            alternativa_d="Sujeito oculto"
            resposta_correta="a",
            atividade_id=atividade1.id
        )
        db.session.add(q1)

        q2 = Questao(
            enunciado="2. Assinale a frase em que o sujeito é oculto:",
            alternativa_a="Ontem compraram muitas frutas.",
            alternativa_b="Estudamos para a prova de português.",
            alternativa_c="Marina e Mariana foram ao mercado.",
            alternativa_d="Havia muitas pessoas na loja."
            resposta_correta="b",
            atividade_id=atividade1.id
        )
        db.session.add(q2)

        q3 = Questao(
            enunciado="3. Em qual alternativa o verbo é impessoal, indicando oração sem sujeito?",
            alternativa_a="Precisa-se de voluntários.",
            alternativa_b="Trabalhamos ontem.",
            alternativa_c="Os alunos terminaram cedo.",
            alternativa_d="Faz muito calor no verão."
            resposta_correta="d",
            atividade_id=atividade1.id
        )
        db.session.add(q3)

        q4 = Questao(
            enunciado="4. Complete a frase corretamente: “________ poucas pessoas no shopping ontem.”",
            alternativa_a="Havia",
            alternativa_b="Haviam",
            alternativa_c="Existiam",
            alternativa_d="Tinha"
            resposta_correta="b",
            atividade_id=atividade1.id
        )
        db.session.add(q4)

        q5 = Questao(
            enunciado="5. Complete a frase com a opção que forma uma oração sem sujeito: “______ três meses que não vou à praia.”",
            alternativa_a="Fazem",
            alternativa_b="Tem",
            alternativa_c="Faz",
            alternativa_d="Estão"
            resposta_correta="c",
            atividade_id=atividade1.id
        )
        db.session.add(q5)
#atividade2#




        db.session.commit()
        print("atividades do sistema inseridas com sucesso no banco de dados.")
if__name_ == "_main_":
    inserir_atividades_sistema()



