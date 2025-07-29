## input1,input2,input3=map(input("Enter the values:").split(','))
# if any[(input1,input2,input3)]==True:
# 	print('True')

input1,input2,input3=input("Enter the values:").split(',')
if any([input1,input2,input3]) and (input1+input2+input3==1) :
	print('Exactly one')
print("Nope")