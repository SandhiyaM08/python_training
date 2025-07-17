#solution 1
x="426"
print(str(x[1]))

#solution 2
x = 426
middle_digit = (x // 10) % 10
print(middle_digit)

#print statement
print("Hello")
# #newline command
print("Hello,\n world")
#example of separators
print("16","07","2025",sep="-")
#instead of newline 'end'
print("sandhiya",end="...")
print("Done")
   
#split function
v1,v2,v3,v4=input("Enter three number:").split()
print(f'v1:{v1}\nv2:{v2}\nv3:{v3}\nv4:{v4}')

#split function
v1,v2,v3=map(int,input("Enter three integers:").split(','))
print(chr(v1),chr(v2))

#input 5,6
v1,v2=input("Enter two number:").split(',')
print(v1,v2)

x,y,z=map(int,input("Enter three number:").split(','))
print(x,y,z)

#index 0 in that first character
guests = ["Anitha", "Rahul", "Kiran","Meera"]
print(guests[0][0])

#extend
a=[1,2,3]
b=[3,4]
c=[5,6]
a.extend(b,c)

#index 0 in that third character
print()
list1=['Alice','Bob','Charlie','David']
print(list1[0].index('i'))


numbers=[123,287,9001]
numbers[2][3]=0
print(str(numbers))

#replace
numbers = [123, 287, 9001]
numbers[2] = int(str(numbers[2]).replace('0', '2'))
print(numbers)

#without square brackets
a=[1,2,3,4]
print(*a)


a=list("hello")
for val in a:
    print(chr(ord(val)-32),end="")


list1=['Alice','Bob','Charlie','David']
print(list1[0].index('i'))

num=[123,287,9001]
print(str(num[2]).index('0'))

#second occurence sol1
list=[1,2,3,4,2]
value=2
removed=list.remove(value)
removed=list.remove(value)
print(list)

#sol2
list=[1,2,3,4,2]
value=2
new_list=list[0],list[2],list[3]
print(new_list)

#return third value third index
num=[123,287,9001]
print(2*(num[2]==9001))

#sort()
num=[123,287,9001]
s=num.sort()
print(num)

list1=['Alice','Bob']
list2=['Charlie','David']
print(list1+list2)


num=[123,287,9001]
print(str(num[2]).index('0'))

#three list join
list1=['Alice','Bob']
list2=['Charlie','David']
list3=['Sandy','Muthu']
print(list1.extend(list2+list3))
print(list1)

#all capital
list=['Geeks','For','Geeks']
lst=[]
for val in list:
    set=''
    for value in val.lower():
        set+=chr(ord(value)-32)
    lst.append(set)   
print(' '.join(lst))
