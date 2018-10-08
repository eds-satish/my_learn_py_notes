#!/usr/bin/env python
#Program to sort the words in a given sentence without using the 'sort' function.

n = input('Enter the value of n: ').lower()
str_split = n.split()
length = len(str_split)
new_str = []

for i in range(0, length):
    m = min(str_split) #gets you the word according to the ASCII value
    ind = str_split.index(m)
    new_str.append(m)
    str_split.pop(ind)

tar_str = ' '.join(new_str)
print('Sorted string is: ', tar_str)

