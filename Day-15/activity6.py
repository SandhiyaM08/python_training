codes=['4686','ABCD','--','00x0','0000','0']
for val in codes:
	if val=='0'and val.isalnum():
		break
	if val.isdigit() and int(val)!=0:
		print(val)
	
	
	


'''codes=list(map(int,input("enter integer:").split(',')))
for val in codes:
	if val in codes:
		continue
	if count('0')>1:
		break
	if val.isdigit():
		print(val)'''