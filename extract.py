#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

""" 
    Função getCoordinates
        Entrada: string dataFile
        Sa
"""
def getCoordinates (dataFile):
    coordinates = []
    try: 
        coordinatesFile = open(dataFile,'r')
    except FileNotFoundError:
        return 0

    for line in coordinatesFile:
        if line.find("Latitude") != -1:
            tmp = line.split('   ',1)
            tmp = tmp[1].split('\n',1)
            coordinates.append(tmp[0])
        elif line.find("Longitude") != -1:
            tmp = line.split('   ',1)
            tmp = tmp[1].split('\n',1)
            coordinates.append(tmp[0])
    coordinatesFile.close()
    return coordinates