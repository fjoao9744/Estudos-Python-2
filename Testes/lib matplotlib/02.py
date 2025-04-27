import matplotlib.pyplot as plt

x = [1, 2, 3, 5, 7, 8, 9]
y = [1, 3, 5, 7, 9, 11, 12]

plt.plot(x, y)

# personalizando
plt.title("Meu grafico")
plt.xlabel("eixo X")
plt.ylabel("eixo Y")
plt.grid(True)


plt.show()