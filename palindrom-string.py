
n = input('Enter any string to check for palindrome: ')
n1 = ''
n2 = ''


for i in n:
    n1 = n1+i

print('='*20)

for j in range(1, len(n)+1):
   # print('j is and xx: ',j, n[-j])
    n2 = n2+n[-j]   

    
    
print('n1 is: ', n1)
print('n2 is: ', n2)

if n1 == n2:
    print('String is palindrome: ', n1)
else:
    print('Not Palindrome')



