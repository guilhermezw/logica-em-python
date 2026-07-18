

continuar = True

while continuar:

    print("\n[Menu] ---------------")
    print("Iniciar programa - [1]")
    print("Fechar programa - [2]")
    print("-------------------------")

    opcao = int(input("Selecione uma opção: "))

    match opcao:
        case 1:
            print("\n")
            valor_horas_trabalhas = float(input("Informe quanto você receber em R$ por horas trabalhadas: "))
            horas_trabalhas_mes = int(input("Informe quantas horas você trabalha mês: "))

            print("\n")

            salario_bruto = valor_horas_trabalhas * horas_trabalhas_mes

            desconto_imposto_renda = salario_bruto * 0.11
            desconto_inss = salario_bruto * 0.08
            desconto_sindicato = salario_bruto * 0.05

            total_desconto = desconto_imposto_renda + desconto_inss + desconto_sindicato
            salario_liquido = salario_bruto - total_desconto

            print("+ Salário Bruto: R$ {:.2f}".format(salario_bruto))
            print("- IR (11%): R$ {:.2f}".format(desconto_imposto_renda))
            print("- INSS (8%): R$ {:.2f}".format(desconto_inss))
            print("- Sindicato (%5): R$ {:.2f}".format(desconto_sindicato))
            print("= Salário Liquido: R$ {:.2f}".format(salario_liquido))
            print("\n")

        case 2:
            print("Encerrando programa..\n")
            continuar = False
        case _:
            print("[Erro] Digite um opção de 1 a 2\n")


