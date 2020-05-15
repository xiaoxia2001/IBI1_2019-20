# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:11:05 2020

@author: 86133
"""

#open the file
get_mito_gene = open(r'C:\Users\86133\Desktop\IBI\week 8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
import re#import neccessary libraries
seq =[]
seqName =[]
count = 0
z =str()
x =[]
for line in get_mito_gene:
    if line.startswith('>'):#get the sequence name
        if z != '':
            seq.append(z)
        s = re.search(r'(gene):(\w+)',line)
        s1 = s.group(2)
        seqName.append(s1)#get the sequence name behind the 'gene:'
        z = ''
        x.append(line)
        count +=1
    else:
        line = line.rstrip()#get the sequence
        z += line
seq.append(z)#get the sequence
xfile=open('mito_gene.fa','w')#create a file
for i in range(count):
    if ':Mito:' in x[i]:
        a = '\n'+'>'+seqName[i] + '       ' + str(len(seq[i])) + '\n'+seq[i]#putting gene name and gene length
        xfile.write(a)
get_mito_gene.close
xfile.close
yfile = open('mito_gene.fa')
for line in yfile:
    print(line)#examine


        
        
        
