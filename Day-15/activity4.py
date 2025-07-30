#star pyramid

n=int(input("Enter the number:"))
for i in range(1,n+1):
	print(' '*(n-i) + '*'*((2*i-1))


solution:
'''n=int(input("Enter the number:"))
for i in range(1,n+1):
	print(' '*(i-n) + '*'*(i*2)-1)'''