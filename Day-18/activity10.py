#swapped
data = {'a': 1, 'b': 2, 'c': 1}
result = {v: tuple(k for k in data if data[k] == v) for v in set(data.values())}
print(result)

'''data = {'a': 1, 'b': 2, 'c': 1}
result = {v: tuple(k for k in data if data[k] == v) for v in data.values()}
print(result)'''


