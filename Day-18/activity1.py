x=2
print(lambda x:x**2)

square=lambda x:x**2
print(square(2)) #without variable x

#function
def square(num):
	val=lambda x:x**2
	return val(2)
print(square(2))

