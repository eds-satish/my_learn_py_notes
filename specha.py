sp = "~!@#$%^&*()_+"
n = input('Enter the value of n: ')
r = ''
t = ''

for i in n:
    if i in sp:
        r = r+i
    else:
        t = t+i

print('string is: ', t)

print('*' * 20)

tar=''
spch=''

for i in range(0, len(n)):
    if not n[i].isalnum():
        n.strip(n[i])
        spch = spch+n[i]
    else:
        tar=tar+n[i]
 


print('String is: ', tar)
print('Special characters are: ', spch)

    
