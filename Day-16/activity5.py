'''def insertion(val):
	for i in range(1,len(val)):
		for j in range(0,len(val)):
			while val[j]>=0	
			if val[i]>val[j+1]:
				val[i],val[j+1]=val[j+1],val[i]


			

val=[1,23,10,34,45]
def insertion(val):
    for i in range(1, len(val)):
        j = i - 1
        while j >= 0 and val[j] > val[i]:
            val[j + 1] = val[j]
            j -= 1
        val[j + 1] = val[i]
    return val
print(insertion(val))'''
	

#solution
val = [1, 23, 10, 34, 45]
def insertion(val):
    for i in range(1, len(val)):
        j = i
        while j > 0 and val[j] < val[j - 1]:
            val[j], val[j - 1] = val[j - 1], val[j]
            j -= 1
    return val
print(insertion(val))



			