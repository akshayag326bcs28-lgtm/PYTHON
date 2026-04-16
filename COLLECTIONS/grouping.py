from collections import defaultdict
words = ["python","java","go","c","ruby","php"]
length_dict = defaultdict(list)
for word in words:
    length_dict[len(word)].append(word)
for length, group in length_dict.items():
    print(length, "->", group)
