n = int(input('Enter any number between 1 to 10: '))

for i in range(1, n+1):
    if i <=2:
        for j in range(1, i+1):
            print(i, end=' ')
    else:
        for j in range(1, 4):
            print(i, end=' ')

    print()

print('='*30)

for a in range(1, n+1):
    for b in range(1, a+1):
        print(a, end=' ')

    print()

