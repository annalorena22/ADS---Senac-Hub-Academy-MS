from models.livros import Livro
from config.database import Database

class ControllerLivro:
    def __init__(self):
        self.bd = Database("localhost","root","","biblioteca")

    def cadastrarLivro(self, informacoesLivro):
        self.bd.conectar()

        self.livro = Livro(informacoesLivro['titulo'], informacoesLivro['autor'], informacoesLivro['genero'], informacoesLivro['codigo'])
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
    


controladora = ControllerLivro()
controladora.cadastrarLivro()
controladora.procurarLivro()
print("Cadastrou.... Será?!?!?!?!")