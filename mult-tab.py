#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 11:04:29 2018

@author: root
"""

"""
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
"""

"""
n = int(input('n-->'))

for i in range(1, n+1): #iterations = 1, 2, 3, 4, 5 example n = 5
    print('{:^30}'.format(' '))
    for m in range(1,11):
        c = i * m
        print('{0} x {1} = {2}'.format(i, m, c))
"""        




"""
print('{:<20} {:^20} {:>20}'.format('1 x 1 = 1', '2 x 1 = 2', '3 x 1 = 3'))
print('{:<20} {:^20} {:>20}'.format('1 x 2 = 2', '2 x 2 = 4', '3 x 2 = 6'))
print('{:<20} {:^20} {:>20}'.format('1 x 3 = 3', '2 x 3 = 6', '3 x 3 = 9'))
"""



"""    
width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()
"""

"""

n = int(input('n-->')) #3

for i in range(1, n+1): #iterations = 1, 2, 3, 4, 5 example n = 5
    for m in range(1,11):
        c = i * m
        #print('{0} x {1} = {2}'.format(i, m, c))
        print('{0:{m1}{n1}}'.format(i, 'aa', m1=m, n1=n))
    print()

#{i:<10}
    
"""


X = 1
Y = 1
for X in range(1,11):
    print('{:>4}'.format(X), end=' ')
    while Y <= 10:
        print('{:>4}'.format(X * Y), end=' ')
        Y+=1
    print()
    Y=1
 
 
