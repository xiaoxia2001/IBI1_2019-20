# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:58:19 2020

@author: 86133
"""
#some simple math
a = 123
b = 123123 #give a and b values
print(b % 7)#to examine whether b can be divided by 7
c = b / 7
d = c / 11
e = d / 13
print(e == a)#to examine e and a which is greater.
#Booleans
X = True or False
Y = True or False
Z = (X and not Y) or (Y and not X)
print(Z == X or Y)#verify that it true if either X or Y (but not both) are true
W = X !=Y
print(Z == W)# verify that W and Z are always the same, no matter the values of X and Y.
    
