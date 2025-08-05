#takes circle radius as input calculate diameter,circumference,area
radius=int(input("enter radius"))
from math import pi
diameter = 2 * radius
circumference = 2 * pi * radius
area = pi * radius ** 2
print("Diameter:",diameter)
print("Circumference:",circumference)
print("Area:",area)


from math import pi,floor,ceil
radius=int(input("enter radius"))
print("Diameter:",floor(2 * radius))
print("Circumference:",ceil(2 * pi * radius))
print("Area:",pi * radius ** 2)

