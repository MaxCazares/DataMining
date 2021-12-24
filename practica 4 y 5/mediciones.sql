create table Mediciones(
    Elemento varchar(30),
	Id_estacion int,
	Medicion float,
	Dia int,
	Mes varchar(10),
	Anio varchar(5),
    Semana int
);

select * from Mediciones;
delete from Mediciones;

-- Esta tabla de MySQL se utiliza en la práctica 7

create table Mediciones_(
    Elemento varchar(30),
	Id_estacion int,
	Medicion float,
	Dia int,
	Mes int,
	Anio int,
    Semana int
);

select * from Mediciones;
delete from Mediciones;