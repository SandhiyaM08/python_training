'''#scrambled key words getting user the unscrambled word


#assigning values
fruit_prices={"elppa":100,"egnaro":80,"ananab":60}
#getting input from user
fruit_name = input("Enter fruit name: ")
#printing
print(fruit_prices.get(fruit_name,{}))


#assigning values
fruit_prices = {"alpep": 100, "egnaro": 80, "ananab": 60}
#getting input from user
fruit_name = input("Enter fruit name:")
#performing operations
key = list(fruit_prices)[list(map(sorted, fruit_prices)).index(sorted(fruit_name))]
print(fruit_prices[key])


