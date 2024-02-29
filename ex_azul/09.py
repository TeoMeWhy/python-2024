# Faça um programa que receba uma quantidade indefinida
# de valores correspondentes a “saldo em conta”,
# mas quando o usuário apertar “enter” sem digitar valor algum,
#  o programa para de receber valores, e exibe a soma te todos
#  os valores digitados anteriormente.

total = 0

while True:

    entrada = input("Entre com o valor do saldo: ")
    if entrada == "":
        break
    
    total += float(entrada)

print(total)