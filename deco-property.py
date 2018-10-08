#Exmaple-1 https://docs.python.org/3/library/functions.html?highlight=property#property

class C:
    def __init__(self):
        """ This is __init__ docstring """
        self._x = None

    def getx(self):
        """ This is getter docstring """
        print("Returning getter self._x value: {}".format(self._x))

    def setx(self, value):
        """ This is setter docstring """
        self._x = value
        print("Returning setter self._x value: {}".format(self._x))

    def delx(self):
        """ This is del docstring """
        print("deleting now....")
        del self._x

    xy = property(getx, setx, delx, "I'm the 'x' property.")

c = C()
c.xy
c.xy = "I am 11 now"
del c.xy


#Example-2:

class Parrot:
    def __init__(self):
        self._voltage = 100000
    
    @property
    def voltage(self):
        """ Get the current voltage. """
        print("printing voltage: ", self._voltage)

pa = Parrot()
print(dir(pa))
print(type(pa))
pa.voltage
#pa.voltage() : this syntax with paranthesis () is used if @property is NOT used.
#pa.voltage   : this syntax without paranthesis () is used if @property is USED

#Example-3:

class D:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("printing getter: ", self._x)
    #   return self._x

    @x.setter
    def x(self, value):
        self._x = value
        print("printing setter: ", self._x)

    @x.deleter
    def x(self):
        print("in deleter now...deleting....")
        del self._x

dd = D()
dd.x
dd.x = "my value is set to 20 now"
del dd.x


