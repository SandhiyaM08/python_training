previous=int(input("enter the pervious meter:"))
current=int(input("enter the current meter:"))
meter=abs(previous-current)
if (meter<=400):
  print("Price",4.80*meter)
elif(meter>=401 and meter<=500):
  print("Price",meter*6.45)
elif(meter>=501 and meter<=600):
  print("Price",meter*8.55)
elif(meter>=601 and meter<=800):
  print("Price",meter*9.65)
elif(meter>=801 and meter<=1000):
  print("Price",meter*10.70)
else:
  print("Price",meter*11.80)
