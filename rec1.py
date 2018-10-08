import string
import new

def __str__(self):
    class_str = ''
    for name, value in self.__class__.__dict__.items() + self.__dict__.items(): 
        class_str += string.ljust(name, 15) + '\t' + str(value) + '\n'
    return class_str

def add_str(an_instance):
    an_instance.__str__ = new.instancemethod(__str__, an_instance, an_instance.__class__)

# Test it

class TestClass:
    class_sig = 'My Sig'
    def __init__(self, a=1, b=2, c=3):
        self.a = a
        self.b = b
        self.c = c

test = TestClass()
add_str(test)
print(test)
