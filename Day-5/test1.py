#step1:All of you get user name
#step2:input should be in lower case
#step 3: then convert to upper case without using upper

name=input("enter user name:")
user_name=name.lower()
user1=chr(user_name[0]+user_name[1]+user_name[2]+user_name[3])
print("Converted upper case:",user1)

#solution for single character
name=input("enter user name:")
user_name=name.lower()
user1=chr(ord(user_name)-32)
print("Converted upper case:",user1)

#solution
user_name = input('Enter your name: ').lower()
 
resulting_name = ""
 
resulting_name+=chr(ord(user_name[0])-32)
resulting_name+=chr(ord(user_name[1])-32)
resulting_name+=chr(ord(user_name[2])-32)
resulting_name+=chr(ord(user_name[3])-32)
resulting_name+=chr(ord(user_name[4])-32)
resulting_name+=chr(ord(user_name[5])-32)
resulting_name+=chr(ord(user_name[6])-32)
 
print(resulting_name)

