try:
	num1=int(input("Enter numerator:"))
	num2=int(input("Enter denominator:"))
	print(num1/num2)
except ZeroDivisionError:
	print("Cannot divide by zero!")
