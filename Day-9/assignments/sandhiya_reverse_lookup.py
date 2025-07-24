scores = {
    "Anita": 92,
    "Ravi": 85,
    "Kiran": 76,
    "Zoya": 88
}
input_score=int(input("Enter score:"))
data=dict(zip(scores.values(),scores.keys()))
print(data.get(input_score,"Not found"))
