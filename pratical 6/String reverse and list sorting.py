# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:48:37 2020

@author: 86133
"""

#import the length
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths1=sorted(gene_lengths)
#following the guide,we need to delete the maximum and the minimum
del(gene_lengths1[9])
del(gene_lengths1[0])
print(gene_lengths1)
#start making plot
import numpy as np
import matplotlib.pyplot as plt
score = gene_lengths1
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=True,showbox=True,showcaps=True,
            showfliers=True,notch=False,boxprops = {'facecolor':'orange'})
plt.title('Gene',fontsize=20)
plt.show()