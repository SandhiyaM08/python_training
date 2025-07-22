'''#scrambled key words getting user the unscrambled word


#assigning values
fruit_prices={"elppa":100,"egnaro":80,"ananab":60}
#getting input from user
fruit_name = input("Enter fruit name: ")[::-1]
#printing
print(fruit_prices.get(fruit_name,{}))

fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}
fruit_name=input("Enter the fruit_name:")
print(index(sorted(fruit_name)))
print(sorted(fruit_prices))
print(fruit_prices.keys(sorted))
print(list(fruit_prices))
print(index(sorted(fruit_prices)))


#assigning values
fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}
# #getting input from user
fruit_name = input("Enter fruit name:")
# #performing operations
key =list(fruit_prices)[list(map(sorted,fruit_prices)).index(sorted(fruit_name))]
print(fruit_prices[key])


fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}
fruit_name = input("Enter fruit name:")
key = list(fruit_prices)[list(map(sorted, fruit_prices)).index(sorted(fruit_name))]
print(fruit_prices[key])'''


fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}
fruit_name = input("Enter fruit name:")
sorted_prices = {(''.join(sorted(fruit_name):fruit_prices.values())}
print(sorted_prices)
print(map(''.join(sorted(fruit_name):


fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}
fruit_name = input("Enter fruit name:")
print({fruit_name: ''.join(sorted(fruit_name))})
