from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([]) # obrigatorio, todo codigo tem que ter essa instancia

# Cria uma janela (QWidget é a base para todas as janelas)
window = QWidget()
window.setWindowTitle('Minha Primeira Janela PyQt')

# Cria um rótulo
label = QLabel('Olá, PyQt!', parent=window)
label.move(50, 50)  # Posiciona o rótulo dentro da janela

# Mostra a janela
window.show()

# Executa a aplicação
app.exec_()
