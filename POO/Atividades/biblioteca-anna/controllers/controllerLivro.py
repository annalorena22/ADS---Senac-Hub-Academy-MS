from models.livros import Livros
from config.database import Database

class ControllerLivro:
    def __init__(self):
        self.bd = Database("localhost","root","","biblioteca")

    def cadastrarLivro(self):
        self.bd.conectar()

        self.livro = Livros("Dom Casmuro", "Machado de Assis", "Suspense", 123)
        self.bd.cursor.execute(self.livro.create())
        self.bd.conexao.commit()
        self.bd.desconectar()

    def procurarLivro(self):
        self.bd.conectar()
        self.bd.cursor.execute(self.livro.read())
        resultado = self.bd.cursor.fetchall() 
        self.bd.desconectar()
        print(resultado)

    def atualizarLivro(self):
        pass

    def excluirLivro(self):
        pass
    
    # 30min para terminar!!!!


controladora = ControllerLivro()
controladora.cadastrarLivro()
controladora.procurarLivro()
print("Cadastrou.... Será?!?!?!?!")