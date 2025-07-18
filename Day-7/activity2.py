#printing jugs and mugs
val = int((num := input("Enter the number: ")).isdigit() and num or input("enter numeric value: "))
print((val % 3 == 0 and val %5==0 and "jugs mugs") or (val % 3 == 0 and "jugs") or (val % 5 == 0 and "mugs") or val) 
