
multa = 0.00
opcao = 0
limite_peso = 50.00
continuar = True

while continuar:

    print("\n[Menu] -----------------")
    print("Iniciar redimento diário - [1]")
    print("Ver minhas multas - [2]")
    print("Fechar programa - [3]")
    print("--------------------------")

    opcao = int(input("Selecione um opção: "))
    print("\n")

    match opcao:
        case 1:
            kilo_pesca = float(input("Quantos kilos de pescar você realizou hoje?:  "))

            if(kilo_pesca > limite_peso):
                multa += 4.00
                print("Você excedeu o limite de peso maior que o estabelecido pelo regulamento de pesca do estado de São Paulo")
                print("Você recebeu uma multa R$ 4.00")
            else:
                print("Limite de peso não foi maior que o estabelecido pelo regulamento de pesca do estado de São Paulo\n")
        case 2:
            print("Suas multas são do valor de R$: {}\n".format(multa))
        case 3:
            print("Encerrando programa..\n")
            continuar = False
        case _:
            print("[Erro] Digite um opção de 1 a 3\n")

                
