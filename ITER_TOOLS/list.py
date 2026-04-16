import itertools
items = [1, 2]
combinations = itertools.combinations_with_replacement(items, 2)
for combo in combinations:
    print(combo)
