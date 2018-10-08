
def func1(ch):
    names = dict(
       Rajesh = "A",
        Raju = "B",
        Rao = "C",
        Reddy = "D")
    
    if (ch == "Rajesh"):
        print(names["Rajesh"])
    elif (ch == "Raju"):
        print(names["Raju"])
    elif (ch == "Rao"):
        print(names["Rao"])
    elif (ch == "Reddy"):
        print(names["Reddy"])
    else:
       print('Enter one of these names: Rajesh, Raju, Rao, Reddy')


#ch = input()
func1(input())
