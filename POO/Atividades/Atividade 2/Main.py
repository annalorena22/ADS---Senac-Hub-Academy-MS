from Livro import Livros
from Usuario import Usuario
from Biblioteca import Biblioteca
import mysql.connector

conexao = mysql.connector.connect(
    host = '10.28.2.63',
    user = 'suporte',
    password = 'suporte',
    database = 'biblioteca'
)

cursor = conexao.cursor()

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

conexao.commit()


rafaela = Usuario('Rafaela','01223839020','67940028922')

# dom_casmurro = Livros('Dom Casmurro','Machado de Assís','romance',1)
# antares = Livros('Incidente em Antares','Érico Veríssimo','Ficção distópica',2)
# poliana = Livros('Poliana','Eleanor H. Porter','Literatura infantil',3)
# monica = Livros('Almanacão Da Turma Da Mônica','Maurício de Souza','Literatura infantil',4)

# Biblioteca.emprestar(rafaela, [dom_casmurro, poliana, monica, antares] )

# print(poliana.status)
# print(rafaela.lista_livros)

# saraiva = Biblioteca()

# print(dir(saraiva))