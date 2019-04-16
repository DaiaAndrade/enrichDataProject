#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import requests, json


def enrichData (coord,apiKey):
    coord = [str(coord[0]),str(coord[1])]
    coordinates = coord[0]+','+coord[1]
    queue = {'key': apiKey, 'location': coordinates, 'outFormat': 'json', 'thumbMaps': 'true', 'includeNearestIntersection': 'true', 'includeRoadMetadata':'true'}
    url = 'https://www.mapquestapi.com/geocoding/v1/reverse'

    resp = requests.get(url,params=queue)
    enrichedData = json.loads(resp.text)

    if enrichedData["info"]["statuscode"] != 0:
        return 0        
    return enrichedData

def cleanData (enrichedData):
    data = enrichedData["results"][0]["locations"][0]
    newMapping = {'Latitude': data['latLng']['lat'],'Longitude': data['latLng']['lng'], 'Rua': data['street'], 'Cidade': data['adminArea5'], 'Estado': data['adminArea3'], 'País': data['adminArea3'], 'CEP': data['postalCode'], 'Tipo de endereço': data['geocodeQuality'], 'URL do Mapa': data['mapUrl'], 'Intersecção mais próxima': None, 'Unidade de Velocidade': None, 'Limite de Velocidade': None}
    if data['nearestIntersection'] != None:
        newMapping['Intersecção mais próxima'] = data['nearestIntersection']['label']
    if data['roadMetadata'] != None:
        newMapping['Unidade de Velocidade'] = data['roadMetadata']['speedLimitUnits']
        newMapping['Limite de Velocidade'] = data['roadMetadata']['speedLimit']
    return newMapping
