import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QMainWindow
ui_file = "POO/Atividades/biblioteca-anna/views/cadastrarUsuario.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botaoCadastrarUsuario.clicked.connect(self.cadastrarUsuario)

    def cadastrarUsuario(self):
        informacoesUsuario = {
            "nomeUsuario" : self.inputNomeDeUsuario.text(),
            "telefoneUsuario" : self.inputTelefone.text(),
            "CPF" : self.inputCPF.text(),
            
        }
        print(informacoesUsuario)
        teste = ''
        print(teste != '')

        aviso = self.label_aviso
        if informacoesUsuario["nomeUsuario"] == "" or informacoesUsuario["telefoneUsuario"] == "" or informacoesUsuario["CPF"] == "":
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("Você deve preencher todos os campos para realizar o cadastro.")
        else:
            aviso.setStyleSheet("background-color: white; color: green")
            aviso.setText(" Cadastro realizado com sucesso!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())