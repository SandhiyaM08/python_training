'''o/p:{'x':10,'y':20,'z':30}'''

dict1={'x':10,'y':20}
dict2={'y':99,'z':30}
result={**dict2,**dict1}
print(result)

#or

dict1={'x':10,'y':20}
dict2={'y':99,'z':30}
result={dict2|dict1}
print(result)

#or

dict1={'x':10,'y':20}
dict2={'y':99,'z':30}
result=dict1.update(dict2)
print(result)