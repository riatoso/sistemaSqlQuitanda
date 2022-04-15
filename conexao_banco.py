def conexao():
    import sqlite3
    try:
        conection = sqlite3.connect("precos.db", timeout=200)
        return conection
    except sqlite3.InternalError as err:
        print(f"Erro {err}")
