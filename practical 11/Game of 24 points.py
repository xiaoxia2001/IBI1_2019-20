# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:45:23 2020

@author: 86133
"""

import re
import sys
import copy
judge = True; c = float(); R = []; result = False; num_float = [];count = 0
origin = input('''Please input numbers to compute 24:(use ',' to divide them)
''')
nums = re.split(',', origin)
for item in nums:
    num_float.append(float(item))
for n in range(len(nums)):
    if int(nums[n]) >= 24 or int(nums[n]) < 1:
        judge = False
if judge == False:
    print('The input numbers must be integers from 1 to 23')
else:
    def operation(a,b,op):
        global c,count
        if op == 1:
            c = a + b
        elif op == 2:
            c = a * b
        elif op == 3:
            c = a - b
        elif op == 4:
            if b == 0.0:
               c = str(1)
            else:
               c = a/b
        elif op == 5:
            if a == 0.0:
               c = str(1)
            else:
               c = b/a
        if c == 24.0:
            count += 1
            print('Yes')
            print('Recursion times:',count)
            sys.exit()
        else:
            return c
    def cal(L):
        global c,count
        if len(L) == 1:
            R.append(L[0])
        else:
         for i in range(0,len(L)-1):
          for j in range (i+1,len(L)):
            L_copy = copy.deepcopy(L)
            A = L[i]
            B = L[j]
            L_copy.remove(A)
            L_copy.remove(B)
            for k in range(1,6):
                copyL_copy = copy.deepcopy(L_copy)
                Result = operation(A,B,k)
                count += 1
                if c == str(1):
                   c = float()
                else:
                 copyL_copy.append(Result)
                 cal(copyL_copy)

    cal(num_float)
    for r in range(len(R)):
        if R[r] == 24:
            result = True
    if result == True:
        print('Yes')
    else:
        print('No')
    print('Recursion times:',count)