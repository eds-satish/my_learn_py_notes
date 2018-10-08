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

