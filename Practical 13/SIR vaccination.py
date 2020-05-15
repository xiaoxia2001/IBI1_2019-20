# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:14:33 2020

@author: 86133
"""

# import necessary libraries
Infected = {}
import matplotlib.pyplot as plt
import numpy as np

# import neccessary parameter
for i in range(11):
    if i != 10:
        Vaccine_rate = i / 10
        N = 10000
        β = 0.3
        γ = 0.05
        S = 9999
        I = 1
        R = 0
        S = S - N * Vaccine_rate#Calculate the actual susceptible population
        Infected[i] = []
        for t in range(1000):
            a = I / N
            c = a * 0.3
            b = 1 - c
            S2=list(np.random.choice(range(2), int(S), p=[1 - c, c])).count(1)#Count the number of people newly infected in each round
            S = S - S2
            I += S2
            I = I - list(np.random.choice(range(2), int(I), p=[0.95, 0.05])).count(1)#Count the number of new convalescents in each round
            Infected[i].append(I)
    else:
        Infected[i] = []
        for t in range(1000):
            Infected[i].append(0)
# draw the figure
figure = plt.figure()
from matplotlib import cm

plt.figure(figsize=(6, 4), dpi=150)
inf_line0 = plt.plot(Infected[0], label='0%', color=cm.viridis(3))
inf_line1 = plt.plot(Infected[1], label='10%', color=cm.viridis(6))
inf_line2 = plt.plot(Infected[2], label='20%', color=cm.viridis(9))
inf_line3 = plt.plot(Infected[3], label='30%', color=cm.viridis(12))
inf_line4 = plt.plot(Infected[4], label='40%', color=cm.viridis(15))
inf_line5 = plt.plot(Infected[5], label='50%', color=cm.viridis(18))
inf_line6 = plt.plot(Infected[6], label='60%', color=cm.viridis(21))
inf_line7 = plt.plot(Infected[7], label='70%', color=cm.viridis(24))
inf_line8 = plt.plot(Infected[8], label='80%', color=cm.viridis(27))
inf_line9 = plt.plot(Infected[9], label='90%', color=cm.viridis(30))
inf_line10 = plt.plot(Infected[10], label='100%', color=cm.viridis(33))
plt.legend()
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rate')#name the plot
plt.savefig('SIR model with different vaccination rate', type='png')#save the plot
plt.show()
plt.close()