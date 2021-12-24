import os
import openpyxl
from conexionbd import *

connection = connectionBD()
cursor = connection.cursor()

file = f"{os.path.dirname(__file__)}/{'CarpetasInvestigacionCDMX.xlsx'}"
book = openpyxl.load_workbook(file)
sheet = book.active
rows = sheet.max_row
data_raw = sheet['A2': f'S{rows}'] # 808872

query = """Insert into CarpetasInvestigacionCDMX(id, ao_hechos, 
        mes_hechos, fecha_hechos, delito, categoria_delito, fiscalia, 
        agencia, unidad_investigacion, colonia_hechos, alcaldia_hechos,
        fecha_inicio, mes_Inicio, ao_inicio, calle_hechos, calle_hechos2, 
        longitud, latitud, geopoint)
        values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

data = []
for r in data_raw:
    a = [c.value for c in r]
    data.append(a)

for i in range(len(data)):
    ID = data[i][0]
    AnioHechos = data[i][1]
    MesHechos = data[i][2]
    FechaHechos = data[i][3]
    Delito = data[i][4]
    CateDelito = data[i][5]
    Fiscalia = data[i][6]
    Agencia = data[i][7]
    UnidadInvest = data[i][8]
    ColHechos = data[i][9]
    AlcaHechos = data[i][10]
    FechaInicio = data[i][11]
    MesInicio = data[i][12]
    AnioInicio = data[i][13]
    CalleHechos = data[i][14]
    CalleHechos2 = data[i][15]
    Longitud = data[i][16]
    Latitud = data[i][17]
    Geopoint = data[i][18]

    FH = FechaHechos.strftime('%d/%m/%Y')
    FI = FechaInicio.strftime('%d/%m/%Y')
    
    values = (ID, AnioHechos, MesHechos, FH, Delito, CateDelito, Fiscalia, 
    Agencia, UnidadInvest, ColHechos, AlcaHechos, FI, MesInicio, AnioInicio,
    CalleHechos, CalleHechos2, Longitud, Latitud, Geopoint)
    cursor.execute(query, values)

cursor.commit()
cursor.close()
connection.close()