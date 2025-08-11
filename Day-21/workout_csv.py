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
		print(reader.line_num,row)

#reading csv as dictionaries
import csv
with open("demo.csv",newline='') as f:
	reader=csv.DictReader(f)
	for row in reader:
		print(row["name"],row["age"])

#reading csv as writer row
import csv
with open("demo.csv",newline='') as f:
	writer=csv.writer(f)
	writer.writerow(["name","age","city"])
	writer.writerow(["alice","34","london"])

#reading csv as writer rows

import csv
rows=[["name","age","city"],["alice",34,"london"]]
with open("demo.csv",'w',newline='') as f:
	writer=csv.writer(f)
	writer.writerows(rows)'''

#reading csv as dictionaries in writer
import csv
rows=[{"name":"alice","age":30,"city":"london"},{"name":"bob","age":30,"city":"new york"}]
with open("demo.csv",'w',newline='') as f:
	writer=csv.DictWriter(f,fieldnames=["name","age","city"])
	writer.writeheader()
	writer.writerows(rows)

#reading csv as reader delimiter
'''import csv
with open("demo.csv",newline='') as f:
	reader=csv.reader(f,delimiter=';')
	for row in reader:
		print(row)

#reading csv as writer delimiter

import csv
rows=[["name","age","city"],["alice","34","london"]]
with open("demo.csv",newline='') as f:
	writer=csv.writer(f,delimiter=';')
	writer.writerows(rows)

#quote character quote_all

import csv
rows=[["name","age","city"],["alice","34","london"]]
with open("demo.csv",newline='') as f:
	writer=csv.writer(f,quotechar="$",quoting=csv.QUOTE_ALL)
	writer.writerows(rows)


import csv
rows=[["name","age","city"],["alice","34","london"]]
with open("demo.csv",newline='') as f:
	writer=csv.writer(f,quotechar="$",quoting=csv.QUOTE_NON)
	writer.writerows(rows)

#escapechar 

import csv
with open("demo.csv",newline='') as f:
	reader=csv.reader(f,quotechar='"',escapechar='\\')
	for row in reader:
		print(row)'''




