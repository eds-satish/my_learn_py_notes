# syntax while

"""
while (condition):
    block of code

while is basically an infinite loop

when the while breaks
1. you can manually break it
2. you must write a code inside which will make this condition false sometime later down the line
3. RAM is completely filled up with output

break ctrl+c : in python it will show you the line line before breaking out

"""

"""
program to print fibonacci series

#0 1 1 2 3 5 6 13 21 34 55 89


"""

a = int(input('enter the value for a: '))
b = int(input('enter the value for b: '))
n = int(input('enter the value of n to end the series: '))

print(a, end=' ')
print(b, end=' ')

while n > 0:
    c = a+b
    print(c, end=' ')
    a = b
    b = c
    n = n - 1
   
print('\n')
    








