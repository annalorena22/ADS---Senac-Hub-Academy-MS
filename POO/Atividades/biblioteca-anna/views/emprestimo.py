import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QMainWindow
ui_file = "POO/Atividades/biblioteca-anna/views/emprestimo.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())