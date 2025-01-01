import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 20, 25, 30, 45, 60, 90, 100, 120, 150]

plt.plot(x, y, label="Line")
plt.title("Graph")
plt.legend()
plt.show()