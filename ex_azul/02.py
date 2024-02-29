# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de água

escolha = input("Você gostaria de uma garrafa de água mineral ou com gás? [mineral/gas]: ")
quantidade = int(input("Quantas águas você deseja? "))

total = 0

if escolha == "mineral":
    total = 1.5 * quantidade 

elif escolha == "gas":
    total = 2.5 * quantidade

else:
    print("Faça uma escolha válida!")


print("Você me deve R$", total)