#Activity-2
#generate a valid secret santa pairing

'''import random
participants=["Michael","Jim","Pam","Dwight","Angela"]
secret=random.choice(participants)
for item in participants:
	if item!=secret and secrets not in participants:
		print(f"{item}->{secret}")

import random
participants = ["Michael", "Jim", "Pam", "Dwight", "Angela"]
secret = random.choice(participants)
pairings = set()
for person in participants:
    if person != secret:
        pairings.add(f"{person} -> {secret}")
for pairing in pairings:
    print(pairing)'''

import random
participants=["Michael","Jim","Pam","Dwight","Angela"]
new_list=[]
i=0
while True:
	secret=random.choice(participants)
	if participants[i] != secret and secret not in new_list:
		new_list.append(secret)
		print(f"{participants[i]} -> {secret}")
		i+=1
	if i == len(participants):
		break

	

		
	
