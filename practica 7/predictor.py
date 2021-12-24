import os
import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import precision_score,accuracy_score

script_directory = os.path.dirname(__file__)
dataSetTraining = f'{script_directory}/{"SetTraining.csv"}'
dataSetTesting = f'{script_directory}/{"SetTesting.csv"}'

dfTraining = pd.read_csv(dataSetTraining)
dfTesting = pd.read_csv(dataSetTesting)

X_train = dfTraining[["Anio","Mes","Dia"]]
y_train=dfTraining.Medicion

X_testing = dfTesting[["Anio","Mes","Dia"]]
y_testing = dfTesting.Medicion

print("-------------------- Normal SVM -------------------------")

clf = SVR(C=1.0, epsilon=0.2)
clf.fit(X_train, y_train) 
SVR(C=1.0, cache_size=200, coef0=0.0,
    degree=3, gamma='auto', kernel='rbf',
    max_iter=-1,  shrinking=True,
    tol=0.001, verbose=False)
scores = cross_val_score(clf, X_train, y_train, cv = 10)
res1=clf.predict(X_testing)

print("\n\n")
index=0
for element in res1:
    error=(abs((element-y_testing[index]))/y_testing[index])*100
    print(f'Valor predecido: {element} -- Valor real: {y_testing[index]} -- % de Error: {error}')
    index=index+1
    
import csv
pathCsvfile=f'{script_directory}/{"outRealTesting1.csv"}'
with open(pathCsvfile, 'w', encoding='utf-8', newline='') as csvFile:
    fieldnames = ['Valor predecido', 'Valor real','% de Error']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames) 
    writer.writeheader() 
    index=0
    for element in res1:
        error=(abs((element-y_testing[index]))/y_testing[index])*100
        print(f'Valor predecido: {element} -- Valor real: {y_testing[index]} -- % de Error: {error}')
        writer.writerow({'Valor predecido': "'"+format(element)+"'", 'Valor real': "'"+format(y_testing[index])+"'", '% de Error': "'"+format(error)+"'"})
        index=index+1