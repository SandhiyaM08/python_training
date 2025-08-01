#return the mean of any number of values

def average(*scores):
	avg=sum(scores)/len(scores)
	return avg
print(average(1,2,3,4,5))
