def compose_greet_func(name):
    def get_message():
        return "Hello there " + name 

    return get_message


greet1_fobj = compose_greet_func
greet = compose_greet_func("John")

print(id(compose_greet_func))
#print(id(compose_greet_func.get_message)) #AttributeError:

print(greet1_fobj)
print(greet)
print("Function object: {} + Id: {}".format(greet1_fobj, id(greet1_fobj)))
print("Inside Function obj: {}\nId: {}\nFunction Executed: {}".format(greet, id(greet), greet()))
#format(compose_greet_func, id(compose_greet_func))
#print("Function executed/Invoked: {}".format(greet))
#print("Inside Function object: {} + Id: {}".format(greet2_fobj, id(greet2_fobj))
#print("Inside Function executed/invoked: {}".format(greet2_ink))
