import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conexao.cursor()
        if self.conexao.is_connected():
            print("Conectado com sucesso ao Banco de Bados.")
        else:
            print("Não foi possível conectar ao Banco de Dados.") 
            

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            print("Desconectado.")