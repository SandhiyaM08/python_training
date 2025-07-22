#merge two dict and overwrite it
dict1={"name":"ravi","age":25}
dict2={"age":30,"city":"chennai"}
print({**dict1,**dict2})
o/p:{"name":"ravi","age":30,"city":"chennai"}