#!/usr/bin/env python

n = input('Enter the value of n: ')

k = n.split()
print('type of k is: ', type(k))
k.sort()
p = ' '.join(k)
print('Sorted sentence is: ', p)

print('*' * 25)
str_split = n.split()
length = len(str_split)
new_str = []

for i in range(0, length):
    m = min(str_split)
    ind = str_split.index(m)
    new_str.append(m)
    str_split.pop(ind)

tar_str = ' '.join(new_str)
print('Sorted string is: ', tar_str)

