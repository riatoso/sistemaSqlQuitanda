import time

from conexao_banco import conexao as bd


class Loja:
    def __init__(self):
        # lendo os dados
        self.conn = bd()  # conexão
        self.cursor = bd().cursor()  # banco = connection e indica o cursor
        self.lista_final = []

    def itens_lista(self):
        conn = bd()  # CONEXAO
        cursor = conn.cursor()  # CONEXAO.CURSOR
        lista = []
        cursor.execute("""
        SELECT * FROM produtos;
        """)
        print("\nLISTA DE PRODUTOS NA QUITANDA")
        for linha in cursor.fetchall():
            lista.append([linha[1], linha[2]])
            print(f"PRODUTO: {linha[1]} /-/ PRECO R$ {linha[2]:.2f}")
        cursor.close()
        return lista

    def verifica_item(self, produto):
        conn = bd()
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM produtos;
        """)
        if produto in [linha[1] for linha in cursor.fetchall()]:
            print("Produto esta cadastrado no banco de dados")
            cursor.close()
            return 1
        else:
            print("Produto não cadastrado")
            cursor.close()
            return 0

    def inserir_itens(self, produto, preco):
        conn = bd()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO produtos (produto, preco) VALUES ('{produto}','{preco}')")
        conn.commit()
        print("Sendo cadastrado.")
        time.sleep(1)
        cursor.close()

    def apagar_item(self, produto):
        conn = bd()
        cursor = conn.cursor()
        cursor.execute(f"delete from produtos where produto = '{produto}'")
        conn.commit()
        print("Sendo apagado.")
        time.sleep(1)
        cursor.close()

    def carrinho_compras(self, lista):
        l_temp = []
        for i in lista:
            if i[0] in [y[0] for y in self.lista_final]:
                for x in self.lista_final:
                    if i[0] == x[0]:
                        temp_qtd = x[1]
                        self.lista_final.remove(x)
                        l_temp.append([i[0], i[1] + temp_qtd])
                    else:
                        continue
            else:
                self.lista_final.append(i)
            continue
        for i in l_temp:
            self.lista_final.append(i)

    def finaliza_compras(self):
        conn = bd()
        cursor = conn.cursor()
        cursor.execute("""select * FROM produtos""")
        lista = [(x[1], x[2]) for x in cursor.fetchall()]
        lista_compras = []
        lista_final = []
        total = 0
        for i in lista:
            if i[0] in [x[0] for x in self.lista_final]:
                for x in self.lista_final:
                    if i[0] == x[0]:
                        lista_compras.append([x[0], x[1], i[1]])
            else:
                continue
        print("############ PEDIDO FINALIZADO ############")
        for x in lista_compras:
            lista_final.append(x)
            total = total + (x[2] * x[1])
            print(f"Produto {x[0]} - Quantidade {x[1]} - R$ {x[2] * x[1]:.2f}")
        print("############ TOTAL DO PEDIDO ##############")
        print(f"R$ - {total:.2f}")
        print("###########################################")
        time.sleep(4)
        self.lista_final = []

    def modificar_preco(self, produto, preco):
        conn = bd()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE produtos SET preco = '{preco}'  WHERE produto = '{produto}'")
        conn.commit()
        conn.close()
        print(f"Preço do produto {produto} alterado para R$ {preco:.2f}")

