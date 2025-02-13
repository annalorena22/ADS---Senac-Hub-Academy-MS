#VIEW Cadastrar Usuário PRONTA(?)

import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QMainWindow
ui_file = "POO/Atividades/biblioteca-anna/ui/cadastrarUsuario.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botaoCadastrarUsuario.clicked.connect(self.cadastrarUsuario)

    def cadastrarUsuario(self):
        informacoesUsuario = {
            "nomeUsuario" : self.inputNomeDeUsuario.text(),
            "cpf" : self.inputCpf.text(),
            "telefoneUsuario" : self.inputTelefone.text()
        }
        print(informacoesUsuario)

        aviso = self.label_aviso
        if informacoesUsuario["nomeUsuario"] == "" or informacoesUsuario["telefoneUsuario"] == "" or informacoesUsuario["cpf"] == "":
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("Você deve preencher todos os campos para realizar o cadastro.")
        elif not informacoesUsuario["cpf"].isnumeric():
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("O CPF deve conter apenas números.")
        elif not informacoesUsuario["telefoneUsuario"].isnumeric():
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("O Telefone deve conter apenas números.")
        else:
            aviso.setStyleSheet("background-color: white; color: green")
            aviso.setText("Cadastro de usuário realizado com sucesso!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())