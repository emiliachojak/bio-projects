# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 19:28:50 2019

@author: Emilia Chojak
"""
import os

for i in range(100, 1000, 100):
    min_len = i
    max_len = i + 99
    folder_name = f"{min_len}_{max_len}"
    if not os.path.exists(folder_name): 
        os.mkdir(folder_name)

seqs = []
for file in os.listdir("./"):
    if file.endswith(".dna"):
        with open(file) as f:
            dna_file = f.read().splitlines()
            for dna_seq in dna_file:
                seqs.append(dna_seq)
            
for seq in seqs:
    min_len = len(seq)-(len(seq)%100)
    max_len = min_len + 99
    folder_name = f"{min_len}_{max_len}"
    if len(seq) >= min_len and len(seq) < max_len:
        path = f"./{folder_name}/{seqs.index(seq)}"
        output = open(f"{path}.txt", "w")
        output.write(seq)
        output.close()