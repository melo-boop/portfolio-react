import random 
import string 

def gerador():
    while True: 
        print("~-~-~-~-~-~GERADOR DE SENHAS~-~-~-~-~-~")
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ""
        tam = int(input("Digite o tamanho de sua senha: "))
        if tam <= 5 or tam >= 20: 
            print("Digite uma quantidade de 6 a 19 caracteres: ")
        else:
            for i in range(tam):
                senha += random.choice(caracteres)
            print(f'Senha Gerada: {senha}')

gerador()