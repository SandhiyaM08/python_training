'''import zipfile
zip_path=input("enter path:")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    if "foo.txt" in zip_ref.namelist():
        print("Found!")
    else:
        print("Missing!")'''

import zipfile

zip_path = input("Enter the path to your ZIP file: ")

try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        with zip_ref.open('foo.txt') as f:
            print("Found!")
except KeyError:
    print("Missing!")


import zipfile

zip_path = input("Enter the path to your ZIP file: ")

try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Try to open the file directly
        with zip_ref.open('foo.txt') as f:
            print("Found!")
except KeyError:
    print("Missing!")

