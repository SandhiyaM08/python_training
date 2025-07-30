#print multiplication table from 1 to n both rows and columns

n=int(input("enter the number:"))
for i in range(1,n+1):
	for j in range(1,n+1):
		print(i*j,end=' ')
	print()


