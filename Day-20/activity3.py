#compress multiple text file print name and compress size

'''import zipfile
with zipfile.ZipFile("archive.zip", "w") as activity2:
	

with zipfile.ZipFile('achive.zip',mode='w',compression=zipfile.ZIP_BZIP2) as activity2:'''


'''
import zipfile


with zipfile.ZipFile("archive.zip", mode="w", compression=zipfile.ZIP_BZIP2) as activity2:
    activity2.write("file1.txt")
    activity2.write("file2.txt")
    activity2.write("file3.txt")

with zipfile.ZipFile("archive.zip", "r") as activity2:
    for info in activity2.infolist():
        print(f"{info.filename}: {info.compress_size} bytes")
'''

#activity_03
 
import zipfile
 
with zipfile.ZipFile('activity_03.zip','w') as zf:
	zf.write('file1.txt')
	zf.write('file2.txt')
	zf.write('file3.txt')
 
 
with zipfile.ZipFile('activity_03.zip','r',compression = zipfile.ZIP_BZIP2) as zf:
	for file_name in zf.namelist():
		print(f"{file_name} => {zf.getinfo(file_name).file_size} bytes")