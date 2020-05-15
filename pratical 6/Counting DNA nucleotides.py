# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:32:31 2020

@author: 86133
"""
#set variables
A0 = 0
C0 = 0
G0 = 0
T0 = 0
genes = {}
DNA = 'ATGCTTCAGAAAGGTCTTACG'
for i in DNA:#count(A)
    if i == 'A':
        A0 += 1
genes['A']=A0#store in genes
for i in DNA:#count(C)
    if i =='C':
        C0 += 1
genes['C']=C0#store in genes
for i in DNA:#count(G)
    if i == 'G':
        G0 +=1
genes['G']=G0#store in genes
for i in DNA:#count(T)
    if i == 'T':
        T0 +=1
genes['T']=T0#store in genes
print(genes)
#start making plot
import matplotlib.pyplot as plt
labels = 'A','C','G','T'
sizes = [A0,C0,G0,T0]
explode=[0.1,0.1,0,0]
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('pie of the four DNA nucleotides')
plt.show