#CONTROLER Livro PRONTA(?)

from models.livro import Livro
from config.database import Database

class ControllerLivro:
    def __init__(self):
        self.bd = Database("localhost","root","","biblioteca")

    def cadastrarLivro(self, informacoesLivro):
        self.bd.conectar()
        self.livro = Livro(informacoesLivro['titulo'], informacoesLivro['autor'], informacoesLivro['genero'], informacoesLivro['codigo'])
        query = self.livro.create()
        self.bd.cursor.execute(query)
        self.bd.conexao.commit()
        self.bd.desconectar()

    def procurarLivro(self):
        self.bd.conectar()
        query = self.livro.read()
        self.bd.cursor.execute(query)
        resultado = self.bd.cursor.fetchall() 
        self.bd.desconectar()
        return resultado

    def atualizarLivro(self):
        self.bd.conectar()
        query = self.livro.update()
        self.bd.cursor.execute(query)
        self.bd.conexao.commit()
        self.bd.desconectar()

    def excluirLivro(self, cod_livro):
        self.bd.conectar()
        query = Livro.delete(cod_livro)
        self.bd.cursor.execute(query)
        self.bd.conexao.commit()
        self.bd.desconectar()
    