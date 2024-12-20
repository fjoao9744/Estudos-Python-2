# teste de widgets

from PyQt5.QtWidgets import *

app = QApplication([])

# conteiner principal
window = QWidget()

#layout vertical
layout = QVBoxLayout()

#label
label = QLabel("isso é uma label", parent=window)

#botão
button = QPushButton("isso é um pushbutton", parent=window)

# caixa de entrada
line_edit = QLineEdit("isso é uma linha de edição", parent=window)

#caixa de texto
text_edit = QTextEdit("isso é uma linha de texto", parent=window)

#checkbox
checkbox = QCheckBox('Aceito os termos')

#checkbox mas com bolinha
radio_button = QRadioButton('Opção 1')

# caixa de escolha
combo_box = QComboBox()
combo_box.addItem('Opção 1')
combo_box.addItem('Opção 2')

# entrada de numeros
spin_box = QSpinBox()

# entrada de numeros flutuantes
double_spin_box = QDoubleSpinBox()

# adicionando todos os widgets no layout
layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(line_edit)
layout.addWidget(text_edit)
layout.addWidget(checkbox)
layout.addWidget(radio_button)
layout.addWidget(combo_box)
layout.addWidget(spin_box)
layout.addWidget(double_spin_box)

window.setLayout(layout)

window.show()
app.exec_()


