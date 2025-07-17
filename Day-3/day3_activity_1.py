#Qus greater number:

#opt1:
#declaring values
v1=2
v2=3
#creating tuple
val=(v1,v2)
#true[1],false[0]
ind=(v1<v2)
print(val[ind])


#opt2:
a, b = 4, 5
bigger = a * bool(a > b) + b * bool(b > a)
print("The bigger number is:", bigger)

#opt3:
a, b = 2,3
bigger = sorted([a, b])[-1]
print("The bigger number is:", bigger)

#solution:
a=2
b=3
print("v1 is bigger than v2-the statement is",{v1>v2})