import itertools

string = '123'
permutations = itertools.permutations(string)

for perm in permutations:
    print(''.join(perm))
