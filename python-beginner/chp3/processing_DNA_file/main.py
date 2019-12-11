# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:49:13 2019

@author: Emilia Chojak
@e-mail: emilia.chojak@gmail.com
"""

input_file = open("input.txt")
seqs = input_file.read().splitlines()

output_file = open("trimmed_sequences.txt", "w")

for seq in seqs[:-1]:
    output_file.write(seq+"\n")
output_file.write(seq)

for seq in seqs:
    print(len(seq))