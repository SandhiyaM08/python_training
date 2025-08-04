'''x=2
y=3
print(lambda x,y:x*y)

multiply=lambda x,y:x*y
print(multiply(3,4) is 12)

#error
f=lambda x:return x*2
print(f(3))

#42 no error
f=lambda:42
print(f())

#error
f=lambda x:x+2,x*2
print(f(3))

#return tuple value
f=lambda x:(x+2,x*2)
print(f(3))

my_list=[1,2,3,4,5]
result=list(map(lambda x:x**2,my_list) if x%2==0 )
print(result)

#even print square odd cube
my_list = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2 if x % 2 == 0 else x**3, my_list))
print(result)


my_list=(1,2,3,4,5,6,7,8,9,10,101)
result=list(filter(lambda x:x%2==0,my_list))
print(result)

#prime numbers
my_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 101)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
result = list(filter(lambda x:is_prime(x), my_list))
print(result)

from functools import reduce
my_list=(1,2,3,4,5)
result=reduce(lambda x,y:x*y,my_list)
print(result)


#multiply every number if repeat it should not multiply
from functools import reduce
my_list=[1,2,3,3,4,5,7,7]
unique_list = list(set(my_list))
result=reduce(lambda x,y:x*y,unique_list)
print(result)

#printing the square of odd number
square=[x*x for x in range(6) if x%2==0]
print(square)

#printing the square of odd number
square=[x*x for x in range(6) if x%2!=0]
print(square)

#printing the square of prime number
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
square = [x*x for x in range(6) if is_prime(x)]
print(square)

lst=[1,2,3,4,5,6,7]
value=['even' if x%2==0 else 'odd' for x in range(5)]


lst = [1, 2, 3, 4, 5, 6, 7]
labels = ['even' if x % 2 == 0 else 'odd' for x in lst]
for num, labels in zip(lst, labels):
    print(f"{num}: {label}")

#order matters 
pairs=[(x,y) for y in range(2) for x in range(3)]
print(pairs)

square={x : x**2 for x in range(10) if x%2!=0 else 0}
print(square)

#square root of odd number
square={x : x**0.5 for x in range(10) if x%2!=0}
print(square)

#dicitionary
data=[('a',1),('b',2),('c',3)]
print({k:v for (v,k) in data})

lst=['one','two','three']
result = {i + 1: v for i, v in enumerate(lst)}
print(result)

lst=['one','two','three']
result = {i: v for i, v in enumerate(lst,start=1)}
print(result)

#3loop in dict
c={(x,y):x*y for x in range(2) for y in range(2) for z in range(2)} 
print(c)

#generator
squares=(x*x for x in range(5))
print(squares)
print(next(squares))
print(list(squares))'''

#try and except:
try:
	v1=int(input("enter integer value"))
except ValueError:
	v1=int(input("enter the correct numeric value"))
	print(v1)


You have a list of students, each with a list of scores. Create a dictionary mapping the names of students who have an average score of 90 or higher to their average score.
Concepts: nested list, list of dict, filter, map, lambda, dictionary comprehension.


 
 














 
	