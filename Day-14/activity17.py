# #input string is equal to its reverse print 'mirror' else 'broken' without slicing 
# string1=input("Enter the string:")
# string2=list(string1)
# string2.reverse()
# if (list(string1)==string2):
# 	print("Mirror")
# else:
# 	print("Broken")

string1=input("Enter the string:")
string2=''.join(reversed(string1))
if (string1==string2):
	print("Mirror")
else:
	print("Broken")

