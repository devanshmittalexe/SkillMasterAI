# tools/grading_tools.py

def grade_answer(question_id: int, topic: str, question: str, answer: str, difficulty: str) -> dict:
    """Grade a single answer — Claude will evaluate it using its knowledge."""
    return {
        "question_id": question_id,
        "topic": topic,
        "question": question,
        "answer": answer,
        "difficulty": difficulty,
        "status": "awaiting_llm_grading",
        "instruction": "Grade this answer now. Score 0-10 and give specific feedback."
    }