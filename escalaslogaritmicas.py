from math import log10 

def menu():
    while True:
        print("calculadora de escalas logaritmicas")
        print("selecione uma opção abaixo: \n" \
        "1- Escala pH \n" \
        "2- Escala Richtere \n" \
        "3- Sair")
        
        opção = int(input("Escolha"))

        if opção == 1:
            print("pH placeholder")
        elif opção == 2:
            print("richter placeholder")
        elif opção == 3:
            print("Até logo!")
        break
    else:
        print("opção invalida")

def ph():
    print("Escala de pH")
    print("-------------")

    while True:
        print("para sair do programa digite 0")
        h30 = float(input("digite a quantidade de h30\mol na substancia: "))

        if h30 == 0:
            print("saindo")
            break
        else:
            ph = -1 * log10(h30)

            if ph > 0 and ph < 7:
                print(f'O pH de {ph:.2f} é considerado acido')
            elif ph < 7 and ph <= 14:
                print(f'O pH de {ph:.2f} é considerado elcalino')
            elif ph == 7:
                print(f'O pH de 7 é cosiderado neutro')
            else:
                print("O pH nao pode ser calculado")

def richter():
    print("escala Richter")
    print("--------------")

    while True:
        print("selecione uma opção abaixo: \n" \
        "1 - Joules para Magnetude \n" \
        "2 - Magnetude para Joules \n" \
        "3 - Voltar ao menu Principal")
        opcao = int(input("Opção Escolhida: "))

        if opcao == 1:
            joules = float(input("Digite a quantidadde de energia(joules): "))
            if joules <= 0:
                print("Qunatidade de energia invalida")
            else:
                res = (log10(joules) - 4.8) / 1.5
                print(f'A magnetude do terremoto é de {res:.2f} na escala Richter')
        elif opcao == 2: 
                magnetude = float(input("digite a magnetude do terremoto"))       
                if magnetude <= 0:
                    print("Magnetude invalida!")
                else:
                    res = 10 ** (1.5 * magnetude + 4.8)
                    print(f'A magnetude equivalente a {res:.2f} joules de Eenergia')
        elif opcao == 3 :
            break
                
menu()