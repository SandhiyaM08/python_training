'''def greet(name):
	print(f"Hello,{name}")
greet("sandhiya")

def greet(name):
	if name=="sandhiya":
		return "yes"
def greet1():
	return "sand"
print(greet("sandhiya"))

#function returns 
def stats(x,y):
	return x+y,x*y
print(stats(2,5))
print(type(stats(2,5)))
v1=stats(3,5)
print(v1,type(v1))

def stats1(x):
	return x*x
print(stats1(2),type(stats1(2)))


def add_numbers(a, b):
	total = sum(numbers)
	return total  	
my_list = [10, 20, 30, 40]


#cant return assign value
def test():
	return x=5
print(test())

#positional
def divide(num,deno):
	return num/deno
print(divide(2,10))

#keyword argument
def divide(num,deno):
	return num/deno
print(divide(num=10,deno=2))
print(divide(deno=2,deno=10))

def divide(num,deno):
	return num/deno
print(divide(num=10,deno=2))
print(divide(2,deno=10))

#default parameter follows parameter with default
def greet(time="morning",name):
	print(f"good{time},{name}")
greet("alice")
greet("b","c")



def ex_list(val,lst=[]):
	lst+=[val]
	return lst
v1=(ex_list(1))
v2=ex_list(2,[])
v3=(ex_list(3))
v4=(ex_list(4))
print(f"{id(v1)},{v1},{id(v2)},{v2},{id(v3)},{v3},{id(v4)},{v4}")


def total(*args):
	print(args)
	return sum(args)
print(total(2,6))
print(total(10))
print(total())


def foo(args):
	print(args)
foo([1,2,3])

def foo(*args):
	print(args)
foo(1,2,3)

#error dictionary
def show(**kwargs):
	print(kwargs)
show("nam",age=30)'''

def tag(*args,**kwargs):
	print("[log]:",*args,**kwargs)
tag("Hello","world",sep="~",end="$$\n")







	














	