
try:
    value = int(input("Enter the number: "))
    check = lambda x: x if x % 2 == 0 else (_ for _ in ()).throw(ValueError)
    print("Even number:", check(value))
except ValueError:
    print("Odd number")
