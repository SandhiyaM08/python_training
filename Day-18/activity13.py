data=[[1,2,None],[],[3,'',4],[0,5,5],[None,6]]
result = []
value = set()
for sublist in data:
    for item in sublist:
        if item and item not in value:
            result.append(item)
            value.add(item)
print(result)
