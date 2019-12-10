#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:02:56 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""
out_file = open("sequences.fasta", "w")

headers = ["ABC123", "DEF456", "HIJ789"]
sequences = ["ATCGTACGATCGATCGATCGCTAGACGTATCG", "actgatcgacgatcgatcgatcacgact", "ACTGAC-ACTGT--ACTGTA----CATGTG"]

correct_sequences = []

for seq in sequences:
    a = seq.replace("-", "")
    correct_sequences.append(a.upper())

headers_and_seqs = dict(zip(headers, correct_sequences))

for header, seq in headers_and_seqs.items():
    out_file.write(f">{header}\n")
    out_file.write(seq + "\n")