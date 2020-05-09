# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:45:56 2020

@author: 86133
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:\\Users\\86133\\Desktop\\IBI1_2019-20\\practical 7")
covid_data = pd.read_csv("full_data.csv")# importing the .csv file works
print(covid_data.iloc[0:16:3,:])#showing all columns, and every third row between (and including) 0 and 15
# using a Boolean to show “total cases” for all rows corresponding to Afghanistan
a = covid_data.loc[:,"location"] == 'Afghanistan'
b = covid_data.describe()
c = int((b.iloc[0,0]))
d = []
for i in range(c):
    if a[i] == True:
        d.append(i)
print(covid_data.loc[d,"total_cases"])
#making an object called world_new_cases to store only the data on new cases for the entire world
e = covid_data.loc[:,"location"] == 'World'
f = covid_data.describe()
g = int((f.iloc[0,0]))
h = []
for i in range(g):
    if e[i] == True:
        h.append(i)
world_new_cases = covid_data.loc[h,"new_cases"]
#calculate meam and median
np.mean(world_new_cases)
np.median(world_new_cases)
#plot box need to check
plt.boxplot(world_new_cases,
            vert=True,whis=1.5,patch_artist=True,
            meanline=True,showbox=True,showcaps=True,
            showfliers=True,notch=False)
#'b+' plot x-y figure in blue color
world_dates = covid_data.loc[h,"date"]
plt.plot(world_dates, world_new_cases, 'b+')
#'r+' plot x-y figure in red color
plt.plot(world_dates, world_new_cases, 'r+')
#'bo' make the point bold
plt.plot(world_dates, world_new_cases, 'bo')
# creat both new death and new cases
j = covid_data.loc[:,"location"] == 'World'
k = covid_data.describe()
l = int((k.iloc[0,0]))
m = []
for i in range(l):
    if e[i] == True:
        m.append(i)
world_new_deaths = covid_data.loc[h,"new_deaths"]
plt.plot(world_dates, world_new_deaths, 'r+')
plt.plot(world_dates, world_new_cases, 'b+')
plt.ylabel('Numbers')
plt.xlabel('Date')
plt.title('Daily new cases and new death')
#interval is 4 and clockwise rotate 90 degree
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
#How has total cases developed over time in China?
o = covid_data.loc[:,"location"] == 'China'
p = covid_data.describe()
q = int((p.iloc[0,0]))
r = []
for i in range(q):
    if o[i] == True:
        r.append(i)
China_date = covid_data.loc[r,"date"]
China_total_cases = covid_data.loc[r,"total_cases"]
plt.plot(China_date, China_total_cases,'r+')
