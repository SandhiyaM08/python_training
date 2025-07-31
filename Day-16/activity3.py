#selection sort

list1=[5,4,2,1,6,3]
for i in range(len(list1)):
	min_value=i
	for j in range(i+1,len(list1)):
		if list1[j]>list1[min_value]:
			min_value=j
		list1[j],list1[min_value]=list1[min_value],list1[j]
print(list1)


#bubble sort:

'''list1=[5,4,2,1,6,3]
for i in range(0,len(list1)):
	for j in range(0,len(list1)-1):
		if list1[j]>list1[j+1]:
			list1[j],list1[j+1]=list1[j+1],list1[j]
print(list1)'''











		