#set comprehension vowels
items = {'banana'}
result = {char for item in items for char in item if char == 'a'}
print(result)
