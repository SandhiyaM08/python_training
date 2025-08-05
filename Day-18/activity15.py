def numbers():
	num1=int(input("Enter numerator:"))
	while True:
		try:
			num2=int(input("Enter denominator:"))
			print(num1/num2)
			break
		except ZeroDivisionError:
			print("Cannot divide by zero!")
numbers()