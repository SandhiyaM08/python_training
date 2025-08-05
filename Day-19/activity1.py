#should simulates a weighted coin should return 70% of time and tails 30% time

'''import random
def flip_biased_coin():
	result=random.choice([Heads,Tail],weighted_value=[70,30])
	return result
print(flip_biased_coin)'''

import random
def flip_biased_coin():
	if random.random()<=0.7:
		print("Heads")
	else:
		print("Tails")
flip_biased_coin()

		
