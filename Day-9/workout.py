'''scrambled in membership:
d={"a":1,"b":2}
keys=d.keys()
d["c"]=3
print(len(keys))
print(d.items())

#error
d={"a":1,"b":2}
keys=d.keys()
d["c"]=3
print(d.pop())

d={"a":1,"b":2}
print(4 in d)

d={"a":1,"b":2}
print('a' in d)

d={"apple":100,"orange":200}
print("papaya" not in d)

d=[{1:2,3:4}]
print(d)

#print
student={"a":{"math":95,"science":89},
"b":{"math":80,"science":92},}
print(student["b"]["science"])


d={"a":1,"b":2,[1,2]}
print(len(d)

#reference values
d={"x":10}
key_view=d.values()
d['y']=20
print(list(key_view))

#setdefault
config = {}
result = config.setdefault('database', {}).setdefault('connections', [])
result.extend(['mysql', 'postgres'])
config.setdefault('database', {}) ['port'] = 5432
print(len(config['database']), len(result))

o/p:2,2

#replace the b value
d={'a':10,'b':15}
d['b']+=5
print(d)

#popitem()

d={'a':10,'b':15}
d.popitem()
print(d)--->last item pop

#pop
d={'a':10,'b':15}
d.pop('a')
print(d)--->pops the key and value

#delete
d={'a':10,'b':15}
d.del['a']
print(d)


x=(1,2)
y=[1,2]
d={}
d[x]=10
d[y[0],y[1]]=20
print(d)

#clear
d={'x':5}
d2=d
d.clear()
print(len(d2))

d={'a':1,'b':2}
v=d.values()
d['c']=3
print(3 in v)

d={'a':1,'b':2}
v=list(d.values())
v.append(3)
print(len(d))


data=({'count':5},)
result=data*2
result[0]['count']+=10
result[1]['total']=25
print(result[0]['count'],result[1]['total'])'''

#update
# base={'u':{'p':{'n':'john'}}}
# update_data={'u':{'p':{'a':25},'s':{'t':'dark'}}}
# base['u'].update(update_data['u'])
# print(base['u']['p'])

fruit_prices = {100:"alpep", 80:"egnaro", 60:"ananab"}
fruit_name=sorted(input("enter the fruit name:"))
value=(fruit_prices)
print(fruit_name)
print(value)



