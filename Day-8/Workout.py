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
print(a)'''

(a,(b,c))=(1,(2,3))
print(a,b,c)
















