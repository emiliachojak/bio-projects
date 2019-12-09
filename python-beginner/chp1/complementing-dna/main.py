#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 9 2019

@author: emilia
@e-mail: emilia.chojak@gmail.com
"""

complementing_rule  = {"A" : "T",
                       "G" : "C",
                       "T" : "A",
                       "C" : "G"
        }

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
seq_trans = str.maketrans(complementing_rule)
compl_seq = seq.translate(seq_trans)
print(compl_seq)