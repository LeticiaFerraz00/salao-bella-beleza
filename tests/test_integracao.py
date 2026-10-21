import sqlite3

import app as modulo_app


def test_cadastro_cliente_integracao(tmp_path, monkeypatch):
    banco_teste = tmp_path / "teste_salao.db"

    def conectar_teste():
        conexao = sqlite3.connect(banco_teste)
        conexao.row_factory = sqlite3.Row
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao

    monkeypatch.setattr(modulo_app, "conectar", conectar_teste)

    with conectar_teste() as conexao:
        conexao.execute("""
            CREATE TABLE clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        """)

    modulo_app.app.config["TESTING"] = True
    cliente = modulo_app.app.test_client()

    resposta = cliente.post(
        "/clientes",
        data={"nome": "Ana Teste", "telefone": "11988887777"},
        follow_redirects=True
    )

    assert resposta.status_code == 200
    assert b"Ana Teste" in resposta.data

    with conectar_teste() as conexao:
        cadastro = conexao.execute(
            "SELECT nome, telefone FROM clientes WHERE nome = ?",
            ("Ana Teste",)
        ).fetchone()

    assert cadastro is not None
    assert cadastro["telefone"] == "11988887777"