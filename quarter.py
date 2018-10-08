#Program to print quarter number based on month ouput

def quarter(n):
    if n == 'jan' or n=='feb' or n == 'mar':
        print('quarter-1')
    elif n == 'apr' or n=='may' or n=='jun':
        print('quarter-2')
    elif n=='jul' or n=='aug' or n=='sep':
        print('quarter-3')
    elif n=='oct' or n=='nov' or n=='dec':
        print('quarter-4')
    else:
        print('Invalid month')

#My program using lists

def myquarter(n):
    q1 = ['jan', 'january', 'feb', 'february', 'mar', 'march']
    q2 = ['apr', 'april', 'may', 'jun', 'june']
    q3 = ['jul', 'july', 'aug', 'august', 'sep', 'september']
    q4 = ['oct', 'october', 'nov', 'november', 'dec', 'december']

    if n in q1:
        print('myquarter-1')
    elif n in q2:
        print('myquarter-2')
    elif n in q3:
        print('myquarter-3')
    elif n in q4:
        print('myquarter-4')
    else:
        print('Invalid month or check the correct spelling')




n = input('enter the value of n: ').lower()

quarter(n)    #sir's function 

myquarter(n)  #my function




