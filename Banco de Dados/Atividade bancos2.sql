create database bancos;
use bancos;

create table estado(
	id_estado int auto_increment primary key,
    uf varchar(2) not null
);

create table cidade(
	id_cidade int auto_increment primary key,
    cidade varchar(100) not null,
    id_estado int not null,
    foreign key (id_estado) references estado(id_estado)
);

create table genero (
	id_genero int auto_increment primary key,
    genero varchar(50) not null
);

create table raca (
	id_raca int auto_increment primary key,
    raca varchar(50) not null
);

create table religiao (
	id_religiao int auto_increment primary key,
    religiao varchar(50) not null
);

create table estado_civil (
	id_estado_civil int auto_increment primary key,
    estado_civil varchar(50) not null
);

create table agencia (
	id_agencia int auto_increment primary key,
    num_agencia varchar(50),
    banco varchar(50),
	endereco varchar(100),
    id_cidade int,
    id_estado int,
    foreign key (id_cidade) references cidade(id_cidade),
    foreign key (id_estado) references estado(id_estado)
);

create table cliente(
	id_cliente int auto_increment primary key,
	CPF varchar(11),
	nome varchar(255), 
	RG varchar(7),
    data_nasc date,
	fone varchar(30),
	endereco varchar(50),
	id_cidade int, 
    id_estado int,
	id_genero int,
	id_raca int,
	id_religiao int,
	id_estado_civil int,
    id_agencia int,
	foreign key (id_cidade) references cidade(id_cidade),
	foreign key (id_estado) references estado(id_estado),
	foreign key (id_genero) references genero(id_genero),
	foreign key (id_raca) references raca(id_raca),
	foreign key (id_religiao) references religiao(id_religiao),
	foreign key (id_estado_civil) references estado_civil(id_estado_civil),
    foreign key (id_agencia) references agencia(id_agencia)
);

select * from cliente;

create table conta_cliente(
	id_conta_cliente int auto_increment primary key,
    id_cliente int,
    numero_conta varchar(10),
    saldo float,
    id_agencia int,
    foreign key (id_cliente) references cliente(id_cliente),
    foreign key (id_agencia) references agencia(id_agencia)
);

ALTER TABLE cliente ADD COLUMN id_conta_cliente int;
ALTER TABLE cliente ADD CONSTRAINT fk_conta_cliente FOREIGN KEY (id_conta_cliente) REFERENCES conta_cliente(id_conta_cliente);

INSERT INTO estado (uf) VALUES
('SP'),
('RJ'),
('MG'),
('ES');

INSERT INTO cidade (cidade, id_estado) VALUES
('São Paulo', 1),
('Rio de Janeiro', 2),
('Belo Horizonte', 3),
('Vitória', 4);

INSERT INTO genero (genero) VALUES
('Masculino'),
('Feminino'),
('Outro');

INSERT INTO raca (raca) VALUES
('Branco'),
('Negro'),
('Pardo'),
('Indígena'),
('Outro');

INSERT INTO religiao (religiao) VALUES
('Católica'),
('Evangélica'),
('Espírita'),
('Ateu'),
('Outra');

INSERT INTO estado_civil (estado_civil) VALUES
('Solteiro'),
('Casado'),
('Divorciado'),
('Viúvo');

INSERT INTO agencia (num_agencia, banco, endereco, id_cidade, id_estado) VALUES
('5247', 'Banco do Brasil S.A.', 'Rua A, 123', 1, 1),
('2256', 'Caixa Econômica Federal', 'Rua B, 456', 2, 2),
('3269', 'Itaú Unibanco S.A.', 'Rua C, 789', 3, 3),
('1236', 'Bradesco S.A.', 'Rua D, 101', 4, 4);

INSERT INTO cliente (CPF, nome, RG, data_nasc, fone, endereco, id_cidade, id_estado, id_genero, id_raca, id_religiao, id_estado_civil, id_agencia, id_conta_cliente) VALUES
('12345678901', 'João da Silva', '1234567', '1985-03-15', '11987654321', 'Rua A, 12', 1, 1, 1, 1, 1, 1, 1, NULL),
('09876543210', 'Maria Souza', '7654321', '1990-07-22', '21998765432', 'Rua B, 34', 2, 2, 2, 2, 2, 2, 2, NULL),
('11122233344', 'Carlos Pereira', '3456789', '1978-10-09', '31987654321', 'Rua C, 56', 3, 3, 1, 3, 3, 3, 3, NULL),
('55566677788', 'Ana Oliveira', '8765432', '1995-02-27', '27987654321', 'Rua D, 78', 4, 4, 2, 4, 4, 1, 4, NULL);

INSERT INTO conta_cliente (id_cliente, numero_conta, saldo, id_agencia) VALUES
(1, '1001001001', 19.99, 1),
(2, '2002002002', 399.40, 2),
(3, '3003003003', 4500.60, 3),
(4, '4004004004', 2525.50, 4);

SET SQL_SAFE_UPDATES = 0;
UPDATE cliente SET id_conta_cliente = (SELECT id_conta_cliente FROM conta_cliente WHERE cliente.id_cliente = conta_cliente.id_cliente);
SET SQL_SAFE_UPDATES = 1;

select * from cliente;
select * from conta_cliente;

create table saque(
	id_transacao_saque int auto_increment primary key,
	id_conta_cliente int,
	valor float,
	data_saque date,
	hora_saque time,
    foreign key (id_conta_cliente) references conta_cliente(id_conta_cliente)
);

create table deposito(
	id_transacao_deposito int auto_increment primary key,
	id_conta_cliente int,
	valor float,
	data_deposito date,
	hora_deposito time,
    foreign key (id_conta_cliente) references conta_cliente(id_conta_cliente)
);


delimiter $

create trigger tgr_saque after insert
on saque
for each row
begin
update conta_cliente set saldo = saldo - new.valor
where id_conta_cliente = new.id_conta_cliente;
end$

select * from conta_cliente $

delimiter ;

insert into deposito values (null,  3, 2000, '2024-09-25', '10:11:00');

describe conta_cliente;
describe saque;

delimiter $

create trigger tgr_deposito after insert
on deposito
for each row
begin
update conta_cliente set saldo = saldo + new.valor
where id_conta_cliente = new.id_conta_cliente;
end$