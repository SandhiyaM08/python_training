
try:
    value = int(input("Enter the number: "))
    check = lambda x: x if x % 2 == 0 else x.throw(ValueError)
    print("Even number:", check(value))
except ValueError:
    print("Odd number")

try:
    value = int(input("Enter the number: "))
    check = lambda x: x if x % 2 == 0 else generator.throw(ValueError)
    print("Even number:", check(value))
except ValueError:
    print("Odd number")



high_achievers = {
    student["name"]: avg_score
    for student in students
    if (avg_score := sum(student["scores"]) / len(student["scores"])) >= 90
}

print(high_achievers)
