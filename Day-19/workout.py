#datetime
'''import datetime
print(datetime.datetime.now())#current date time

#only time
from datetime import time
t=time(10,45,30)
print(t)
print(t.hour,t.minute,t.second)#10 45 30
print(t.hour,t.minute)

from datetime import time
t=time(10,45,30)
print(t)
print(t.hour,t.minute,t.second)#10 45 30
print(t.hour,t.minute)
print(t.hour)

from datetime import time
t=time(10)
print(t)
print(t.minute)

from datetime import time
t=time(10,0,3)
print(t)
print(t.minute)

from datetime import date
t=date(2001,8,20)
print(t)

#date+time
from datetime import datetime
now=datetime.now()
print(now.day,now.month,now.year,sep="-")
print(now.hour,now.minute,now.second)

#creating custom datetime
dt=datetime(2025,12,25,17,30)
print(dt)


import greetings

print(greetings.say_hello("Abi"))

#only say hello
from greetings import say_hello,say_bye
print(hello("Abi"))

#file manipulation
file_handle=open('hello1.txt','r')
content=file_handle.read()
print(content)
print(type(content))
print(type(file_handle))
file_handle.close()

if the file has error without knowing what kind of error it should display what error is use try except else finally
try:
	file_handle=open('hello1.txt','r')
	content=file_handle.read()
	print(content)
	print(type(content))
	print(type(file_handle))
	file_handle.close()
else :
	print("File not found")
except:
	file_handle.close()


try:
    file_handle = open('hello.txt', 'r')
    content = file_handle.read()
    print(content)
    print(type(content))
    print(type(file_handle))
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully.")
finally:
    try:
        file_handle.close()
    except:
        pass


try:
    with open('hello1.txt', 'r') as file_handle:
        content = file_handle.read()
        print(content)
except Exception as e:
    print(f"Error: {e}")'''


try:
    file_handle = open('hello1.txt', 'r')
    content = file_handle.read()
    print(content)
    file_handle.close()
except Exception as e:
    print(f"Error: {e}")

  








