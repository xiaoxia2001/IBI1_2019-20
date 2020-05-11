# -*- coding: utf-8 -*-
"""
Created on Sun May 10 17:17:31 2020

@author: 86133
"""

filename = input('filename:')
#open the file
gene = open('filename','r')
import re
seq =[]
seqName =[]
count = 0
z =str()
x =[]
for line in gene:
    if line.startswith('>'):#get the sequence name
        if z != '':
            seq.append(z)
        s = re.search(r'(gene):(\w+)',line)
        s1 = s.group(2)
        seqName.append(s1)
        z = ''
        x.append(line)
        count +=1
    else:
        line = line.rstrip()
        z += line
seq.append(z)#get the sequence
#Building a complementary dictionary
comp_dict = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G"}
for n in range(count):
    rev_seq=[]
    for i in seq[n]:
        rev_seq[n]=''
        rev_seq[n] +=comp_dict[i]#Complementary matching
        rev_seq[n] = rev_seq[n][::-1]#Reverse order
        rev_seq.append(rev_seq[n])
xfile = open('reverse complementary sequences.fa','w')
for n in range(count):
    a = '\n'+'>'+seqName[n] + '       ' + str(len(rev_seq[n])) + '\n'+rev_seq[n]
    xfile.write(a)
gene.close
xfile.close
yflie=open('reverse complementary sequences.fa')
for line in yflie:
    print(line)
        