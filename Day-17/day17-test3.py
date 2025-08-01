def func1(password,username,first_name,last_name):
	if (password==username):
		return "Enter the correct username"
	if password==first_name or password==last_name:
		return "Enter the correct password doesn't match with first_name"
	if len(password)<10:
		return "Enter atleast 10 characters"
	if not password.isalnum():
		return "Enter the alphanumeric"
	if password==password.lower() or password==password.upper():
		return "Enter the password that should be uppercase and lowercase"
	return password
print(func1("Muthumaniii","sdcf","sandhiya","abc"))

