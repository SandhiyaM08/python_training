'''Take a string, remove all spaces, convert to uppercase, replace every 'A' with 'XXX', then extract characters at positions that are multiples of 3, and finally reverse the result.
 
input:
text = "amazing python language"
 
output:
"GNGXXXA"'''


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
