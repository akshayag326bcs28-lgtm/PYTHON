import itertools
list= ['a', 'b','c']
cycler = itertools.cycle(list)
sliced = itertools.islice(cycler, 6)
for item in sliced:
    print(item)
