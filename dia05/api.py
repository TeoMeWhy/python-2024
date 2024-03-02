
# %%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"
resposta = requests.get(url)

# %%
resposta.status_code

# %%
dados = resposta.json()

# %%
for i in dados:
    print(i['localized_name'])

# %%
df = pd.DataFrame(dados)

df.to_csv("heroes_dota.csv", sep=";")

# %%

url = "https://api.opendota.com/api/proMatches"
data = requests.get(url).json()
df_partida = pd.DataFrame(data)
df_partida.to_csv("partidas_dota.csv", sep=";")

# %%

df_partida