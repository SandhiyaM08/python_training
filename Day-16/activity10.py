#redesign f(x,lst=???)each call gives a fresh list

def f(x,lst=list()):
	lst.append(x)
	return lst
print(f(1))
print(f(2))


#with using None:
'''def f(x,lst=None):
	if lst is None:
		lst=[]
	lst.append(x)
	return lst
print(f(1))
print(f(2))'''


