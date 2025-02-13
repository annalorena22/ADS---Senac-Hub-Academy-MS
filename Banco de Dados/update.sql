create database atividade;
use atividade;

CREATE TABLE pessoa (
 CPF varchar(11) primary key,
 nome varchar(255), 
 RG varchar(7),
 fone varchar(30),
 idade int(3),
 id_cidade int, 
 id_sexo int,
 id_nacionalidade int,
 id_raca int,
 id_escolaridade int,
 id_estado_civil int(30),
 foreign key (id_cidade) references cidade(id_cidade), 
 foreign key (id_sexo) references sexo(id_sexo),
 foreign key (id_nacionalidade) references nacionalidade(id_nacionalidade),
 foreign key (id_raca) references raca(id_raca),
 foreign key (id_escolaridade) references escolaridade(id_escolaridade),
 foreign key (id_estado_civil) references estado_civil(id_estado_civil)
);

create table estado (
	id_estado int auto_increment primary key, 
    estado varchar(50)
);

create table cidade (
	id_cidade int auto_increment primary key,
    Cidade varchar(50),
    id_estado int,
    foreign key (id_estado) references estado(id_estado)
    );
    
create table sexo (
	id_sexo int auto_increment primary key,
    sexo varchar(50)
);

create table nacionalidade (
	id_nacionalidade int auto_increment primary key,
    nacionalidade varchar(50)
);

create table raca (
	id_raca int auto_increment primary key,
    raca varchar(50)
);

create table escolaridade (
	id_escolaridade int auto_increment primary key,
    escolaridade varchar(50)
);

create table estado_civil (
	id_estado_civil int auto_increment primary key,
    estado_civil varchar(50)
);

INSERT INTO estado (estado) VALUES ('Acre');
INSERT INTO estado (estado) VALUES ('Alagoas');
INSERT INTO estado (estado) VALUES ('Amapá');
INSERT INTO estado (estado) VALUES ('Amazonas');
INSERT INTO estado (estado) VALUES ('Bahia');
INSERT INTO estado (estado) VALUES ('Ceará');
INSERT INTO estado (estado) VALUES ('Distrito Federal');
INSERT INTO estado (estado) VALUES ('Espírito Santo');
INSERT INTO estado (estado) VALUES ('Goiás');
INSERT INTO estado (estado) VALUES ('Maranhão');
INSERT INTO estado (estado) VALUES ('Mato Grosso');
INSERT INTO estado (estado) VALUES ('Mato Grosso do Sul');
INSERT INTO estado (estado) VALUES ('Minas Gerais');
INSERT INTO estado (estado) VALUES ('Pará');
INSERT INTO estado (estado) VALUES ('Paraíba');
INSERT INTO estado (estado) VALUES ('Paraná');
INSERT INTO estado (estado) VALUES ('Pernambuco');
INSERT INTO estado (estado) VALUES ('Piauí');
INSERT INTO estado (estado) VALUES ('Rio de Janeiro');
INSERT INTO estado (estado) VALUES ('Rio Grande do Norte');
INSERT INTO estado (estado) VALUES ('Rio Grande do Sul');
INSERT INTO estado (estado) VALUES ('Rondônia');
INSERT INTO estado (estado) VALUES ('Roraima');
INSERT INTO estado (estado) VALUES ('Santa Catarina');
INSERT INTO estado (estado) VALUES ('São Paulo');
INSERT INTO estado (estado) VALUES ('Sergipe');
INSERT INTO estado (estado) VALUES ('Tocantins');

select * from estado;

-- Acre
INSERT INTO cidade (Cidade, id_estado) VALUES ('Rio Branco', 1);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Cruzeiro do Sul', 1);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Sena Madureira', 1);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Tarauacá', 1);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Feijó', 1);

-- Alagoas
INSERT INTO cidade (Cidade, id_estado) VALUES ('Maceió', 2);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Arapiraca', 2);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Palmeira dos Índios', 2);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Rio Largo', 2);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Penedo', 2);

-- Amapá
INSERT INTO cidade (Cidade, id_estado) VALUES ('Macapá', 3);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Santana', 3);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Laranjal do Jari', 3);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Oiapoque', 3);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Mazagão', 3);

-- Amazonas
INSERT INTO cidade (Cidade, id_estado) VALUES ('Manaus', 4);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Parintins', 4);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Itacoatiara', 4);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Manacapuru', 4);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Tefé', 4);

-- Bahia
INSERT INTO cidade (Cidade, id_estado) VALUES ('Salvador', 5);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Feira de Santana', 5);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Vitória da Conquista', 5);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Camaçari', 5);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Juazeiro', 5);

-- Ceará
INSERT INTO cidade (Cidade, id_estado) VALUES ('Fortaleza', 6);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Caucaia', 6);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Juazeiro do Norte', 6);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Maracanaú', 6);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Sobral', 6);

