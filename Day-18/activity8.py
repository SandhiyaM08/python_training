#list of fruit create dictionary fruit name and value are length of those name
fruits=['apple','banana','cherry']
length={(fruit,len(fruit)) for fruit in fruits}
print(length)