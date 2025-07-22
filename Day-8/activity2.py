# sentence="Python makes you think differently"
# output:makes you think


# print(" ".join("Python makes you think differently".split()[1:4]))


#solution:
first,*middle,last="Python makes you think differently"
print(middle)