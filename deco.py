#!/usr/bin/evn python 

from time import gmtime, strftime, ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print('{} {} called'.format(ctime(), func.__name__))
        print('returning func: ', func, end='\t')
        print('returning func(): ', func())
        return func()
    print('returing wrappedFunc: ', wrappedFunc)
    return wrappedFunc

print('entering the program: ') 
print('tsfunc address: ', tsfunc)


@tsfunc
def foo():
    print('I am in foo')

print('foo address: ', foo)
print('starting foo()...')
foo()
print('Sleep started....')
sleep(4)
print('Sleep ended....')
print('type is: ', type(foo))
print('ID is: ', foo)

print(''.center(20, '*'))
for i in range(0, 2):
    foo()
    sleep(1)

