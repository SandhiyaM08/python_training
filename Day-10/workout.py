'''#quiz1
a=[[0]*2]*3
a[0][0]=99
print(a)--->o/p:[99,0]

s1={1,2}
s2={1}
print(id(s1))
print(id(s2))

#checking datatype accepting in set
set1={1,2,(3,4),"hello",True,3.14,None,{1:2}}
print(set1)

#bool is accepted(without 0's and 1's)
set1={1,2,(3,4),"hello",True}
print(set1)

#complex accepted
set1={1,2,(3,4),"hello",True,3+4j}
print(set1)

#dict not accepted
set1={1,2,(3,4),"hello",True,{1:2}}
print(set1)

#set inside
s1={{1,2}}

data={1,2,3,3,4,4,5}
print(data)
print(len(data))
word=set(('programming','programming'))
print(word)
print(len(word))

#adding
fruits={'apple','banana'}
fruits.add('orange')
print(fruits)

#update values in dict(only key will update)
fruits={'apple','banana'}
fruits.update({'grape':100})
print(fruits)

fruits={'apple','banana'}
fruits.update(('grape,orange'))
print(fruits)

#update
fruits={'apple','banana'}
fruits.update(['grape','orange'])
print(fruits)

#discard
fruits={'apple','banana'}
fruits.discard('banana')
print(fruits)

#remove
fruits={'apple','banana'}
fruits.remove('grape')
print(fruits)

#pop
fruits={'apple','banana'}
fruits.pop()
print(fruits)

#clear
fruits={'apple','banana'}
fruits.clear()
print(fruits)

#memebership
colors={'red','green','blue'}
condition={'red' in colors,'yellow' not in colors}
print(condition)
o/p:only one time true

s=set("banana")
print(len(s))--->o/p:3

s={"banana"}
print(len(s))--->o/p:1

s={'a','b'}
s.update('cd',['e','f'])
print(sorted(s))
o/p:{'a','b','c','d','e','f'}

s=set()
print(s.pop())-->error

s={1,2,3}
s.remove(4)
print(s)

s={1,2,3}
s.discard(4)
print(s)

s={'x','y','z'}
s.discard('a')
print(len(s))

a=set()
a.update([1],(2,),{3})
print(len(a))-->o/p:3

a={1,2}
b=a
a.clear()
print(b)--->o/p:set()'''

x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x & y
result1=x and y
print(result)
print(result1)





