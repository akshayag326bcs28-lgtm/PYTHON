import itertools
colorslist= ['red', 'green', 'blue']
product_combinations = itertools.product(colorslist, repeat=2)
for combo in product_combinations:
    print(combo)
