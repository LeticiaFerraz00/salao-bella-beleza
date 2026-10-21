import sqlite3

from database import conectar


def test_conexao_sqlite():
    conexao = conectar()

    try:
        assert isinstance(conexao, sqlite3.Connection)
        assert conexao.row_factory == sqlite3.Row
    finally:
        conexao.close()