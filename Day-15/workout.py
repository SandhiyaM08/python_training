'''if []==False:
	print("A")
if not []:
	print("B")



primes=[1,2,3]
for numbers in primes:
	print(f'{numbers} is prime)


#iterate over keys
scores={'A':95,'B':8,'C':9}
for name in scores:
	print(name)

#iterate over key-value pair
for name,score in scores.items():
	print(f'{name}:{score}') 

#iterate over unordered way
scores={'A':95,'c':8,'b':9}
for name in scores:
	print(name)
for name,score in scores.items():
	print(f'{name}:{score}')

#iterate using set (unorder)
colors={'red','blue','green'}
for color in colors:
	print(color)

#iterate using set (order)
colors={1,3,2}
for color in colors:
	print(color)


for i in range(2,2):
	print(i)

#continue example
for char in 'back-2-home':
	if not char.isalpha():
		continue
	print(char)

#loop for else using continue
for char in 'back-2-home':
	if not char.isalpha():
		continue
	print(char)
else:
	print("completed")

#loop for else using break
for char in 'back-2-home':
	if not char.isalpha():
		break
	print(char)
else:
	print("completed")


print(list(zip([1,2],['a','b','c'])))-->o/p:[(1,'a'),(2,'b')]'''


for i in range(2):
	for j in range(3):
		if j==1:
			break
		print(j,end='')--->00









