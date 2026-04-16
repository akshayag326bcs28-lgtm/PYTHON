from collections import Counter
nums = [5,3,5,2,3,1,4,1,2]
counter = Counter(nums)
uniqueelements = [num for num, count in counter.items() if count == 1]
print(uniqueelements)
