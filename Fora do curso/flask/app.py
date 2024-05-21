from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def erro404():
    return "<h1>404</h1>"

@app.route("/teste")
def fucao():
    return render_template("fucao.html")

@app.route("/nova")
def pagina2():
    return render_template("nova.html")

@app.route("/teste/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)

app.run()