#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

from extract import *
from transform import *
from database import *
import sys

def run(server,user,password,fileName,key): 
    connection = Database(server,user,password)
    
    if connection == 0:
        print ('Houve um erro na conexão, tente novamente')
        sys.exit()    
    
    connection.runDatabase('GeoData')
    connection.createTable('Location')

    print("Iniciando extração das coordenadas.\n")
    coordinates = getCoordinates(fileName)
    if coordinates == 0:
        print ("Arquivo inválido, tente novamente.")
        connection.endDatabase('Location')
        sys.exit()

    i,j = 0,1

    print("Transformando coordenadas e colocando no banco.\n")
    print("Isso pode demorar um pouco, por favor aguarde.\n")

    while (i < len(coordinates) and j < len(coordinates)):
        tmp = coordinates[i],coordinates[j]
        data = enrichData(tmp,key)
        
        if data == 0:
            print('Houve um problema com a API de mapas. Tente novamente.')
            connection.endDatabase('Location')
            sys.exit()
        
        cleanedData = cleanData(data)
        connection.insertElement(cleanedData,'Location')
        i += 2
        j += 2
    
    while True: 
        userInteraction = input("Digite 1 para ver os dados resumidos, 2 para ver o banco completo ou 3 para terminar.\n")
        if userInteraction == '1':
            connection.showEssentialTable('Location')
        elif userInteraction == '2':
            connection.showCompleteTable('Location')
        elif userInteraction == '3':
            print("Finalizando tabela.")
            connection.endDatabase('Location')
            break
        else:
            print("Entrada inválida. Tente Novamente.\n")
    sys.exit()

if len(sys.argv) == 6:
    run(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
else:
    print ("Parâmetros de entrada insuficientes. Tente novamente")
    sys.exit()