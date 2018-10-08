import re
import sys
import os
import shutil
import io
import re_pattern.py 
#/root/mypython-root/test-dir

f = open('/root/mypython-root/test-dir/pattern.txt','r')
pat = f.readlines()
print('pattern :', pat)

print('pattern1: ', pat)
f.close()

k = open('/root/mypython-root/test-dir/pattern.txt','r')
st = k.read()
print('string: ', st)
print()
print('string1: ', st)
f.close()


