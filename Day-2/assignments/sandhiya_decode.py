#declaring string
data = "Luna42Kai3.14True#Knight"
#performing operation
Name=data[:4].upper()
Number=int(data[4:6])+8
float_value=float(data[9:13])*2
reverse=data[-1:-7:-1]
#printing the values
print(f"Name: {Name}")
print(f"42 + 8 = {Number}")
print(f"3.14 * 2 = {float_value}")
print(f"Reversed Title: {reverse}")