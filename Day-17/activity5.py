'''num=int(input("Enter the number:"))
def prime(num):
	while num>=1:
		for num in range(2,int(num**0.5)+1):
			for i in range(num,1001):
				if num%i==0:
					return False
				else:
					return True
print(prime(num))



num = int(input("Enter the number: "))

def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime" if prime(num) else "Not Prime")'''



num = int(input("Enter the number: "))

def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
found = False
for i in range(num + 1, 1001):
    if prime_num(i):
        print(i)
        found = True
if not found:
    print("Not found")



			