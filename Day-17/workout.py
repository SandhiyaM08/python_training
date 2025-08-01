'''x = 10 #global
def func1():
    y = 5 #local
    x= x + y  	
    print("x =", x)  
    print("y =", y)  
func1()
print(x)

x = 10 #global
def func1():
    y = 5 #local
    x=sum(x,y)	
    print("x =", x)  
    print("y =", y)  
func1()
print(x)

x="global"
def outer():
	def inner():
		print(x)
	x="enclosing"
	return inner
f=outer()
f()

def gen_odd(num):
	n=0
	while n<=num:
		if n%2==1:
			yield n
		n+=1
odd_num=gen_odd(10)
for i in odd_num:
	print(i)



def simple():
    for i in range(1, 6):
        yield i
for number in simple():
    print(number)'''


def simple():
	"""sandhi"""
	return "sandhiya"
print(simple.__doc__)


