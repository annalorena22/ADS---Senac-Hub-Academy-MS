#MODEL Emprestimo PRONTA(?)

class Emprestimo():
    def __init__(self, cod_livro, cpf_usuario, data_emprestimo, data_devolucao, status):
        self.cod_livro = cod_livro
        self.cpf_usuario = cpf_usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.status = status


    def create(self):
        return f'insert into emprestimos(cod_livro, cpf_usuario, data_emprestimo, data_devolucao) values("{self.cod_livro}", "{self.cpf_usuario}", "{self.data_emprestimo}", "{self.data_devolucao}");'

    def read(self):
        return f'select * from emprestimos where cpf like {self.cpf_usuario} or cod_livro like {self.cod_livro};'
        
    def update(self):
        return f'update emprestimos set data_devolucao = "{self.data_devolucao} where cod_livro = {self.cod_livro}";'
    
    @staticmethod
    def delete(cod_livro):
        return f'delete from livros where codigo={cod_livro};'
