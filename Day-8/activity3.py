
#assigning
students = {
    "anita": {"math": 95, "science": 89},
    "ravi": {"math": 80, "science": 92},
    "pavi": {"math": 88, "science": 85}
}

#getting input from user

student_name = input("Enter student name: ")
subject_name = input("Enter subject: ")

print(students.get(student_name,{}).get(subject_name, "invalid input"))

