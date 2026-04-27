def extract_skills(text):
    skills_db = [
        "Python", "SQL", "Machine Learning",
        "Statistics", "Power BI", "Tableau",
        "AWS", "Docker"
    ]

    found = []
    for skill in skills_db:
        if skill.lower() in text.lower():
            found.append(skill)

    return found