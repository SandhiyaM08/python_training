names=["Alice","Bob","Charlie"]
marks=[85,90,88]
grades=["B","A","A"]
for i in range(len(names)):
	values=f"{i+1},{names[i]},{marks[i]},{grades[i]}"
	print(values)