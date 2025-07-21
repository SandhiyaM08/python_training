'''a=10
b=20
c=30
without using tempoaray variable reassign them a become val c,b become value a,c become value b in one line'''

#assign values
a=10
b=20
c=30

#operations solution 1
# a, b, c = c, a, b
# print(a,b,c)

#solution2
a=10
b=20
c=30
a, b, c = (b + c) // 2, (a + c) // 2, (a + b) // 2
print(a,b,c)
