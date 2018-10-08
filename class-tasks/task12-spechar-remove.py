n = input('Enter the value of n: ')

tar_str=''
sp_cha=''

for i in range(0, len(n)):
    if not n[i].isalnum():
        n.strip(n[i])
        sp_cha = sp_cha+n[i]
    else:
        tar_str=tar_str+n[i]
 


print('String is: ', tar_str)
print('Special characters are: ', sp_cha)

    
