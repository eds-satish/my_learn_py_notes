#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:19:03 2018

@author: root
"""
#reminder = 8008003988 % 10
#number_reduces_by_one_digit = 8008003988 // 10


n = int(input('Enter mobile number: '))
count = 0

while n>0:
    p = n%10
    n = n//10
    count = count + 1
    
    
print('p = ', p, 'n = ', n, 'count = ', count)
print(bool(count == 10 and p == 9 or p == 8 or p == 7))

# Wrong output is coming when we give number starting with 9,8,7 but not 10 digits

if count == 10 and p == 9 or p == 8 or p == 7:
    print('Mobile number')
else:
    print('Not a mobile number')
'''    

if p == 9 or p == 8 or p == 7:
    if count == 10:
        print('Mobile number')
    else:
        print('Not a mobile number')
else:
    print('not a mooooooobile nuuuu')
'''
