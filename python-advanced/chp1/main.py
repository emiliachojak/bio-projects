# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:00:00 2019

@author: Emilia Chojak
@e-mail: emilia.chojak@gmail.com
"""

tax_dict = {
'Pan troglodytes' : 'Hominoidea', 'Pongo abelii' : 'Hominoidea',
'Hominoidea' : 'Simiiformes', 'Simiiformes' : 'Haplorrhini',
'Tarsius tarsier' : 'Tarsiiformes', 'Haplorrhini' : 'Primates',
'Tarsiiformes' : 'Haplorrhini', 'Loris tardigradus' :
'Lorisidae',
'Lorisidae' : 'Strepsirrhini', 'Strepsirrhini' : 'Primates',
'Allocebus trichotis' : 'Lemuriformes', 'Lemuriformes' :
'Strepsirrhini',
'Galago alleni' : 'Lorisiformes', 'Lorisiformes' :
'Strepsirrhini',
'Galago moholi' : 'Lorisiformes'
}
    
def find_ancestors(taxon):
    if taxon == 'Primates':
        return [taxon]
    parent = tax_dict[taxon]
    parent_ancestors = find_ancestors(parent)
    return [taxon] + parent_ancestors

def find_ancestors_for_many(taxon_list):
    many_parents = []
    for taxon in taxon_list:
        many_parents.append(find_ancestors(taxon))
    return many_parents

def last_common_ancestor(many_parents):
    for  parent in many_parents[0]:
        is_ok = True
        for parent_list in  many_parents:
            if parent not in parent_list:
                is_ok = False
        if is_ok == True:
            return parent
    
print(last_common_ancestor(find_ancestors_for_many(["Galago alleni", "Galago moholi"])))