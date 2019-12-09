#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
AT_cont = (seq.count("A")+seq.count("T"))/len(seq)
print(AT_cont)
