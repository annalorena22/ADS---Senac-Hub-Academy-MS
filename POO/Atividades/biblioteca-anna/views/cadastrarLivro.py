import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QMainWindow
# from services import biblioteca
ui_file = "POO/Atividades/biblioteca-anna/views/cadastrarLivro.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botaoCadastrarL.clicked.connect(self.cadastrarLivro)
    def cadastrarLivro(self):
        informacoesLivro = {
            "nomeLivro" : self.inputNomeDoLivro.text(),
            "generoLivro" : self.inputGeneroDoLivro.text(),
            "autorLivro" : self.inputAutorDoLivro.text(),
            "codigoLivro" : self.inputCodigoDoLivro.text()
        }
        print(informacoesLivro)
        teste = ''
        print(teste != '')

        aviso = self.label_aviso
        if informacoesLivro["nomeLivro"] == "" or informacoesLivro["generoLivro"] == "" or informacoesLivro["autorLivro"] == "" or informacoesLivro["codigoLivro"] == "":
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