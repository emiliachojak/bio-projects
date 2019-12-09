#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:01:32 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

seq ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
coding_region_1 = seq[:62]
coding_region_2 = seq[90:]
intron = seq[62:90].lower()
print(coding_region_1+intron+coding_region_2)