# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re

accession_names = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

print("Accession names that contain the number 5")
for accession_name in accession_names:
    if len(re.findall(r"5", accession_name)) >= 1:
        print(accession_name)

print("Accession names that contain the letter d or e")
for accession_name in accession_names:
    if len(re.findall(r"[de]", accession_name)) >= 1:
        print(accession_name) 
    
print("Accession names that contain the letters d and e in that order")    
for accession_name in accession_names:
    if len(re.findall(r"d.*e", accession_name)) >= 1:
        print(accession_name)

print("Accession names that contain the letters d and e in that order with a single letter between them")    
for accession_name in accession_names:
    if len(re.findall(r"d.e", accession_name)) >= 1:
        print(accession_name)        

print("Accession names that contain both the letters d and e in any order")
for accession_name in accession_names:
    if len(re.findall(r"d.*e|e.*d", accession_name)) >= 1:
        print(accession_name)
        
print("Accession names that start with x or y")
for accession_name in accession_names:
    if len(re.findall(r"^x|^y", accession_name)) >= 1:
        print(accession_name)
 
print("Accession names that start with x or y and end with e")       
for accession_name in accession_names:
    if len(re.findall(r"^(x|y).*e$", accession_name)) >= 1:
        print(accession_name)
   
print("Accession names that contain three or more numbers in a row")       
for accession_name in accession_names:
    if len(re.findall(r"[1-9]{3,}", accession_name)) >= 1:
        print(accession_name)

print("Accession names that end with d followed by either a, r or p") 
for accession_name in accession_names:
    if len(re.findall(r"d[arp]$", accession_name)) >= 1:
        print(accession_name)