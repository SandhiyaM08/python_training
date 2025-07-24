'''manage 3 guest lists invited by email,phone,blocked guests
print set of peopple invited both email and phone but not blocked plus only blocked list and nowhere else




email= {"Alice", "Bob", "Charlie", "David"}
phone= {"Charlie", "David", "Eve", "Frank"}
blocked= {"David", "George", "Helen"}
both=(email&phone)-blocked
only_blocked=blocked-(email|phone)
print((email&phone)-blocked)
print(only_blocked)'''


email= {"Alice", "Bob", "Charlie", "David"}
phone= {"Charlie", "David", "Eve", "Frank"}
blocked= {"David", "George", "Helen"}
print((email&phone)-blocked | blocked-(email|phone))