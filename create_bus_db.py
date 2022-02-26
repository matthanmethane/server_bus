import ast as ast
from unicodedata import name
_list = []

with open('all.txt', 'r') as f:
    i = 0
    temp = {}
    for l in f:
        if i%2==0:
            temp['name'] = l.replace("\n","")
        else:
            temp['geocode'] = ast.literal_eval('('+l.replace("\n","")+')')
            _list.append(temp)
            temp = {}
        i+=1

dlist = [dict(t) for t in {tuple(d.items()) for d in _list}]
print(dlist)

nlist = {}
name_list = ['Campus Red','Campus Red Express 1','Campus Red Express 2','Campus Red Lunch Express','Campus Blue','Campus Blue Express 1','Campus Red Lunch Express','Campus Green','Campus Green Express 1']
with open('name_all.txt', 'r') as f:
    i = 0
    temp = {}
    bus_type = ''
    for l in f:
        if l.rstrip() in name_list and l.rstrip() != bus_type:
            bus_type = l.rstrip().replace("\n","").replace(" ","_").lower()
            nlist[bus_type] = []
        else:
            if i%2==0:
                nlist[bus_type].append(l.replace("\n",""))
            i+=1
            
print()
print(nlist)