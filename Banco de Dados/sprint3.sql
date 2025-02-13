-- ---------------------------------------------------------------------------------
-- Exercício 1:
create database sprint;
use sprint;

create table atleta (
idAtleta int(9) auto_increment primary key,
nome varchar(40), 
modalidade varchar(40), 
qtdMedalha int(100)
);

insert into atleta values (null, "Ana", "Natação", 12);
insert into atleta values (null, "João", "Basquete", 9);
insert into atleta values (null, "Kelvin", "Futebol", 15);
insert into atleta values (null, "Paulo", "Vôlei", 7);
insert into atleta values (null, "Ricardo", "Tênis", 16);

select * from atleta;

update atleta set qtdMedalha='13' where idAtleta=1;

update atleta set qtdMedalha='10' where idAtleta=2;

update atleta set qtdMedalha='16' where idAtleta=3;

update atleta set nome='Ezequiel' where idAtleta=4;

alter table atleta add column dtNasc date;

update atleta set dtNasc = '1985-09-25' where idAtleta = 1;
update atleta set dtNasc = '1999-07-03' where idAtleta = 2;
update atleta set dtNasc = '1998-02-24' where idAtleta = 3;
update atleta set dtNasc = '1992-10-18' where idAtleta = 4;
update atleta set dtNasc = '2000-12-13' where idAtleta = 5;

delete from atleta where idAtleta= 5;

select * from atleta where not modalidade='Natação';

select * from atleta where qtdMedalha >=3;

alter table atleta modify modalidade varchar(60);

describe atleta;

truncate table atleta;

select * from atleta;

-- ---------------------------------------------------------------------------------
-- Exercício 2:

create table musica (
idMusica int auto_increment primary key,
titulo varchar(40),
artista varchar(40),
genero varchar(40)
);

insert into musica (titulo, artista, genero) values
('Musica1', 'Artista1', 'Pop'),
('Musica2', 'Artista1', 'Pop'),
('Musica 3', 'Artista2', 'Rock'),
('Musica 4', 'Artista2', 'Rock'),
('Musica5', 'Artista3', 'Rap'),
('Musica6', 'Artista4', 'Axé'),
('Musica7', 'Artista4', 'Pop');


select * from musica;

alter table musica add column curtidas int;

update musica set  curtidas = 256 where idMusica = 1;
update musica set curtidas = 123 where idMusica = 2;
update musica set curtidas = '421' where idMusica = 3;
update musica set curtidas = '99' where idMusica = 4;
update musica set curtidas = '37' where idMusica= 5;
update musica set curtidas = '99' where idMusica = 6;
update musica set curtidas = '37' where idMusica= 7;

alter table musica modify artista varchar(80);

describe musica;

update musica set  curtidas = 274 where idMusica = 1;
update musica set curtidas = 125 where idMusica = 2;
update musica set curtidas = '425' where idMusica = 3;

update musica set titulo = 'MusicaN5' where idMusica = 5;

delete from musica where idMusica= 4;

select * from musica where not genero='funk';

select * from musica where curtidas >=20;

truncate table musica;

-- ---------------------------------------------------------------------------------
-- Exercício 3:

create table filme(
idFilme int auto_increment primary key,
titulo varchar(50), 
genero varchar(40), 
diretor varchar(40)
);

insert into filme (titulo, genero, diretor) values
('Ação Explosiva', 'Ação', 'John Doe'),
('Missão Impossível', 'Ação', 'John Doe'),
('O Último Ato', 'Drama', 'Jane Smith'),
('Noite de Mistério', 'Mistério', 'Robert Brown'),
('Aventura no Espaço', 'Ação', 'John Doe'),
('Segredos da Cidade', 'Mistério', 'Robert Brown'),
('O Enigma do Passado', 'Drama', 'Jane Smith');

select * from filme;

alter table filme add column protagonista varchar(50);

update filme set protagonista = 'Olivia Brown' where idFilme =1;
update filme set protagonista = 'Liam Wilson' where idFilme =2;
update filme set protagonista = 'Emily Johnson' where idFilme =3;
update filme set protagonista = 'Sophia Martins' where idFilme =4;
update filme set protagonista = 'Peter Smith' where idFilme =5;
update filme set protagonista = 'Matheus Aguiar' where idFilme =6;
update filme set protagonista = 'Rafael Moreira' where idFilme =7;

alter table filme modify diretor varchar(150);

describe filme;
update filme set diretor='Pedro Alvez' where idFilme=5;
update filme set diretor='João Gabriel' where idFilme=2;
update filme set diretor='Paulo Matheus' where idFilme=7;

update filme set titulo='Segredos do Bairro' where idFilme=6;

delete from filme where idFilme=3;

select * from filme where not genero='drama';

select * from filme where genero='suspense';

truncate table filme;








