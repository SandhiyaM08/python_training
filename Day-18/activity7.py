#print[3,6,9] instead [9,9,9]

funcs=[lambda i=i:i*3 for i in range(1,4)]
print([f() for f in funcs])