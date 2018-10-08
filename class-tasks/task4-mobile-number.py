"""
Task to chek if the given number is mobile number or not without using a counter variable like count.

Conditions to qualify for a number to be a mobile number:
1. Length must be 10
2. First digit of the number should start from 9, 8, or 7

Hints:
1. Formula to extract the first digit of the number. I used floor division (//)
and 10 power rasied to less than one of the given number so that it will give us the first digit.

"""
####### -- START -- #######

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


####### -- END -- #######    
