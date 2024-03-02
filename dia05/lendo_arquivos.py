# %%
arquivo = open("arquivo.txt", 'a') # w
arquivo.write("1")
arquivo.close()


# %%

arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
print(type(conteudo))

# %%

arquivo = open("arquivo.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

print(linhas)


# %%

with open("arquivo.txt", "r") as file:
    conteudo = file.read()

print(conteudo)