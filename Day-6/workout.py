# list=[2,'Raja',3,'Vimal']
print(list.sort())

#tuple expression
a=(5+4)
print(a)

#boolean
a=(True+4)
print(a)

#shift
a=(1>>5)
print(a)

list=[1,2,3]
tuple=(list[::-1])
print(tuple)

name=tuple("john")
print(name)

x=tuple(5,)
print(x)

t=((1,2),(3,4))
print(t[0])
print(t[0])
print(t[::-1])

particular index
tt=((1,2),(3,4),(5,6))
print(tt[-2][0])

adding without bracket
tuple1=(1,3)
tuple2=('a','b')
tuple3=tuple1+tuple2
print(*tuple)

#retrieving the index 
tuple1=(10,20,30,40,50,60,20)
print(tuple1.index(20))

tuple1=(10,20,30,40,50,60,20)
value=[:2]+[2:]
print(tuple1.count((value)))
print(value)


tuple1=(10,20,30,40,50,60,20)
value=tuple1[:2]+tuple1[2:]
print(value)

#min value
tuple1=(10,20,(30,40,(50,60)))
print(min(tuple1))

#max value
tuple1=(10,20,(30,40,(50,60)))
print(max(tuple1))

#performing arthemetic operation
x=(99,101,42,67)
print(min(x+(10,)))

#convert float to int
print(int(10.5))

#delete on tuple
t=(10,20)
del t
print(t)

#bank details
tuple1=(12344,'sandhiya','sky12234',1000,1200,2500)
new_tuple=tuple1[0],tuple1[1],tuple1[2],(tuple1[3]+tuple1[4]-tuple1[5]),tuple1[4],tuple1[5]
print(new_tuple)

#poping the index element
t=(10,20,30,40)
s=t.pop(0)
print(t)
