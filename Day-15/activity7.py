#print all prime numbers upto range n

n=int(input("Enter the number:"))
for val in range(2,n+1):
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            break
    else:
        print(val, end=' ')






