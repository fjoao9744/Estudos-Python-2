# json

import pandas as pd

dados = {
    "smogon": [2, 3, 4, 5],
    "pessoas": ["joao", "hendrick", "muses", "gabriel"]
}

df = pd.DataFrame(dados)

df.to_json("smogon.json")

df = pd.read_json('smogon.json')

print(df.to_string())