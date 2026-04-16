def input_skills(prompt):
    skills = input(prompt)
    return set(skill.strip().lower() for skill in skills.split(','))

# Inputs
required_skills = input_skills("Enter required skills for the job (comma-separated): ")
applicant_skills = input_skills("Enter applicant's skills (comma-separated): ")
outdated_skills_input = input("Enter outdated skills (comma-separated): ")
outdated_skills = set(skill.strip().lower() for skill in outdated_skills_input.split(','))

# Filter out outdated skills from required skills
current_required_skills = required_skills.difference(outdated_skills)

# Identify missing required skills excluding outdated ones
missing_skills = current_required_skills.difference(applicant_skills)

print("\nMissing required skills (excluding outdated):", missing_skills)
