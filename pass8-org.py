n = input('Enter any password: ')     #'w3IDsat@2018'

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
print('Counts are: ', count_a, count_A, count_num, count_spch)
print('*'*23)
 
if count_a >=1 and count_A >= 1 and count_num >=1 and count_spch >= 1:
    print('Valid password.....Accepted')
else:
    print('invalid password')

    
