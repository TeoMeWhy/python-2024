# Faça um programa que verifique se a pessoa pertence
# à família “calvo” ou “silva”.

nome = input("Entre com o seu nome: ")
nome = nome.lower()

if "calvo" in nome or "silva" in nome:
    print("Você pertence a família calvo ou silva")

else:
    print("Não conheço a sua família")
