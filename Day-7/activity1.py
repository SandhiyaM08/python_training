#printing jugs
val = int((num := input("Enter the number: ")).isdigit() and num or input("Enter numeric value: "))
print((val % 3 == 0 and "jugs") or val)
