#empty dictionary
d1=()
d2=dict()
print(type(d1),type(d2))

#acesiing  values using keys
d3={'a':1,3:'codegnan'}
print(d3['a'])

#adding or updating the items
d4={'language':'python'}
d4['language']='java'
print(d4)

#dictionary methods
#keys(),values(),items()
d5={'language':'python','version':'3.13.5','level':'high level'}
keys=d5.keys()
values=d5.values()
items=d5.items()
print(keys)
print(values)
print(items)
#a,b=list((items)[1])
#a,b=items_list[1]
#print(a,b)

#pop(key),pop(item)
d6={'language':'python','version':'3.13.5','level':'high level'}
val=d6.pop('level')
print(val)
#items=d6.pop(items('3.13.5'))
#print(items)
#print(d6)

#update(),clear()
d7={'language':'python','version':'3.13.5','level':'high level'}
d8={'language':'java','version':'3.13.5','level':'high level'}
d7.update(d8)
print(d7)
print(d8)

#clear()
d9={'language':'python','version':'3.13.5','level':'high level'}
d9.clear()
print(d9)


   


