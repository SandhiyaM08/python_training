#count vowels check should case sensitive

text=input("enter the string:")
count={}
vowels='AEIOUaeiou'
for char in text:
   if char in vowels:
      if char in count:
          count[char] +=1
print(count) 

text=input("enter the string:")
count={}
vowels='AEIOUaeiou'
for char in text:
   if char in vowels:
          count[char] =count.get(char,0)+1
print(count)

text=input("enter the string:").lower()
for char in text:
    if char in 'a,e,i,o,u':
	






