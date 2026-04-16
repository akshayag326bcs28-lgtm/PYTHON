def input_roll_numbers(day):
    roll_numbers = input(f"Enter roll numbers of students present on {day} (separated by spaces): ")
    # Convert input string to a set of integers
    return set(map(int, roll_numbers.split()))

# Get inputs for both days
day1 = input_roll_numbers("day 1")
day2 = input_roll_numbers("day 2")

# Students present on both days (intersection)
present_both_days = day1.intersection(day2)

# Students present on either day (union)
present_either_day = day1.union(day2)

# Students absent on the second day (present on day1 but not on day2)
absent_second_day = day1.difference(day2)

print("Students present on both days:", present_both_days)
print("Students present on either day:", present_either_day)
print("Students absent on the second day:", absent_second_day)
