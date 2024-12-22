# dropna, inplace

import pandas as pd

dados = {
    "smogon": [2, 3, 4, 5, 6, 7],
    "pessoas": ["joao", "hendrick", "muses", "gabriel", None, "giovana"]
}

df = pd.DataFrame(dados)

df.dropna(inplace = True)

print(df)

