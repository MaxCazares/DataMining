SELECT [folio]
      ,[fecha_creacion]
      ,[hora_creacion]
      ,[dia_semana]
      ,[codigo_cierre]
      ,[fecha_cierre]
      ,[año_cierre]
      ,[mes_cierre]
      ,[hora_cierre]
      ,[delegacion_inicio]
      ,[incidente_c4]
      ,[latitud]
      ,[longitud]
      ,[clas_con_f_alarma]
      ,[tipo_entrada]
      ,[delegacion_cierre]
      ,[geopoint]
      ,[mes]
  FROM [test].[dbo].[incidentevial2dsem2020]

select count(*) from [test].[dbo].[incidentevial2dsem2020]
select min([fecha_creacion]) from [test].[dbo].[incidentevial2dsem2020]
select max([fecha_creacion]) from [test].[dbo].[incidentevial2dsem2020]
select min([dia_semana]) from [test].[dbo].[incidentevial2dsem2020]
select max([dia_semana]) from [test].[dbo].[incidentevial2dsem2020]

SELECT [fecha_creacion], [dia_semana], [mes] FROM [test].[dbo].[incidentevial2dsem2020]
WHERE [fecha_creacion] = (select min([fecha_creacion]) from [test].[dbo].[incidentevial2dsem2020])

SELECT distinct [fecha_creacion], [dia_semana], [mes] FROM [test].[dbo].[incidentevial2dsem2020]
WHERE [fecha_creacion] = (select max([fecha_creacion]) from [test].[dbo].[incidentevial2dsem2020])
(son 38 resultados iguales)

select min([latitud]) from [test].[dbo].[incidentevial2dsem2020]
select max([latitud]) from [test].[dbo].[incidentevial2dsem2020]

select min([longitud]) from [test].[dbo].[incidentevial2dsem2020]

select max([longitud]) from [test].[dbo].[incidentevial2dsem2020]

select [codigo_cierre], [fecha_cierre], [año_cierre], [mes_cierre], [hora_cierre], [delegacion_cierre] 
from [test].[dbo].[incidentevial2dsem2020]
where [año_cierre] = (select min([año_cierre]) from [test].[dbo].[incidentevial2dsem2020])
son 33072 consultas

select [codigo_cierre], [fecha_cierre], [año_cierre], [mes_cierre], [hora_cierre], [delegacion_cierre] 
from [test].[dbo].[incidentevial2dsem2020]
where [año_cierre] = (select max([año_cierre]) from [test].[dbo].[incidentevial2dsem2020])
son 33072 consultas

select [incidente_c4] from [test].[dbo].[incidentevial2dsem2020]
select distinct [tipo_entrada] from [test].[dbo].[incidentevial2dsem2020]
select distinct [clas_con_f_alarma] from [test].[dbo].[incidentevial2dsem2020]
select distinct [delegacion_inicio] from [test].[dbo].[incidentevial2dsem2020]
select distinct [delegacion_cierre] from [test].[dbo].[incidentevial2dsem2020]

select count([incidente_c4]) from [test].[dbo].[incidentevial2dsem2020] where [incidente_c4] = 'NULL'
select count([tipo_entrada]) from [test].[dbo].[incidentevial2dsem2020] where [tipo_entrada] = 'NULL'
select count([clas_con_f_alarma]) from [test].[dbo].[incidentevial2dsem2020] where [clas_con_f_alarma] = 'NULL'
select count([delegacion_inicio]) from [test].[dbo].[incidentevial2dsem2020] where [delegacion_inicio] = 'NULL'
select count([delegacion_cierre]) from [test].[dbo].[incidentevial2dsem2020] where [delegacion_cierre] = 'NULL'