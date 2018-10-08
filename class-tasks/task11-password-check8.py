def uid1():
    u = input('Enter username: ')
    if u.isalnum():
        pass1()
    else:
        print('Invalid Username'.center(30,'*'))

def pass1():
    n = input('Enter any password: ')     #'w3EMMsat@2018'
    length = len(n)
    count_a=0
    count_A=0
    count_num=0
    count_spch=0
    for i in range(0, length):
        print(n[i], end='')

        if n[i].islower():
            count_a+=1
        elif n[i].isupper():
            count_A+=1
        elif n[i].isnumeric():
            count_num+=1
        elif not n[i].isalnum():
            count_spch+=1

    print()
    print('Counts are: small_letters: {0}, capital_letter: {1}, numbers: {2}, special_char: {3}'.format(count_a, count_A, count_num, count_spch), 
          'pwd length is: ', length)
    print('*'*23)
 
    if length >=8 and count_a >=1 and count_A >=1 and count_num >=1 and count_spch >=1:
        print('Valid password.....Accepted')
    else:
        print('invalid password')
    
    print('END'.center(30, '*'))
        
#### Main program starts here. Above are the functions. #####
uid1()
#pass1()
