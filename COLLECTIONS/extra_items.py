from collections import Counter
list1 = [1,2,3,4,5]
list2 = [1,2,2,3,4,4,5]
counter1 = Counter(list1)
counter2 = Counter(list2)
extra = counter2 - counter1
print(list(extra.elements()))
