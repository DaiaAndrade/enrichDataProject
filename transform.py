#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import requests, json

""" 
    Função enrichData
        função para procurar dados dado uma latitude e longitude
    Entrada:
        list string coord, string apiKey
    Saída:
        mensagem de errou ou dict com os dados crus
"""

def enrichData (coord,apiKey):
    #transformar coordenadas em string
    coord = [str(coord[0]),str(coord[1])]
    coordinates = coord[0]+','+coord[1]
    
    #dict com os parametros da queue da URL
    queue = {'key': apiKey, 'location': coordinates, 'outFormat': 'json', 'thumbMaps': 'true', 'includeNearestIntersection': 'true', 'includeRoadMetadata':'true'}
    url = 'https://www.mapquestapi.com/geocoding/v1/reverse'
    
    resp = requests.get(url,params=queue)
    enrichedData = json.loads(resp.text)
    
    #teste para verificar se houve algum problemacom a request
    if enrichedData["info"]["statuscode"] != 0:
        return 0        
    return enrichedData

""" 
    Função cleanData
        função para selecionar os dados mais adequados depois de enriquecidos
    Entrada:
        dict enrichedData
    Saída:
        mensagem de errou ou dict com os dados limpos
"""

def cleanData (enrichedData):
    #acesso no dict aos dados que de fato interessam
    data = enrichedData["results"][0]["locations"][0]
    #criação de um novo dict pros dados limpos
    newMapping = {'Latitude': data['latLng']['lat'],'Longitude': data['latLng']['lng'], 'Rua': data['street'], 'Cidade': data['adminArea5'], 'Estado': data['adminArea3'], 'País': data['adminArea3'], 'CEP': data['postalCode'], 'Tipo de endereço': data['geocodeQuality'], 'URL do Mapa': data['mapUrl'], 'Intersecção mais próxima': None, 'Unidade de Velocidade': None, 'Limite de Velocidade': None}
    #tratamentos para o caso de presença de intersecção
    if data['nearestIntersection'] != None:
        newMapping['Intersecção mais próxima'] = data['nearestIntersection']['label']
    #tratamento para o caso de haver dados de limite de velocidade
    if data['roadMetadata'] != None:
        newMapping['Unidade de Velocidade'] = data['roadMetadata']['speedLimitUnits']
        newMapping['Limite de Velocidade'] = data['roadMetadata']['speedLimit']
    return newMapping
