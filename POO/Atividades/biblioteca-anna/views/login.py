#VIEW Login PRONTA(?)

import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QMainWindow
ui_file = "POO/Atividades/biblioteca-anna/ui/login.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botaoLogin.clicked.connect(self.logar)

    def logar(self):
        informacoesUsuario = {
            "login" : self.inputLogin.text(),
            "senha" : self.inputSenha.text()
        }
        print(informacoesUsuario)

        aviso = self.label_aviso
        if informacoesUsuario["login"] == "" or informacoesUsuario["senha"] == "":
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("Você deve preencher todos os campos para realizar o cadastro.")
        else:
            aviso.setStyleSheet("background-color: white; color: green")
            aviso.setText("Login realizado com sucesso!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())