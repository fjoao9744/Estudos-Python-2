import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y, '-.') # estilização

"""
Estilos de linha:
- linha solida
-- linha tracejada
: linha pontilhada
-. linha com ponto e traço
"""

plt.title('Gráfico Estilizado')
plt.show()
