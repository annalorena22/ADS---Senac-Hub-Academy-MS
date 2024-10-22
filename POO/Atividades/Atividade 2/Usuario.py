class Usuario:
    max_emprestimo = 5
    def __init__(self, cpf, nome, telefone, qntdLivroEmprestado):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.qntdLivroEmprestado = qntdLivroEmprestado