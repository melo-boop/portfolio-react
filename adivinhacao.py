from random import randint

def adivinhacao():
    secreto = randint(0, 100)
    tentativas = 0

    while True:
        chute = int(input("Tente adivinhar o numero de 0 a 100: "))
        tentativas += 1

        if secreto > chute:
            print("Chutou baixo")
        elif secreto < chute:
            print("Chute alto ")
        else:
            print(f"Você acertou!!! O numer era {secreto} e levou {tentativas} tentativas para acertar.")
            break
while True:
    adivinhacao()
    continuar = str(input("Deseja continuar jogando? s / n ?")).lower().strip()
    if continuar != "s":
        break
            