#declaring inputs
nested_data = (["X", "Y"], ("A", "B", "C"), "PQRS")
multipliers = [2, 3, 1]
separators = ("|-|", "***", "^^^")
positions = [(1, 0), (2, 1, 0), (3, 1)]

#operations
values=nested_data[0][1]+separators[0]+nested_data[0][1]+nested_data[1][0]+separators[1]+nested_data[1][2]+separators[1]+nested_data[1][0]+nested_data[1][1]+nested_data[2][2]+nested_data[2][3]+separators[2]+nested_data[2][3]+separators[2]+nested_data[2][2]

#printing the values
print(values)
 


 
