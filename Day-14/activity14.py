#print "truthy" when passed to bool() after type conversion the value is true 

number=input("Enter the number:")
if number and bool(number):
	print("Truthy")
else:
	print("Falsy")