#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:19:41 2021

@author: anderjackf
"""

from appparams import AppParams
import file_iterators as fi



def main():
    params_manager = AppParams()
    params = params_manager.get_params()
    ########print('using params:',params)
    
    #Se extraen los parametros del usuario
    data_path=params["data"]
    id_dict=params["id"]
    query=params["query"][0]
    
    
    #El query "proteinseq" se maneja diferente pues tiene un codigo de 
    #acceso que debe buscarse
    if "proteinseq" in query:
        protseq=query[11:]
        query=query[:10]
    else:
        protseq=0
    ########print(protseq,query)

    #Dependiendo de la presencia de la opcion "id" la busqueda se maneja de
    #forma diferente. 
    if len(id_dict) == 1:
        fi.cycler_id(data_path,query,id_dict,protseq)
    elif len(id_dict) == 0:
        fi.cycler_full(data_path,query,protseq)

   

if __name__ == '__main__':
    main()
         


