# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 08:05:21 2019

@author: echojak
"""
import re

dna_file = open("dna.txt")
dna = dna_file.read()

enzymes = [("AbcI", r"A[ATGC]TAAT"), ("AbcII", r"GC[AG][AT]TG")] #enzyme AbcI cuts after ANT, enzyme AbcII cuts after GCNN

res_site1 = re.compile(enzymes[0][1])
res_site2 = re.compile(enzymes[1][1])

sites_for_enz1 = [site.start(0)+3 for site in re.finditer(res_site1, dna)]
sites_for_enz2 = [site.start(0)+4 for site in re.finditer(res_site2, dna)]

all_sites = sorted(sites_for_enz1 + sites_for_enz2)

dna_fragments_length = []
for i, site in enumerate(all_sites):
        if i == 0:
            dna_fragments_length.append(len(dna[0:site]))
        else:
            dna_fragments_length.append(len(dna[all_sites[i-1]:site]))
            
dna_fragments_length.append(len(dna[site:]))

#print(f"DNA fragments after double digestion with AbcI & AbcII: {dna_fragments_length}")