'''#armstrong number

def armstrong(number):
	num=str(number)
	while len(num)>3:
		for i in num:
			value=sum(num)**num
print(Armstrong(number))




    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    return total == number

# Example usage
num = int(input("Enter a number: "))
if armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")'''



def armstrong(number):
    digits = len(str(number))
    total = 0
    for digit in str(number): 
    	total += int(digit) ** digits
    return total == number
number=int(input("Enter number:"))
print(armstrong(number))
