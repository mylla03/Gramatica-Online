from flask import Flask, render_template
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:labinfo@localhost/Gramatica_Online'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from models import *

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/usuario")
def usuario():
    return render_template("usuario.html")

@app.route("/escolha")
def escolha():
    return render_template("escolha.html")

@app.route("/gramatica")
def gramatica():
    return render_template("gramatica.html")

@app.route("/atividades")
def atividades():
    return render_template("atividades.html")

@app.route("/sujeito_detalhe")
def sujeito_detalhe():
    return render_template("sujeito_detalhe.html")

@app.route("/revisao_geral_detalhe")
def revisao_geral_detalhe():
    return render_template("revisao_geral_detalhe.html")

@app.route("/predicado_detalhe")
def predicado_detalhe():
    return render_template("predicado_detalhe.html")

@app.route("/complemento_verbal_detalhe")
def complemento_verbal_detalhe():
    return render_template("complemento_verbal_detalhe.html")

@app.route("/complemento_nominal_detalhe")
def complemento_nominal_detalhe():
    return render_template("complemento_nominal_detalhe.html")

@app.route("/aposto_detalhe")
def aposto_detalhe():
    return render_template("aposto_detalhe.html")

@app.route("/agente_da_passiva_detalhe")
def agente_da_passiva_detalhe():
    return render_template("agente_da_passiva_detalhe.html")

@app.route("/adjunto_adverbial_detalhe")
def adjunto_adverbial_detalhe():
    return render_template("adjunto_adverbial_detalhe.html")

@app.route("/adjunto_adnominal_detalhe")
def adjunto_adnominal_detalhe():
    return render_template("adjunto_adnominal_detalhe.html")

@app.route("/atividade1")
def atividade1():
    return render_template("atividade1.html")

@app.route("/atividade2")
def atividade2():
    return render_template("atividade2.html")

@app.route("/atividade3")
def atividade3():
    return render_template("atividade3.html")

@app.route("/atividade4")
def atividade4():
    return render_template("atividade4.html")

@app.route("/atividade5")
def atividade5():
    return render_template("atividade5.html")

@app.route("/atividade6")
def atividade6():
    return render_template("atividade6.html")

@app.route("/atividade7")
def atividade7():
    return render_template("atividade7.html")

@app.route("/atividade8")
def atividade8():
    return render_template("atividade8.html")

@app.route("/atividade9")
def atividade9():
    return render_template("atividade9.html")


if __name__ == "__main__":
    app.run(debug=True)
