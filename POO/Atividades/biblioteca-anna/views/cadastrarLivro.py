import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QMainWindow
ui_file = "POO/Atividades/biblioteca-anna/views/cadastrarLivro.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botaoCadastrarL.clicked.connect(self.clicked)
    def clicked(self):
        self.toolButtonStyle
        # if self.inputNomeDoLivro == "" and len(inputNomeDoLivro) < 10:
        #     print("tem q preencher tudo carai")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())