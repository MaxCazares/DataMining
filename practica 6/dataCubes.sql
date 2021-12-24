SELECT ao_hechos as Año, alcaldia_hechos as Alcaldia, delito as Delito, count(delito) as Numero_Delitos
into Carpetas#Alcaldia#Delitos#Año
from Localizacion, Delito, Tiempo
where IDLocalizacion = IDDelito and IDTiempo = IDDelito and alcaldia_hechos is not NULL
GROUP BY alcaldia_hechos, delito, ao_hechos;

select * from Carpetas#Alcaldia#Delitos#Año 
where Año is not null and Año >= 2009 and Numero_Delitos >= 1000 
order by Año, Alcaldia; 

select ao_hechos as Año, colonia_hechos as Colonia, delito as Delito, count(delito) as Numero_Delitos
into Carpetas#Colonia#Delitos#Año
from Delito, Localizacion, Tiempo
where IDLocalizacion = IDDelito and IDTiempo = IDLocalizacion and colonia_hechos is not NULL 
group by colonia_hechos, delito, ao_hechos

select * from Carpetas#Colonia#Delitos#Año where Numero_Delitos >= 100 order by Numero_Delitos;

select ao_hechos as Año, count(delito) as Numero_Delitos
into Carpetas#Delito#Año from Tiempo, Delito 
where IDTiempo = IDDelito and ao_hechos is not null
group by ao_hechos;

select * from Carpetas#Delito#Año order by Año;

select mes_hechos as Mes, COUNT(delito) as Numero_Delito
into Carpetas#Delito#Mes from Tiempo, Delito
where IDDelito = IDTiempo and mes_hechos is not null and ao_hechos >= 2010
group by mes_hechos;

select Numero_Delito from Carpetas#Delito#Mes where Mes = 'Enero';