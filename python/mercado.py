estoque = {
    "Maça": 10,
    "Banana": 20,
    "Laranja": 15
}

continuar = True

while continuar:
    
    print("\n[Menu] -----------------")
    print("[1]. Adicionar Novo Item")
    print("[2]. Ver Estoque")
    print("[3]. Alterar Quantidade")
    print("[4]. Remover Item")
    print("[5]. Encerrar")
    print("------------------------")
    
    try:
        opcao = int(input("Selecione uma opção: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        continue

    match opcao:
        case 1:
            nome_item = input("Qual nome do item que você deseja cadastrar?: ")
            escolha = int(input(f"Deseja cadastrar quantidade inicial para {nome_item}? [1] Sim [2] Não: "))
            
            if escolha == 1:
                qtd = int(input("Quantidade: "))
                estoque[nome_item] = qtd
            else:
                estoque[nome_item] = 0
            print(f"{nome_item} adicionado!")

        case 2:
            print("\n---[Estoque] ---")
            for item, quantidade in estoque.items():
                print(f"Item: {item:10} | Quantidade: {quantidade}")

        case 3:
            item_procurado = input("Qual o nome do item?: ")
           
            if item_procurado in estoque:
                print(f"Item encontrado: [{item_procurado}] | Atual: {estoque[item_procurado]}")
                tipo_alteracao = int(input("[1] Aumentar | [2] Diminuir: "))
                valor = int(input("Valor da alteração: "))
                
                if valor < 0:
                    print("Erro: Use valores positivos para a alteração.")
                else:
                    if tipo_alteracao == 1:
                        estoque[item_procurado] += valor
                    elif tipo_alteracao == 2:
                        if estoque[item_procurado] - valor < 0:
                            print("Erro: Estoque insuficiente para essa retirada.")
                        else:
                            estoque[item_procurado] -= valor
                    print("Atualizado com sucesso!")
            else:
                print("Item não encontrado no sistema.")
        case 4:
            if item_procurado in estoque:
                print(f"Removendo [{item_procurado}] que tinha {estoque[item_procurado]} unidades...")
                del estoque[item_procurado]
                print("Item removido com sucesso!")
            else:
                print(f"Erro: O item '{item_procurado}' não foi encontrado no estoque.")
        case 5:
            print("Encerrando programa...")
            continuar = False
        
        case _:
            print("[Erro] Digite uma opção válida (1 a 4).")