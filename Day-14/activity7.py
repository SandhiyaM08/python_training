num1,num2=map(int,input("Enter two number:").split(','))
if num1%num2==0 or num2%num1==0:
	print("Larger")
else:
	print(num1+num2)