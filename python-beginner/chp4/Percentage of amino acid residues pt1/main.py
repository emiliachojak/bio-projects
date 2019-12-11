#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:21:03 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

def amino_acid_content(protein_seq, amino_acid):
    amino_acid = amino_acid.upper()
    if amino_acid in protein_seq:
        return (protein_seq.count(amino_acid)/len(protein_seq))*100
    else:
        return 0

assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP", "L") == 50
assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP", "Y") == 0