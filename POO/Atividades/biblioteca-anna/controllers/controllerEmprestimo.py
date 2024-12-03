# emprestimo_controller.py
from models.livro import Livro 
from models.usuario import Usuario 
from models.emprestimo import Emprestimo 
from config.database import Database  

class controllerEmprestimo:
    def __init__(self):
        self.bd = Database("localhost","root","","biblioteca")

    def realizar_emprestimo(self, cpf_usuario, cod_livro):
        self.bd.conectar()
        aviso = self.label_aviso

        queryCpf = Usuario.read(cpf_usuario)
        self.bd.cursor.execute(queryCpf)
        usuarioCpf = self.bd.cursor.fetchone()
        if not usuarioCpf:
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("Usuario não encontrado.")
        
        queryLivro = Livro.read(cod_livro)
        self.bd.cursor.execute(queryLivro)
        livroCod = self.bd.cursor.fetchone()
        if not livroCod:
            aviso.setStyleSheet("background-color: white; color:red")
            aviso.setText("Livro não encontrado.")


        #COMO FAZ?

        queryEmprestar = Emprestimo.create()
        self.bd.cursor.execute(queryEmprestar)

        
        queryStatus= Livro.update_status(status)
        self.bd.cursor.execute(queryStatus)

        self.bd.conexao.commit()
        print("Empréstimo realizado com sucesso.")

        self.bd.desconectar()