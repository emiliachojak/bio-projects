#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:42:33 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

out_file1 = open("sequence1.fasta", "w")
out_file2 = open("sequence2.fasta", "w")
out_file3 = open("sequence3.fasta", "w")

headers = ["ABC123", "DEF456", "HIJ789"]
sequences = ["ATCGTACGATCGATCGATCGCTAGACGTATCG", "actgatcgacgatcgatcgatcacgact", "ACTGAC-ACTGT--ACTGTA----CATGTG"]

correct_sequences = []

for seq in sequences:
    a = seq.replace("-", "")
    correct_sequences.append(a.upper())
    
out_file1.write(f">{headers[0]}\n{correct_sequences[0]}\n")
out_file2.write(f">{headers[1]}\n{correct_sequences[1]}\n")
out_file3.write(f">{headers[2]}\n{correct_sequences[2]}\n")