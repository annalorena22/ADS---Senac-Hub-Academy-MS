class Livro:
    def __init__(self,titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro
        self.usuario = None
        self.status = "Disponível"
 
 
    def emprestar_livro(self,usuario):
        if self.status != "Disponível":
            return "Emprestar"
       
        self.usuario = usuario
        self.status = "Emprestado"
        
 
    def devolver_livro(self):
        if self.status != "Emprestado":
            return "Não pode ser devolvido."
        
        self.usuario = None
        self.status = "Disponível"