
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

@app.route("/servicos", methods=["GET", "POST"])
def servicos():
    conexao = conectar()

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        preco = request.form.get("preco", "").strip()
        duracao = request.form.get("duracao", "").strip()

        if nome and preco and duracao:
            try:
                preco = float(preco)
                duracao = int(duracao)

                if preco >= 0 and duracao > 0:
                    conexao.execute(
                        "INSERT INTO servicos (nome, preco, duracao) VALUES (?, ?, ?)",
                        (nome, preco, duracao)
                    )
                    conexao.commit()
            except ValueError:
                pass

        conexao.close()
        return redirect(url_for("servicos"))

    lista_servicos = conexao.execute(
        "SELECT * FROM servicos ORDER BY nome"
    ).fetchall()

    conexao.close()
    return render_template("servicos.html", servicos=lista_servicos)

if __name__ == "__main__":
    app.run(debug=True)
