#bank details
tuple1=(12345,'sandhiya','sky1234',[1000,1200,2500])
new_tuple=tuple1[0]


tuple1=(12344,'sandhiya','sky12234',[1000,1200,2500])
new_tuple=tuple1[0],tuple1[1],tuple1[2],(tuple1[3]+tuple1[4]-tuple1[5]),tuple1[4],tuple1[5]
print(new_tuple)

declaring values
tuple1 = (12344, 'sandhiya', 'sky12234', [1000, 1200, 2500])
#balance
calculated_value = tuple1[3][0] + tuple1[3][1] - tuple1[3][2]
#updated tuple
new_tuple = (tuple1[0], tuple1[1], tuple1[2], calculated_value, tuple1[3][1], tuple1[3][2])
print(new_tuple)


tuple1 = (12344, 'sandhiya', 'sky12234', [1000, 1200, 2500])

# Get credit and debit from user
credit = int(input("Enter new credit amount: "))
debit = int(input("Enter new debit amount: "))

#balance
calculated_value = tuple1[3][0] + tuple1[3][1] - tuple1[3][2]
# Update the list inside the tuple
updated_list = [tuple1[3][0], credit, debit]

# Create new tuple with updated values
new_tuple = (tuple1[0], tuple1[1], tuple1[2], updated_list)

# Print the updated tuple
print("Updated tuple:", new_tuple)


# Original tuple
tuple1 = (12344, 'sandhiya', 'sky12234', [1000, 1200, 2500])

# Get user input
credit = int(input("Enter credit amount: "))
debit = int(input("Enter debit amount: "))

credit = (credit > 0 and credit < 10000 and credit) or 1200
debit = (debit > 0 or debit < 5000 and debit) or 2500

# updated tuple
new_tuple = (tuple1[0], tuple1[1], tuple1[2], [tuple1[3][0], credit, debit])

# Print result
print("Updated tuple:", new_tuple)

print(4 or 5)
print(1 or 3)
print(1 and 4)
print(4 and 5)

#print the operations divisible by 3
num=int(input("Enter the number:"))
print((num%3==0 and "jugs") or num)

num=input("Enter the number:")
print((num!=int(num) and num) or "Enter the numeric value")

num = input("Enter the number: ")
print((num !=int(num) and int(num)) or "Enter the numeric value")

num = input("Enter the number: ")
num[1:]=num in(1,2,3,4,5,6,7)and num or "Enter the numeric value"


num = input("Enter the number: ")
print((num.isdigit() and (int(num) % 3 == 0 and "jugs" or num)) or "Enter the numeric value")

num = input("Enter the number: ").isdigit() and input("Enter the number: ")
print((num%3==0 and "jugs") or num)

print((num.isdigit() and (int(num) % 3 == 0 and "jugs" or num)) or "Enter the numeric value")  or input("Enter the numeric value: ")

num=input("enter the number:").isdigit or input("Enter the number:")
print((num.isdigit() and (int(num) % 3 == 0 and "jugs" or num)) or "Enter the numeric value")  or input("Enter the numeric value: ") and int(num) % 3 == 0 


print((num.isdigit() and int(num) % 3 == 0 and "jugs") or (num.isdigit() and int(num) % 3 == 0 and "jugs") or (input("Enter the number: ")))


num = input("Enter the number: ") or input("Enter the numeric value: ")
print((num.isdigit() and (int(num) % 3 == 0 and "jugs" or num)) or "Enter the numeric value")



num = input("Enter the number: ")
print((num.isdigit() and (int(num) % 3 == 0 and "jugs" or int(num))) or "Invalid input")

num=input().isdigit and input() and input()
print(num)

num = input("Enter the number: ").isdigit() and input("Enter the number: ") or input("Enter the number:")
print((num%3==0 and "jugs") or num)

num = input("Enter the number: ").isdigit() or input("Enter the numeric value: ") or input("Enter the numeric value: ") 
print((num.isdigit() and (int(num) % 3 == 0 and "jugs" or num)) or "Enter the numeric value")

num = input("Enter the number: ").isdigit() or input("Enter the number: ") or input("Enter the number: ")
print((num%3==0 and "jugs") or num)

ip = int(input("Enter the number: ").isdigit()  or input("Kindly enter numeric value: "))
 


num = (input("Enter the number: ").isdigit() and int(input("Enter the number: ")) or int(input("Kindly enter numeric value: ")))
print((num%3==0 and "jugs") or num)

num = input("Enter the number: ").isdigit() and input("Enter the number: ")
print((num%3==0 and "jugs") or num)



num = n:=input("Enter the number: ")).isdigit() and (val := int(num)) or (val := int(input("Kindly enter numeric value: ")))) and ("jugs" if val % 3 == 0 else val))


val = (num := input("Enter the number: ")).isdigit() and int(num) or int(input("Kindly enter numeric value: "))
print("jugs" if val % 3 == 0 else val)


val = int((num := input("Enter the number: ")).isdigit() and num or input("Kindly enter numeric value: "))
print((val % 3 == 0) "jugs" or val)

#printing jugs
val = int((num := input("Enter the number: ")).isdigit() and num or input("Enter numeric value: "))
print((val % 3 == 0 and "jugs") or val)


val1 = int((num := input("Enter the number: ")).isdigit() and num or input("enter numeric value: "))
val=str(val1)
print((int(val[1]) % 3 == 0 and "jugs") or val) or (int(val[2])% 3 == 0 and "jugs") or val

#printing jugs and mugs
val = int((num := input("Enter the number: ")).isdigit() and num or input("enter numeric value: "))
print((val % 3 == 0 and val %5==0 and "jugs mugs") or (val % 3 == 0 and "jugs") or (val % 5 == 0 and "mugs") or val) 

#printing jugs and mugs and pugs 
val = int((num := input("Enter the number: ")).isdigit() and num or input("enter numeric value: "))
print((val % 3 == 0 and val % 5==0 and val % 7==0 and "jugs mugs pugs") or (val % 3 == 0 and val % 5==0 and "jugs mugs") or (val % 3 == 0 and val % 7==0 and "jugs pugs") or (val % 5==0 and val % 7==0 and "mugs pugs") or (val % 3 == 0 and "jugs") or (val % 5 == 0 and "mugs") or (val % 7 == 0 and "pugs") or val) 


# jugs mugs pugs
# jugs mugs
# jugs pugs
# mugs pugs
# jugs
# mugs
# pugs

