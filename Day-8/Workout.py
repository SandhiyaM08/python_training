'''#updated
t=(1,2,'python',[1000,(1,2)])
t[3][0]=1
print(t)

#empty tuple not modified
t=(1,2,'python',[1000,tuple()]
print(t)

#empty tuple not modified
t=(1,2,1000,tuple(map(int,input("number:"))))
print(t)

#None values passing onside tuple
v1=print()
v2=(None,None)
print(v1,v2)
tuple(print(),)

#printing type
v1=print()
v2=tuple(type(v1))
print(v1," ",v2)

#type(type())
v1=print()
v2=type(type(v1))
v3=tuple(v2,)
print(v1," ",v2,v3)

#dynamically allocate values 
a,b,c=(input(),int(input()),input())
print(a,b,c)

a,b,c=map(int,input("Enter:").split(","))
print(a,b,c)

a,b,c=(12,34,input("Enter:")
print(a,b,c)

tuple1=(12,34,12)
print(min(tuple))

#tuple to list
tuple1=(1,2,3,4)
list1=list(tuple1)
print(list1)

number=1,2,3,4,5,6,7,8,9)
first,*middle,last=number
print(first)
print(middle)
print(last)

numbers=(input())
*first,middle,last=numbers
print(first,middle,last)

numbers=(input())
*first,middle,last=numbers
print(first,middle,last)
print(type(first))


#tuple of list of elements
number=tuple(input("Enter number:"))
*a,=number
print(a)
print(a[0])
print(type(a))
print(len(a))

number=1,2,3,4,5,6,7,8,9
first,*middle,last=number
print(type(first))
print(type(middle))
print(type(last))

#tuple unpacking

a=(1,2)
print(a)

(a,(b,c))=(1,(2,3))
print(a,b,c)

dictionary:
print(my_dict.get("email"))

#same key different values 
players={1:"dhoni",1:"kholi"}
print(players)--->o/p:1:"kholi"



d={1:'A',True:'B',1.0:'C'}
print(d)-->{1,'C'}

print(type({1:'a'}))
print(type({1,2}))

print(dict([(1,2,3)]))
print(dict([(1,2)]))

#None also accepted the key
d=dict()
d[None]='empty'
print(d)


players={1:"dhoni",2:"kholi"}
print(players[2])

#getting input from user
players={input():input()}

#getting input from user
players={input():input(),1:input()}

#getting input()
players={1:"dhoni",2:"kholi",3:"rohit"}
players[4]=input()
print(players)

#print()
players={1:"dhoni",2:"kholi",3:"rohit"}
players[4]=print()
print(players)--->None

#getting bool()
players={1:"dhoni",2:"kholi",3:"rohit"}
players[4]=bool()--->0
print(players)

#getting int()
players={1:"dhoni",2:"kholi",3:"rohit"}
players[4]=int()
print(players)--->0

#modify
players={1:"dhoni",2:"kholi",3:"Rohit"}
players[3]="sachin"
print(players)

#update
players={1:"dhoni",2:"kholi",3:"Rohit"}
players[4]="sachin"
print(players)

#deleting element
players={1:"dhoni",2:"kholi",3:"Rohit"}
del players[3]
print(players)'''

#poping element

players={1:"dhoni",2:"kholi",3:"Rohit"}
pop players[3]
print(players)












