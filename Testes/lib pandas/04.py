# index

import pandas as pd

a = [1, 2, 3]

serie = pd.Series(a, index=['a', 'b', 'c'])

print(serie)

print(serie['b'])
