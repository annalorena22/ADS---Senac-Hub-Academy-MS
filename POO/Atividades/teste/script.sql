create database teste;
use teste;

   create table usuario(
	id_usuario int auto_increment primary key,
	nome varchar(100) not null,
	cpf varchar(13) unique not null,
	telefone varchar(20) not null,
	email varchar(100) unique not null,
    id_user_admin int(10) not null
    );


create table livro(
	isbn int primary key not null,
    titulo varchar(50) not null,
    autor varchar(50) not null,
    genero varchar(50) not null,
    status varchar(50) not null
    );

    create table emprestimo(
    id_emprestimo int auto_increment primary key,
	isbn int,
	id_usuario int,
	foreign key (isbn) references livro(isbn),
	foreign key (id_usuario) references usuario(id_usuario)
    );
 
 select * from livro;
 select * from usuario;
 select * from emprestimo;
 