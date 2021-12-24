import pyodbc

def connectionBD():
    server = 'MAXO'
    database = 'PPH_2010_2019'
    user = 'sa'
    password = ''

    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+user+';PWD='+password)
        print('connection successfully')
    except Exception as e:
        print(f'error during connection: {e}')

    return connection