-- Distrito Federal
INSERT INTO cidade (Cidade, id_estado) VALUES ('Brasília', 7);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Ceilândia', 7);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Taguatinga', 7);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Planaltina', 7);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Samambaia', 7);

-- Espírito Santo
INSERT INTO cidade (Cidade, id_estado) VALUES ('Vitória', 8);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Vila Velha', 8);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Serra', 8);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Cariacica', 8);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Linhares', 8);

-- Goiás
INSERT INTO cidade (Cidade, id_estado) VALUES ('Goiânia', 9);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Aparecida de Goiânia', 9);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Anápolis', 9);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Rio Verde', 9);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Luziânia', 9);

-- Maranhão
INSERT INTO cidade (Cidade, id_estado) VALUES ('São Luís', 10);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Imperatriz', 10);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Caxias', 10);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Timon', 10);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Codó', 10);

-- Mato Grosso
INSERT INTO cidade (Cidade, id_estado) VALUES ('Cuiabá', 11);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Várzea Grande', 11);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Rondonópolis', 11);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Sinop', 11);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Tangará da Serra', 11);

-- Mato Grosso do Sul
INSERT INTO cidade (Cidade, id_estado) VALUES ('Campo Grande', 12);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Dourados', 12);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Três Lagoas', 12);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Corumbá', 12);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Ponta Porã', 12);

-- Minas Gerais
INSERT INTO cidade (Cidade, id_estado) VALUES ('Belo Horizonte', 13);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Uberlândia', 13);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Contagem', 13);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Juiz de Fora', 13);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Betim', 13);

-- Pará
INSERT INTO cidade (Cidade, id_estado) VALUES ('Belém', 14);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Ananindeua', 14);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Santarém', 14);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Marabá', 14);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Parauapebas', 14);

-- Paraíba
INSERT INTO cidade (Cidade, id_estado) VALUES ('João Pessoa', 15);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Campina Grande', 15);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Santa Rita', 15);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Patos', 15);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Bayeux', 15);

-- Paraná
INSERT INTO cidade (Cidade, id_estado) VALUES ('Curitiba', 16);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Londrina', 16);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Maringá', 16);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Ponta Grossa', 16);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Cascavel', 16);

-- Pernambuco
INSERT INTO cidade (Cidade, id_estado) VALUES ('Recife', 17);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Jaboatão dos Guararapes', 17);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Olinda', 17);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Caruaru', 17);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Petrolina', 17);

-- Piauí
INSERT INTO cidade (Cidade, id_estado) VALUES ('Teresina', 18);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Parnaíba', 18);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Picos', 18);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Piripiri', 18);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Floriano', 18);

-- Rio de Janeiro
INSERT INTO cidade (Cidade, id_estado) VALUES ('Rio de Janeiro', 19);
INSERT INTO cidade (Cidade, id_estado) VALUES ('São Gonçalo', 19);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Duque de Caxias', 19);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Nova Iguaçu', 19);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Niterói', 19);

-- Rio Grande do Norte
INSERT INTO cidade (Cidade, id_estado) VALUES ('Natal', 20);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Mossoró', 20);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Parnamirim', 20);
INSERT INTO cidade (Cidade, id_estado) VALUES ('São Gonçalo do Amarante', 20);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Macau', 20);

-- Rio Grande do Sul
INSERT INTO cidade (Cidade, id_estado) VALUES ('Porto Alegre', 21);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Caxias do Sul', 21);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Pelotas', 21);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Canoas', 21);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Santa Maria', 21);

-- Rondônia
INSERT INTO cidade (Cidade, id_estado) VALUES ('Porto Velho', 22);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Ji-Paraná', 22);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Ariquemes', 22);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Vilhena', 22);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Cacoal', 22);

-- Roraima
INSERT INTO cidade (Cidade, id_estado) VALUES ('Boa Vista', 23);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Rorainópolis', 23);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Caracaraí', 23);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Pacaraima', 23);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Alto Alegre', 23);

-- Santa Catarina
INSERT INTO cidade (Cidade, id_estado) VALUES ('Florianópolis', 24);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Joinville', 24);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Blumenau', 24);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Chapecó', 24);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Itajaí', 24);

-- São Paulo
INSERT INTO cidade (Cidade, id_estado) VALUES ('São Paulo', 25);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Guarulhos', 25);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Campinas', 25);
INSERT INTO cidade (Cidade, id_estado) VALUES ('São Bernardo do Campo', 25);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Santo André', 25);

-- Sergipe
INSERT INTO cidade (Cidade, id_estado) VALUES ('Aracaju', 26);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Nossa Senhora do Socorro', 26);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Lagarto', 26);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Itabaiana', 26);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Estância', 26);

