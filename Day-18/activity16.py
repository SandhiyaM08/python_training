try:
	data=[1,2,3,45,6]
	index = int(input("Enter index: "))
	print(data[index])
	print("Found")
except IndexError:
	print("Out of bounds")