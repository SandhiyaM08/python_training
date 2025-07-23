access_data={(103,209):"alice",(104,210):"bob",(105,211):"charlie",(106,212):"diana"}
access_input=map(int,input("enter the access input:").split(','))
# print(access_data.get(tuple(sorted(access_input))))
print(access_data[1][0])

