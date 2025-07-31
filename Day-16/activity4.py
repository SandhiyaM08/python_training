#user has to guess the randam number from 1-100 using random.randint

import random
num=random.randint(1,100)
while True:
	guess=int(input("Enter the number:"))
	if guess<num:
		print("Too low")
	elif guess>num:
		print("Too high")
	else:
		print("correct")
		break

