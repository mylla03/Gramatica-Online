from app import app
from models import Assunto, Atividade, Questao
from database import db

def inserir_atividades_sistema():
    with app.app_context():
        # if Atividade.query.filter_by(tipo="SISTEMA").first():
        #     print("Atividades do sistema já existem no banco de dados.")
        #     return
        
        print("Inserindo assuntos e atividades do grupo...\n")

        # ASSUNTO 1 — Sujeito
        assunto1 = Assunto.query.filter_by(nome="Módulo 1: Sujeito").first()
        if not assunto1:
            assunto1 = Assunto(
                nome="Módulo 1: Sujeito",
                tipo="SISTEMA",
                conteudo="""
<h3>O que é sujeito?</h3>
<p>O sujeito é o ser principal da oração e indica quem participa, pratica ou sofre a ação.</p>

<h3>Tipos de sujeito</h3>
<p>No total, existem cinco tipos principais de sujeito na língua portuguesa: simples, composto, oculto, indeterminado e oração sem sujeito.</p>

<h3>Sujeito simples:</h3>
<p>O sujeito simples é aquele que possui apenas um núcleo, isto é, uma palavra principal que indica quem realiza ou sofre a ação.</p>
<p>Observe as seguintes frases:</p>
<ul>
    <li>O menino dormiu.</li>
    <li>A menina mordeu a maçã.</li>
</ul>
<p>Na frase "O menino dormiu", menino é o sujeito e dormiu é a ação.</p>
<p>Em "A menina mordeu a maçã", menina é o sujeito, mordeu é a ação e maçã é o objeto direto, que sofreu a ação.</p>
<p><em>Dica: O sujeito simples fala de apenas uma pessoa ou coisa.</em></p>

<h3>Sujeito Oculto (ou Elíptico):</h3>
<p>O sujeito oculto (ou elíptico) é aquele que não aparece na oração, mas pode ser identificado pelo verbo ou pelo contexto.</p>
<p>Exemplos:</p>
<ul>
    <li>Fui à praia ontem.</li>
    <p>O sujeito não está explícito, mas o verbo "fui" indica que o sujeito é eu.</p>
    <li>Fomos ao cinema hoje.</li>
    <p>O verbo "fomos" está na primeira pessoa do plural, então percebemos que o sujeito oculto é "nós", mesmo que não esteja escrito na frase.</p>
</ul>

<h3>Sujeito Composto:</h3>
<p>O sujeito composto é aquele que possui dois ou mais núcleos, isto é, duas ou mais palavras principais que indicam quem realiza ou sofre a ação.</p>
<p>Exemplos:</p>
<ul>
    <li>Marina e Mariana foram ao shopping.</li>
    <p>Os núcleos são Marina e Mariana. O verbo está no plural porque, na frase, existe mais de um núcleo.</p>
    <li>Cecília e Gael foram ao mercado.</li>
    <p>Os núcleos são Cecília e Gael.</p>
</ul>
<p><em>Dica: se houver dois ou mais núcleos, o sujeito é composto.</em></p>

<h3>Sujeito Indeterminado:</h3>
<p>O sujeito indeterminado é aquele em que alguém realiza uma ação, mas não sabemos exatamente quem.</p>
<p>1. Com o verbo na terceira pessoa do plural, sem indicar quem é o sujeito.</p>
<p>Exemplo:</p>
<ul><li>Pegaram minha comida.</li></ul>
<p>Nesse caso, alguém pegou, mas não sabemos quem.</p>
<p>2. Com o verbo na terceira pessoa do singular, acompanhado da partícula "se", que é o índice de indeterminação do sujeito.</p>
<p>Exemplos:</p>
<ul>
    <li>Dorme-se pouco nessa cidade.<br>(Alguém dorme, mas não sabemos quem.)</li>
    <li>Precisa-se de atendente.<br>(Alguém precisa, mas não sabemos quem.)</li>
</ul>

<h3>Oração sem Sujeito:</h3>
<p>A oração sem sujeito é aquela que não possui um sujeito possível, isto é, não tem alguém que realiza a ação.</p>
<p>Nesses casos, o verbo é impessoal, pois não se refere a ninguém.</p>

<p>Isso pode acontecer com:</p>
<p><strong>1. Fenômenos da natureza:</strong></p>
<ul>
    <li>Fez muito sol ontem.</li>
    <li>Hoje está nublado.</li>
</ul>
<p>Esses verbos indicam acontecimentos da natureza, então não têm sujeito.</p>

<p><strong>2. Verbo "haver" com sentido de acontecer ou existir:</strong></p>
<ul>
    <li>Havia poucas pessoas na praia.</li>
    <li>Vai haver passeio amanhã.</li>
</ul>
<p>O verbo "haver" é impessoal nesses sentidos, portanto, a oração não tem sujeito.</p>

<p><strong>3. Verbo "fazer" indicando tempo ou fenômeno natural:</strong></p>
<ul>
    <li>Faz três anos que moro longe.</li>
    <li>Faz vento hoje.</li>
</ul>
<p>Nesse caso, o verbo "fazer" também é impessoal, então a oração é sem sujeito.</p>

<p><em>Dica: Se não há alguém realizando a ação e não dá pra saber quem faz, é uma oração sem sujeito.</em></p>

conteudo = """
<h3>Mapa Mental</h3>
<div class="mapa-mental-container">
    <img src="/static/img/mapa_sujeito.png" alt="Mapa Mental de Sujeito" class="mapa-mental">
</div>
"""

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto1)
            db.session.flush()
            print(" Assunto 1 — Sujeito criado")

        atividade1 = Atividade(
            nome="Atividade 1 - Sujeito",
            dificuldade="Fácil",
            assunto_id=assunto1.id
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
        assunto2 = Assunto.query.filter_by(nome="Módulo 2: Predicado").first()
        if not assunto2:
            assunto2 = Assunto(
                nome="Módulo 2: Predicado",
                tipo="SISTEMA",
                conteudo="""
<h3>O que é predicado?</h3>
<p>O predicado é uma parte da oração que contém aquilo que se afirma sobre o sujeito.</p>
<p>Ele traz ação, característica ou estado atribuído ao sujeito.</p>
<p>Exemplo:</p>
<ul><li>O menino brincou no parquinho.</li></ul>
<p>Sujeito: O menino.</p>
<p>Predicado: brincou no parquinho.</p>

<h3>Tipos de predicado:</h3>
<p>Na língua portuguesa, temos três tipos principais de predicado: predicado verbal, nominal e verbo-nominal.</p>

<h3>Predicado verbal:</h3>
<p>O núcleo do predicado é um verbo de ação. O foco está no que o sujeito faz.</p>
<p>Quando ocorre, há um verbo significativo, como correr, cantar ou brincar. Esse verbo é o elemento principal.</p>
<p>Exemplo:</p>
<ul><li>Essa menina dança muito.</li></ul>
<p>Núcleo verbal: dança.</p>

<h3>Predicado nominal:</h3>
<p>O predicado nominal é aquele em que o núcleo é um nome, adjetivo ou substantivo, e o verbo de ligação demonstra característica ou estado do sujeito.</p>
<p>Nesse caso, o verbo apenas liga o sujeito a uma característica, não indica uma ação.</p>
<p>Alguns verbos de ligação comuns são: estar, ficar, permanecer, ser, aparecer e continuar.</p>
<p>Exemplo:</p>
<ul><li>A menina está animada.</li></ul>
<p>Núcleo: animada, característica do sujeito.</p>

<h3>Predicado verbo-nominal:</h3>
<p>O predicado verbo-nominal combina os dois anteriores.</p>
<p>Mostra uma ação e, ao mesmo tempo, uma característica ou estado do sujeito.</p>
<p>Exemplo:</p>
<ul><li>O menino chegou atrasado.</li></ul>
<p>Ação: chegou.</p>
<p>Estado: atrasado.</p>

<h3>Relação entre sujeito e predicado:</h3>
<p>Toda oração pode ser dividida em sujeito e predicado.</p>
<p>O sujeito é alguém ou algo sobre o qual se faz uma declaração, enquanto o predicado é a informação dada sobre ele.</p>
<p>Exemplo:</p>
<ul><li>As meninas ficaram animadas com o passeio.</li></ul>
<p>Sujeito: As meninas.</p>
<p>Predicado: ficaram animadas com o passeio.</p>
<p>Tipo: verbo-nominal.</p>

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/2f_fPWs4I60" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto2)
            db.session.flush()
            print(" Assunto 2 — Predicado criado")

        atividade2 = Atividade(
            nome="Atividade 2 - Predicado",
            dificuldade="Fácil",
            assunto_id=assunto2.id
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
        assunto3 = Assunto.query.filter_by(nome="Módulo 3: Aposto").first()
        if not assunto3:
            assunto3 = Assunto(
                nome="Módulo 3: Aposto",
                tipo="SISTEMA",
                conteudo="""
<h3>O que é aposto?</h3>
<p>Aposto é um termo que aparece junto de um substantivo para especificar, explicar, resumir ou transmitir informações sobre ele.</p>
<p>Exemplo:</p>
<ul><li>Alice, minha vizinha, é engraçada.</li></ul>
<p>→ "minha vizinha" é o aposto, pois explica quem é Alice.</p>

<h3>Tipos de aposto</h3>

<h3>Aposto explicativo</h3>
<ul>
<li>Explica quem é a pessoa ou o que é o termo.</li>
<li>Geralmente fica entre vírgulas.</li>
</ul>
<p>Exemplo:</p>
<ul><li>Theo, meu primo, ganhou um carrinho novo.</li></ul>
<p>→ "meu primo" é o aposto.</p>

<h3>Aposto especificativo:</h3>
<ul>
<li>Especifica qual pessoa ou objeto estamos falando.</li>
<li>Não fica entre vírgulas.</li>
</ul>
<p>Exemplo 1:</p>
<ul><li>A menina de vestido rosa é minha amiga.</li></ul>
<p>→ "de vestido rosa" é o aposto.</p>
<p>Exemplo 2:</p>
<ul><li>O menino que chegou agora é meu primo.</li></ul>
<p>→ "que chegou agora" é o aposto.</p>

<h3>Aposto resumitivo</h3>
<ul>
<li>Resume vários elementos citados anteriormente.</li>
</ul>
<p>Exemplo:</p>
<ul><li>Vestidos, saias, blusas, todas essas peças são tendências.</li></ul>
<p>→ "todas essas peças" é o aposto.</p>

<h3>Aposto distributivo</h3>
<p>O aposto distributivo aparece normalmente depois de dois ou mais elementos.</p>
<p>Ele distribui uma ação ou característica para cada um deles separadamente.</p>
<p>Exemplos:</p>
<ul>
<li>Catarina e Manuella, ambas amigas, foram embora cedo da pizzaria.</li>
<li>Marina e Théo, cada um com sua garrafa, foram à academia.</li>
</ul>

<h3>Aposto e vocativo: qual a diferença?</h3>

<h4>Aposto:</h4>
<ul>
<li>Acrescenta informações sobre um elemento da frase.</li>
<li>Ele faz parte da estrutura da oração e não chama ninguém.</li>
<li>Apenas explica, especifica ou caracteriza algo ou alguém.</li>
</ul>

<h4>Vocativo:</h4>
<ul>
<li>O vocativo não faz parte da estrutura da frase.</li>
<li>Ele serve para chamar, invocar ou atrair a atenção de alguém.</li>
<li>É como um chamado dentro da frase.</li>
</ul>
<p>Exemplos de vocativo:</p>
<ul>
<li>Maria, pega meu caderno, por favor.</li>
<li>Gente, prestem atenção.</li>
</ul>

<h3>Mapa Mental</h3>
<div class="mapa-mental-container">
<img src="{{ url_for('static', filename='img/mapa_aposto.png') }}" alt="Mapa Mental de Aposto" class="mapa-mental">
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto3)
            db.session.flush()
            print(" Assunto 3 — Aposto criado")

        atividade3 = Atividade(
            nome="Atividade 3 - Aposto",
            dificuldade="Fácil",
            assunto_id=assunto3.id
        )
        db.session.add(atividade3)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Identifique o tipo de aposto na frase: 'Gael, meu amigo, chegou atrasado hoje.'",
            alternativa_a="Aposto especificativo", alternativa_b="Aposto explicativo",
            alternativa_c="Aposto resumitivo", alternativa_d="Aposto distributivo",
            resposta_correta="b", atividade_id=atividade3.id))
        db.session.add(Questao(enunciado="2. Na frase 'Os estudantes que se deram bem estudaram para a prova', o trecho destacado é:",
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
        assunto4 = Assunto.query.filter_by(nome="Módulo 4: Complemento Verbal").first()
        if not assunto4:
            assunto4 = Assunto(
                nome="Módulo 4: Complemento Verbal",
                tipo="SISTEMA",
                conteudo="""
<h3>O que são?</h3>
<p>Os complementos verbais são termos que completam o sentido de um verbo, já que nem todos conseguem ter um significado completo sozinhos.</p>
<p>Quando o verbo precisa de um complemento sem preposição, esse termo é chamado de <strong>objeto direto</strong>.</p>
<p>Exemplo:</p>
<ul><li>"Comprei um livro."</li></ul>
<p>O verbo comprar precisa de algo que complete a ideia, e esse algo é um livro.</p>
<p>Já quando o verbo exige preposição, o complemento é o <strong>objeto indireto</strong>.</p>
<p>Exemplo:</p>
<ul><li>"Gosto de música."</li></ul>
<p>O verbo gostar pede a preposição de, por isso a música é o objeto indireto.</p>
<p>Os verbos que precisam desses complementos são chamados <strong>verbos transitivos</strong>, podendo ser transitivos diretos, indiretos ou diretos e indiretos.</p>
<p>Por outro lado, os <strong>verbos intransitivos</strong> não precisam de complemento para ter sentido completo.</p>
<p>Exemplo:</p>
<ul><li>"O bebê dormiu."</li></ul>
<p>O verbo dormir já tem significado completo sozinho.</p>

<h3>Mapa Mental</h3>
<div class="mapa-mental-container">
<img src="{{ url_for('static', filename='img/mapa_complemento_verbal.png') }}" alt="Mapa Mental de Complemento Verbal" class="mapa-mental">
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto4)
            db.session.flush()
            print(" Assunto 4 — Complemento Verbal criado")

        atividade4 = Atividade(
            nome="Atividade 4 - Complemento Verbal",
            dificuldade="Médio",
            assunto_id=assunto4.id
        )
        db.session.add(atividade4)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Qual alternativa define corretamente o Complemento Verbal?",
            alternativa_a="Termo acessório que indica circunstância e é necessário para verbos intransitivos.",
            alternativa_b="Termo essencial que completa o sentido de verbos transitivos.",
            alternativa_c="Termo que modifica um nome e só é usado com verbos de ligação.",
            alternativa_d="Termo que é sempre preposicionado e obrigatório para todos os verbos.",
            resposta_correta="b", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="2. A principal diferença entre Objeto Direto e Objeto Indireto é:",
            alternativa_a="Advérbios.", alternativa_b="Substantivos.",
            alternativa_c="Preposição obrigatória.", alternativa_d="Artigos definidos.",
            resposta_correta="c", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="3. Na frase 'A menina encontrou seu gato', 'seu gato' é:",
            alternativa_a="Objeto Direto.", alternativa_b="Adjunto Adverbial.",
            alternativa_c="Objeto Indireto.", alternativa_d="Complemento Nominal.",
            resposta_correta="a", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="4. Verbo transitivo direto e indireto é aquele que:",
            alternativa_a="Possui apenas um complemento sem preposição.",
            alternativa_b="Não exige complemento para ter sentido completo.",
            alternativa_c="Possui dois complementos: um OD e um OI.",
            alternativa_d="Liga o sujeito a uma característica.",
            resposta_correta="c", atividade_id=atividade4.id))
        db.session.add(Questao(enunciado="5. O verbo 'dormir' em 'O bebê dormiu' é intransitivo porque:",
            alternativa_a="É verbo de ligação.", alternativa_b="Não exige complemento.",
            alternativa_c="O sujeito está oculto.", alternativa_d="Exige preposição.",
            resposta_correta="b", atividade_id=atividade4.id))

        # ASSUNTO 5 — Complemento Nominal
        assunto5 = Assunto.query.filter_by(nome="Módulo 5: Complemento Nominal").first()
        if not assunto5:
            assunto5 = Assunto(
                nome="Módulo 5: Complemento Nominal",
                tipo="SISTEMA",
                conteudo="""
<h3>O que é Complemento nominal?</h3>
<p>O complemento nominal completa o sentido de um nome (substantivo, adjetivo ou advérbio) que exige preposição.</p>
<p>Ele sempre vem acompanhado de uma preposição obrigatória e geralmente indica quem recebe a ação.</p>
<p>Exemplo:</p>
<ul><li>"Tenho medo de altura." → "de altura" é o complemento nominal.</li></ul>

<p>Diferença entre Complemento Nominal e Objeto Indireto:</p>
<ul>
<li>CN completa um nome; OI completa um verbo.</li>
<li>CN é sempre preposicionado; OI nem sempre.</li>
</ul>

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zFMsnEeAoGA" frameborder="0" allowfullscreen></iframe>
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto5)
            db.session.flush()
            print(" Assunto 5 — Complemento Nominal criado")

        atividade5 = Atividade(
            nome="Atividade 5 - Complemento Nominal",
            dificuldade="Médio",
            assunto_id=assunto5.id
        )
        db.session.add(atividade5)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Característica obrigatória do Complemento Nominal:",
            alternativa_a="Liga-se a um verbo.", alternativa_b="É sempre preposicionado.",
            alternativa_c="Modifica um verbo.", alternativa_d="É opcional.",
            resposta_correta="b", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="2. Em 'Tenho medo de altura', o CN é:",
            alternativa_a="Tenho", alternativa_b="medo", alternativa_c="de altura", alternativa_d="altura",
            resposta_correta="c", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="3. Diferença estrutural entre CN e OI:",
            alternativa_a="CN liga-se a nomes; OI a verbos.",
            alternativa_b="CN é opcional; OI é obrigatório.",
            alternativa_c="CN não usa preposição; OI sim.",
            alternativa_d="CN modifica verbos; OI modifica nomes.",
            resposta_correta="a", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="4. O CN complementa principalmente:",
            alternativa_a="Verbos.", alternativa_b="Substantivos, adjetivos e advérbios.",
            alternativa_c="Artigos e pronomes.", alternativa_d="Conjunções.",
            resposta_correta="b", atividade_id=atividade5.id))
        db.session.add(Questao(enunciado="5. Em 'Ela está ansiosa por novidades', o CN é:",
            alternativa_a="ansiosa", alternativa_b="por novidades",
            alternativa_c="Ela", alternativa_d="novidades",
            resposta_correta="b", atividade_id=atividade5.id))

        # ASSUNTO 6 — Agente da Passiva
        assunto6 = Assunto.query.filter_by(nome="Módulo 6: Agente da Passiva").first()
        if not assunto6:
            assunto6 = Assunto(
                nome="Módulo 6: Agente da Passiva",
                tipo="SISTEMA",
                conteudo="""
<h3>O que é o Agente da Passiva?</h3>
<p>Termo que indica quem praticou a ação na voz passiva, sempre introduzido por preposição (por/pela/pelo).</p>
<p>Exemplo:</p>
<ul><li>"O livro foi escrito por Machado de Assis."</li></ul>

<h3>Transformação Ativa → Passiva:</h3>
<ol>
<li>Objeto direto da ativa vira sujeito paciente da passiva.</li>
<li>Verbo vira: ser + particípio.</li>
<li>Sujeito da ativa vira agente da passiva.</li>
</ol>
<p>Exemplo:</p>
<ul>
<li>Ativa: "A professora corrigiu as provas."</li>
<li>Passiva: "As provas foram corrigidas pela professora."</li>
</ul>

<h3>Mapa Mental</h3>
<div class="mapa-mental-container">
<img src="{{ url_for('static', filename='img/mapa_agente_da_passiva.png') }}" alt="Mapa Mental" class="mapa-mental">
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto6)
            db.session.flush()
            print(" Assunto 6 — Agente da Passiva criado")

        atividade6 = Atividade(
            nome="Atividade 6 - Agente da Passiva",
            dificuldade="Médio",
            assunto_id=assunto6.id
        )
        db.session.add(atividade6)
        db.session.flush()

        db.session.add(Questao(enunciado="1. O Agente da Passiva é encontrado somente na:",
            alternativa_a="Voz ativa.", alternativa_b="Voz passiva analítica.",
            alternativa_c="Voz reflexiva.", alternativa_d="Oração sem sujeito.",
            resposta_correta="b", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="2. Em 'A cidade foi destruída pelos invasores', o Agente da Passiva é:",
            alternativa_a="A cidade", alternativa_b="foi destruída",
            alternativa_c="pelos invasores", alternativa_d="invasores",
            resposta_correta="c", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="3. Passo correto Ativa → Passiva:",
            alternativa_a="Sujeito vira OD, OD vira Sujeito.",
            alternativa_b="OD vira Sujeito, Sujeito vira Agente da Passiva, verbo → ser+particípio.",
            alternativa_c="Sujeito vira predicativo.",
            alternativa_d="Verbo permanece igual.",
            resposta_correta="b", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="4. O Agente da Passiva é introduzido por:",
            alternativa_a="Verbo de ligação.", alternativa_b="Preposição.",
            alternativa_c="Advérbio.", alternativa_d="Artigo.",
            resposta_correta="b", atividade_id=atividade6.id))
        db.session.add(Questao(enunciado="5. 'O artista pintou o quadro' → Passiva correta:",
            alternativa_a="O quadro foi pintado pelo artista.",
            alternativa_b="O artista foi pintado.",
            alternativa_c="Pintou-se o quadro.",
            alternativa_d="O quadro pintou o artista.",
            resposta_correta="a", atividade_id=atividade6.id))

        # ASSUNTO 7 — Adjunto Adnominal
        assunto7 = Assunto.query.filter_by(nome="Módulo 7: Adjunto Adnominal").first()
        if not assunto7:
            assunto7 = Assunto(
                nome="Módulo 7: Adjunto Adnominal",
                tipo="SISTEMA",
                conteudo="""
<h3>O que é Adjunto Adnominal?</h3>
<p>Termo acessório que modifica, caracteriza ou acompanha um substantivo. Pode ser adjetivo, artigo, numeral ou pronome.</p>
<p>Diferença para Complemento Nominal:</p>
<ul>
<li>Adjunto Adnominal: caracteriza, é opcional, indica posse, matéria, tipo.</li>
<li>Complemento Nominal: completa nome que exige, é essencial, indica alvo/objeto da ideia.</li>
</ul>
<p>Exemplos:</p>
<ul>
<li>O livro da estante → Adjunto Adnominal (caracteriza)</li>
<li>O amor de Deus → Adjunto Adnominal (quem ama)</li>
<li>O amor a Deus → Complemento Nominal (quem é amado)</li>
</ul>

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/WuRXBvnNCnQ" frameborder="0" allowfullscreen></iframe>
<p><em>O vídeo também fala sobre Adjunto Adverbial</em></p>
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto7)
            db.session.flush()
            print(" Assunto 7 — Adjunto Adnominal criado")

        atividade7 = Atividade(
            nome="Atividade 7 - Adjunto Adnominal",
            dificuldade="Médio",
            assunto_id=assunto7.id
        )
        db.session.add(atividade7)
        db.session.flush()

        db.session.add(Questao(enunciado="1. 'Os filmes antigos da Disney' → termo destacado é:",
            alternativa_a="Complemento Nominal", alternativa_b="Adjunto Adnominal",
            alternativa_c="Objeto Indireto", alternativa_d="Predicativo",
            resposta_correta="b", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="2. 'O carro rosa da Penélope' → termo destacado é:",
            alternativa_a="Adjunto Adnominal", alternativa_b="Complemento Nominal",
            alternativa_c="Objeto Direto", alternativa_d="Agente da Passiva",
            resposta_correta="a", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="3. 'Ela não gosta de viagens longas' → termo destacado é:",
            alternativa_a="Adjunto Adnominal", alternativa_b="Complemento Nominal",
            alternativa_c="Objeto Indireto", alternativa_d="Adjunto Adverbial",
            resposta_correta="b", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="4. 'O cuidado à natureza é importante' → termo destacado é:",
            alternativa_a="Adjunto Adnominal", alternativa_b="Complemento Nominal",
            alternativa_c="Agente da Passiva", alternativa_d="Predicativo",
            resposta_correta="b", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="5. 'O respeito ao próximo é importante' → termo destacado é:",
            alternativa_a="Adjunto Adnominal", alternativa_b="Complemento Nominal",
            alternativa_c="Objeto Indireto", alternativa_d="Adjunto Adverbial",
            resposta_correta="b", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="6. 'As músicas do Stray Kids' → termo destacado é:",
            alternativa_a="Adjunto Adnominal", alternativa_b="Complemento Nominal",
            alternativa_c="Objeto Indireto", alternativa_d="Agente da Passiva",
            resposta_correta="a", atividade_id=atividade7.id))
        db.session.add(Questao(enunciado="7. 'No final do ano, a vontade de estudar diminui' → 'de estudar' é:",
            alternativa_a="Adjunto Adnominal", alternativa_b="Complemento Nominal",
            alternativa_c="Objeto Direto", alternativa_d="Adjunto Adverbial",
            resposta_correta="b", atividade_id=atividade7.id))

        # ASSUNTO 8 — Adjunto Adverbial
        assunto8 = Assunto.query.filter_by(nome="Módulo 8: Adjunto Adverbial").first()
        if not assunto8:
            assunto8 = Assunto(
                nome="Módulo 8: Adjunto Adverbial",
                tipo="SISTEMA",
                conteudo="""
<h3>O que é Adjunto Adverbial?</h3>
<p>Termo acessório que indica circunstância ligada ao verbo ou à oração inteira: tempo, lugar, modo, causa, finalidade, intensidade, negação, afirmação, dúvida, meio, instrumento, companhia...</p>
<p>Responde perguntas como: quando? onde? como? por quê? para quê?</p>
<p>Exemplos:</p>
<ul>
<li>Cheguei <strong>ontem</strong> → tempo</li>
<li>Estou <strong>bem</strong> → modo</li>
<li>Atrasou <strong>por causa do trânsito</strong> → causa</li>
</ul>

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/WuRXBvnNCnQ" frameborder="0" allowfullscreen></iframe>
<p><em>Mesmo vídeo do assunto anterior</em></p>
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar seu conhecimento sobre a sintaxe?</p>
                """
            )
            db.session.add(assunto8)
            db.session.flush()
            print(" Assunto 8 — Adjunto Adverbial criado")

        atividade8 = Atividade(
            nome="Atividade 8 - Adjunto Adverbial",
            dificuldade="Médio",
            assunto_id=assunto8.id
        )
        db.session.add(atividade8)
        db.session.flush()

        db.session.add(Questao(enunciado="1. 'Ele esteve aqui mais cedo' → tipo de adjunto adverbial:",
            alternativa_a="modo", alternativa_b="tempo/lugar", alternativa_c="causa", alternativa_d="intensidade",
            resposta_correta="b", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="2. 'Ela estava na escola' → tipo:",
            alternativa_a="lugar", alternativa_b="modo", alternativa_c="causa", alternativa_d="finalidade",
            resposta_correta="a", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="3. 'Ele me explicou calmamente' → tipo:",
            alternativa_a="modo", alternativa_b="tempo", alternativa_c="causa", alternativa_d="intensidade",
            resposta_correta="a", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="4. 'Está muito frio por causa do ar-condicionado' → 'por causa de' indica:",
            alternativa_a="causa", alternativa_b="finalidade", alternativa_c="meio", alternativa_d="concessão",
            resposta_correta="a", atividade_id=atividade8.id))
        db.session.add(Questao(enunciado="5. 'Estudou para passar' → 'para' indica:",
            alternativa_a="causa", alternativa_b="finalidade", alternativa_c="meio", alternativa_d="modo",
            resposta_correta="b", atividade_id=atividade8.id))

        # ASSUNTO 9 — Revisão Geral
        assunto9 = Assunto.query.filter_by(nome="Módulo 9: Revisão Geral").first()
        if not assunto9:
            assunto9 = Assunto(
                nome="Módulo 9: Revisão Geral",
                tipo="SISTEMA",
                conteudo="""
<h3>Como se relacionam na estrutura da oração:</h3>
<p><strong>Termos essenciais:</strong> Sujeito e Predicado — formam o núcleo da oração.</p>
<p><strong>Termos integrantes (complementos):</strong></p>
<ul>
<li>Objeto Direto</li>
<li>Objeto Indireto</li>
<li>Complemento Nominal</li>
<li>Predicativo do Sujeito / do Objeto</li>
</ul>
<p><strong>Termos acessórios:</strong></p>
<ul>
<li>Adjunto Adnominal — caracteriza/substantivo, opcional</li>
<li>Adjunto Adverbial — circunstância/verbo, opcional</li>
<li>Aposto — explica/substantivo</li>
<li>Vocativo — chama alguém, fora da estrutura</li>
</ul>

<h3>Resumo prático:</h3>
<ul>
<li>Se completa verbo → complemento verbal (OD/OI)</li>
<li>Se completa nome → complemento nominal</li>
<li>Se caracteriza substantivo → adjunto adnominal</li>
<li>Se indica circunstância → adjunto adverbial</li>
<li>Se pratica ação na passiva → agente da passiva</li>
</ul>

<h3>Material de Estudo</h3>
<a href="https://drive.google.com/open?id=1SyMjR6UpN1ZgHtkF1e_7NCZsuWsxWOv0" target="_blank" class="btn btn-detalhe">
 Abrir PDF de Exercícios
</a>

<div class="video-container">
<iframe width="560" height="315" src="https://www.youtube.com/embed/zouWyLPtcXY" frameborder="0" allowfullscreen></iframe>
</div>

<h3>Próximos Passos</h3>
<p>Pronto para testar tudo? Boa revisão!</p>
                """
            )
            db.session.add(assunto9)
            db.session.flush()
            print(" Assunto 9 — Revisão Geral criado")

        atividade9 = Atividade(
            nome="Atividade 9 - Revisão Geral",
            dificuldade="Difícil",
            assunto_id=assunto9.id
        )
        db.session.add(atividade9)
        db.session.flush()

        db.session.add(Questao(enunciado="1. Qual conjunto contém apenas termos integrantes da oração?",
            alternativa_a="Adjunto Adnominal, Adjunto Adverbial, Aposto",
            alternativa_b="Sujeito, Predicado, Vocativo",
            alternativa_c="Objeto Direto, Objeto Indireto, Complemento Nominal",
            alternativa_d="Agente da Passiva, Aposto, Vocativo",
            resposta_correta="c", atividade_id=atividade9.id))
        db.session.add(Questao(enunciado="2. Qual alternativa apresenta corretamente a diferença entre Complemento Nominal e Adjunto Adnominal?",
            alternativa_a="Ambos completam o substantivo, mas o Adjunto Adnominal é obrigatório.",
            alternativa_b="O Complemento Nominal completa nome que exige; o Adjunto Adnominal apenas caracteriza.",
            alternativa_c="Não há diferença, são sinônimos.",
            alternativa_d="O Adjunto Adnominal liga-se a verbos; o Complemento Nominal a nomes.",
            resposta_correta="b", atividade_id=atividade9.id))
        db.session.add(Questao(enunciado="3. Em 'O respeito à pátria é sagrado', o termo destacado é:",
            alternativa_a="Adjunto Adnominal", alternativa_b="Complemento Nominal",
            alternativa_c="Objeto Indireto", alternativa_d="Agente da Passiva",
            resposta_correta="b", atividade_id=atividade9.id))
        db.session.add(Questao(enunciado="4. Assinale a alternativa correta sobre o Adjunto Adverbial:",
            alternativa_a="É termo essencial, sem ele a frase não tem sentido.",
            alternativa_b="Responde perguntas como 'quando? onde? como?' e pode ser deslocado.",
            alternativa_c="Sempre vem antes do verbo.",
            alternativa_d="Completa o sentido do sujeito.",
            resposta_correta="b", atividade_id=atividade9.id))
        db.session.add(Questao(enunciado="5. Na transformação de voz ativa para passiva, o sujeito da ativa passa a ser:",
            alternativa_a="Sujeito da passiva", alternativa_b="Objeto Direto",
            alternativa_c="Agente da Passiva", alternativa_d="Predicativo",
            resposta_correta="c", atividade_id=atividade9.id))

        db.session.commit()
        print("\n TODOS os assuntos e atividades foram inseridos com sucesso!")
        print(f" Total: 9 assuntos | 9 atividades | ~50 questões")

if __name__ == "__main__":
    inserir_atividades_sistema()