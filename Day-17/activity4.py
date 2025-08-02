'''password=input("Enter the password:")
def password1(password):
	for char in password:		
		if any(c.isdigit() for c in password):
			digit=1 
		if len(password)>8 and digit and any(char.islower()) and any(char.isupper()) and any(not char.isalnum()):
			return "correct"
		else:
			return "Incorrect"
print(password1(password))'''




def password1(password):
	for char in password:
        	if char.isdigit():
        		digit = 1
        	elif char.islower():
            		lower = 1
        	elif char.isupper():
            		upper = 1
        	elif not char.isalnum():
            		special = 1	
	if len(password) > 8 and digit and lower and upper and special:
        	return "Correct"
	else:
    		return "Incorrect"
password = input("Enter the password: ")
print(password1(password))
