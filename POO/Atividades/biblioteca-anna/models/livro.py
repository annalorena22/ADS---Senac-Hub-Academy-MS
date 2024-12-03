#MODEL Livro PRONTA(?)

class Livro():
    def __init__(self, titulo, autor, genero, cod_livro, status):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro
        self.status = status
        self.usuario = None

    def create(self):
        return f'insert into livros(titulo, autor, genero, status, codigo) values("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", "{self.cod_livro}");'

    
    def read(self):
        return f'select * from livros where titulo like "{self.titulo}" or autor like "{self.autor}" or genero like "{self.genero}" or codigo like "{self.cod_livro}";'

    
    def update(self):
        return f'update livros set titulo = {self.titulo}, autor = {self.autor}, genero = {self.genero} where codigo = {self.cod_livro};'
    
    def update_status(self):
        return f'update livros set status = {self.status} where codigo = {self.cod_livro};'
    
    
    @staticmethod
    def delete(cod_livro):
        return f'delete from livros where codigo={cod_livro};'