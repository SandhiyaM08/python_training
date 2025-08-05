data=[[1,2,None],[],[3,'',4],[0,5,5],[None,6]]
result = []
value = set()
for sublist in data:
    for item in sublist:
        if item and item not in value:
            result.append(item)
            value.add(item)
print(result)

data=[[1,2,None],[],[3,'',4],[0,5,5],[None,6]]
result=[y for x in data for y in x if y]
result1=list(dict.fromkeys(result))
print(result1)

