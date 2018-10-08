
#Program to check if the given number is even or odd.

def even_or_odd():
    ''' Program to check if the given number is even or odd. '''
    n = int(input('Enter a number, n-->: '))
    if n%2 == 0:
        print(n, 'is an even number')
    else:
        print(n, 'is an odd number')
    
    print('--- END ---')


#Program to print all prime number

def prime_number():
    ''' Program to print all prime number in a given range. Hint: Prime has only two factors, so count them using counter. '''

    n = int(input("Enter any number to see all the primes within it's range, n-->: "))
    
    for i in range(1, n+1):
        count = 0 #this is the hint. Reinitialize the counter at the beginning of the new number.
        #print('Iteration no i->: ', i)
        for j in range(1, i+1):
            #print('Iteration no j->: ', j)
            if i%j == 0: #Hint: this finds all the factorials i.e. divisors. If the divisors after dividing give a zero, it is a factor or else it is not.
                #print('i%j-: ', i%j)
                count+=1
                #print('count is->:  ',count)
                
        if count == 2:   #Hint: we need the total number of iterations of a given number, so checking the condition at first loop's level.
            print(i, 'is prime')
        else:
            print(i, 'is not prime')

    print('--- END ---')


#Program to do a continuous and also unique split of a given string

def continuous_unique_split():
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
    
    print('--- END ---')

#Program to print combination of letter in a given string with and without duplicates removed.

def combination_of_letters():
#Program to print combinaitons of letter from two strings
# 1. iglobal 2. python ; produce all the combinations
# using string concatenation symbol 
# remove duplicates: Hint: which line is producing the duplicate, register is at one place, now compare  and how can you separate it.
# Made it generic to work for any string, will also work for oracle and orange string combination
# test: give: aaaa & aaaa de-duplicate must be just: aa original: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#a = 'iglobal'
#b = 'python'
    a = input('Enter any stringA: ')
    b = input('Enter any stringB: ')
    k = ''
    m = ''
    dup = ''
    count = 0
    count1 = 0
    for i in a:
        for j in b:
            k = i+j
            if k not in m:
                print(k, end=' ') #these lines will only register non-duplicates. So print this statment.
                count1 = count1 + 1
                dup = dup + k
            #print(k, end=' ')   #these lines would register every combination
            count = count + 1
            m = m+k

    print()
    print('printing last word i+j: ', k)
    print('printing original combination: ', m)
    print('printing de-duplicated combination: ', dup)
    print('No: of comibnations are before: ', count, 'After dedupe: ', count1)
    print('--- END ---')


#Program to check whether a given number is a mobile number or not

def task_mobile_number():
    """
    Task to chek if the given number is mobile number or not without using a counter variable like count.

    Conditions to qualify for a number to be a mobile number:
    1. Length must be 10
    2. First digit of the number should start from 9, 8, or 7

    Hints:
    1. Formula to extract the first digit of the number. I used floor division (//)
    and 10 power rasied to less than one of the given number so that it will give us the first digit.

    """

    mob = int(input('Enter a mobile number: '))
    length = len(str(mob))
    ten_power = (length - 1)
    first_digit = (mob // 10 ** ten_power)

    if first_digit == 9 or first_digit == 8 or first_digit == 7:
        if length == 10:
            print('It is a Mobile Number')
        else:
            print('Length is ', length, ' Not a mobile number')
    else:
        print('Number starting with', first_digit, 'is not a mobile number')

    print('--- END ---')


#Program to print multiplication tables in a tabbed/horizontal view.

def mult_table_worked():
    # Very specific experimented 
    x = 1
    y = 1

    for x in range(1, 11): #for is getting printed horizontally
        while y <= 10:   #while is also getting printed horizontally 
            print(y, 'x ', x, '= ', x*y, end='\t')
            y += 1
        print()
        y=1

    print()

    #Printing the tables till a choosen number.
 
    n = int(input('Enter any number to print tables: n--> '))
    w = 1

    for nn in range(1, 11):
        while w <= n:
            print(w, 'x', nn, '=', w*nn, end='\t')
            w += 1
        print()
        w = 1
    
    print('--- END ---')     



def showmenu():
    prompt = """
1. even_or_odd
2. prime_number
3. continuous_unique_split
4. combination_of_letters
5. task_mobile_number
6. mult_table_worked

Enter choice: """
    print(prompt, end=' ')
    choice = int(input())
    return choice

"""
#Hint: You can keep a dict of all functions and any other modules as another switcher
#Instead of declaring globally, i declared it locally inside the dictionary_showmenu()

switcher = {
       1: even_or_odd,
       2: prime_number}
"""       

def dictionary_showmenu():
    switcher = {
           1: even_or_odd,
           2: prime_number,
           3: continuous_unique_split,
           4: combination_of_letters,
           5: task_mobile_number,
           6: mult_table_worked}
    
    return switcher


if __name__ == '__main__':
#    even_or_odd()
#    prime_number()
    
    my_choice = showmenu()
    print('You chose: ', my_choice)

    my_switcher = dictionary_showmenu()
    print('You chose switcher: ', my_switcher.get(my_choice, 'no_key_found')) #check the syntax of get function of dict
    
    
    my_function = my_switcher.get(my_choice, 'Function does not exist')
    print('Now running the function.....: ')
    
    if my_switcher.get(my_choice, 'no_key_found') == 'no_key_found':
        print('Function does not exist....choose the correct number')
    else:
        my_function()
    

    



