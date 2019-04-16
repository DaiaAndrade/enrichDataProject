#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import MySQLdb

class Database:

    def __init__(self, server,user,password):
        self.server = server
        self.user = user
        self.password = password
    
    def databaseConnect(self):
        self.connection = MySQLdb.connect(self.server,self.user,self.password)

    def getCursor(self):
        self.cursor = self.connection.cursor()

    def createdatabase(self,databaseName):
        tmp = "CREATE DATABASE "+databaseName
        self.getCursor()
        self.cursor.execute(tmp)

    def databaseSelect(self,databaseName):
        self.getCursor()
        self.connection.select_db(databaseName)

    def createTable(self,tableName):
        tmp1 = "create table "
        tmp2 = "(ID INT NOT NULL auto_increment,Latitude varchar(20),Longitude varchar(20),Rua varchar(250),Cidade varchar(100),Estado varchar(100),Pais varchar(100),CEP varchar(20),Tipo_endereco varchar(20),URL_Mapa varchar(1000),Interseccao varchar(500),Unidade_Velocidade varchar(10),Limite_Velocidade int,PRIMARY KEY (ID))"
        tmp3 = tmp1+tableName+tmp2
        self.getCursor()
        self.cursor.execute(tmp3)

    def insertElement(self,data,tableName):
        tmp1 = "insert into "
        tmp2 = "(Latitude,Longitude,Rua,Cidade,Estado,Pais,CEP,Tipo_endereco,URL_Mapa,Interseccao,Unidade_Velocidade,Limite_Velocidade) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        tmp3 = tmp1+tableName+tmp2
        self.getCursor()
        self.cursor.execute(tmp3,(data['Latitude'],data['Longitude'],data['Rua'],data['Cidade'],data['Estado'],data['País'],data['CEP'],data['Tipo de endereço'],data['URL do Mapa'],data['Intersecção mais próxima'],data['Unidade de Velocidade'],data['Limite de Velocidade']))
        self.connection.commit()

    def runDatabase(self,databaseName):
        self.databaseConnect()
        self.createdatabase(databaseName)
        self.databaseSelect(databaseName)
    
    def showCompleteTable(self,tableName):
        self.getCursor()
        tmp = "SELECT * FROM "+tableName
        self.cursor.execute(tmp)
        resultTable = self.cursor.fetchall()
        for i in resultTable:
            print(i)
    
    def showEssentialTable(self,tableName):
        self.getCursor()
        tmp = "SELECT Latitude,Longitude,Rua,Cidade,Estado,Pais FROM "+tableName
        self.cursor.execute(tmp)
        resultTable = self.cursor.fetchall()
        for i in resultTable:
            print(i)

    def endDatabase(self,tableName,databaseName):
        tmp = "DROP " + tableName + " IF EXISTS"
        self.getCursor()
        self.cursor.execute(tmp)
        self.connection.commit()
        tmp = "DROP " + databaseName + " IF EXISTS"
        self.getCursor()
        self.cursor.execute(tmp)
        self.connection.commit()