#read csv file print 
import csv
with open("data.csv",newline='') as f:
	reader=csv.reader(f)
	for row in reader:
		if row : 
			print(row)
