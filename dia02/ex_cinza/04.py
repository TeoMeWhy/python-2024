# Faça um programa que calcule a raiz quadrada de um número
# e exiba o resultado.

numero = int(input("Entre com um número para calcular a raiz quadrada: "))

raiz = numero ** 0.5
raiz = round(raiz, 2)

print("Raiz quadrada de", numero, "é:", raiz)