# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:01:01 2020

@author: 86133
"""

seq = 'ATGCGACTACGATCGAGGGCCAT'
#Building a complementary dictionary
comp_dict = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"}
rev_seq=''
for i in seq:
    rev_seq +=comp_dict[i]#Complementary matching
rev_seq = rev_seq[::-1]#Reverse order
print(rev_seq)