#csv reading
'''import csv
with open("demo.csv",newline='') as f:
	reader=csv.reader(f)
	for row in reader:
		print(row)

#using head-remove the first line
import csv
with open("demo.csv",newline='') as f:
	reader=csv.reader(f)
	next(reader)
	for row in reader:
		print(row)

#reading and print it in list
import csv
with open("demo.csv",newline='') as f:
	reader=csv.reader(f)
	data=list(reader)
print(data)

#using line_num
import csv
with open("demo.csv",newline='') as f:
	reader=csv.reader(f)
	for row in reader:
		print(reader.line_num,row)'''

#reading csv as dictionaries
import csv
with open("demo.csv",newline='') as f:
	reader=csv.DictReader(f)
	for row in reader:
		print(row["name"],row["age"])