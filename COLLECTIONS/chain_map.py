from collections import ChainMap
d1 = {"a":10,"b":20}
d2 = {"b":30,"c":40}
combined = ChainMap(d2, d1)
print(combined["b"]) # Output 30 because d2 shadows d1
