
def logged(func):
    def func1():
        return 'you called: ', func 
    return 'it returned: ', func1

@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4)
print('id of a: ', id(a))
print('repr of a: ', repr(a))
print('type of a: ', type(a))

print('id of func: ', id(func))
print('repr of func: ', repr(func))
print('type of func: ', type(func))

print(a)
print(func)
print('=='*20)

#func = logged(func)
print('id of logged: ', id(logged))
print('repr of logged: ', repr(logged))
print('type of logged: ', type(logged))

print('id of func-returned: ', id(func))
print('repr of func-returned: ', repr(func))
print('type of func-returned: ', type(func))




