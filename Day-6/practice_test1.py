#getting input
list=input().split(',')

#extracting
extract=list[1:3] 

#reverse
reverse=extract[::-1]

#second number
second=reverse[::2]
combine=reverse+second

#multiply
print(combine*2)


