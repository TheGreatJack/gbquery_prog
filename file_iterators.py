#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 08:39:47 2021

@author: anderjackf
"""

import os
import query_search as qs



#Itera sobre los gbff y hace una busqueda en cada uno de los archivos
#presentes en el directorio de los archivos
def cycler_full(data_path,query,protseq):
    for file in os.listdir(data_path):
        file_handler = open(data_path+"/"+file)
        file_data = file_handler.readlines()
        file_data= record_checker(file_data)
        
        for record in file_data:
            qs.query_search(record,query,file,protseq)
        file_handler.close()
        
        
        
#Itera sobre los gbff y hace una busqueda en los archivos que tengan un 
#match con la opcion "ID"         
def cycler_id(data_path,query,id_dict,protseq):
    for file in os.listdir(data_path):
        file_handler = open(data_path+"/"+file)
        file_data = file_handler.readlines()
        file_data= record_checker(file_data)
        
        ##Ignoro el tipo de ID que se busca, si matchea el ID debe bastar
        id_pattern=list(id_dict.values())[0]
        for record in file_data:
            if id_search(record,id_pattern) == True:
                qs.query_search(record,query,file,protseq)
        file_handler.close()
        
        
        
#Esta funcion evalua cuantos records hay en un archivo gbff y los separa
#para poder hacer las busquedas en cada record.
def record_checker(file_data):
    parts=[-1]
    file_records=[]
    for line_number in range(len(file_data)):
        if "//\n" in file_data[line_number]:
            parts.append(line_number)  
    for parts_id in range(1,len(parts)):
        file_records.append(file_data[parts[parts_id-1]+1:parts[parts_id]])
    return file_records
        


#Busca en un record de gbff linea por linea el ID que se pasó para buscar.
#Retorna True si hace 1 match
def id_search(file_data,id_pattern):
    is_match = False
    for lines in file_data:
        if id_pattern in lines:
            is_match=True
            break
    return is_match

    



