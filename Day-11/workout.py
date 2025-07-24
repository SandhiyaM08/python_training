'''set1={1,2,3}
set2={1,2}
print(set1-set2)

s1={1,2,3}
s2={3,4,5}
s1.symmetric_difference_update(s2)
print(sorted(s1))

x=set()
y={1,2}
z=x^y
print(type(z),len(z))

a={1,2,3}
b=a
a|={4}
print(id(b),id(a))
print(len(b))

a={1,2,3}
b={1,2,3,4,5}
c={1,2}
print(a<b)
print(b<c)
print(a<c)
print(b<a)
print(c<a)
print(a<a)

a=set()
b={frozenset()}
c={frozenset(),frozenset({1})}
print(b.issubset(c))--->true

d={{1,2,3}:"set as"}
print(d)'''

d={frozenset([1,2,3]):"set as"}
print(d)

nest={{1,2},{3,4}}