-- Tocantins
INSERT INTO cidade (Cidade, id_estado) VALUES ('Palmas', 27);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Araguaína', 27);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Gurupi', 27);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Porto Nacional', 27);
INSERT INTO cidade (Cidade, id_estado) VALUES ('Paraíso do Tocantins', 27);

select * from cidade; 

insert into sexo (sexo) values ('Feminino');
insert into sexo (sexo) values ('Masculino');
insert into sexo (sexo) values ('Outros');

insert into nacionalidade (nacionalidade) values ('Brasileira');
insert into nacionalidade (nacionalidade) values ('Estrangeira');

INSERT INTO raca (raca) VALUES ('Branca');
INSERT INTO raca (raca) VALUES ('Preta');
INSERT INTO raca (raca) VALUES ('Parda');
INSERT INTO raca (raca) VALUES ('Amarela');
INSERT INTO raca (raca) VALUES ('Indígena');

INSERT INTO escolaridade (escolaridade) VALUES ('Ensino Fundamental Incompleto');
INSERT INTO escolaridade (escolaridade) VALUES ('Ensino Fundamental Completo');
INSERT INTO escolaridade (escolaridade) VALUES ('Ensino Médio Incompleto');
INSERT INTO escolaridade (escolaridade) VALUES ('Ensino Médio Completo');
INSERT INTO escolaridade (escolaridade) VALUES ('Ensino Superior Incompleto');
INSERT INTO escolaridade (escolaridade) VALUES ('Ensino Superior Completo');
INSERT INTO escolaridade (escolaridade) VALUES ('Pós-graduação');
INSERT INTO escolaridade (escolaridade) VALUES ('Mestrado/Doutorado');

INSERT INTO estado_civil (estado_civil) VALUES ('Solteiro(a)');
INSERT INTO estado_civil (estado_civil) VALUES ('Casado(a)');
INSERT INTO estado_civil (estado_civil) VALUES ('Divorciado(a)');
INSERT INTO estado_civil (estado_civil) VALUES ('Viúvo(a)');
INSERT INTO estado_civil (estado_civil) VALUES ('Separado(a) Judicialmente');
INSERT INTO estado_civil (estado_civil) VALUES ('União Estável');


INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_Sexo, id_Nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('12345678901', 'João Silva', '1234567', '(11) 98765-4321', 30, 25, 2, 1, 1, 6, 1);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('10987654321', 'Maria Oliveira', '7654321', '(21) 97654-3210', 45, 13, 1, 1, 3, 8, 2);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('11122334455', 'Carlos Pereira', '1122334', '(31) 95555-1111', 38, 9, 2, 1, 2, 4, 3);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('12233445566', 'Ana Costa', '2233445', '(41) 94444-2222', 29, 24, 1, 1, 1, 3, 4);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('13344556677', 'Roberto Santos', '3344556', '(51) 93333-3333', 52, 21, 2, 1, 2, 5, 2);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('14455667788', 'Beatriz Almeida', '4455667', '(61) 92222-4444', 27, 7, 1, 1, 4, 7, 1);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('15566778899', 'Felipe Martins', '5566778', '(71) 91111-5555', 33, 5, 2, 1, 2, 6, 5);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('16677889900', 'Júlia Pereira', '6677889', '(81) 90000-6666', 41, 15, 1, 2, 1, 8, 3);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('17788990011', 'Marcos Lima', '7788990', '(91) 98888-7777', 50, 18, 2, 1, 3, 5, 2);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('18899001122', 'Larissa Souza', '8899001', '(11) 97777-8888', 22, 12, 1, 1, 5, 4, 1);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('19900112233', 'Gabriel Oliveira', '9900112', '(21) 96666-9999', 36, 8, 2, 2, 1, 7, 2);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('20011223344', 'Camila Fernandes', '0011223', '(31) 95555-6666', 30, 20, 1, 1, 2, 6, 4);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('21122334455', 'Lucas Costa', '1122334', '(41) 94444-7777', 27, 4, 2, 1, 1, 3, 6);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('22233445566', 'Amanda Silva', '2233445', '(51) 93333-8888', 23, 19, 1, 2, 4, 5, 2);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('23344556677', 'Rafael Almeida', '3344556', '(61) 92222-9999', 35, 22, 2, 1, 3, 4, 3);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('24455667788', 'Patrícia Nascimento', '4455667', '(71) 91111-0000', 40, 6, 1, 1, 5, 8, 1);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('25566778899', 'Gustavo Souza', '5566778', '(81) 90000-1111', 28, 3, 2, 2, 2, 7, 5);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('26677889900', 'Daniela Rodrigues', '6677889', '(91) 98888-2222', 33, 17, 1, 1, 1, 6, 2);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('27788990011', 'André Silva', '7788990', '(11) 97777-3333', 47, 14, 2, 1, 4, 5, 3);
INSERT INTO pessoa (CPF, nome, RG, fone, idade, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade, id_estado_civil) VALUES
('28899001122', 'Juliana Lima', '8899001', '(21) 96666-4444', 26, 25, 1, 2, 1, 8, 4);

