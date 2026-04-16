import itertools
items = ['A', 'B', 'C', 'D']
combinations = itertools.combinations(items, 2)
for combo in combinations:
    print(combo)
