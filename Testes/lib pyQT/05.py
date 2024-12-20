# teste de layouts

from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

main_layout = QVBoxLayout()
# QHBoxLayout()
# QGridLayout()
# QFormLayout()

label = QLabel("QVBoxLayout")
label1 = QLabel("label 1")
label2 = QLabel("label 2")
label3 = QLabel("label 3")

main_layout.addWidget(label)
main_layout.addWidget(label1)
main_layout.addWidget(label2)
main_layout.addWidget(label3)


window.setLayout(main_layout)

window.show()
app.exec_()