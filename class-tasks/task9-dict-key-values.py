
d = {'sachin': 'cricket',
     'david': 'football',
     'warne': 'cricket',
     'messi': 'football'}

print(d)

newdict = {}
for k, v in d.items():
    keys = newdict.setdefault(v, [])
    keys.append(k)

print(newdict)

print('type of newdict: ', type(newdict))
print('type of keys: ', type(keys))



