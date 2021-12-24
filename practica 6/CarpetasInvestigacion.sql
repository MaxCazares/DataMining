	-- create table CarpetasInvestigacionCDMX(
--     id INT,
--     ao_hechos INT,
--     mes_hechos VARCHAR(20),
--     Fecha_hechos VARCHAR(15),
--     delito VARCHAR(100),
--     categoria_delito VARCHAR(100),
--     fiscalia VARCHAR(100),
--     agencia VARCHAR(100),
--     unidad_investigacion VARCHAR(100),
--     colonia_hechos VARCHAR(100),
--     alcaldia_hechos VARCHAR(100),
--     fecha_inicio VARCHAR(15),
--     mes_inicio VARCHAR(20),
--     ao_inicio INT,
--     calle_hechos VARCHAR(200),
--     calle_hechos2 VARCHAR(200),
--     longitud FLOAT,
--     latitud FLOAT,
--     geopoint VARCHAR(100)
-- );

-- Modelo de estrella

SELECT id as IDTiempo, ao_hechos, mes_hechos, ao_inicio, mes_inicio into Tiempo 
FROM CarpetasInvestigacionCDMX;
SELECT * FROM Tiempo order by IDTiempo asc;

SELECT id as IDDelito, delito, categoria_delito into Delito 
from CarpetasInvestigacionCDMX;
SELECT * FROM Delito order by IDDelito asc;

SELECT id as IDLocalizacion, colonia_hechos, alcaldia_hechos, 
calle_hechos, calle_hechos2, longitud, latitud, geopoint 
into Localizacion FROM CarpetasInvestigacionCDMX;
SELECT * FROM Localizacion  order by IDLocalizacion asc;

-- create view Carpetas as select Tiempo.IDTiempo, Delito.IDDelito, Localizacion.IDLocalizacion
-- from Delito, Tiempo, Localizacion where IDTiempo = IDLocalizacion and IDDelito = IDTiempo;

SELECT alcaldia_hechos, delito, count(delito) as Numero_Delitos
from Localizacion, Delito
where Localizacion.IDLocalizacion = Delito.IDDelito
GROUP BY alcaldia_hechos, delito;