class Livro:
    def __init__(self, cpf, nome, qntdLivroEmprestado, codLivro, titulo, autor, genero):
        super().__init__(cpf, nome, qntdLivroEmprestado)
        self.codLivro = codLivro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = "Disponível"
        self.usuario = None

    def emprestarLivro(self, usuario):
        if self.status != "Disponível":
            return 'Livro emprestado.'
        
        self.usuario = usuario
        self.usuario = "Emprestado"
    
    def devolverLivro(self):
        if self.status != "Emprestado":
            return 'Não pode ser devolvido'

        self.usuario = None
        self.status = "Disponível"


        # if self.qntdLivroEmprestado == self.max_emprestimo:
        #     print("Você atingiu a quantidade máxima de livros emprestados. Devolva pelo menos 1(um) para realizar o empréstimo.")
        # else:
        #     print(f"Você pegou o {self.titulo} emprestado.")
    