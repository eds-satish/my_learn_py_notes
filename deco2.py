#!/usr/bin/evn python 

from time import gmtime, strftime, ctime, sleep

def tsfunc(func):
    def wrappedFunc():
        print('I am in wrappedFunc')
        print('{} {} called'.format(ctime(), func.__name__))
        return func()
    print('I am in tsfunc')
    return wrappedFunc


@tsfunc
def foo():
    print('I am in foo')
    

for i in range(0, 3):
    foo()
    sleep(1)

