# Very specific experimented 
x = 1
y = 1

for x in range(1, 11): #for is getting printed horizontally
    #print(xx, end='\t')
    while y <= 10:   #while is also getting printed horizontally 
        print(y, 'x ', x, '= ', x*y, end='\t')
        y += 1
    print()
    y=1

print()

#Printing the tables till a choosen number.
 
n = int(input('Enter any number to print tables: n--> '))
w = 1

for nn in range(1, 11):
    while w <= n:
        print(w, 'x', nn, '=', w*nn, end='\t')
        w += 1
    print()
    w = 1     
