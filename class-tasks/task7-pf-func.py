# Program to calculate PF value based on age input

def pf(a):
    
    #a = int(input('Enter age: '))
    while True:
        if a < 10 or a > 60:
            print('Invalid age')
            a = int(input('Enter correct age between 10 and 60: '))
        else:
            b = float(input('Enter basic salary: '))
            break 
    if a>=10 and a<30:
        pf = b * 0.08
    elif a>=30 and a<=60:
        pf = b * 0.1
    else:
        print('passsssss')
    
    return pf

age = int(input('Enter the age: '))
#basic = float(input('Enter basic salary: '))

k = pf(age)
print('The pf value is: ', k)


