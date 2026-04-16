records = [
    "Arun:AI,ML,Robotics",
    "Bala:ML,IoT",
    "Chitra:AI,CyberSecurity",
    "Divya:Robotics,IoT,AI",
    "Ezhil:ML,CyberSecurity",
    "Farah:AI,ML",
    "Ganesh:IoT,Robotics,AI",
    "Hari:ML"
]

# 01. Extract all unique student names into a set
student_names = set()
for record in records:
    name = record.split(":")[0]
    student_names.add(name)

# 02. Extract all unique clubs into a set
clubs = set()
for record in records:
    club_list = record.split(":")[1].split(",")
    for club in club_list:
        clubs.add(club)
#3
student_clubs_map = {}
for record in records:
    name, club_str = record.split(":")
    club_set = set(club_str.split(","))
    student_clubs_map[name] = club_set
#5
ai_ml_members = {name for name, clubs_set in student_clubs_map.items() if {"AI", "ML"}.issubset(clubs_set)}


# 06. Find students who are members of AI but not Robotics
ai_not_robotics = {name for name, clubs_set in student_clubs_map.items() if "AI" in clubs_set and "Robotics" not in clubs_set}

print("Unique Student Names:", student_names)
print("Unique Clubs:", clubs)
print("Student to Clubs Mapping:", student_clubs_map)
print("Students in both AI and ML:", ai_ml_members)
print("Students who are members of AI but not Robotics:",ai_not_robotics)
