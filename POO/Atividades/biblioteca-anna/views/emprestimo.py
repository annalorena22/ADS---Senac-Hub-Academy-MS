#VIEW Empréstimo PRONTA(?)

import sys
from PyQt6 import uic 
from PyQt6.QtWidgets import QApplication, QMainWindow
ui_file = "POO/Atividades/biblioteca-anna/ui/emprestimo.ui"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.botaoRealizarEmprestimo.clicked.connect(self.realizarEmprestimo)

    def realizarEmprestimo(self):
        informacoesEmprestimo = {
            "codigoDoLivro" : self.inputCodigoDoLivro.text(),
            "CPF" : self.inputCPF.text(),
            "dataEmprestimo" : self.inputDataEmprestimo.text(),
            "dataDevolucao" : self.inputDataDevolucao.text()
        }
        print(informacoesEmprestimo)

        aviso = self.label_aviso
        if informacoesEmprestimo["codigoDoLivro"] == "" or informacoesEmprestimo["CPF"] == "" or informacoesEmprestimo["dataEmprestimo"] == "" or informacoesEmprestimo["dataDevolucao"] == "":
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("Você deve preencher todos os campos para realizar o cadastro.")
        else:
            aviso.setStyleSheet("background-color: white; color: green")
            aviso.setText("Empréstimo realizado com sucesso!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())