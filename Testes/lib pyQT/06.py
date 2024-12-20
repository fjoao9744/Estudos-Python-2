from PyQt5.QtWidgets import QApplication, QWidget, QStyleFactory, QPushButton

app = QApplication([])

class MainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
                
        botao = QPushButton("texto", parent=self)
        
        botao.setStyleSheet("""
            QPushButton {
                background-color: "grey";
            }
        """)        

janela_principal = MainPage()

janela_principal.show()
app.exec_()