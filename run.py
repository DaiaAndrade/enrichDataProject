#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from extract import *
from transform import *
from database import *
import sys

def run(server,user,password,fileName,key): 
    connection = Database(server,user,password)
    connection.runDatabase('GeoData')
    connection.createTable('Location')

    print("Iniciando extração das coordenadas.\n")
    coordinates = getCoordinates(fileName)
    i,j = 0,1
    print("Transformando coordenadas e colocando no banco.\n")
    while (i < len(coordinates) and j < len(coordinates)):
        tmp = coordinates[i],coordinates[j]
        data = enrichData(tmp,key)
        cleanedData = cleanData(data)
        connection.insertElement(cleanedData,'Location')
        i += 2
        j += 2
    loop = False
    while loop == False: 
        userInteraction = input("Digite 1 para ver os dados resumidos ou 2 para ver o banco completo.\n")
        if userInteraction == 1:
            connection.showEssentialTable('Location')
            loop = True
        elif userInteraction == 2:
            connection.showCompleteTable('Location')
            loop = True
        else:
            print("Entrada inválida. Tente Novamente")
    while loop == True:
        userInteraction = ("Terminado. Podemos finalizar? s/n")
        if userInteraction == 's':
            loop = False
    connection.endDatabase('Location','GeoData')
    sys.exit()

if len(sys.argv) == 6:
    run(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
else:
    print ("Parâmetros de entrada insuficientes. Tente novamente")
    sys.exit()