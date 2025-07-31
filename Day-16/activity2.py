#binary search

list1=[10,34,56,78,89,90]
element=78
low=0
high=len(list1)-1
while low<=high:
	mid=(high+low)//2
	if list1[mid]>element:
		high=mid-1
	elif list1[mid]<element:
		low=mid+1
	else:
		print(mid)
		break
else:
	print(-1)
