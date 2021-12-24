SELECT ao_hechos as A�o, alcaldia_hechos as Alcaldia, delito as Delito, count(delito) as Numero_Delitos
into Carpetas#Alcaldia#Delitos#A�o
from Localizacion, Delito, Tiempo
where IDLocalizacion = IDDelito and IDTiempo = IDDelito and alcaldia_hechos is not NULL
GROUP BY alcaldia_hechos, delito, ao_hechos;

select * from Carpetas#Alcaldia#Delitos#A�o 
where A�o is not null and A�o >= 2009 and Numero_Delitos >= 1000 
order by A�o, Alcaldia; 

select ao_hechos as A�o, colonia_hechos as Colonia, delito as Delito, count(delito) as Numero_Delitos
into Carpetas#Colonia#Delitos#A�o
from Delito, Localizacion, Tiempo
where IDLocalizacion = IDDelito and IDTiempo = IDLocalizacion and colonia_hechos is not NULL 
group by colonia_hechos, delito, ao_hechos

select * from Carpetas#Colonia#Delitos#A�o where Numero_Delitos >= 100 order by Numero_Delitos;

select ao_hechos as A�o, count(delito) as Numero_Delitos
into Carpetas#Delito#A�o from Tiempo, Delito 
where IDTiempo = IDDelito and ao_hechos is not null
group by ao_hechos;

select * from Carpetas#Delito#A�o order by A�o;

select mes_hechos as Mes, COUNT(delito) as Numero_Delito
into Carpetas#Delito#Mes from Tiempo, Delito
where IDDelito = IDTiempo and mes_hechos is not null and ao_hechos >= 2010
group by mes_hechos;

select Numero_Delito from Carpetas#Delito#Mes where Mes = 'Enero';