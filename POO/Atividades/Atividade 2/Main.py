from Livro import Livro
from Usuario import Usuario

rafaela = Usuario("Rafaela", "012345678911", "991999999")
print(vars(rafaela))

dom_casmurro = Livro(9788532279392, "Dom Casmurro", "Machado de Assis", "Romance")
print(vars(dom_casmurro))

rafaela.pegar_emprestado(dom_casmurro)

rafaela.pegar_emprestado('Teste')