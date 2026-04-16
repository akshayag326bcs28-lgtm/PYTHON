from collections import Counter
s = "aabbccddeeffgg"
counter = Counter(s)
freqs = list(counter.values())
print(all(f == freqs[0] for f in freqs))
