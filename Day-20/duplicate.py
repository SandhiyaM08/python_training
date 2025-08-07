

import zipfile
'''with zipfile.ZipFile('duplicate.zip','w') as zf:
	zf.write('file1.txt')
	zf.write('file2.txt')
	zf.write('file2.txt')
	zf.write('file3.txt')
	zf.write('file3.txt')
	zf.write('file3.txt')

with zipfile.ZipFile("duplicate.zip") as zipf:
    names = list(map(lambda n: n.split("/")[-1], zipf.namelist()))
    for name in set(names):
        if names.count(name) > 1:
            print("Duplicate:", name)'''


with zipfile.ZipFile("duplicate.zip") as zipf:
    names = list(map(lambda n: n.split("/")[-1], zipf.namelist()))
    for name in set(names):
        if names.count(name) > 1:
            print("Duplicate:", name)