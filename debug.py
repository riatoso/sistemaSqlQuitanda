import sqlite3

conn = sqlite3.connect("precos.db", timeout=100)
cursor = conn.cursor()
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o valor a ser modificado: "))
cursor.execute(f"UPDATE produtos SET preco = '{preco}'  WHERE produto = '{nome}'")
conn.commit()
print("Comitado no banco")

