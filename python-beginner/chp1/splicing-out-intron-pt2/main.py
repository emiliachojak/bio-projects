#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:58:36 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

seq ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
coding_region_1 = seq[:62]
coding_region_2 = seq[90:]
coding_region_length = len(coding_region_1 + coding_region_2)
coding_percentage = (coding_region_length/len(seq))*100
print(coding_percentage)