#largest element and smallest element print true or false
tuple1=(15,22,5,10)
min_val = min(tuple1)
max_val = max(tuple1)
result = tuple1.index(min_val) < tuple1.index(max_val)
print(result)
