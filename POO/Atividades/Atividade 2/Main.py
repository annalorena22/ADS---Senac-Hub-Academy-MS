from Livro import Livros
from Usuario import Usuario
from Biblioteca import Biblioteca
import mysql.connector

# conexao = mysql.connector.connect(
#     host = '10.28.2.63',
#     user = 'suporte',
#     password = 'suporte',
#     database = 'biblioteca'
# )

# cursor = conexao.cursor()

#-----INSERT------
# cursor.execute('insert into livro (titulo, autor, genero, status, codigo) values ("Senhor dos aneis", "Tolkein", "Fantasia", "Disponível", 123454)')
# cursor.execute('insert into livro (titulo, autor, genero, status, codigo) values ("Barbie", "Barbinha", "Fantasia", "Disponível", 12344564)')
# cursor.execute('insert into livro (titulo, autor, genero, status, codigo) values ("Suzy", "Suzinha", "Fantasia", "Disponível", 1256544)')

#-----SELECT------
# cursor.execute('select * from livro;')
# print(cursor.fetchall())

#-----UPDATE------
# cursor.execute('update livro set titulo= "Senhor dos Anéis" where titulo= "Senhor dos aneis"')

#-----DELETE------
# cursor.execute('delete from livro where id_livro=9 or id_livro=11')

#-----SELECT------
# cursor.execute('select titulo as Título, autor as Autor, genero as Gênero, status as Status, codigo as Código from livro;')
# print(cursor.fetchall())

# conexao.commit()


# rafaela = Usuario('Rafaela','01223839020','67940028922')

# dom_casmurro = Livros('Dom Casmurro','Machado de Assís','romance',1)
# antares = Livros('Incidente em Antares','Érico Veríssimo','Ficção distópica',2)
# poliana = Livros('Poliana','Eleanor H. Porter','Literatura infantil',3)
# monica = Livros('Almanacão Da Turma Da Mônica','Maurício de Souza','Literatura infantil',4)

# Biblioteca.emprestar(rafaela, [dom_casmurro, poliana, monica, antares] )

# print(poliana.status)
# print(rafaela.lista_livros)

# saraiva = Biblioteca()

# print(dir(saraiva))

# print(vars(conexao))

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

