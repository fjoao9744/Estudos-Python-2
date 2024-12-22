# mean(), median(), mode()

import pandas as pd

dados = {
    "smogon": [2, 3, 4, 5, 6, 7, None],
    "pessoas": ["joao", "hendrick", "muses", "gabriel", None, "giovana", None]
}

df = pd.DataFrame(dados)

x = df["smogon"].mean()

df["smogon"].fillna(x, inplace=True)

print(df)



