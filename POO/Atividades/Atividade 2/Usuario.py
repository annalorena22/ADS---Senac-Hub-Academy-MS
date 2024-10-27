
class Usuario:
    MAX_EMPRESTIMO = 3
    def __init__(self, cpf, nome, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []
        
    def pegar_emprestado(self, livro):
        if len(self.lista_livros) == self.MAX_EMPRESTIMO:
            return 'Você não pode pegar mais de 3 livros emprestado.'
        
        self.lista_livros.append(livro.titulo)
    

