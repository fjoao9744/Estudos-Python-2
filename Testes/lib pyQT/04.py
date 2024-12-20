# teste do layout e do conteiner groupbox

from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()


layout = QVBoxLayout() # layout principal
group_layout = QVBoxLayout() # layout do group

group_box = QGroupBox('Grupo de Opções') # conteiner do group

label1 = QLabel("label 1")
label2 = QLabel("label 2")
label3 = QLabel("label 3")

group_layout.addWidget(label1) # adiciona widgets no layout do grupo
group_layout.addWidget(label2)
group_layout.addWidget(label3)

group_box.setLayout(group_layout) # seta o layout do conteiner

layout.addWidget(group_box) # adiciona o conteiner no layout principal

window.setLayout(layout)


window.show()
app.exec_()


