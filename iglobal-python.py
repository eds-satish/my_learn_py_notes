a = 'iglobal'
b = 'python'
count = 0
k = ''

for i in a:
    for j in b:
        k = i + j
        print(k, end=' ')
        count += 1

print()
print('No: of comibnations: ', count)

