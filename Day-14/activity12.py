#print ascending if sorted ,descending if sorted in descending order else unordered

# numbers=map(int,input("Enter the numbers:").split(','))
# num1=list(numbers)
# if num1==num1.sort():
# 	print("Ascending")
# elif num1[::-1]==num1:
# 	print("Descending")
# else:
# 	print("Unordered")

numbers=list(map(int,input("Enter the numbers:").split(',')))
if numbers==sorted(numbers):
	print("Ascending")
elif numbers==sorted(numbers, reverse=True):
	print("Descending")
else:
	print("Unordered")