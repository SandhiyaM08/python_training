employee="Abi"
hours_worked=45.75
hourly_rate=350.50
bonus=1500
target_hours=40
print("{0:*^40}".format("Employee Report"))
print("{0:>20}{1:>20}" .format("Employee name:",employee))
print("{0:>20}{1:>20}" .format("Hours worked:",hours_worked))
print("{0:>20}{1:>20}" .format("Target hours:",target_hours))
print("{0:>20}{1:>20}" .format("Overtime:",hours_worked-target_hours))
print("{0:>21}{1:>010.2f}" .format("Total Pay:$",(hours_worked*hourly_rate)+bonus))