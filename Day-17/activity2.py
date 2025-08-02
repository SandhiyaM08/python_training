'''def gcd(n1,n2):
	while n2!=0:
		n1,n2=n2%n1,n1%n2
	return n1
print(gcd(48, 18))'''

def gcd(n1,n2):
	while n2!=0:
		n1,n2=n2,n1%n2
	return n1
n1=int(input("Enter the first integer:"))
n2=int(input("Enter the second integer:"))
print(gcd(n1,n2))