#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:48:49 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""
SEQ_FILE = open("genomic_dna.txt")
seq = SEQ_FILE.read()

coding_region_1 = seq[:62]
coding_region_2 = seq[90:]

out1 = open("coding_region_1.txt", "w")
out2 = open("coding_region_2.txt", "w")

out1.write(coding_region_1)
out2.write(coding_region_2)