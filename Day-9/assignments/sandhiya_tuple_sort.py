data = [('A', 1, 2),('B', 3),('C', 4, 5, 6),('D',),('E', 7, 8)]
data_sorted=sorted(data,key=len) 
first_elements = list(zip(*data_sorted))[0]
result=list(first_elements)
print(result)
