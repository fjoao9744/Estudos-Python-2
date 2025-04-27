import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label='Linha 1') # label permite que a linha apareça na legenda
plt.plot(x, y2, label='Linha 2')

plt.title('Gráficos Juntos')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()  # Mostrar legenda

plt.show()
