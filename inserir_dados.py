from app import app
from models import Assunto, Atividade, Questao
from database import db

def inserir_atividades_sistema():
    with app.app_context():
        if Atividade.query.filter_by(tipo="SISTEMA").first():
            print("Atividades do sistema já existem no banco de dados.")
            return
        
        print("Inserindo assuntos e atividades do sistema...\n")

        # ASSUNTO 1 — Sujeito
        assunto_sujeito = Assunto.query.filter_by(nome="Sujeito").first()
        if not assunto_sujeito:
            assunto_sujeito = Assunto(
                nome="Sujeito",
                conteudo="O sujeito é o ser principal da oração e indica quem participa, pratica ou sofre a ação. Tipos: simples, composto, oculto, indeterminado e oração sem sujeito."
            )
            db.session.add(assunto_sujeito)
            db.session.flush()
            print(" Assunto 1 — Sujeito criado")
        else:
            print(" Assunto 1 — Sujeito já existe")

        atividade1 = Atividade(
            nome="Atividade 1 - Sujeito",
            dificuldade="Fácil",
            tipo="SISTEMA",
            assunto_id=assunto_sujeito.id
        )
        db.session.add(atividade1)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Identifique o tipo de sujeito na frase: 'Maria foi à padaria pela manhã.'",
            alternativa_a="Sujeito simples", alternativa_b="Sujeito composto",
            alternativa_c="Sujeito indeterminado", alternativa_d="Sujeito oculto",
            resposta_correta="a", atividade_id=atividade1.id))
        db.session.add(Questao(enunciado="2. Assinale a frase em que o sujeito é oculto:",
            alternativa_a="Ontem compraram muitas frutas.", alternativa_b="Estudamos para a prova de português.",
            alternativa_c="Marina e Mariana foram ao mercado.", alternativa_d="Havia muitas pessoas na loja.",
            resposta_correta="b", atividade_id=atividade1.id))
        db.session.add(Questao(enunciado="3. Em qual alternativa o verbo é impessoal, indicando oração sem sujeito?",
            alternativa_a="Precisa-se de voluntários.", alternativa_b="Trabalhamos ontem.",
            alternativa_c="Os alunos terminaram cedo.", alternativa_d="Faz muito calor no verão.",
            resposta_correta="d", atividade_id=atividade1.id))
        db.session.add(Questao(enunciado="4. Complete a frase corretamente: '________ poucas pessoas no shopping ontem.'",
            alternativa_a="Havia", alternativa_b="Haviam", alternativa_c="Existiam", alternativa_d="Tinha",
            resposta_correta="a", atividade_id=atividade1.id))
        db.session.add(Questao(enunciado="5. Complete a frase com a opção que forma uma oração sem sujeito: '______ três meses que não vou à praia.'",
            alternativa_a="Fazem", alternativa_b="Tem", alternativa_c="Faz", alternativa_d="Estão",
            resposta_correta="c", atividade_id=atividade1.id))

        # ASSUNTO 2 — Predicado
        assunto_predicado = Assunto.query.filter_by(nome="Predicado").first()
        if not assunto_predicado:
            assunto_predicado = Assunto(
                nome="Predicado",
                conteudo="O predicado é a parte da oração que contém aquilo que se afirma sobre o sujeito. Tipos: verbal (núcleo verbo de ação), nominal (núcleo nome/adjetivo + verbo de ligação) e verbo-nominal (combina ação e característica)."
            )
            db.session.add(assunto_predicado)
            db.session.flush()
            print(" Assunto 2 — Predicado criado")
        else:
            print(" Assunto 2 — Predicado já existe")

        atividade2 = Atividade(
            nome="Atividade 2 - Predicado",
            dificuldade="Fácil",
            tipo="SISTEMA",
            assunto_id=assunto_predicado.id
        )
        db.session.add(atividade2)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Qual é o sujeito da frase: 'As meninas chegaram cedo'?",
            alternativa_a="chegaram cedo", alternativa_b="cedo", alternativa_c="As meninas", alternativa_d="chegaram",
            resposta_correta="c", atividade_id=atividade2.id))
        db.session.add(Questao(enunciado="2. Em 'Choveu muito ontem', o sujeito é:",
            alternativa_a="oculto", alternativa_b="simples", alternativa_c="inexistente", alternativa_d="composto",
            resposta_correta="c", atividade_id=atividade2.id))
        db.session.add(Questao(enunciado="3. Na frase 'João e Maria estudaram juntos', o sujeito é classificado como:",
            alternativa_a="simples", alternativa_b="oculto", alternativa_c="inexistente", alternativa_d="composto",
            resposta_correta="d", atividade_id=atividade2.id))
        db.session.add(Questao(enunciado="4. Em 'Fomos ao cinema ontem', o sujeito é:",
            alternativa_a="simples", alternativa_b="oculto", alternativa_c="inexistente", alternativa_d="composto",
            resposta_correta="b", atividade_id=atividade2.id))
        db.session.add(Questao(enunciado="5. Qual alternativa apresenta sujeito simples?",
            alternativa_a="Ana e Pedro viajaram.", alternativa_b="Choveu bastante.",
            alternativa_c="O cachorro latiu alto.", alternativa_d="Fizeram a tarefa.",
            resposta_correta="c", atividade_id=atividade2.id))

        # ASSUNTO 3 — Aposto
        assunto_aposto = Assunto.query.filter_by(nome="Aposto").first()
        if not assunto_aposto:
            assunto_aposto = Assunto(
                nome="Aposto",
                conteudo="Aposto é o termo que aparece junto de um substantivo para especificar, explicar, resumir ou transmitir informações sobre ele. Tipos: explicativo, especificativo, resumitivo e distributivo. Diferencia-se do vocativo, que serve apenas para chamar alguém."
            )
            db.session.add(assunto_aposto)
            db.session.flush()
            print(" Assunto 3 — Aposto criado")
        else:
            print(" Assunto 3 — Aposto já existe")

        atividade3 = Atividade(
            nome="Atividade 3 - Aposto",
            dificuldade="Fácil",
            tipo="SISTEMA",
            assunto_id=assunto_aposto.id
        )
        db.session.add(atividade3)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Identifique o tipo de aposto na frase: 'Gael, meu amigo, chegou atrasado hoje.'",
            alternativa_a="Aposto especificativo", alternativa_b="Aposto explicativo",
            alternativa_c="Aposto resumitivo", alternativa_d="Aposto distributivo",
            resposta_correta="b", atividade_id=atividade3.id))
        db.session.add(Questao(enunciado="2. Na frase 'Os estudantes que se deram bem, estudaram para a prova', o trecho destacado é:",
            alternativa_a="Aposto explicativo", alternativa_b="Aposto especificativo",
            alternativa_c="Aposto resumitivo", alternativa_d="Vocativo",
            resposta_correta="a", atividade_id=atividade3.id))
        db.session.add(Questao(enunciado="3. Qual frase contém aposto resumitivo?",
            alternativa_a="Catharina e Manuella, ambas amigas, foram embora cedo da pizzaria.",
            alternativa_b="A menina de vestido vermelho está chamando você.",
            alternativa_c="Alice, a professora de história, faltou hoje.",
            alternativa_d="Fungos, plantas, animais, todos esses seres fazem parte dos ecossistemas.",
            resposta_correta="d", atividade_id=atividade3.id))
        db.session.add(Questao(enunciado="4. Assinale a alternativa com aposto distributivo:",
            alternativa_a="As meninas, muito animadas, dançaram juntas.",
            alternativa_b="A menina que venceu a prova ganhou medalha de ouro.",
            alternativa_c="Guilherme e Miguel, cada um com seu material, começaram o trabalho.",
            alternativa_d="Lavínia, minha prima, ama viajar.",
            resposta_correta="c", atividade_id=atividade3.id))
        db.session.add(Questao(enunciado="5. Em qual frase o termo destacado é vocativo, e não aposto?",
            alternativa_a="Miguel, o vizinho novo, precisa de ajuda.",
            alternativa_b="O menino que chegou agora é meu amigo.",
            alternativa_c="Livros, cadernos, tudo isso estava na mochila.",
            alternativa_d="Meninas, prestem atenção aqui!",
            resposta_correta="d", atividade_id=atividade3.id))

        # ASSUNTO 4 — Complemento Verbal
        assunto_comp_verbal = Assunto.query.filter_by(nome="Complemento Verbal").first()
        if not assunto_comp_verbal:
            assunto_comp_verbal = Assunto(
                nome="Complemento Verbal",
                conteudo="Os complementos verbais são termos que completam o sentido de verbos que não têm significado completo sozinhos. Objeto Direto: sem preposição. Objeto Indireto: com preposição. Verbos transitivos diretos, indiretos e bitransitivos. Verbos intransitivos não precisam de complemento."
            )
            db.session.add(assunto_comp_verbal)
            db.session.flush()
            print(" Assunto 4 — Complemento Verbal criado")
        else:
            print(" Assunto 4 — Complemento Verbal já existe")

        atividade4 = Atividade(
            nome="Atividade 4 - Complemento Verbal",
            dificuldade="Médio",
            tipo="SISTEMA",
            assunto_id=assunto_comp_verbal.id
        )
        db.session.add(atividade4)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Qual alternativa define corretamente o Complemento Verbal e a necessidade de alguns verbos por ele?",
            alternativa_a="Termo acessório que indica circunstância e é necessário para verbos intransitivos.",
            alternativa_b="Termo essencial que completa o sentido de verbos transitivos, pois eles não possuem sentido completo por si só.",
            alternativa_c="Termo que modifica um nome e só é usado com verbos de ligação.",
            alternativa_d="Termo que é sempre preposicionado e obrigatório para todos os verbos.",
            resposta_correta="b", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="2. A principal diferença entre Objeto Direto (OD) e Objeto Indireto (OI) é a presença ou ausência de:",
            alternativa_a="Advérbios.", alternativa_b="Substantivos.", alternativa_c="Artigos definidos.", alternativa_d="Preposição obrigatória.",
            resposta_correta="d", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="3. Na frase 'A menina encontrou seu gato', o termo destacado 'seu gato' é classificado como:",
            alternativa_a="Objeto Direto.", alternativa_b="Adjunto Adverbial.", alternativa_c="Objeto Indireto.", alternativa_d="Complemento Nominal.",
            resposta_correta="a", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="4. Um verbo é classificado como Transitivo Direto e Indireto (Bitransitivo) quando:",
            alternativa_a="Possui apenas um complemento sem preposição.",
            alternativa_b="Não exige complemento para ter sentido completo.",
            alternativa_c="Possui dois complementos: um Objeto Direto e um Objeto Indireto.",
            alternativa_d="Liga o sujeito a uma característica por meio de um predicativo.",
            resposta_correta="c", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="5. O verbo dormir na frase 'O bebê dormiu' é classificado como intransitivo porque:",
            alternativa_a="Ele é um verbo de ligação.", alternativa_b="Ele possui sentido completo e não exige complemento.",
            alternativa_c="O sujeito está oculto.", alternativa_d="Exige apenas um complemento preposicionado.",
            resposta_correta="b", atividade_id=atividade4.id))

        # ASSUNTO 5 — Complemento Nominal
        assunto_comp_nominal = Assunto.query.filter_by(nome="Complemento Nominal").first()
        if not assunto_comp_nominal:
            assunto_comp_nominal = Assunto(
                nome="Complemento Nominal",
                conteudo="O complemento nominal completa o sentido de um nome (substantivo, adjetivo ou advérbio) que exige preposição. Diferencia-se do Objeto Indireto: CN liga-se a nomes, OI liga-se a verbos. A preposição é obrigatória, exigida pelo próprio nome."
            )
            db.session.add(assunto_comp_nominal)
            db.session.flush()
            print(" Assunto 5 — Complemento Nominal criado")
        else:
            print(" Assunto 5 — Complemento Nominal já existe")

        atividade5 = Atividade(
            nome="Atividade 5 - Complemento Nominal",
            dificuldade="Médio",
            tipo="SISTEMA",
            assunto_id=assunto_comp_nominal.id
        )
        db.session.add(atividade5)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Qual a principal característica obrigatória do Complemento Nominal (CN)?",
            alternativa_a="É sempre ligado a um verbo.", alternativa_b="É sempre um termo acessório.",
            alternativa_c="Completa o sentido de um substantivo concreto.", alternativa_d="É sempre introduzido por preposição.",
            resposta_correta="d", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="2. Identifique o Complemento Nominal na frase: 'Ela tem orgulho de suas raízes.'",
            alternativa_a="de suas raízes", alternativa_b="tem orgulho", alternativa_c="Ela", alternativa_d="raízes",
            resposta_correta="a", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="3. A principal diferença estrutural entre o Complemento Nominal (CN) e o Objeto Indireto (OI) é que:",
            alternativa_a="O CN liga-se a verbos, e o OI a nomes (substantivos, adjetivos, advérbios).",
            alternativa_b="O CN é introduzido por preposição, e o OI nunca é.",
            alternativa_c="O CN liga-se a nomes, e o OI liga-se a verbos.",
            alternativa_d="O CN é facultativo, e o OI é obrigatório.",
            resposta_correta="c", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="4. O Complemento Nominal complementa, predominantemente, o sentido de quais classes de palavras?",
            alternativa_a="Verbos, preposições e pronomes.",
            alternativa_b="Adjetivos, substantivos abstratos e advérbios.",
            alternativa_c="Substantivos concretos, artigos e numerais.",
            alternativa_d="Conjunções, interjeições e verbos.",
            resposta_correta="b", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="5. Em 'Tenho medo de altura', a expressão 'de altura' é Complemento Nominal porque complementa o sentido de:",
            alternativa_a="um verbo (Tenho).", alternativa_b="um substantivo abstrato (medo).",
            alternativa_c="um advérbio de intensidade.", alternativa_d="um substantivo concreto.",
            resposta_correta="b", atividade_id=atividade5.id))

        # ASSUNTO 6 — Agente da Passiva
        assunto_agente_passiva = Assunto.query.filter_by(nome="Agente da Passiva").first()
        if not assunto_agente_passiva:
            assunto_agente_passiva = Assunto(
                nome="Agente da Passiva",
                conteudo="O agente da passiva é o termo que indica quem praticou a ação na voz passiva analítica, sempre introduzido por preposição (geralmente 'por'). Na transformação da voz ativa para passiva: o objeto direto vira sujeito paciente, o verbo vai para 'ser + particípio' e o antigo sujeito vira agente da passiva."
            )
            db.session.add(assunto_agente_passiva)
            db.session.flush()
            print(" Assunto 6 — Agente da Passiva criado")
        else:
            print(" Assunto 6 — Agente da Passiva já existe")

        atividade6 = Atividade(
            nome="Atividade 6 - Agente da Passiva",
            dificuldade="Médio",
            tipo="SISTEMA",
            assunto_id=assunto_agente_passiva.id
        )
        db.session.add(atividade6)
        db.session.flush()

        db.session.add(Questao(enunciado="1. O Agente da Passiva é encontrado exclusivamente em qual construção e indica quem praticou a ação?",
            alternativa_a="Voz ativa e liga-se sempre sem preposição.",
            alternativa_b="Voz passiva, introduzido por preposição (geralmente 'por').",
            alternativa_c="Voz reflexiva, sem preposição.",
            alternativa_d="Apenas na voz passiva sintética, sem preposição.",
            resposta_correta="b", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="2. Na frase 'A carta foi escrita por mim', o trecho 'por mim' é:",
            alternativa_a="Sujeito da voz ativa.", alternativa_b="Objeto Direto.",
            alternativa_c="Agente da Passiva.", alternativa_d="Complemento Nominal.",
            resposta_correta="c", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="3. Na transformação: 'O aluno fez o trabalho' → 'O trabalho foi feito pelo aluno', o trecho 'pelo aluno' corresponde:",
            alternativa_a="ao sujeito da voz ativa.", alternativa_b="ao objeto direto da voz ativa.",
            alternativa_c="ao sujeito paciente da voz passiva.", alternativa_d="ao verbo da voz ativa.",
            resposta_correta="a", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="4. Assinale a alternativa que apresenta corretamente o Agente da Passiva:",
            alternativa_a="As crianças brincaram no parque.",
            alternativa_b="O parque foi visitado por muitas pessoas.",
            alternativa_c="Visitou-se o parque com alegria.",
            alternativa_d="Muitas pessoas visitaram o parque.",
            resposta_correta="b", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="5. Na construção da voz passiva analítica, o sujeito da voz ativa transforma-se em:",
            alternativa_a="Sujeito da voz passiva.", alternativa_b="Objeto Indireto.",
            alternativa_c="Agente da Passiva.", alternativa_d="Complemento Verbal.",
            resposta_correta="c", atividade_id=atividade6.id))

        # ASSUNTO 7 — Adjunto Adnominal
        assunto_adj_adnominal = Assunto.query.filter_by(nome="Adjunto Adnominal").first()
        if not assunto_adj_adnominal:
            assunto_adj_adnominal = Assunto(
                nome="Adjunto Adnominal",
                conteudo="Adjunto Adnominal é o termo acessório que acompanha e caracteriza um substantivo, indicando tipo, posse, matéria etc. Pode ser adjetivo, artigo, numeral ou pronome. Diferencia-se do Complemento Nominal: o adjunto caracteriza, o complemento completa o sentido exigido pelo nome."
            )
            db.session.add(assunto_adj_adnominal)
            db.session.flush()
            print(" Assunto 7 — Adjunto Adnominal criado")
        else:
            print(" Assunto 7 — Adjunto Adnominal já existe")

        atividade7 = Atividade(
            nome="Atividade 7 - Adjunto Adnominal",
            dificuldade="Médio",
            tipo="SISTEMA",
            assunto_id=assunto_adj_adnominal.id
        )
        db.session.add(atividade7)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Em 'Os filmes antigos da Disney', o termo destacado funciona como:",
            alternativa_a="complemento nominal", alternativa_b="objeto indireto",
            alternativa_c="adjunto adnominal", alternativa_d="adjunto adverbial",
            resposta_correta="c", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="2. Em 'o carro rosa da Penélope Charmosa', o termo destacado é:",
            alternativa_a="adjunto adnominal", alternativa_b="complemento nominal",
            alternativa_c="predicativo", alternativa_d="objeto direto",
            resposta_correta="a", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="3. Em 'ela não gosta de viagens longas', o termo destacado é:",
            alternativa_a="adjunto adnominal", alternativa_b="objeto indireto",
            alternativa_c="agente da passiva", alternativa_d="complemento nominal",
            resposta_correta="d", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="4. Em 'o cuidado à natureza é importante', o termo destacado é:",
            alternativa_a="adjunto adnominal", alternativa_b="complemento nominal",
            alternativa_c="predicativo", alternativa_d="adjunto adverbial",
            resposta_correta="b", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="5. Em 'o respeito ao próximo é importante', o termo destacado é:",
            alternativa_a="objeto indireto", alternativa_b="adjunto adnominal",
            alternativa_c="complemento nominal", alternativa_d="agente da passiva",
            resposta_correta="c", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="6. Em 'as músicas do Stray Kids são boas', o termo destacado é:",
            alternativa_a="adjunto adnominal", alternativa_b="objeto indireto",
            alternativa_c="complemento nominal", alternativa_d="adjunto adverbial",
            resposta_correta="a", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="7. Em 'no final do ano a vontade de estudar diminui', o termo destacado é:",
            alternativa_a="predicativo", alternativa_b="adjunto adnominal",
            alternativa_c="adjunto adverbial", alternativa_d="complemento nominal",
            resposta_correta="b", atividade_id=atividade7.id))

        # ASSUNTO 8 — Adjunto Adverbial
        assunto_adj_adverbial = Assunto.query.filter_by(nome="Adjunto Adverbial").first()
        if not assunto_adj_adverbial:
            assunto_adj_adverbial = Assunto(
                nome="Adjunto Adverbial",
                conteudo="Adjunto Adverbial é o termo acessório que indica uma circunstância ligada ao verbo ou à oração inteira: tempo, lugar, modo, causa, finalidade, intensidade, negação, dúvida, afirmação etc. Responde a perguntas como 'quando?', 'onde?', 'como?', 'por quê?', 'para quê?'."
            )
            db.session.add(assunto_adj_adverbial)
            db.session.flush()
            print(" Assunto 8 — Adjunto Adverbial criado")
        else:
            print(" Assunto 8 — Adjunto Adverbial já existe")

        atividade8 = Atividade(
            nome="Atividade 8 - Adjunto Adverbial",
            dificuldade="Médio",
            tipo="SISTEMA",
            assunto_id=assunto_adj_adverbial.id
        )
        db.session.add(atividade8)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Em 'ele esteve aqui mais cedo', o termo destacado é um adjunto adverbial de:",
            alternativa_a="modo", alternativa_b="tempo", alternativa_c="intensidade", alternativa_d="negação",
            resposta_correta="b", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="2. Em 'ela estava na escola', o adjunto adverbial é de:",
            alternativa_a="causa", alternativa_b="modo", alternativa_c="dúvida", alternativa_d="lugar",
            resposta_correta="d", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="3. Em 'ele me explicou calmamente', o termo destacado é adjunto adverbial de:",
            alternativa_a="modo", alternativa_b="tempo", alternativa_c="intensidade", alternativa_d="causa",
            resposta_correta="a", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="4. Em 'está muito frio por causa do ar condicionado', o termo destacado é adjunto adverbial de:",
            alternativa_a="meio", alternativa_b="afirmação", alternativa_c="causa", alternativa_d="finalidade",
            resposta_correta="c", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="5. Em 'tenho que ir para a consulta', o termo destacado indica:",
            alternativa_a="causa", alternativa_b="intensidade", alternativa_c="modo", alternativa_d="finalidade",
            resposta_correta="d", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="6. Em 'talvez eu não possa ir', o termo destacado é adjunto adverbial de:",
            alternativa_a="dúvida", alternativa_b="afirmação", alternativa_c="modo", alternativa_d="intensidade",
            resposta_correta="a", atividade_id=atividade8.id))

        # ASSUNTO 9 — Revisão Geral
        assunto_revisao = Assunto.query.filter_by(nome="Revisão Geral").first()
        if not assunto_revisao:
            assunto_revisao = Assunto(
                nome="Revisão Geral",
                conteudo="Revisão da estrutura da oração: termos essenciais (sujeito, predicado), integrantes (objeto direto, indireto, complemento nominal, predicativo) e acessórios (adjunto adnominal, adjunto adverbial). Diferenças e relações entre todos os termos estudados."
            )
            db.session.add(assunto_revisao)
            db.session.flush()
            print(" Assunto 9 — Revisão Geral criado")
        else:
            print(" Assunto 9 — Revisão Geral já existe")

        atividade9 = Atividade(
            nome="Atividade 9 - Revisão Geral",
            dificuldade="Médio",
            tipo="SISTEMA",
            assunto_id=assunto_revisao.id
        )
        db.session.add(atividade9)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Em 'as integrantes do BlackPink arrasaram', o termo destacado é:",
            alternativa_a="objeto direto", alternativa_b="complemento nominal",
            alternativa_c="adjunto adnominal", alternativa_d="adjunto adverbial",
            resposta_correta="c", atividade_id=atividade9.id))
        db.session.add(Questao(enunciado="2. Qual alternativa apresenta somente termos acessórios?",
            alternativa_a="objeto direto e predicativo", alternativa_b="complemento nominal e objeto indireto",
            alternativa_c="objeto direto e adjunto adnominal", alternativa_d="adjunto adnominal e adjunto adverbial",
            resposta_correta="d", atividade_id=atividade9.id))
        db.session.add(Questao(enunciado="3. O complemento nominal se liga normalmente a:",
            alternativa_a="adjetivos ou substantivos abstratos", alternativa_b="verbos transitivos",
            alternativa_c="advérbios", alternativa_d="substantivos concretos",
            resposta_correta="a", atividade_id=atividade9.id))
        db.session.add(Questao(enunciado="4. O adjunto adnominal:",
            alternativa_a="completa o sentido de um adjetivo", alternativa_b="caracteriza um nome",
            alternativa_c="indica circunstância do verbo", alternativa_d="é exigido pelo nome",
            resposta_correta="b", atividade_id=atividade9.id))

        # FIM — Salvar tudo no banco!
        db.session.commit()
        print("\n TODOS os dados foram inseridos com SUCESSO no banco de dados!")

if __name__ == "__main__":
    inserir_atividades_sistema()