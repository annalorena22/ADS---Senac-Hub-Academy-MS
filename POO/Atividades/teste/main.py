from controller import ControllerLivro
from livro import Livros
from database import Database

db = Database("localhost", "root", "", "teste")

db.conectar()
# print(db.conexao)
db.desconectar()

controller = ControllerLivro(db)
