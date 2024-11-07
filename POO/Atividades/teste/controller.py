from livro import Livros
from database import Database

class ControllerLivro:
    def __init__(self, db: Database):
        self.db = db

    def cadastrar_livro(self, livro):
        query, values = livro.create()
        self.db.cursor.execute(query, values)
        self.db.conexao.commit()

    def atualizar_livro(self, livro, id_livro):
        query, values = livro.update(id_livro)
        self.db.cursor.execute(query, values)
        self.db.conexao.commit()

    def deletar_livro(self, id_livro):
        query, values = Livros.delete(id_livro)
        self.db.cursor.execute(query, values)
        self.db.conexao.commit()
        self.db.desconectar()

    def listar_livros(self):
        query = Livros.read_all()
        self.db.cursor.execute(query)
        livros = self.db.cursor.fetchall()
        return livros


# livro = Livros(titulo="Livro Exemplo", autor="Autor", genero="Ficção", ....)
# controller.cadastrar_livro(livro)


# livro_a_ser_atualizado = Livros(titulo="Novo Título", autor="Autor", genero="Ficção", ....)
# controller.atualizar_livro(livro_a_ser_atualizado, isbn=1)

# controller.deletar_livro(isbn=1)
