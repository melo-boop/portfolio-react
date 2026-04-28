from math import sqrt

a = int(input("Digite o primeiro lado do triangulo: "))
b = int(input("Digite o segundo lado do triangulo: "))
c = int(input("digite o terceiro lado do triangulo: "))
perimetro = a + b + c 
semiper = perimetro / 2 
area = sqrt(semiper * (semiper - a ) * (semiper - b ) * (semiper - c ))

if a == b == c:
    print(f'O triangulo é equilatero, seu perimetro é de {perime elif})