# Program to calculate PF value based on age input

def pf(a, b):
    if a>10 and a<30:
        pf = b * 0.08
        return pf
    elif a>=30 and a<60:
        pf = b * 0.1
        return pf
    else:
        print('invalid age')


age = int(input('Enter the age: '))
basic = float(input('Enter basic salary: '))

k = pf(age, basic)
print('The pf value is: ', k)


