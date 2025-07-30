#give positive integer ,print triangle pattern of incerasing numbers

n=int(input("Enter the number:"))
num=1
for i in range(1,n+1):
	for j in range(i):
		print(num,end=' ')
		num+=1
	print()






