
def array_size(nums):
    value= []
    unique_value= set()
    for i in nums:
        if i not in unique_value:
            count = nums.count(i)
            value.append((i, count))
            unique_value.add(i)
    return value
nums = list(map(int,input("Enter value:").split(',')))
print(array_size(nums))  

