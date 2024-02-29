# Faça um programa que receba 4 alturas,
# armazene em uma lista e depois mostre
# a soma dessas alturas.

a1 = int(input("Entre com a alturas em cm 1: "))
a2 = int(input("Entre com a alturas em cm 2: "))
a3 = int(input("Entre com a alturas em cm 3: "))
a4 = int(input("Entre com a alturas em cm 4: "))

alturas = [a1,a2,a3,a4]

soma = sum(alturas)
print(soma)