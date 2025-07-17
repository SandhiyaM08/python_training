#getting input
input=input()

#removing
removed=input.replace(' ','')

#upper
convert=removed.upper()

#replacing
replaced=convert.replace('A','XXX')

#extract

print(replaced[::3][::-1])
