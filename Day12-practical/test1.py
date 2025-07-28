'''read the input from user if it is string you should check whether given string is palindrom or not if it is number you need to print the given number is odd or even if number is float length of digits float if not these not valid type not use conditional loop function dont do type casting


input1=(input2:=input("Enter the string:")) or input2.isdigit() or input2==float(input)
print(input1==input1[::-1]) or (print(input2%2==0 ) or print('even') or print('odd')) and ((print(len(input1))))

input1=(input2:=input("Enter the string:")) or input2.isdigit() or input2==float(input)
print(input1==input1[::-1]) or (int(input2)%2==0 or print('even') and print('odd')) or (len(input1)) and (print('not valid type')

input1=input("Enter the string:")
(int(input1)%2==0 or print('odd')) and print('even')) and print('invalid')

input1=input("Enter the string:")
input1=float(input1) or print(len(input1))or print('invalid')

input1=input("Enter the string:")
input1.isdigit() and (int(input1)%2==0 or print('odd')) and print('even') 
type(input) and (type is float or print(len(input1))) and print('invalid') 
input1.isalpha() and (input1==input1[::-1] or print('not palindrome')) and print('palindrome')or print('invalid')

input1=input("Enter the string:")
(input1.isdigit() and (int(input1)%2==0 or print('odd')) and print('even'))or(type(input) and (type is float or print(len(input1))) and print('invalid'))or(input1.isalpha() and (input1==input1[::-1] or print('not palindrome')) and print('palindrome'))or print('invalid')

input1=input("Enter the string:")
input1.isdigit() and (int(input1)%2==0 or print('odd')) and print('even') 
type(input) and (type is float or print(len(input1))) and print('invalid') 
input1.isalpha() and (input1==input1[::-1] or print('not palindrome')) and print('palindrome')or print('invalid')
 
 input1=input("Enter the string:")
input1.isdigit() and (int(input1)%2==0 or print('odd')) and print('even') or type(input) and (type is float or print(len(input1))) and print('invalid') or input1.isalpha() and (input1==input1[::-1] or print('not palindrome')) and print('palindrome')

print(input1==str(input1) or input1[::-1]) and print('not valid type')
input1==(int(input))
print(input1%2==0 or print('even')) or print('odd')
input1==(float(input1))
print(len(input1))

input1=input("Enter the string:")
r1=input1.isdigit() and (int(input1)%2==0 or print('odd')) and print('even') 
r2=type(input) and (type is float or print(len(input1))) 
r3=input1.isalpha() and (input1==input1[::-1] or print('not palindrome')) and print('palindrome')
r4=(r1 or r2 or r3 or print('invalid'))
print(r4)

#final
input1=input("Enter the string:")
r1=input1.isdigit() and (int(input1)%2==0 or ('odd')) and ('even') 
r2=type(input) and (type is float or len(input1)) 
r3=input1.isalpha() and (input1==input1[::-1] or ('not palindrome')) and ('palindrome')  
r4=(r1 or r2 or r3 or print('invalid'))
print(r4)'''


input1=input("Enter the string:")
r1=input1.isdigit() and (int(input1)%2==0 or ('odd')) and ('even') 

r3=input1.find('.') and input1.replace('.','') 

r2=type(input1) and (type is float or len(input1)) 
r4=(r3==r3[::-1] and ('palindrome')  or ('not palindrome')) 
r5=(r1 or r2 or r4 or print('invalid'))
print(r4)



