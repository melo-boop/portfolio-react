from random import randint

def main():
    while True:
        dadosRPG = [4, 6, 18, 10, 12, 20, 100]
        resultados = []
        print("==Simulador de dados==")
        dados = int(input("Digite o Dado desejado: ")) 
        if dados not in dadosRPG:
            print("Digite um Dado valido!")
            break
        else:
            quantidade = int(input("Quantos dados você gostaria de rolar?: "))
            if quantidade <= 0:
                print("Quantidade Invalida!")
            else:
                for i in range(quantidade):
                    rolagem = randint(1, dados)
                    resultados.append(rolagem)
            print(f"A soma das rolagens foram: {sum(resultados)}")
            print(f"As rolagens foram: {resultados}")

main()