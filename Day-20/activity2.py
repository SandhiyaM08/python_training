#create zip file 3 text file within each contain hello from file<no>! extract it and print out all filename
'''import zipfile
with zipfile.ZipFile('achive.zip','w') as file:
	file.write('file1.txt')
	file.write('file2.txt')
	file.write('file3.txt')
	print(file.extractall())
	print(file.namelist())

import zipfile

for i in range(1, 4):
    with open(f"file{i}.txt", "w") as f:
        f.write(f"Hello from file")

with zipfile.ZipFile("archive.zip", "w") as file:
    for i in range(1, 4):
        file.write(f"file{i}.txt")

with zipfile.ZipFile("archive.zip", "r") as zipf:
    zipf.extractall()
    print("Extracted files:")
    print(zipf.namelist())'''

import zipfile
with open("file1.txt", "w") as f1:
    f1.write("Hello from file1!")
with open("file2.txt", "w") as f2:
    f2.write("Hello from file2!")
with open("file3.txt", "w") as f3:
    f3.write("Hello from file2!")

with zipfile.ZipFile("archive.zip", "w") as file:
	file.write('file1.txt')
	file.write('file2.txt')
	file.write('file3.txt')


with zipfile.ZipFile("archive.zip", "r") as file:
	file.extractall()
	print("Files in ZIP:", file.namelist())
	
	



