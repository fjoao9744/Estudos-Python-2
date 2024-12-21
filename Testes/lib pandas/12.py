# max_row

import pandas as pd

pd.options.display.max_rows = 3 
# agora o pandas só vai poder exibir tabelas de no maximo 3 linhas

df = pd.read_csv("smogon.csv")

print(df)

