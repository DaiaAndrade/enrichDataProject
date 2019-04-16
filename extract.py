#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

def getCoordinates (dataFile):
    coordinates = []
    coordinatesFile = open(dataFile,'r')
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