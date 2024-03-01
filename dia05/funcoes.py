# y = f(x) = x + 10
# -------
# y = f(x) = x * x + 1

# %%
def funcao(x):
    res = x + 10
    return res

y = funcao(100)
print(y)

# %%

# definção da função
def fodase():
    print("fodase")

# invocação da função
fodase()

# %%

def soma(a=0, b=0):
    return a + b

soma(10, 20)

# %%
soma(10)

# %%
soma(b=10)

# %%
soma(a=10, b=20)

# %%
soma(b=10, a=20)

# %%
soma(10, b=10)