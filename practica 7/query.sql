select Id_estacion ,Anio, Mes, Dia, Medicion 
into p7 from _mediciones_ 
where Id_estacion = 3 and Medicion != -99 or Id_estacion = 11 
and Medicion != -99 or Id_estacion = 12 and Medicion != -99;

select top 588 * into _80porciento_p7_ from p7;
select top 588 * into _19porciento_p7_ from p7;

select * from _80porciento_p7_;
select * from _19porciento_p7_;