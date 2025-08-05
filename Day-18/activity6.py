#pythagorean triplet
square=[(x,y,z)for x in range(1,30)  for y in range(1,30) for z in range(1,30) if x**2+y**2==z**2 ]
print(square)

square=[(x,y,z) for x,y,z in zip (range(1,31),range(1,31),range(1,31)]
print(square)