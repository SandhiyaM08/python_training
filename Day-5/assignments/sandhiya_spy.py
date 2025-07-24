#getting inputs
values=input().split(' ')
#getting the every third character
third_character=(values[1::3])
#reverse
reverse=third_character[::-1]
#final message
final_message =''
for index in reverse:
    final_message+=chr(int(index))
print(final_message)