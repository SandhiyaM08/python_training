
quote = "Believe yourself"

with open("quote.txt", "w") as file:
    file.write(quote)
print(open("quote.txt").read())