'''import zipfile

with zipfile.ZipFile('achive.zip',mode='w') as file:
	file.write('text1.txt')
	file.write('demo1.txt.txt')

import zipfile

with zipfile.ZipFile('achive.zip',mode='r') as file:
	file.read('text1.txt')
	file.read('demo1.txt.txt')

import zipfile

with zipfile.ZipFile('achive.zip',mode='r') as file:
	file.read('text1.txt')
	file.read('demo1.txt.txt')
	print(file.namelist())	
	file.extractall()'''

import zipfile
zipfile.ZipFile('data.zip','w',compression=zipfile.zip_deflated)	