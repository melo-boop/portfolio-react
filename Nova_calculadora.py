a = int(input("digite o primeiro numero:"))
b = int(input("digite o primeiro numero:"))

def menu():
    while True:
        print("selecione a operação abaixo: \n" \
        "1- Soma \n" \
        "2- Subtração \n" \
        "3- Multiplicação \n" \
        "4- Divisão \n" \
        "5- Sair")
        opcao = int(input("Selecione uma operação: "))

        if opcao == 1:
            soma(a, b)
        elif opcao == 2:
            subtracao(a, b)
        elif opcao == 3:
            multiplicacao(a, b)
        elif opcao == 4:
            divisao(a, b)
        elif opcao == 5:
            break
        else:
            print("Opção inesistente")

def soma(a, b):
    print(f'O resultado é {a + b}')
def subtracao(a, b):
    print(f'O resultado é {a + b}')
def multiplicacao(a, b):
    print(f'O resultado é {a + b}')
def divisao(a, b):
    print(f'O resultado é {a + b}')

menu()