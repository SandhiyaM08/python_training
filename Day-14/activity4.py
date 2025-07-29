'''temp=37
advice="see a doctor" if temp>38 else "rest and hydrate"

advice="see a doctor" if int(input("enter temp:"))>38 else "rest and hydrate"

advice="see a doctor" if int(input("enter temp:"))>38 else "rest and hydrate"

advice = "see a doctor" if (temp:=37) > 38 else "rest and hydrate"'''


temp, advice = 37, "see a doctor" if temp := 37 > 38 else "rest and hydrate"

# solution:
advice = "see a doctor" if (temp:=37) > 38 else "rest and hydrate"