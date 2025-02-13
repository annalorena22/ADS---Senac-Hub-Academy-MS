#MODEL Usuario PRONTA(?)

class Usuario:
    MAX_EMPRESTIMO = 3
    def __init__(self,nome,cpf,telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_emprestado(self,livro):
        if len(self.lista_livros) == self.MAX_EMPRESTIMO:
            return 'Limite de empréstimos atingido.'
        
        self.lista_livros.append(livro.titulo)

    def create(self):
        return f'insert into usuarios(nome, cpf, telefone) values("{self.nome}", "{self.cpf})";'
        
    def read(self):
        return f'select * from usuarios where nome like "{self.nome}" or cpf like "{self.cpf}";'
    
    def update(self):
        return f'update usuarios set nome = {self.nome}, telefone = {self.telefone} where cpf = {self.cpf};'
    
    @staticmethod
    def delete(cpf):
        return f'delete from usuarios where cpf={cpf};'
    
    