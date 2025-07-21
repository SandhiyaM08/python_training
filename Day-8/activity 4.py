#assigning values
fruit_prices={"elppa":100,"egnaro":80,"ananab":60}
#getting input from user
fruit_name = input("Enter fruit name: ")[::-1]
#printing
print(fruit_prices.get(fruit_name,{}))
