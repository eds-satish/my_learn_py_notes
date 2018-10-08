
class SumClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        

    def mysum(self, aa, bb):
        print('Sum is: ', aa + bb, 'another sum is: ', self.a + self.b)

    def mysub(self):
        print('Subtraction is: ', self.a - self.b)

    def mymul(self):
        print('Multiplication is: ', a * b)


a = int(input('Enter the value for a: '))
b = int(input('Enter the value for b: '))


s = SumClass(a, b)
s.mysum(10, 20)
s.mysub()
s.mymul()



