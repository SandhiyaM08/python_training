#get input from user that should be zipfile
#inside zipfile list what are files there
#based on user input extract file

try:

	import zipfile
	user_zipfile=input("Enter the zipfile name:")
	with zipfile.ZipFile('user_zipfile.zip','r') as file:
		print(file.namelist())
		extracting=input("Enter the extract file:")
		file.extract(extracting)
except:
	print("No file found")

'''
import zipfile

with zipfile.ZipFile('achive.zip','r') as file:
	print(file.namelist())
	extracting=input("Enter the extract file:")
	file.extract(extracting) '''