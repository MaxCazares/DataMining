import os
import xlrd
from conexionbd import *
from datetime import datetime
from xlrd import xldate_as_tuple

books = ["2010PPH.xls", "2011PPH.xls", "2012PPH.xls", "2013PPH.xls", "2014PPH.xls", 
        "2015PPH.xls", "2016PPH.xls", "2017PPH.xls", "2018PPH.xls", "2019PPH.xls"]

connection = connectionBD()
cursor = connection.cursor()

def FillTable(file):
    path = f"{os.path.dirname(__file__)}/{f'xlsFiles/{file}'}"
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)
    query = """Insert into
            Mediciones(Elemento, Id_estacion, Medicion, Dia, Mes, Anio, Semana) 
            values (?, ?, ?, ?, ?, ?, ?);"""

    for c in range(1, sheet.ncols):
        for r in range(1,sheet.nrows):        
            date = datetime (* xldate_as_tuple (sheet.cell(r,0).value, 0)).date()

            if sheet.cell(0,c).value == 'LOM':                
                values = ('Precipitación Pluvial', 1, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'TEC':
                values = ('Precipitación Pluvial', 2, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'DIC':
                values = ('Precipitación Pluvial', 3, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'MCM':
                values = ('Precipitación Pluvial', 4, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'TLA':
                values = ('Precipitación Pluvial', 5, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'XAL':
                values = ('Precipitación Pluvial', 6, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'EDL':
                values = ('Precipitación Pluvial', 7, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'IBM':
                values = ('Precipitación Pluvial', 8, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'NEZ':
                values = ('Precipitación Pluvial', 9, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'MON':
                values = ('Precipitación Pluvial', 10, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'EAJ':
                values = ('Precipitación Pluvial', 11, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'AJU':
                values = ('Precipitación Pluvial', 12, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'MPA':
                values = ('Precipitación Pluvial', 13, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            elif sheet.cell(0,c).value == 'SNT':
                values = ('Precipitación Pluvial', 14, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))            
            elif sheet.cell(0,c).value == 'COR':
                values = ('Precipitación Pluvial', 15, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))          
            elif sheet.cell(0,c).value == 'LAA':
                values = ('Precipitación Pluvial', 16, sheet.cell(r,c).value, date.day, date.strftime('%b'), date.strftime('%Y'), date.strftime('%U'))
            
            cursor.execute(query, values)

try:
    for i in range(len(books)):
        FillTable(books[i])
    print('All works properly')
except Exception as e:
    print(f'Something is wrong: {e}')

cursor.commit()
cursor.close()
connection.close()