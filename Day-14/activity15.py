#print exactly one is odd

value1,value2=map(int,input("Enter the values:").split(','))
if (value1%2==0 or value2%2==0):
	print("Exactly one is odd!")

val1,value2=map(int,input("Enter the values:").split(','))
if (val1%2 != value2%2):
	print("Exactly one is odd!")