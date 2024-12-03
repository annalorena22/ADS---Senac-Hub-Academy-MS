CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE livros (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    genero VARCHAR(50),
    cod_livro VARCHAR(20) UNIQUE
);

CREATE TABLE usuarios (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(11) UNIQUE,
    telefone VARCHAR(15)
);

CREATE TABLE emprestimos (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    codigo_livro VARCHAR(20),
    cpf_usuario VARCHAR(11),
    data_emprestimo DATE,
    data_devolucao DATE,
    status (como pre setar o status??)
    FOREIGN KEY (codigo_livro) REFERENCES livros(codigo),
    FOREIGN KEY (cpf_usuario) REFERENCES usuarios(cpf)
);
