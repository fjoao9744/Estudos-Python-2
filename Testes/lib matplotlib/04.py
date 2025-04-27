import matplotlib.pyplot as plt

labels = ["Maça", "Banana", "Melão"]
valores = [3, 5, 4]

plt.pie(valores, labels=labels, autopct='%1.1f%%')
plt.title('Distribuição de Frutas')

plt.show()