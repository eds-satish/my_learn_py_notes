
for i in range(1, 11):
    print(i)

n = [1,2,3,4,5,6,7,8,9,10]
print(n)

m = [1,7,3,9,10,4,5,2,6,8]
m.sort(reverse=True)
print(m)

m2_even=[]
m3_odd=[]
for j in m:
    if j%2 == 0:
        m2_even.append(j)
        m2_even.sort(reverse=True)
        index2 = m2_even.index(j)
        item2 = m2_even.pop(index2)
        print(item2)
    else:
        m3_odd.append(j)
        m3_odd.sort(reverse=True)
        index3 = m3_odd.index(j)
        item3 = m3_odd.pop(index3)
        print(item3)

#m2_even.sort(reverse=True)
#m3_odd.sort(reverse=True)
print(m2_even)
print(m3_odd)


