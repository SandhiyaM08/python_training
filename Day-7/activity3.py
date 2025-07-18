#printing jugs and mugs and pugs
val = int((num := input("Enter the number: ")).isdigit() and num or input("enter numeric value: "))
print((val % 3 == 0 and val % 5==0 and val % 7==0 and "jugs mugs pugs") or (val % 3 == 0 and val % 5==0 and "jugs mugs") or (val % 3 == 0 and val % 7==0 and "jugs pugs") or (val % 5==0 and val % 7==0 and "mugs pugs") or (val % 3 == 0 and "jugs") or (val % 5 == 0 and "mugs") or (val % 7 == 0 and "pugs") or val) 
