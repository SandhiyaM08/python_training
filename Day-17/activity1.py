'''n=10
def fibonacci():
	for i in range(0,n):
		a==0
		b==1
		c==(n-1)+(n-2)
	yield f(n)
fib=fibonacci()
print(next(fib))
print(fibonacci())'''


#fibonacci endlessly
def fibonacci():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b
fib=fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))	


