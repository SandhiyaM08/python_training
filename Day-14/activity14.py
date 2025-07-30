#print "truthy" when passed to bool() after type conversion the value is true 

number=input("Enter the number:")
if number== 0 or number =='False' :
	print("Truthy")
else:
	print("Falsy")