select * from pessoa;

-- select apenas com o nome e a cidade
	select pessoa.nome as Pessoa, cidade.Cidade
	from pessoa 
    join cidade on pessoa.id_cidade = cidade.id_cidade;

-- select apenas nome e o estado
select pessoa.nome as Pessoa, estado.estado as Estado 
	from pessoa 
    join cidade on pessoa.id_cidade = cidade.id_cidade 
    join estado on cidade.id_estado = estado.id_estado;
    
-- select apenas nome, cpf e a raça.
	select pessoa.nome as Pessoa, pessoa.cpf, raca.raca as Raça
	from pessoa
    join raca on pessoa.id_raca = raca.id_raca;
    
-- select apenas com o nome e a nacionalidade;
	select pessoa.nome as Pessoa, nacionalidade.nacionalidade as Nacionalidade
	from pessoa
    join nacionalidade on pessoa.id_nacionalidade = nacionalidade.id_nacionalidade;
    
-- select apenas com o nome e a escolaridade;
	select pessoa.nome as Pessoa, escolaridade.escolaridade as Escolaridade
	from pessoa
    join escolaridade on pessoa.id_escolaridade = escolaridade.id_escolaridade;

-- select com nome, cidade e estado;
	select pessoa.nome as Pessoa, cidade.cidade, estado.estado as Estado 
	from pessoa 
    join cidade on pessoa.id_cidade = cidade.id_cidade 
    join estado on cidade.id_estado = estado.id_estado;
    
    
-- select com tudo;
	select 
	pessoa.CPF,
    pessoa.nome as Nome,
    pessoa.idade as Idade,
    pessoa.RG,
    pessoa.fone as Telefone,
    cidade.Cidade,
    estado.estado,
    sexo.sexo as Sexo,
    nacionalidade.nacionalidade as Nacionalidade,
    raca.raca as Raça,
    escolaridade.escolaridade as Escolaridade,
    estado_civil.estado_civil as Estado_Civil
	from pessoa
	join cidade on cidade.id_cidade = cidade.id_cidade
	join estado on cidade.id_estado = estado.id_estado
	join nacionalidade on nacionalidade.id_nacionalidade = nacionalidade.id_nacionalidade
	join escolaridade on pessoa.id_escolaridade = escolaridade.id_escolaridade
    join sexo on pessoa.id_sexo = sexo.id_sexo
	join raca on pessoa.id_raca = raca.id_raca
    join estado_civil on pessoa.id_estado_civil = estado_civil.id_estado_civil;
    
	set sql_safe_updates=0;
	
    -- Exercício 1:
    update cidade set cidade='Abaixo de M' where cidade >="A" and cidade <="M";
    update cidade set cidade='Acima de M' where cidade >="N" and cidade <="Z";
    select * from cidade;
    
    -- Exercício 2:
    update estado set estado='Centro-Oeste' where estado="Mato Grosso do Sul" or estado="Mato Grosso" or estado="Goiás";
	update estado set estado='Norte' where estado="Amazonas" or estado="Pará" or estado="Roraima" or estado="Amapá" or estado="Rondônia" or estado="Acre" or estado="Tocantins";
    update estado set estado='Nordeste' where estado="Piauí" or estado="Maranhão" or estado="Pernambuco" or estado="Rio Grande do Norte" or estado="Alagoas" or estado="Paraíba" or estado="Ceará" or estado="Bahia" or estado="Sergipe";
	update estado set estado='Sudeste' where estado="São Paulo" or estado="Rio de Janeiro" or estado="Espírito Santo" or estado="Minas Gerais";
    update estado set estado='Sul' where estado="Paraná" or estado="Rio Grande do Sul" or estado="Santa Catarina";
    select * from estado;
    
    -- Exercício 3:
    update nacionalidade set nacionalidade='Fora do Brasil' where nacionalidade="Estrangeira";
    select * from nacionalidade;
    
    -- Exercício 4:
    update raca set raca='Seres Humanos' where raca="Branca" or raca="Preta" or raca="Parda" or raca="Amarela" or raca="Indígena";
    select * from raca;
    
    -- Exercício 5:
	update escolaridade set escolaridade='Ensino Básico' where escolaridade="Ensino Fundamental Completo" or escolaridade="Ensino Médio Incompleto" or escolaridade="Ensino Médio Completo" or escolaridade="Ensino Superior Incompleto";
	update escolaridade set escolaridade='Ensino Avançado' where escolaridade="Ensino Superior Completo" or escolaridade="Pós-graduação" or escolaridade="Mestrado/Doutorado";
	select * from escolaridade;

set sql_safe_updates = 1;

	


