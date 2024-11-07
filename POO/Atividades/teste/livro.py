class Livros:
    def __init__(self, titulo, autor, genero, isbn, status="Disponível"):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.isbn = isbn
        self.status = status 

    def create(self):
        query = f"INSERT INTO livro (titulo, autor, genero, isbn, status) VALUES ('{self.titulo}', '{self.autor}', '{self.genero}', '{self.isbn}', '{self.status}')"
        return query

    def update(self, isbn):
        query = f"UPDATE livro SET titulo = '{self.titulo}', autor = '{self.autor}', genero = '{self.genero}', status = '{self.status}' WHERE isbn = '{isbn}'"
        return query

    @staticmethod
    def delete(isbn):
        query = f"DELETE FROM livro WHERE isbn = '{isbn}'"
        return query

    @staticmethod
    def read_all():
        return "SELECT * FROM livro"


# livros = controller.listar_livros()
# for livro in livros:
#     print(livro)