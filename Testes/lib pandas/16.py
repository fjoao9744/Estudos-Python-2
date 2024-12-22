# dropna

import pandas as pd

dados = {
    "smogon": [2, 3, 4, 5, None, 7],
    "pessoas": ["joao", "hendrick", "muses", "gabriel", None, "giovana"]
}

df = pd.DataFrame(dados)

new_df = df.dropna()

print(new_df)

