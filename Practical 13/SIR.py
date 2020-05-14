# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:06:30 2020

@author: 86133
"""

# import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
#import neccessary parameter
N = 10000
β = 0.3
γ = 0.05
S = 9999
I = 1
R = 0
Susceptible = []
Infected = []
Recovered = []
L1 =[]
L2 =[]
for t in range(1,1000+1):#loop over 1000 time pointsloop over 1000 time points
    L1 = np.random.choice(range(2),I,p=[1-γ,γ])#The number of people who recovered was calculated at random
    L2 = np.random.choice(range(2),S,p=[1-β*I/N,β*I/N])#The number of people who infected was calculated at random
    l1 = sum(L1)
    l2 = sum(L2)
    S = S-l2
    I = I +l2-l1
    R = R+l1
    Susceptible.append(S)
    Infected.append(I)
    Recovered.append(R)
#draw the figure
figure = plt.figure()
plt.figure(figsize =(6 ,4) , dpi=150)
inf_line =plt.plot(Infected, label='Infected')
sus_line = plt.plot(Susceptible, label='Susceptible')
rec_line = plt.plot(Recovered, label='Recovered')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.savefig('SIR model',type='png')