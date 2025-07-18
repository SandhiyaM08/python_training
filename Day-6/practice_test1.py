'''
Given a list of numbers, extract every 3rd element starting from index 1,
reverse it, then combine it with
every 2nd element from the original list starting from index 0.
Finally, multiply the entire result by 2.'''

#getting input
list=list(map(int,input().split(',')))

#extracting
extract=list[1::3] 

#reverse
reverse=extract[::-1]

#second number
second=list[::2]
combine=reverse+second

#multiply
print(combine*2)


