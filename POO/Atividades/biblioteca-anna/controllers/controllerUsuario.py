from models.usuario import Usuario
from config.database import Database

class ControllerUsuario:
    def __init__(self):
        self.bd = Database("localhost","root","","biblioteca")

    def cadastrarUsuario(self, informacoesUsuario):
        self.bd.conectar()
        self.usuario = Usuario(informacoesUsuario['nome'], informacoesUsuario['cpf'], informacoesUsuario['telefone'])
        query = self.usuario.create()
        self.bd.cursor.execute(query)
        self.bd.conexao.commit()
        self.bd.desconectar()

    def procurarUsuario(self):
        self.bd.conectar()
        query = self.usuario.read()
        self.bd.cursor.execute(query)
        resultado = self.bd.cursor.fetchall() 
        self.bd.desconectar()
        return resultado

    def atualizarUsuario(self):
        self.bd.conectar()
        query = self.usuario.update()
        self.bd.cursor.execute(query)
        self.bd.conexao.commit()
        self.bd.desconectar()

    def excluirUsuario(self, cpf):
        self.bd.conectar()
        query = Usuario.delete(cpf)
        self.bd.cursor.execute(query)
        self.bd.conexao.commit()
        self.bd.desconectar()
        
    