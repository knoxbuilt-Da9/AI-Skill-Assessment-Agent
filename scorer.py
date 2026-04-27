def calculate_score(jd_skills, resume_skills):
    matched = set(resume_skills) & set(jd_skills)

    if len(jd_skills) == 0:
        return 0

    return round((len(matched) / len(jd_skills)) * 100, 2)