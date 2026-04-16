from collections import defaultdict
data = [("Alice",85),("Bob",78),("Alice",92),("Bob",88)]
marks = defaultdict(list)
for student, mark in data:
    marks[student].append(mark)
print(dict(marks))
