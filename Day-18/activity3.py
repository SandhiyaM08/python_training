#return list square of even only

nums=[1,2,3,4,5]
print(list(map(lambda x:x**2,filter(lambda x:x%2==0,nums))))

#using list comprehension
nums=[1,2,3,4,5]
squares=[x**2 for x in nums if x%2==0]
print(squares)


