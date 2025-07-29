'''name=''
if name:
  print("hello,{name}")
else:
  print("false")'''

# age=20
# citizen=True
# if age>=18 and input():
#   print("Eligible")

# r=True or False and False
# print(r)

'''age=17
id=True
member=True
if age>=18 and id or member:
 	print("allowed")
else:
	print("denied")

age=20
status="adult" if age>=18 elif "kk" else "minor"
print(status)


age=20
status="adult" if age>=18 else "minor"
print(status)

data=[]
print(all(data),any(data))

values=["",[],0,None]
print(any(values),all(values))'''

# a=5
# r=~a
# print(r)

a,b=map(int,input("enter the number:").split(','))
if a%b==0 and b%a==0:
   print("larger")
else:
   print(a+b)