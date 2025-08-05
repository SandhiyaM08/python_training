#modify greeter.py it should ask user for name using input() then calls personal_greet() to greet them

def personal_greet(name):
	print(f"Hello,{name}")
if __name__=="__main__":
	user_name=input("Enter name:")
	personal_greet(user_name)
	