# info()

import pandas as pd

dados = {
    "smogon": [2, 3, 4, 5],
    "pessoas": ["joao", "hendrick", "muses", "gabriel"]
}

df = pd.DataFrame(dados)

print(df.info())


