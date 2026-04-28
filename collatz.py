num = int(input("Digite um numero: "))
    

def seq_collatz(num):
    lista = []
    while num != 1: 
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = int((3 * num) + 1)
        lista.append(num)
    return lista
    
collatz = seq_collatz(num)

print(f'O numero inicial é {num} e a sequencia é: \n'
      f'{collatz}')