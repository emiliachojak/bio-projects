#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 21:44:13 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

import csv

def get_at_content(dna):    
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T')   
    at_content = (a_count + t_count)/len(dna)
    return at_content

with open("data.csv") as csv_data:
    csv_reader = list(csv.reader(csv_data, delimiter = ","))
    
    print("Several species")
    for line in csv_reader:
        if line[0] == "Drosophila melanogaster" or line[0] == "Drosophila simulans":
            print(line[2]) 
    
    print("Length range")
    for line in csv_reader:
        if len(line[1]) > 90 and len(line[1]) < 110:
            print(line[2])
    
    print("AT content")
    for line in csv_reader:
        if get_at_content(line[1]) < 0.5 and int(line[3]) > 200:
            print(line[2])

    print("Complex condition")
    for line in csv_reader:
        if (line[2][0] == "k" or line[2][0] == "h") and line[0] != "Drosophila melanogaster":
            print(line[2])

    print("High low medium")
    for line in csv_reader:
        if get_at_content(line[1])  > 0.65:
            print(f"Gene {line[2]} : AT content for this gene is high")
        elif get_at_content(line[1]) < 0.45:
            print(f"Gene {line[2]} : AT content for this gene is low")
        else:
             print(f"Gene {line[2]} : AT content for this gene is medium")s