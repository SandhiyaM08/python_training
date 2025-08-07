You have a list of students, each with a list of scores. Create a dictionary mapping the names of students who have an average score of 90 or higher to their average score.
Concepts: nested list, list of dict, filter, map, lambda, dictionary comprehension.
 students = [     {"name": "Brenda", "scores": [90, 92, 95, 88]},     {"name": "David", "scores": [85, 87, 89]},     {"name": "Cathy", "scores": [98, 99, 100]},     {"name": "Alex", "scores": [70, 100]} ]
 
dict={student[name]:avg_score}
for student in students:
	if avg_score=(sum(students[scores])/len(students[scores]))>=90
print(dict)
