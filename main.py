import time
from quitanda import Loja

if __name__ == "__main__":
    cliente = Loja()
    while True:
        time.sleep(1)
        print("\nMENU DE AÇÕES")
        print(50 * "-")
        print(" 1 - LISTAR ITENS DA QUITANDA.")
        print(" 2 - INSERIR PRODUTO NA LOJA.")
        print(" 3 - MODIFICAR PREÇO DE PRODUTO.")
        print(" 4 - APAGAR PRODUTO DA LOJA.")
        print(" 5 - CARRINHO DE COMPRAS.")
        print(" 6 - VER CARRINHO DE COMPRAS.")
        print(" 7 - FINALIZAR COMPRAS.")
        print(" 8 - SAIR DO SISTEMA.")
        print(50 * "-")
        while True:
            acao = input("Digite uma opção valida -> ")
            try:
                acao = int(acao)
                break
            except:
                print("Digite apenas numeros.")
                continue
        if acao not in range(1, 9):
            print("DIGITE UMA OPCAO VALIDA")
            continue
        if acao == 1:
            cliente.itens_lista()
            continue
        if acao == 2:
            while True:
                while True:
                    produto = input("Digite o produto a ser inserido na quitanda: ").title()
                    verificar = Loja()
                    verifica = verificar.verifica_item(produto)
                    if verifica == 1:
                        print("Cadastre outro produto.")
                        continue
                    else:
                        break
                preco = float(input("Digite o valor do produto a ser inserido: "))
                print(f"Produto {produto} preço {preco}")
                insere = input("Informações estão corretas ? (s/n) ").lower()
                if insere == "s":
                    cliente.inserir_itens(produto, preco)
                    break
                if insere == "n":
                    print("Retornando ao cadastro de produtos.")
                    continue
                if insere not in ["s", "n"] or insere is None:
                    print("Digite uma opcao valida.")
                    continue
        if acao == 3:
            lista_modifica = cliente.itens_lista()
            while True:
                continuar = input("Deseja continuar a mudar o preço. (s/n): ").lower()
                if continuar == "s":
                    nome_item = input("Digite o nome do item que deseja modificar o preço: ").title()
                    if cliente.verifica_item(nome_item) == 1:
                        for i in lista_modifica:
                            if i[0] == nome_item:
                                print(f"Produto {i[0]} , Valor R$ {i[1]}")
                                while True:
                                    preco_item = input("Digite o valor do item a ser mudado: ")
                                    try:
                                        preco_item = float(preco_item)
                                        break
                                    except:
                                        print("Digite um preço valido.")
                                        continue
                                cliente.modificar_preco(nome_item, preco_item)
                if continuar not in ["s", "n"] or continuar is None:
                    print("Digite uma opcao valida.")
                    continue
                if continuar == "n":
                    break

        if acao == 4:
            while True:
                apagar = input("Deseja continuar no modulo de deleção de produto? (s/n) :").lower()
                if apagar == "s":
                    nome = input("Digite o nome do produto a ser deletado: ").title()
                    if cliente.verifica_item(nome) == 1:
                        cliente.apagar_item(nome)
                        print("Produto apagado.")
                        break
                    else:
                        break
                if apagar == "n":
                    print("Saindo do modulo.")
                    break
                if apagar not in ["s", "n"] or apagar is None:
                    print("Digite uma opçcao valida.")
                    continue
        if acao == 5:
            lista_de_compras = []
            while True:
                item = input("Digite o produto a ser adcionado: ").title()
                procura = cliente.verifica_item(item)
                if procura == 1:
                    while True:
                        qtd = input("Digite a quantidade de produtos a serem adcionados ao carrinho: ")
                        try:
                            qtd = int(qtd)
                            break
                        except:
                            print("Digite apenas numeros.")
                            continue
                    lista_de_compras.append([item, qtd])
                    print("Adcionado ao carrinho")
                    mais_produtos = input("Deseja adcionar mais itens? (s/n) : ").lower()
                    if mais_produtos == "s":
                        continue
                    if mais_produtos == "n":
                        break
                    if mais_produtos not in ["s", "n"] or mais_produtos is None:
                        print("Digite uma opção valida.")
                        pergunta = input("Deseja adcionar mais itens? (s/n) : ").lower()
                        if pergunta == "s":
                            continue
                        else:
                            print("Finalizando carrinho.")
                            break

                if procura == 0:
                    continue
            cliente.carrinho_compras(lista_de_compras)
            continue
        if acao == 6:
            print("Seu carrinho de compras.")
            if not cliente.lista_final:
                print("Esta vazio.")
            else:
                for i in cliente.lista_final:
                    print(f"Item {i[0]} quantidade {i[1]}")
            lista_de_compras = []
            print(50 * "#")
            print("FIM DO CARRINHO DE COMPRAS")
            time.sleep(2)
            continue
        if acao == 7:
            cliente.finaliza_compras()
            continue
        if acao == 8:
            print("FINALIZANDO...")
            time.sleep(2)
            break
