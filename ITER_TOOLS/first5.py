import itertools
counter = itertools.count(start=10)
for _ in range(5):
    print(next(counter))
