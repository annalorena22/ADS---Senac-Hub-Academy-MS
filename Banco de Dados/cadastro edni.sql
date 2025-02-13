create database login;
use login;

create table usuario(
login varchar(10) not null,
senha varchar(3) not null
);

insert into usuario values ('anna', '333');
insert into usuario values ('joao', '123');
insert into usuario values ('gun', '345');
insert into usuario values ('ricardo', '678');
insert into usuario values ('paulo', '789');

select * from usuario;
