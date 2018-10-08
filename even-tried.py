#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:55:34 2018

@author: root
"""

#program to check if the number is even or odd

n = int(input('n-->'))
m = n

not_even = []
for i in range(n+1): #range(11)
    if i%2 == 0:
        print(i,'is an even number')
    else:
        not_even.append(i)
else:
    print(*not_even, sep=" is an odd number\n")

#method2


even = []
odd = []
for j in range(m+1):
    if j%2 == 0:
        even.append(j)
    else:
        odd.append(j)

print('\n', *even, sep=' is even\n')
print('\n', *odd, sep=' is odd\n')
        
