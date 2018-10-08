# Program to print the luck number of a given name:
#take the name;
na = input('Enter the name: ').lower().split()
names = ''.join(na)

#assign the numerical value of the alphabet
key_value_dict = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f':6,'g':7,
                  'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m':13,'n':14,
                  'o': 15,'p': 16,'q': 17,'r': 18,'s': 19 ,'t': 20,'u': 21,
                  'v': 22,'w': 23,'x': 24,'y': 25,'z': 26}

total = 0
if names.isalpha():
    for name in names:
        if name in key_value_dict.keys():
            total += key_value_dict[name]
else:
    print(f'Invalid name: {names}')


my_tot = str(total)

"""
single_tot = str(total)
lucky_sum = 0
if len(single_tot) >= 1:
    for single in single_tot:
        lucky_sum += int(single)
    

print(f"Given name is {names}; Total is: {total}; Lucky number is: {lucky_sum} ")
"""

def myrecur(my_tot):
   #print(f'myrecur.my_tot has been called with: {my_tot}')
   s1 = str(my_tot)
   luk1_sum = 0
   #print(f's1 is: {s1}')
   if len(s1) > 1:
       for single in s1:
           luk1_sum += int(single)
       #print(f'luk1_sum is: {luk1_sum}')
       my_tot = str(luk1_sum)
       print(f"nameee is: {names}; luckyyy no: {s1}")
       myrecur(my_tot)
   elif len(s1) == 1:
       print(f"nameee is: {names}; luckyyyy no: {s1}")
       pass
   else:
       print('end') 
  
   print(f'name is: {names}, lucky number is: {s1}')

myrecur(my_tot)
