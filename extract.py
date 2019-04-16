#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

""" 
    Função getCoordinates
        Entrada: string dataFile
        Saída:  zero em caso de arquivo inexistente
                list coordinates com todas as coordenadas onde os índices pares são latitude e ímpares longitude
"""
def getCoordinates (dataFile):
    coordinates = []
    #teste para abrir o arquivo
    try: 
        coordinatesFile = open(dataFile,'r')
    except FileNotFoundError:
        return 0
    
    # laço para iterar as linhas do arquivo 
    for line in coordinatesFile:
        # teste para achar latitude
        if line.find("Latitude") != -1:
            # split dos elementos da linha
            tmp = line.split('   ',1)
            # eliminando o \n
            tmp = tmp[1].split('\n',1)
            coordinates.append(tmp[0])
        # teste para achar longitude
        elif line.find("Longitude") != -1:
            # split dos elementos da linha
            tmp = line.split('   ',1)
            # eliminando o \n
            tmp = tmp[1].split('\n',1)
            coordinates.append(tmp[0])
    coordinatesFile.close()
    return coordinates
