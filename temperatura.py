def menu():
    print("Xx~~ Conversor de Temperatura ~~xX \n" \
    "1 ~ Celsius para Fahrenheit \n" \
    "2 ~ Fahrenheit para Celsius \n" \
    "3 ~ Celsius para Kelvin \n" \
    "4 ~ Fahrenheit para Kelvin \n" \
    "5 ~ Kelvin para Celsius \n" \
    "6 ~ Kenvin para Fahrenheit")
    opcao = int(input(" Escolha sua opção:"))
    temp = float(input("Digite a Temperatura "))

    match opcao:
        case 1:
           CpF(temp)
        case 2:
           FpC(temp)
        case 3:
           CpK(temp)
        case 4:
           FpK(temp)
        case 5:
           KpC(temp)
        case 6:
           return 0
        case _:
            print("Opção invalida")

def CpF(x):
   res = (x * (9/5)) + 32
   print(f'{x}ºC equivalem a {res:.2f}ºF')

def FpC(x):
   res = (x - 32) * (5/9)
   print(f'{x}ºF equivalem a {res:.2f}ºC')

def CpK(x):
   res = x + 273.15 
   print(f'{x}ºC equivalem a {res:.2f}ºK')

def FpK(x):
   res = (x - 32) * 5/9 + 273.15 
   print(f'{x}ºF equivalem a {res:.2f}ºK')

def KpC(x):
   res = x - 273,15 
   print(f'{x}ºK equivalem a {res:.2f}ºC')

def KpF(x):
   res = (x  - 273.15) * 9/5 + 32
   print(f'{x}ºK equivalem a {res:.2f}ºC')



menu()