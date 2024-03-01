# %%

def operacao(op, *num):
    total = 0
    
    if op == "soma":
        for i in num:
            total += i
    
    elif op == "mult":
        total=1
        for i in num:
            total *= i
    
    return total

operacao("mult",1,2,3,4,5,6,7,8,9,10)


# %%

dados = ['téo', 'calvo', 31, ['nah', 'elaine', 'josefina']]

nome, sobrenome, *_, ex = dados

print(nome)
print(sobrenome)
print(ex)

# %%

a = 10
b = 20
print(a, b)

a, b = b,a

c = a
a = b
b = c
print(a, b)

# %%

x = 10,20
type(x)