#input
grades={"anita":92,"ravi":85,"kiran":76,"zoya":88}

#getting input
student_name=input("enter the name:")

#printing
print(grades.get(student_name,"Student not found"))
