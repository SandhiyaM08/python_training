#write an function instead of sum()

number=[1,2,3,4]
def func1(number):
	add=0
	for item in number:
		add+=item
	return add
print(func1(number))