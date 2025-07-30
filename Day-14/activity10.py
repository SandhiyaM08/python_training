#two string if they are equal(case-insensitive) print match else no match

string1=input("Enter the first string:")
string2=input("Enter the two string:")
if string1.lower() == string2.lower():
	print("Match")
else:
	print("No match") 