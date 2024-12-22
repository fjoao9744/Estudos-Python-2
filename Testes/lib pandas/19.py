# fillna

import pandas as pd

dados = {
    "smogon": [2, 3, 4, 5, 6, 7, None],
    "pessoas": ["joao", "hendrick", "muses", "gabriel", None, "giovana", None]
}

df = pd.DataFrame(dados)

df["pessoas"].fillna("smogon", inplace = True) # substitui todo None por "smogon"

print(df)
