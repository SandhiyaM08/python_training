import csv
rows=["name","age","city"],["alice",30,"london"],["bob",25,"new York"]
with open("demo.csv",'w',newline='') as f:
	writer=csv.writer(f)
	writer.writerows(rows)

with open("demo.csv",newline='')as f:
	reader=csv.reader(f)
	writer=csv.writer(f,quotechar='-',quoting=csv.QUOTE_NONNUMERIC)
	for row in reader:
		print(row)