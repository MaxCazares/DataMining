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
    query = """Insert into Principal(Clave_estacion, Localizacion, DiaSemana, Fecha, Medicion) 
            values (?, ?, ?, ?, ?);"""
    
    for c in range(1, sheet.ncols):
        for r in range(1,sheet.nrows):   
            date = datetime (* xldate_as_tuple (sheet.cell(r,0).value, 0)).date() 
            if sheet.cell(0,c).value == 'LOM':
                values = ('LOM','Miguel Hidalgo', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'TEC':
                values = ('TEC','Gustavo A. Madero', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'DIC':
                values = ('DIC', 'Tlalpan', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'MCM':
                values = ('MCM','Cuauhtémoc', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'TLA':
                values = ('TLA','Tlalnepantla de Baz ', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'XAL':
                values = ('XAL','Ecatepec de Morelos', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'EDL':
                values = ('EDL','Cuajimalpa de Morelos', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'IBM':
                values = ('IBM','Miguel Hidalgo', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'NEZ':
                values = ('NEZ','Nezahualcóyotl', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'MON':
                values = ('MON','Texcoco', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'EAJ':
                values = ('EAJ','Tlalpan', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'AJU':
                values = ('AJU','Tlalpan', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'MPA':
                values = ('MPA','Milpa Alta', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            elif sheet.cell(0,c).value == 'SNT':
                values = ('SNT','La Magdalena Contreras', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)            
            elif sheet.cell(0,c).value == 'COR':
                values = ('COR','Xochimilco', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)            
            elif sheet.cell(0,c).value == 'LAA':
                values = ('LAA','Gustavo A. Madero', date.strftime('%A'), date.strftime('%d/%m/%Y'), sheet.cell(r,c).value)
            
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