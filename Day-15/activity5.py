#given integer programm subtracting 3 from n until becomes less than 0 print how many times it ran

n=int(input("Enter the number:"))
count=0
while n>=0:
	n-=3
	count+=1
print(count)