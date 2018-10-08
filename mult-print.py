"""
2x1=2	3x1=3	4x1=4
2x2=3	3x2=6	4x2=8
2x3=6	3x3=9	4x3=12
2x4=8	3x4=12	4x4=16

>>> for i in range(1, 11):                                                                                                                                               
...     print('2x',i,'=',2*i, '3x',i,'=',3*i, '4x',i,'=',4*i, sep='\t')
...
2x      1       =       2       3x      1       =       3       4x      1       =       4                                                                                
2x      2       =       4       3x      2       =       6       4x      2       =       8                                                                                
2x      3       =       6       3x      3       =       9       4x      3       =       12        



>>> for i in range(3):
...     print('2x{0}={1}','3x{0}={1}','4x{0}={1}',sep='\t')
... 
2x{0}={1}       3x{0}={1}       4x{0}={1}
2x{0}={1}       3x{0}={1}       4x{0}={1}
2x{0}={1}       3x{0}={1}       4x{0}={1}
>>> 
>>> 
>>> for i in range(3):
...     print('2x{0}={1}'.format(1,2),'3x{0}={1}'.format(1,3),'4x{0}={1}'.format(1,4),sep='\t')
... 
2x1=2   3x1=3   4x1=4
2x1=2   3x1=3   4x1=4
2x1=2   3x1=3   4x1=4

>>> for i in range(1,3):
...     for j in range(1,11):
...         print(i, 'x', j, '=', i*j)



"""

'''
for i in range(1,3):
    for j in range(1, 11):
        print(i, 'x', j, '=', i*j, sep='\t')
'''     

"""
#It worked. And in below code i tried to remove the harcoding of 2, 3, 4
for i in range(1,11):
    print('2x{0}={1}'.format(i, i*2),'3x{0}={1}'.format(i, i*3),'4x{0}={1}'.format(i, i*4),sep='\t')

"""
n = '123'
print(n[0], n[1], n[2], sep='\t')
for i in range(1,11):
    #print('2x{0}={1}'.format(i, i*2),'3x{0}={1}'.format(i, i*3),'4x{0}={1}'.format(i, i*4),sep='\t')
    print('{0}x{1}={2}'.format(int(n[0]),i,i*int(n[0])),'{0}x{1}={2}'.format(int(n[1]),i,i*int(n[1])),'{0}x{1}={2}'.format(int(n[2]),i,i*int(n[2])),sep='\t')



