
def gcd(n1,n2):
	while n2!=0:
		n1,n2=n2,n1%n2
	return n1
def lcm(n1,n2):
	return abs(n1*n2)//gcd(n1,n2)
n1=int(input("Enter the first integer:"))
n2=int(input("Enter the second integer:"))
print(lcm(n1,n2))



'''def lcm(n1,n2):
	while n2!=0:
		n1,n2=n2,n1%n2
		lcm1=abs(n1*n2)//n1
	return lcm1
print(lcm(4,6))


def gcd(n1, n2):
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return n1

def lcm(n1, n2):
    return abs(n1 * n2) // gcd(n1, n2)

print(lcm(4, 6))''' 
