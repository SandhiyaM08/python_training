a,b=map(int,input("enter values:").split(','))
t=a^b
a=t^a
b=t^b
print("a:",a)
print("b:",b)