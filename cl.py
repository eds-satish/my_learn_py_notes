class myC():
    def __init__(self):
        print("printing from __init__ def")
    print("my class myC")

print('1. ', myC)
print('2. ', myC())
id(myC)
id(myC())
print(type(myC))
print(type(myC()))
#print('3. ', myC)
#print('4. ', myC())

c_inst = myC
print('5. ', c_inst)
print('6. ', c_inst())
id(c_inst)
id(c_inst())
type(c_inst)
type(c_inst())
print('7. ', c_inst)
print('8. ', c_inst())

c_inst2 = myC()
print('9. ', c_inst2)
#print(c_inst2())
id(c_inst2)
#id(c_inst2())
type(c_inst2)
#type(c_inst2())
print('10. ', c_inst2)
#print(c_inst2())
