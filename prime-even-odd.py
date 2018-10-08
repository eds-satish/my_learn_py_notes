#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 19:08:45 2018

@author: root
"""

"""
input()
'50'
int('10')

10 number 
range(start, stop, step)
range(1, 10, 2)
"""

n = int(input('enter number'))

for i in range(n+1):
    if i == 2:
        print(i, 'is even and prime')
    else:
        if i%2 == 0:
            print(i, 'is even number')
        else:
            count = 0
            for j in range(1, i+1):
               if i%j == 0:
                   count = count + 1
            if count == 2:
                print(i, 'is pure prime number')
            else:
                print(i, 'is odd number')
                
                
    