# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:09:24 2019

@author: Emilia Chojak
@e-mail: emilia.chojak@gmail.com
"""
import csv

dna_file = open("genomic_dna.txt")
coding_seq_file = open("coding_seq.txt", "w")

genomic_dna = dna_file.read()

with open('exons.txt') as exon_file:
    new_coords = []
    coords = list(csv.reader(exon_file, delimiter=","))
    for row in coords:
        new_coords.append(list(map(int, row)))
        
    for pair in new_coords:
        coding_seq_file.write(genomic_dna[pair[0]:pair[1]])