from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
import os
from werkzeug.utils import secure_filename
from sqlalchemy import text, func
from flask import session
from dotenv import load_dotenv
from authlib.integrations.flask_client import OAuth
from authlib.integrations.base_client.errors import OAuthError
from requests.exceptions import RequestException
from datetime import datetime

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "outra-chave-segura")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gramatica_online.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True

oauth = OAuth(app)

SUAP_BASE_URL = os.environ.get("SUAP_BASE_URL", "https://suap.ifrn.edu.br").rstrip("/")
SUAP_USER_INFO_ENDPOINT = os.environ.get("SUAP_USER_INFO_ENDPOINT", "api/rh/eu/").lstrip("/")

suap_client_kwargs = {}
suap_scope = os.environ.get("SUAP_SCOPE", "").strip()
if suap_scope:
    suap_client_kwargs["scope"] = suap_scope

suap = oauth.register(
    name="suap",
    client_id=os.environ["SUAP_CLIENT_ID"],
    client_secret=os.environ["SUAP_CLIENT_SECRET"],
    authorize_url=f"{SUAP_BASE_URL}/o/authorize/",
    access_token_url=f"{SUAP_BASE_URL}/o/token/",
    api_base_url=f"{SUAP_BASE_URL}/",
    client_kwargs=suap_client_kwargs,
)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db.init_app(app)

from models import Assunto, Atividade, Questao, ResultadoAtividade

with app.app_context():
    db.create_all()

def arquivo_permitido(nome):
    return '.' in nome and nome.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# IMPORTA E REGISTRA AS ROTAS
from rotas import registrar_rotas
registrar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)