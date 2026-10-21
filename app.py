
from flask import Flask, render_template, request, redirect, url_for
from database import criar_tabelas, conectar

app = Flask(__name__)

criar_tabelas()


@app.route("/")
def pagina_inicial():
    return render_template("index.html")

@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    conexao = conectar()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        telefone = request.form.get("telefone", "").strip()

        if nome and telefone:
            conexao.execute(
                "INSERT INTO clientes (nome, telefone) VALUES (?, ?)",
                (nome, telefone)
            )
            conexao.commit()

        conexao.close()
        return redirect(url_for("clientes"))

    lista_clientes = conexao.execute(
        "SELECT * FROM clientes ORDER BY nome"
    ).fetchall()

    conexao.close()
    return render_template("clientes.html", clientes=lista_clientes)

if __name__ == "__main__":
    app.run(debug=True)
