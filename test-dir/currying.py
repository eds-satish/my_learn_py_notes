def carry(f):
    return lambda a: lambda b: f(a, b)


avg = lambda a, b: (a + b)/2
n1 = avg(1, 3)
print('avg: ', avg)
print('n1: ', n1)

avg1 = carry(avg)(1)
n2 = avg1(3)
print('avg1: ', avg1)
print('n2: ', n2)

curriedAvg = lambda a: lambda b: (a+b)/2
avg3 = curriedAvg(3)
n3 = avg3(3)
print('curriedAvg: ', curriedAvg)
print('avg3: ', avg3)
print('n3: ', n3)




