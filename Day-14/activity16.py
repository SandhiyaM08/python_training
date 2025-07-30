#three booleans if exactly one is true print'exactly one' else 'nope' use only if 
# input1,input2,input3=map(input("Enter the values:").split(','))
# if any[(input1,input2,input3)]==True:
# 	print('True')

input1,input2,input3=input("Enter the values:").split(',')
count=0
if input1== "True":
    count += 1
if input2 == "True":
    count += 1
if input3 == "True":
    count += 1

print("Exactly one" if count == 1 else "Nope")





