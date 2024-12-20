from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle('Janela com Layout')

layout = QVBoxLayout() # cria um layout vertical para posicionar os wigets

label = QLabel('Aqui está o rótulo', parent=window)
button = QPushButton('Clique Aqui', parent=window)

layout.addWidget(label)
layout.addWidget(button)

window.setLayout(layout)

window.show()
app.exec_()
