Clonar o projeto em pasta de sua preferência:
`git clone https://github.com/mylla03/Gramatica-Online.git`

Depois, entre na pasta do projeto e execute os seguintes comandos:

1. Criar ambiente virtual:
`python -m venv venv`

2. Ativar ambiente virtual:
`venv\Scripts\activate.bat`

3. Instalar dependências:
`pip install -r requirements.txt`

4. Criar o arquivo de variáveis de ambiente:
`cp .env.example .env`

Depois, edite o arquivo `.env` e preencha `SECRET_KEY`, `SUAP_CLIENT_ID` e `SUAP_CLIENT_SECRET` com os valores do seu ambiente.

5. Rodar o projeto:
`flask run`

O arquivo `.flaskenv` já ativa o modo debug/reload para desenvolvimento.
