#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:27:48 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""
from decimal import Decimal

def amino_acid_content(protein_seq, amino_acids = ["A", "I", "L", "M", "F", "W", "Y", "V"]):
    amino_acid_count = 0
    for amino_acid in amino_acids:
        if amino_acid in protein_seq:
            amino_acid_count += protein_seq.count(amino_acid)
    return Decimal(Decimal(amino_acid_count)/len(protein_seq)*100)

assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert amino_acid_content("MSRSLLLRFLLFLLLLPPLP") == 65