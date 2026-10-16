from app import app
from models import Atividade, Questao
from database import db

def inserir_atividades_sistema():
    with app.app_context():
        if Atividade.query.filter_by(tipo="SISTEMA").first():
            print("Atividades do sistema já existem no banco de dados.")
            return
        
        print("Inserindo atividades do sistema no banco de dados...")
        
        #  ATIVIDADE 1 - Sujeito 
        atividade1 = Atividade(nome="Atividade 1 - Sujeito", dificuldade="Fácil", tipo="SISTEMA")
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
        
        #  ATIVIDADE 2 - Predicado 
        atividade2 = Atividade(nome="Atividade 2 - Predicado", dificuldade="Fácil", tipo="SISTEMA")
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
        
        #  ATIVIDADE 3 - Aposto 
        atividade3 = Atividade(nome="Atividade 3 - Aposto", dificuldade="Fácil", tipo="SISTEMA")
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
        
        #  ATIVIDADE 4 - Complemento Verbal 
        atividade4 = Atividade(nome="Atividade 4 - Complemento Verbal", dificuldade="Médio", tipo="SISTEMA")
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
        
        #  ATIVIDADE 5 - Complemento Nominal 
        atividade5 = Atividade(nome="Atividade 5 - Complemento Nominal", dificuldade="Médio", tipo="SISTEMA")
        db.session.add(atividade5)
        db.session.flush()
        
        db.session.add(Questao(enunciado="1. Qual a principal característica obrigatória do Complemento Nominal (CN)?",
            alternativa_a="É sempre ligado a um verbo.", alternativa_b="É sempre um termo acessório.",
            alternativa_c="Completa o sentido de um substantivo concreto.", alternativa_d="É sempre introduzido por preposição.",
            resposta_correta="d", atividade_id=atividade5.id))Completa o sentido de um substantivo concreto.
        
        db.session.add(Questao(enunciado="2. Identifique o Complemento Nominal na frase: 'Ela tem orgulho de suas raízes.'",
            alternativa_a="de suas raízes", alternativa_b="tem orgulho", alternativa_c="Ela", alternativa_d="raízes",
            resposta_correta="a", atividade_id=atividade5.id))de suas raízes
        
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
        
        #  ATIVIDADE 6 - Agente da Passiva 
        atividade6 = Atividade(nome="Atividade 6 - Agente da Passiva", dificuldade="Médio", tipo="SISTEMA")
        db.session.add(atividade6)
        db.session.flush()
        
        db.session.add(Questao(enunciado="1. O que é o Agente da Passiva e em que voz verbal ele é encontrado?",
            alternativa_a="É o sujeito da voz ativa e aparece na voz reflexiva.",
            alternativa_b="É o termo que pratica a ação na voz passiva e pode ser encontrado tanto na passiva analítica quanto na passiva sintética.",
            alternativa_c="É o termo que sofre a ação na voz ativa e aparece na voz passiva.",
            alternativa_d="É o termo que pratica a ação na voz passiva, sendo introduzido por preposição, e aparece somente na voz passiva analítica.",
            resposta_correta="d", atividade_id=atividade6.id))
        
        db.session.add(Questao(enunciado="2. Na frase 'A cidade foi destruída pelos invasores', qual é o Agente da Passiva?",
            alternativa_a="A cidade", alternativa_b="foi destruída", alternativa_c="pelos invasores", alternativa_d="os invasores",
            resposta_correta="c", atividade_id=atividade6.id))
        
        db.session.add(Questao(enunciado="3. Quais são os três passos essenciais para transformar uma frase da Voz Ativa para a Voz Passiva Analítica?",
            alternativa_a="O Objeto Direto vira Agente da Passiva, o Sujeito vira Sujeito da Passiva, e o verbo principal é mantido.",
            alternativa_b="O Sujeito da Ativa vira Objeto Direto, o Objeto Direto vira Predicativo, e o verbo passa a ser de ligação.",
            alternativa_c="O Objeto Direto vira Sujeito da Passiva, o Sujeito da Ativa vira Agente da Passiva, e o verbo vira locução verbal (verbo ser + particípio).",
            alternativa_d="O Objeto Indireto vira Sujeito da Passiva, o Sujeito da Ativa é omitido, e o verbo vai para o infinitivo.",
            resposta_correta="c", atividade_id=atividade6.id))
        
        db.session.add(Questao(enunciado="4. Por que o Agente da Passiva sempre é introduzido por uma preposição (de/por e suas variações)?",
            alternativa_a="Porque o Agente da Passiva atua como Objeto Indireto na nova estrutura.",
            alternativa_b="Porque a preposição marca o elemento que pratica a ação no contexto passivo, sendo o resquício do verbo transitivo.",
            alternativa_c="Porque a preposição é exigida pelo sujeito paciente.",
            alternativa_d="Porque a preposição o transforma em um Adjunto Adnominal.",
            resposta_correta="b", atividade_id=atividade6.id))
        
        db.session.add(Questao(enunciado="5. A frase 'O artista pintou o quadro' na Voz Passiva Analítica é e tem o Agente da Passiva indicado em:",
            alternativa_a="O quadro foi pintado pelo artista. (Agente: pelo artista)",
            alternativa_b="Foi pintado o quadro do artista. (Agente: o quadro)",
            alternativa_c="O quadro pintou o artista. (Agente: o quadro)",
            alternativa_d="O artista foi pintado. (Agente: pelo artista)",
            resposta_correta="a", atividade_id=atividade6.id))
        
        #  ATIVIDADE 7 - Adjunto Adnominal 
        atividade7 = Atividade(nome="Atividade 7 - Adjunto Adnominal", dificuldade="Médio", tipo="SISTEMA")
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
        
        #  ATIVIDADE 8 - Adjunto Adverbial 
        atividade8 = Atividade(nome="Atividade 8 - Adjunto Adverbial", dificuldade="Médio", tipo="SISTEMA")
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
        
        #  ATIVIDADE 9 - Revisão Geral 
        atividade9 = Atividade(nome="Atividade 9 - Revisão Geral", dificuldade="Médio", tipo="SISTEMA")
        db.session.add(atividade9)
        db.session.flush()
        
        db.session.add(Questao(enunciado="1. Em 'as integrantes do BlackPink arrasaram', o termo destacado é:",
            alternativa_a="objeto direto", alternativa_b="complemento nominal",
            alternativa_c="adjunto adnominal", alternativa_d="adjunto adverbial",
            resposta_correta="c", atividade_id=atividade9.id))
        
        db.session.add(Questao(enunciado="2. Qual alternativa apresenta somente termos acessórios (que podem ser retirados da frase sem prejuízo de sentido)?",
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
        
        db.session.commit()
        print("Todas as 9 atividades do sistema foram inseridas com sucesso no banco de dados! ")

if __name__ == "__main__":
    inserir_atividades_sistema()