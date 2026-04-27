from fastapi import FastAPI
from pydantic import BaseModel

from backend.skill_extractor import extract_skills
from backend.scorer import calculate_score
from backend.planner import generate_learning_plan
from backend.assessor import generate_questions, evaluate_answer

app = FastAPI()

class InputData(BaseModel):
    resume: str
    jd: str

@app.post("/analyze")
def analyze(data: InputData):
    try:
        resume_skills = extract_skills(data.resume)
        jd_skills = extract_skills(data.jd)

        matched = list(set(resume_skills) & set(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        score = calculate_score(jd_skills, resume_skills)
        plan = generate_learning_plan(missing)

        return {
            "matched_skills": matched,
            "missing_skills": missing,
            "score": score,
            "plan": plan
        }

    except Exception as e:
        return {
            "error": str(e)
        }