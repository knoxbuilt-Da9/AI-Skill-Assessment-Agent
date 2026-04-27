def generate_questions(skill):
    questions = {
        "Python": "What is a list in Python?",
        "SQL": "What is a JOIN in SQL?",
        "Machine Learning": "What is supervised learning?"
    }
    return questions.get(skill, f"What do you know about {skill}?")


def evaluate_answer(skill, answer):
    if len(answer) > 20:
        return {
            "score": 8,
            "feedback": "Good explanation"
        }
    else:
        return {
            "score": 4,
            "feedback": "Answer is too short"
        }