from collections import namedtuple
Employee = namedtuple("Employee", ["name", "salary"])
employees = [Employee("Alice", 70000), Employee("Bob", 80000), Employee("Charlie", 75000)]
highest = max(employees, key=lambda e: e.salary)
print(highest)
