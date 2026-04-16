from collections import OrderedDict
s = "swiss"
counter = OrderedDict()
for ch in s:
    counter[ch] = counter.get(ch, 0) + 1
for ch, count in counter.items():
    if count == 1:
        print(ch)
        break
