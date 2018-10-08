#Program to given a count of each letter in a given string. Ex: mississippi ; m=1, i=3, s=4, p=2


"""
if s1[0] == s1[1] 
if s1[0] == s1[2]
if s1[0] == s1[3]
"""

s1 = 'mississippi'

f1_count=0
f2_count=0
master_count = 0

for f1 in s1:
    count = 0
    f1_count+=1
    for f2 in s1:
        f2_count+=1
        if f1 == f2:
            count = count + 1
    master_count += count
    print('Count of letter', f1, 'is: ', count)
print(f'f1_count is: {f1_count} and f2_count is: {f2_count} and master_count is: {master_count}')

"""
unique_letter = 0
if_found_flag == True then count-f1 = 1 == if_found_count < 1
if_found_flag == True then count-f2 = 1,1,1,1 == if_found_count > 1 
"""

s2 = s1
already_found = False

add = 0
dont_add = 0
add_to_basket = ''



for i in s1:
    if_found = 0
    for j in s1:
        if i == j:
            if_found += 1
            if if_found >= 1:
                already_found = True
                if already_found == True:
                    print('found the element', i)
                else:
                    already_found = False
    #if if_found == 1:
    print('count of letters are: ', if_found)
                


