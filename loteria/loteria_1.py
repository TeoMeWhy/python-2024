numero = int(input("Entre com um número entre 1 e 15: "))

numero_sorte = 7

if numero == numero_sorte:
    print("Você acertou!!")
elif numero > numero_sorte:
    print("Você errou! Tente um número menor!")
else:
    print("Você errou! Tente um número maior")