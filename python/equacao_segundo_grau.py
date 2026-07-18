import math


continuar = True


while continuar:

     
    print("\n[Menu] --------------")
    print("[1]. Iniciar programa")
    print("[2]. Encerrar")
    print("-----------------------")
    
    try:
        opcao = int(input("Selecione uma opção: "))
    except ValueError:
        print("Por favor, digite apenas números.")
        continue

    match opcao:
        case 1:
            a = int(input("Informe o valor do A: \n"))
            b = int(input("Informe o valor do B: \n"))
            c = int(input("Informe o valor do C: \n"))

            if(a == 0):
                print("O valor de A igual a zero, a equação não é do segundo grau")

           
            delta = (b ** 2) - 4 * a * c

            print(f"O resultado do delta: {delta}")

            if delta > 0:
                print("A equação tem duas raízes reais e diferentes.")

                raiz1 = (-b + (delta ** (1 / 2))) / (2 * a)
                raiz2 = (-b - (delta ** (1 / 2))) / (2 * a)

                print(f"Delta maior que zero. A raíz 1 é {raiz1}, e a raiz 2 é {raiz2}")

            elif delta == 0:
                print("A equação tem uma única raiz real (ou duas ráizes iguais).")
                raiz = (-b) / (2 * a)
                print(f"Delta é zero. A raíz é {raiz}")
            elif delta < 0:
                print("A equação não possui raízes reais.")
        case 2:
            print("Encerrando programa...")
            continuar = False
        case _:
            print("Selecione um opção de 1 a 2")
            
            
               
            

