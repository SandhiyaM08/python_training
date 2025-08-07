#numeric columns and sum all values 

'''import csv
with open("data.csv",newline='') as f:
	reader=csv.DictReader(f)
	sum=0.0
	for row in reader:
		sum+=float(row["Amount"])
print(sum)'''

import csv
with open("data.csv",newline='') as f:
	reader=csv.reader(f)
	sum=0
	next(reader)
	for row in reader:
		sum+=float(row[1])
print(sum)