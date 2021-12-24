-- Tabla de hechos
select M.Elemento, 
EM.Delegacion_municipio, 
M.Semana, M.Anio, M.Mes, M.Medicion
into TablaHechos
from EstacionesMonitoreo EM, Mediciones M
where EM.Id_estacion = M.Id_estacion 

select * from TablaHechos;

-- Cube 01 
-- {Delegación},{noSemana},{Anio}
select Delegacion_municipio, Semana, Anio, Medicion
into Cube01 from TablaHechos where Medicion != -99
select * from Cube01;

-- Cube 02
--{Delegación},{noSemana},{Mes}
select Delegacion_municipio, Semana, Mes, Medicion
into Cube02 from TablaHechos where Medicion != -99
select * from Cube02;

-- Cube 03
--{Delegación},{noSemana}
select Delegacion_municipio, Semana, avg(Medicion) as Promedio
into Cube03 from Cube01
group by Delegacion_municipio, Semana order by Promedio desc
select * from Cube03;

-- Cube 04
--{Delegación},{Mes}
select Delegacion_municipio, Mes, avg(Medicion) as Promedio
into Cube04 from TablaHechos where Medicion != -99
group by Delegacion_municipio, Mes order by Delegacion_municipio, Mes, Promedio asc;
select * from Cube04;

-- Cube 05
--{Delegación},{Anio}
select Delegacion_municipio, Anio, avg(Medicion) as Promedio
into Cube05 from Cube01
group by Delegacion_municipio, Anio order by Delegacion_municipio, Anio, Promedio asc
select * from Cube05;

-- Cube 06
--{Delegación}
select Delegacion_municipio, avg(Medicion) as Promedio
into Cube06 from Cube01
group by Delegacion_municipio order by Promedio asc
select * from Cube06;

-- Cube 07
--{Anio}  
select Anio, avg(Medicion) as Promedio
into Cube07 from Cube01
group by Anio order by Anio asc
select * from Cube07;

-- Cube 08
--{Mes} 
select Mes, avg(Medicion) as Promedio
into Cube08 from TablaHechos where Medicion !=-99
group by Mes order by Mes asc
select * from Cube08;

-- Cube 09
--{noSemana}
select Semana, avg(Medicion) as Promedio
into Cube09 from Cube01
group by Semana order by Semana asc
select * from Cube09;