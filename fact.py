def fact(n):
    a = 1
    for i in range(1, n+1):
        a = a*i
    print(f"Factorial of {n} is {a}")
#OR    print("Factorial of {} is {}".format(n, a))

n = int(input("Enter the number to print it's factorial: n-> "))

fact(n)


