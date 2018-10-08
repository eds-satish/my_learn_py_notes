#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 18:35:53 2018

@author: root
"""

"""
def even_odd(A):
    next_even , next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[ next_even ] % 2 == 0:
            next_even += 1
        else:
            A[ next_even ], A[next_odd] = A[next_odd], A[ next_even ]
            next_odd -= 1
"""


def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[ next_even ] % 2 == 0:
            print(next_even)
            next_even += 1
        else:
            A[ next_even ], A[next_odd] = A[next_odd], A[ next_even ]
            print(next_odd)
            next_odd -= 1


#A=list(range(1,11))

A = list(range(1,11))
even_odd(A)


