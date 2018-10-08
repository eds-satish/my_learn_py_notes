"""def FirstFactorial(num):
    num1 = int(num)
    if num1 > 18:
        return print('Enter integer less than 18')
    else:
        num2 = 1
        for a in range(1, num1):
            num2 = num2 * (num1 - a)
            # num3 = num3 * num-1
    return num2 

FirstFactorial(input())
"""

"""
import math
def FirstFactorial(num):
    if num == 0:
        return print('Factorial of zero is: ', 1)
    elif num > 18:
        return print('Number must be within 18')
    else:
        num = math.factorial(num)
    return num

print(FirstFactorial(int(input())))
"""

def FirstFactorial(num): 

  factorial = 1
  
  for i in range(1, num+1):
    # multiply each number between 1 and num  
    # factorial = 1 * 1 = 1
    # factorial = 1 * 2 = 2
    # factorial = 2 * 3 = 6
    # factorial = 6 * 4 = 24
    # ...
    factorial = factorial * i

  return factorial

print(FirstFactorial(4))
