import os
import xlrd
from conexionbd import *

books = ["2010PPH.xls", "2011PPH.xls", "2012PPH.xls", "2013PPH.xls", "2014PPH.xls", 
        "2015PPH.xls", "2016PPH.xls", "2017PPH.xls", "2018PPH.xls", "2019PPH.xls"]

connection = connectionBD()
cursor = connection.cursor()

def FillTable(file):
    path = f"{os.path.dirname(__file__)}/{f'xlsFiles/{file}'}"
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

    query = """Insert into EstacionesMonitoreo (Id_estacion, Clave_estacion, Nombre_estacion, Delegacion_municipio, Entidad) 
            values (?, ?, ?, ?, ?);"""

    for c in range(1, sheet.ncols):
        if sheet.cell(0,c).value == 'LOM':
            values = (1, 'LOM', 'Lomas', 'Miguel Hidalgo', 'CDMX')
        elif sheet.cell(0,c).value == 'TEC':
            values = (2, 'TEC', 'Cerro del Tepeyac', 'Gustavo A. Madero', 'CDMX')
        elif sheet.cell(0,c).value == 'DIC':
            values = (3, 'DIC', 'Diconsa', 'Tlalpan', 'CDMX')
        elif sheet.cell(0,c).value == 'MCM':
            values = (4, 'MCM', 'Museo de la Ciudad de México', 'Cuauhtémoc', 'CDMX')
        elif sheet.cell(0,c).value == 'TLA':
            values = (5, 'TLA', 'Tlalnepantla', 'Tlalnepantla de Baz ', 'Estado de México')
        elif sheet.cell(0,c).value == 'XAL':
            values = (6, 'XAL', 'Xalostoc', 'Ecatepec de Morelos', 'Estado de México')
        elif sheet.cell(0,c).value == 'EDL':
            values = (7, 'EDL', 'Ex Convento Desierto de los Leones', 'Cuajimalpa de Morelos', 'CDMX')
        elif sheet.cell(0,c).value == 'IBM':
            values = (8, 'IBM', 'Legaria', 'Miguel Hidalgo', 'CDMX')
        elif sheet.cell(0,c).value == 'NEZ':
            values = (9, 'NEZ', 'Nezahualcóyotl', 'Nezahualcóyotl', 'Estado de México')
        elif sheet.cell(0,c).value == 'MON':
            values = (10, 'MON', 'Montecillo', 'Texcoco', 'Estado de México')
        elif sheet.cell(0,c).value == 'EAJ':
            values = (11, 'EAJ', 'Ecoguardas Ajusco', 'Tlalpan', 'CDMX')
        elif sheet.cell(0,c).value == 'AJU':
            values = (12, 'AJU', 'Ajusco', 'Tlalpan', 'CDMX')
        elif sheet.cell(0,c).value == 'MPA':
            values = (13, 'MPA', 'Milpa Alta', 'Milpa Alta', 'CDMX')
        elif sheet.cell(0,c).value == 'SNT':
            values = (14, 'SNT', 'San Nicolás Totolapan', 'La Magdalena Contreras', 'CDMX')            
        elif sheet.cell(0,c).value == 'COR':
            values = (15, 'COR', 'CORENA', 'Xochimilco', 'CDMX')            
        elif sheet.cell(0,c).value == 'LAA':
            values = (16, 'LAA', 'Laboratorio de Análisis Ambiental', 'Gustavo A. Madero', 'CDMX')

        cursor.execute(query, values)

try:
    FillTable(books[0])
    print('All works properly')
except Exception as e:
    print(f'Something is wrong: {e}')

cursor.commit()
cursor.close()
connection.close()