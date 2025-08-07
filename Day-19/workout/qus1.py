'''You have a list of students, each with a list of scores. Create a dictionary mapping the names of students who have an average score of 90 or higher to their average score.
Concepts: nested list, list of dict, filter, map, lambda, dictionary comprehension.

students = [     {"name": "Brenda", "scores": [90, 92, 95, 88]},     {"name": "David", "scores": [85, 87, 89]},     {"name": "Cathy", "scores": [98, 99, 100]},     {"name": "Alex", "scores": [70, 100]} ]
 
dict={student['name']:avg_score
      for student in students
      if (avg_score:=sum(student["scores"])//len(student["scores"]))>=90}
print(dict)

avg=list(map(lambda s: (s["names"],sum(s["scores"])//len(s["scores"])),students))

checking=list(filter(lambda x:x[1]>=90,avg))

result=dict(checking)

      for student in students
      if (avg_score:=sum(student["scores"])//len(student["scores"]))>=90}
print(dict)

dict={student['name']:sum(student["scores"])//len(student["scores"])),studentstudents
      for student in students
      if (avg_score:=sum(student["scores"])//len(student["scores"]))>=90}
print(dict)'''


students = [     {"name": "Brenda", "scores": [90, 92, 95, 88]},     {"name": "David", "scores": [85, 87, 89]},     {"name": "Cathy", "scores": [98, 99, 100]},     {"name": "Alex", "scores": [70, 100]} ]

averages = list(map(lambda s: (s["name"], sum(s["scores"]) / len(s["scores"])), students))

high_achievers = dict(list(filter(lambda x: x[1] >= 90, averages)))

result = dict(high_achievers)
print(result)

#solution
averages = list(map(lambda s: (s["name"], sum(s["scores"]) / len(s["scores"])), students))
result = dict(list(filter(lambda x: x[1] >= 90, averages)))
print(result)


