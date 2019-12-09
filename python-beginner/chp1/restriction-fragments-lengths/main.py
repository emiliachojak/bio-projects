#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 9 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

seq = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
cut_motif = "GAATTC" #G*AATTC so it will be cut between G and A
cut_index = seq.find(cut_motif)+1
first_fragment = len(seq[:cut_index])
second_fragment = len(seq[cut_index:])
print(first_fragment, second_fragment)