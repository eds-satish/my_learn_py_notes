'''
0 is even
2 is even
4 is even
6 is even
8 is even


1 is odd
3 is odd
5 is odd
7 is odd
'''

even = []
odd = []

for i in range(11):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
print('\n')

for l in range(1, 2):
    for j in range(0, 11):
        if j%2 == 0:
            print(j, 'is even')
    print('\n')
    
    for j in range(0, 11):
        if j%2 !=0:
            print(j, 'is odd')
    print('\n')
    
    
for a in range(0, 11):
    if a%2 == 0:
        print(a, 'is even')

for b in range(0, 11):
    if b%2 !=0:
        print(b, 'is odd')




for n in range(0, 11):
    if n%2 == 0:
        print(n, 'is evennnnn')
else:
    print(n, 'is oddddddd')
