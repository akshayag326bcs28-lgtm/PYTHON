def input_courses(user):
     courses= input(f"Enter the courses of interest for {user} (separated by commas): ")
     # Convert input string to a set of trimmed course names (case-insensitive)
     return set(course.strip().lower() for course in courses.split(','))
user1_courses = input_courses("User 1")
user2_courses = input_courses("User 2")

     # Find common interests (intersection)
common_interests = user1_courses.intersection(user2_courses)

      # Suggest new courses to User 1 based on User 2's interests (difference)
suggested_courses = user2_courses.difference(user1_courses)

print("\nCommon course interests:", common_interests)
print("Suggested new courses for User 1:", suggested_courses)
