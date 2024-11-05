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
        self.conexao =  mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )

        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()


db = Database(host = '10.28.2.63',
    user = 'suporte',
    password = 'suporte',
    database = 'biblioteca')

print(db.conexao)
print("Conectado")
db.conectar()
print(db.conexao)

print("Livros:")
db.cursor.execute('select * from livro;')

print(db.cursor.fetchall())

db.desconectar()
print("Desconectado")


# print(vars(db.conectar()))
# print(vars(db.desconectar()))

