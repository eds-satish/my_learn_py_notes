n = '1234'
print(n[0], n[1], n[2], sep='\t')

m = len(n)
i = 0


while m>0:
#    for j in range(1,11):
#        print(n[i], 'x', j, '=', int(n[i])*j, sep=' ', end=' ')
    print(n[i],'x', n[i], '=', n[i], end='\t')
    m -= 1
    i += 1
#    print('m value inside loop is: ', m)
#    print('i value inside loop is: ', i)

#print('m value is after exit of loop: ', m)

print()

p = 1
while p<11:
    print('   ', p)
    p += 1


xx = 1
yy = 1

for xx in range(1, 11):
    #print(xx, end='\t')
    while yy <= 10:
        print(yy, 'x ', xx, '= ', xx*yy, end='\t') 
        yy += 1
    print()
    yy=1
 
