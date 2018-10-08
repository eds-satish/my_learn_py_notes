## iglobal = Continuous combination is: ig gl lo ob ba al l
## iglobal = Unique combination is: ig lo ba l
"""
#First tried it out by hardcoding

a = 'iglobal'
split_by = 2

Making it generic by take the input() from user

"""

a = input('Enter a string: ')
split_by = int(input('Enter the split_by no: to split: '))
cont_split = ''
unique_split = ''
cont_list = []
uniq_list = []


#Method1: Continuos split
for i in range(len(a)):
    print(a[i:i+split_by], end=' ')
    cont_split = cont_split + a[i:i+split_by] + ' '
    cont_list.append(a[i:i+split_by])


## Method2: Unique split #Hint: put down on paper and calculate no: of iterations, move_by steps direction, and index/split_by
for i in range(0, len(a), split_by):  #the change is the move_by how many elements i.e given my step argument in range() function
    #print(a[0:2], end=' ')
    print(a[i:i+split_by], end=' ')
    unique_split = unique_split + a[i:i+split_by] + ' '
    uniq_list.append(a[i:i+split_by])

print()
print('Output for Continuous split: ', cont_split)
print('Output for Continous split: ', cont_list)
print('Output for Unique split: ', unique_split)
print('Output for Unique split: ', uniq_list)




