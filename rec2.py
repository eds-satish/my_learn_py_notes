n = 10
for i in range(n+1):
    if i%2 == 0:
        print(i, 'is even')
    elif i%2 != 0:
        print(i, 'is odd')
    else:
        pass

m = 10
l =  []
l1 = []
for j in range(m+1):
    if j%2 == 0:
        l.append(j)

    if j%2 != 0:
        l1.append(j)

print(l, 'is even')
print(l1, 'is odd') 


abc = 10
for ab in range(abc):
    if ab%2 == 0:
        print(ab, 'is even')
        continue

    if ab%2 != 0:
        print(ab, 'is odd')



