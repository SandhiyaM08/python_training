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
print(student["b"]["science"])'''


d={"a":1,"b":2,[1,2]}
print(len(d)
