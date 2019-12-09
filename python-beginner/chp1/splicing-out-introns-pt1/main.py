#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:51:04 2019

@author: emilia_chojak
@e-mail: emilia.chojak@gmail.com
"""

seq ="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
coding_region_1 = seq[:62]
coding_region_2 = seq[90:]
print(coding_region_1 + coding_region_2)
