def menu():
    while True: 
        print("CALCULADORA BÁSICA")
        print("1 - Soma \n" \
        "2 - Subtração \n" \
        "3 - Multiplicação \n" \
        "4 - Divisão \n" \
        "5 - Sair")
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 1:
            soma()
        elif opcao == 2:
            subtracao()
        elif opcao == 3:
            multiplicacao()
        elif opcao == 4:
            divisao()
        elif opcao == 5: 
            break
        else:
            print("opção Invalida")

def soma():
        num1 = int(input("Digite o Pimeiro número: "))
        num2 = int(input("digite o Segundo número: "))

        soma = num1 + num2

        print(f"O resultado da soma é {soma}")

def subtracao():
        num1 = int(input("Digite o Primeiro número: "))
        num2 = int(input("Digite o Segundo número: "))

        Subtracao = num1 - num2

        print(f"O resultado da Subtração é {subtracao}")

def multiplicacao():
        num1 = int(input("Digite o Primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        multipliacao = num1 * num2 

        print(f"O resultado da Multiplicação é {multiplicacao}")

def divisao():
        num1 = int(input("Digite o prieiro número: "))
        num2 = int(input("Digite o Segundo número: "))

        divisao = num1 / num2 

        print(f"O resultado da Divisão é {divisao}")

menu()