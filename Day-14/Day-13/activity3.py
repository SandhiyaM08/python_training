

'''score=int(input("Enter the score:"))
if(score==90 and score>=90):
   print('A\nExcellent work!')
elif(score>=80 and score<89):
   print('B\nGood job!')
elif(score>=70 and score<79):
   print('C\nSatisfactory')
elif(score>=60 and score<69):
   print('D\nNeeds improvement')
else:
   print("please study more")'''


score=int(input("Enter the score:"))
message={'A' :'Excellent work!',
       'B' : 'Good job!',
       'C' : 'Satisfactory',
       'D'  : 'Needs improvement',
       'E'  : 'please study more'}
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print(grade)
print(message[grade])



