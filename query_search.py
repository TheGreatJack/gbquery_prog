#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:10:34 2021

@author: anderjackf
"""



#Funcion que decide que tipo de busqueda se hace sobre los archivos
#dependiendo del parametro que se le pase
def query_search(record,query,file,protseq):
    if query == "files":
        files_search(record,file)
    if query == "totals":
        totals_search(record,file)
    if query == "header":
        header_search(record,file)
    if query == "dnaseq":
        dnaseq_search(record,file)
    if query == "proteinlist":
        protlist_search(record,file)
    if query == "proteinseq":
        protseq_search(record,file,protseq)



def files_search(record,file):
    print("\n"+file+":")
    print(record[0][:-1])
    
    
    
def totals_search(record,file):
    print("\n"+file+":")
    print(record[0][:-1])
    
    can_print=False
    
    for line in record:
        if can_print==True and "##Genome-Annotation-Data-END##" in line:
            break
        if can_print==True:
            print(line[:-1])
        if "##Genome-Annotation-Data-START##" in line:
            can_print=True
            
            
                
def header_search(record,file):
    print("\n"+file+":")
    
    can_print=False
    
    for line in record:
        if "LOCUS" in line:
            can_print=True
        if can_print==True and "REFERENCE" in line:
            break
        if can_print==True:
            print(line[:-1])

    return None



def dnaseq_search(record,file):
    print("\n"+file+":")
    print(record[0][:-1])
    
    can_print=False
    
    for line in record:
        if can_print==True:
            print(line[:-1])
        if "ORIGIN" in line:
            can_print=True
            
            
            
def protlist_search(record,file):
    print("\n"+file+":")
    print(record[0][:-1])
    
    product=""
    for line_number in range(len(record)):
        if "/product=" in record[line_number]:
            product=record[line_number][30:-1]
            for i in range(1,5):
                if "/protein_id=" in record[line_number+i]:
                    break
                else:
                    product+=record[line_number+i][21:-1]
        elif "/protein_id=" in record[line_number]:
            prot_id=record[line_number][33:-1].replace('"','')
            product=product.replace('"','')
            print(prot_id,product)
            
            

def protseq_search(record,file,protseq): 
    for line_number in range(len(record)):
        if protseq in record[line_number]:
            print("\n"+file+":")
            print(record[0][:-1])
            can_print=False
            for line in record[line_number:]:

                if can_print==True:
                    if '"' in line:
                        can_print=False
                        print(line[21:-2])
                        break
                    print(line[21:-1])
                if "/translation=" in line:
                    can_print=True
                    print(line[35:-1])
            break