#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 09:18:18 2018

@author: root
"""


mob = int(input('Enter a mobile number: '))
print(mob)
print('length is: ', len(str(mob)))
print('list is: ', list(str(mob)))
print('list first character is: ', list(str(mob))[0])
print('first character data type: ', int(list(str(mob))[0]))
print(type(int(list(str(mob))[0])))

"""
if len(str(mob)) == 10 and (int(list(str(mob))[0]) == 9 or int(list(str(mob))[0]) == 8 or int(list(str(mob))[0]) == 7):
    print('It is a mobile number')
else:
    print('Not a mobile number')
"""    

if len(str(mob)) == 10 and (int(list(str(mob))[0])) == 9 or (int(list(str(mob))[0])) == 8 or (int(list(str(mob))[0])) == 7:
    print('It is a mobile number')
else:
    print('Not a mobile number')
    
    



if len(str(mob)) == 10:
    print('10 is True')
else:
    print('10 is false')
    
if int(list(str(mob))[0]) == 9:
    print('9 is true')
else:
    print('9 is false')

if int(list(str(mob))[0]) == 8:
    print('8 is true')
else:
    print('8 is false')
    
if int(list(str(mob))[0]) == 7:
    print('7 is True')
else:
    print('7 is false')
    
