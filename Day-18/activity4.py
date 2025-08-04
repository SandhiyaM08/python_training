#list of tuple use lambda to sort score in descending and name if score are equal
data=[('Alice',90),('Bob',75),('Charlie',90),('Dave',60)]
sorted_data=sorted(data,key=lambda x:(-x[1],x[0]))
print(sorted_data)

'''data=[('Alice',90),('Bob',75),('Charlie',90),('Dave',60)]
sorted_data=sorted(data,key=lambda x:x,reverse=True)
print(sorted_data)'''

