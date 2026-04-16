import itertools
elements= [52, 510, 715]
cycler = itertools.cycle(elements)
for _ in range(3):
    print(next(cycler))
